from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import openai

class PoetryGeneratorView(APIView):
    def post(self, request):
        prompt = request.data.get("prompt")
        if not prompt:
            return Response({"error": "Prompt is required!"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Set OpenAI API key
            openai.api_key = settings.OPENAI_API_KEY

            # Use ChatCompletion API for chat-based models
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # Or "gpt-4"
                messages=[
                    {"role": "system", "content": "You are a creative poet."},
                    {"role": "user", "content": f"Write a poem about: {prompt}"}
                ],
                max_tokens=150,
                temperature=0.7,
            )

            # Extract the poem from the response
            poem = response['choices'][0]['message']['content'].strip()
            return Response({"poem": poem}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
