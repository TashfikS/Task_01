from openai import OpenAI

class OpenAIClient:
    def __init__(self, api_key):
        self.api_key = api_key

    def generate_fruit_recommendations(self, party_on_weekends, flavor_preference, texture_aversion, price_range):
        prompt = f"""
        You are helping a customer choose fruits for a drink based on their preferences. They have 5 ingredients to choose from: oranges, apples, pears, grapes, watermelon, lemon, and lime. Answer the following questions:

        1. Do you go out to party on weekends? ({party_on_weekends})
        2. What flavors do you like? ({flavor_preference})
        3. What texture do you not like? ({texture_aversion})
        4. What is your price range for the drink? ({price_range})

        Based on their responses, follow these rules:

        - If they party on weekends, include apples, pears, grapes, and watermelon.
        - If they like cider, include apples, oranges, lemon, and lime.
        - If they like sweet, include watermelon and oranges.
        - If they like waterlike, include watermelon.
        - If grapes are chosen, remove watermelon from the list.
        - If they don't like smooth texture, remove pears.
        - If they don't like slimy texture, remove watermelon, lime, and grapes.
        - If they don't like waterlike texture, remove watermelon.
        - If the price is less than $3, remove lime and watermelon.
        - If the price is greater than $4 and less than $7, remove pears and apples.

        Please generate a list of recommended fruits based on the customer's responses to these questions.
        """

        response = OpenAI(api_key=self.api_key).chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "We have 5 ingredient: oranges, apples, pears, grape,s watermelon, lemon and lime"},
                {"role": "user", "content": prompt}
            ]
        )

        generated_text = response.choices[0].message
        return generated_text
