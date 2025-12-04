## ML App Using GraphQL

A Machine Learning (ML) app using GraphQL works like this:

- You train or load an ML model in Python. (for example: a model that predicts house price from square feet).
- You create a GraphQL mutation where the user sends input. (example: sqft: 1200).
- The GraphQL resolver calls the ML model and gets the prediction.
- GraphQL returns the output in a clean JSON format.

---
#### Screenshot
<img width="960" height="435" alt="Image" src="https://github.com/user-attachments/assets/e6c6eaef-96d8-4713-b5bf-bf2b452e2d7d" />
