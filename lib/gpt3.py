import os
import openai

class GPT:
  """Access the GPT-3 Rest API"""
  def __init__(self):
    openai.api_key = os.getenv("OPENAI_API_KEY")


  def submit_request(self, prompt, **kwargs):
    """Calls the OpenAI API with the specified parameters."""

    response = openai.Completion.create(engine=kwargs.get('engine', 'davinci'),
                                        prompt=prompt,
                                        temperature=kwargs.get('temperature', 0.5),
                                        max_tokens=kwargs.get('max_tokens', 100),
                                        top_p=kwargs.get('top_p', 1),
                                        frequency_penalty=kwargs.get('frequency_penalty', 0.0),
                                        presence_penalty=kwargs.get('presence_penalty', 0.6),
                                        stop=kwargs.get('stop', None)
    )
    return response['choices'][0]['text']

  def get_top_reply(self, 
                    prompt,
                    engine='davinci',
                    temperature=0.5,
                    max_tokens=10,
                    top_p=1,
                    frequency_penalty=0.0,
                    presence_penalty=0.6,
                    stop=None):
      """Obtains the best result as returned by the API."""

      response = self.submit_request(engine,
                                     prompt,
                                     max_tokens,
                                     temperature,
                                     top_p,
                                     frequency_penalty,
                                     presence_penalty,
                                     stop)
      return response['choices'][0]['text']
