# __See&Say__

## __Intro:__

* Language development is a critical part of early childhood.  An average of 23% of children have a language witholdment in the US.

* Clinical support waiting lists are long, with the average being 8 months in OECD countries.

* Delays in support can harm child’s language development.

* Screen time among preschoolers continues to rise. Rather than restricting it, we aim to transform it into a opportunity for monitoring and supporting language development.

* Target age group is children aged 3-6. This is the critical developmental window when proper grammar acquisition typically occurs.


## __Solution:__

With guidance from speech and language therapists, we apply targeted strategies to monitor and enhance communication skills during screen use.
Application guided by the child, with optional parental support:

* Child answers image-based queries and receives positive feedback or grammar corrections.

* Parent receives evaluation of linguistic challenges based on child’s age.

## __Method:__

__Three AI Models__

Our system integrates three neural network models: TTS, Whisper (fine-tuned by ivrit.ai), and  LLMs.

#### Text-to-Speech (TTS)

* Reads out loud the image-related queries to the child.

* Pronounce the grammatically correct sentence as feedback.

#### Speech-to-Text (Whisper)

* Transcribes the child’s spoken response into text for analysis.

#### Large Language Model (LLM)

* Infers the intended correct sentence.

* Analyzes errors and provides age-appropriate developmental feedback.


## __Illustration:__

__Image__
![Image](img1.png "A demo image")

__Leading Question__
* ["למה הילד שמח?"](q1_whyHappy.mp3)

__Child's Answer__
* ["הוא קיבל גלידה"](a1_gotIceCream.mp3)

__Response__
* ["כל הכבוד!"](output_audio.mp3)


__Evaluation (After Some Interactions)__
>**Diagnostic Report**
>
>**Child's Age:** 6 years old
>
>**Language Development Assessment:**
>
>The provided sentences suggest that the child has difficulties with linguistic complexity and grammatical accuracy. At the age of 6, children typically demonstrate more advanced language skills, including the ability to form compound sentences using coordinating conjunctions.
>
>However, the child's sentences consist only of a single verb phrase ("הוא קיבל") followed by a direct object ("גלידה"), with no evidence of more complex sentence structures. This is unusual for a 6-year-old child and may indicate a delay in language development.
>
>**Professional Opinion Required:**
>
>Given the child's age and the observed language patterns, it is essential to consult with a speech-language pathologist (SLP) or a pediatrician who specializes in developmental disorders. A comprehensive assessment by a qualified professional will help determine the underlying cause of the child's language difficulties and provide guidance on appropriate interventions.
>
>**Recommendations:**
>
>1. Conduct a thorough language development assessment, including standardized tests and observational evaluations.
>2. Identify potential underlying causes for the child's language difficulties, such as cognitive or motor skill deficits.
>3. Develop an individualized treatment plan to address specific areas of need, incorporating strategies from speech therapy, language therapy, and/or cognitive training.
>
>**Next Steps:**
>
>Schedule a consultation with a qualified professional to begin the assessment and development process. This will help determine the child's strengths and weaknesses and inform targeted interventions to support their language growth.





__Important Notes:__

(1) This is a simple working prototype, to see a demonstration run:
streamlit run Streamlit.py

(2) A larger LLM model is recommended, as Llama 3.1 8B doesn't handle Hebrew well.