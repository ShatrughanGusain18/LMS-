from pathlib import Path
from langchain_huggingface import HuggingFacePipeline
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from dotenv import load_dotenv
import os
import torch


# Load environment variables from .env
load_dotenv()


class MathQuestionModel:
    def __init__(
        self,
        model_repo: str = "mistralai/Mistral-7B-Instruct-v0.3",
        local_dir: str = "Mistral-7B-Instruct-v0.3",
        torch_dtype: torch.dtype = torch.float16   # ✅ added default dtype
    ):
        # Read token from .env
        hf_token = os.getenv("HF_TOKEN")
        if not hf_token:
            raise ValueError("❌ HF_TOKEN not found in environment variables. Please add it to your .env file.")

        self.local_path = Path(local_dir).resolve()
        self.torch_dtype = torch_dtype   # ✅ save dtype

        # ✅ Load model (download if not local)
        if not self.local_path.exists():
            print(f"⚡ Model not found locally. Downloading {model_repo} to {self.local_path} ...")
            self.tokenizer = AutoTokenizer.from_pretrained(model_repo, token=hf_token)
            self.model = AutoModelForCausalLM.from_pretrained(
                model_repo,
                torch_dtype=self.torch_dtype,   # ✅ fixed
                token=hf_token,
                device_map="auto"               # ✅ recommended
            )
            self.tokenizer.save_pretrained(f"{self.local_path}")
            self.model.save_pretrained(f"{self.local_path}")
            print(f"✅ Model downloaded and saved at {self.local_path}")
        else:
            print(f"📂 Loading model from local directory: {self.local_path}")
            self.tokenizer = AutoTokenizer.from_pretrained(f"{self.local_path}", local_files_only=True)
            self.model = AutoModelForCausalLM.from_pretrained(
                f"{self.local_path}",
                local_files_only=True,
                torch_dtype=self.torch_dtype,   # ✅ fixed
                device_map="auto"
            )

        # ✅ Create HuggingFace pipeline
        self.pipe = pipeline(
            "text-generation",
            model=self.model,
            tokenizer=self.tokenizer,
            max_new_tokens=200,
            temperature=0.7
        )

        # ✅ Wrap with LangChain
        self.llm = HuggingFacePipeline(pipeline=self.pipe)

    def generate_question(self, level: int) -> str:
        """
        Generate a math question with 4 multiple-choice options.
        """
        prompt = (
            f"Create ONE multiple-choice math question of difficulty level {level} "
            f"(where 1 is very easy and 10 is very hard). "
            f"Format it like this:\n\n"
            f"Question: <your question>\n"
            f"A) <option 1>\n"
            f"B) <option 2>\n"
            f"C) <option 3>\n"
            f"D) <option 4>\n\n"
            f"Only return the question and options. Do not include the answer or explanation."
        )

        result = self.llm.invoke(prompt)
        return result.strip()
