from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import AutoTokenizer, TFAutoModelForSequenceClassification
import tensorflow as tf

# Define the Hugging Face model repo
MODEL_NAME = "mikachou/funnypress-model"  # Replace with your model's Hugging Face Hub name

# Load the model and tokenizer from the Hugging Face Hub
try:
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = TFAutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
except Exception as e:
    raise RuntimeError(f"Failed to load model from Hugging Face Hub: {e}")

# Define FastAPI app
app = FastAPI(
    title="Funny Press Web Service",
    description="Webservice to find funny press titles",
    version="1.0",
)

# Input schema for predictions
class PredictionInput(BaseModel):
    title: str

# Endpoint for prediction
@app.post("/predict")
async def predict(input_data: PredictionInput):
    try:
        # Tokenize the input text
        inputs = tokenizer(
            input_data.title,
            return_tensors="tf",
            truncation=True,
            padding=True,
            max_length=512,
        )

        # Run the model
        outputs = model(**inputs)
        logits = outputs.logits
        probabilities = tf.nn.softmax(logits, axis=-1).numpy()[0]


        # Assuming label 1 is the positive class
        positive_score = float(probabilities[1])

        # Format the response
        response = {
            "title": input_data.title,
            "score": positive_score,
        }
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {e}")

# Run the FastAPI app
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
