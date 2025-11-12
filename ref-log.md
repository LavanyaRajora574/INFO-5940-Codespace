Reflection:

Creating the multi-agent workflow in Streamlit increased my insight into the ability of AI agents to share meaningful interactions through structured communication. A Planner agent would derive detailed itineraries or plans from ambiguous input, while a Reviewer agent would verify, and refine, the Plan. This enhanced my understanding of how prompt specificity and context handoff affect the usefulness and coherence of output information.

A challenge that I confronted was understanding the workflow, particularly the context exchange, between the Planner and Reviewer agents. There were times that agents were not conveying or understanding information in proper structured manner. The process of logging and debugging, to see each form of message sent and exchanged, empowered me to understand how the information exchanged, and context handoff occurred, while creating a more reliable exchange of context. Learning to process messages and exchanges in this way increased my understanding of the importance of coordinating availability and the cleanliness of prompts in a multi-agent workflow.

Another choice I made creatively was in how I structured prompts to allow each agent to emphasize some personality and intentionality. The prompts for the Planner agent included terms such as structure and budget rationale, etc., that prompted logical reasoning. The Reviewer agent collected the user experience and assessed validity for fact checking and revising the Plan. This distinction as to the role of each agent in the task made their interaction more coherent and purposeful.

Generative AI Use:
Used ChatGPT for guidance on - 
•⁠  ⁠Write role-based system prompts for agent collaboration and communication – defined distinct personas.
•⁠  ⁠How to invoke internet_search for context verification? – implemented validation logic.
•⁠  ⁠How to log and debug messages between Planner and Reviewer? – improved traceability.
•⁠  ⁠How to improve output readability and formatting in Streamlit? – refined layout and clarity.
•⁠  ⁠What are different sections to form a prompt for an LLM? – learned prompt structure.
•⁠  ⁠How to be concise while giving a prompt for an LLM? – practiced clear, outcome based phrasing.