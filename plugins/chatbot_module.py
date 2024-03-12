__plugin_name__ = "GPT3.5 Response"
__version__ = "1.0"
__author__ = "Sonya Sergeeva BPI21-01"
import openai
def get_gpt3_response(prompt):
    openai.api_key = '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'
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()