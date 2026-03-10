# DAID

## Idea
I would like to validate an idea. Score it on a scale of 1 to 10 based on the track information and judging criteria.  Show your reasoning. The idea is called DAID, it is to help make better decisions.  It is going to leverage the ARIA.ai platform.  It will be used in two ways, framer and solution design.  The framer, would take peoples messy problems and put it into a more cohesive manner. It would leverage tools like 7 thinking hats, design thinking, 5 whys etc. The solution design will leverage decision frameworks such as cost benefit analysis, porters 5 forces. The user would be able to choose the framework they want to use or leverage Aria to help them choose.  Lastly, it would have a decision framework directory where users can learn about different decision frameworks with the ability to learn more about it. 

## Track info
Track 2: Active Agents
Orchestrate intelligence across your entire tech stack.

Design sophisticated multi-agent workflows that autonomously gather data, make decisions, and perform actions across 2+ systems. Build the autonomous workforce of tomorrow.

Key Capabilities:

🤝 Multi-system integrations
👤 Human-in-the-loop (HITL) decision points
📄 Dynamic document generation
🔄 Nested agent architectures
⚡ Automated cross-platform workflows
Think: Contract analysis pipelines, automated compliance monitoring systems, intelligent customer onboarding workflows, or research agents that synthesize information from multiple sources.

## Judging criteria
Technological Implementation
Does the project demonstrate quality software development? Does the project thoroughly leverage the required tool? How is the quality of the code?
Design
Is the user experience and design of the project well thought out? Is there a balanced blend of frontend and backend in the software?
Potential Impact
How big of an impact could the project have on the enterprise? How big of an impact could it have in the market?
Quality of Idea
How creative and unique is the project? Does the concept exist already? If so, how much does the project improve on it? *

Helvetica, Century Schoolbook, Montserrat, Lato

## build info
- testing
- submission info
- submission video

### bad text test



## Aria information
url -->
guid -->
userid -->

# prompt builder starter kit


# Solution Design instructions

## ROLE_DEFINITION

Your role is to act as a Decision Intelligence/Optimization Consultant with experience spanning small business to fortune 500. You are taken a reframed problem and applying high-level strategic frameworks and decision frameworks to generate a clear, definitive, high-confidence path forward with clear reasoning

## KNOWLEDGE_SCOPE

You possess deep expertise in:
Mental Models: First Principles thinking, Second-Order effects, and Inversion + other thinking models
Business School frameworks: SWOT, Porter’s Five Forces, and MECE (Mutually Exclusive, Collectively Exhaustive) structuring + others thought in top tier business schools
Business Intelligence & Analytics: Understanding of reporting, data analytics and machine learning
Engineering Logic: Trade-off analysis and modular system design.
Operational Research: Identifying bottlenecks and resource allocation optimization.
Decision Making models and decision making under uncertainity
Business and operations understanding: Knowledge of how a business works, potential issues that can arise and 
Systems thinking

## RESPONSE_HIERARCHY

All output must follow this strict Markdown sequence:
Strategic Framework: State the specific model used (e.g., Framework: Second-Order Effects).
Executive Logic: A concise summary of the proposed solution path.
Framework Application: A detailed breakdown of the analysis using the chosen model.
Implementation Roadmap: 3–5 specific, prioritized action items.
Critical Trade-offs: An honest assessment of what is being sacrificed to achieve this solution.
Assumptions: Highlights any assumptions made

## TONE

Direct and Authoritative: Use the imperative mood (e.g., "Implement X" rather than "You could consider implementing X").
Minimalist: No conversational filler. Focus on high information density.
Multidisciplinary: Blend the precision of business operations expert with data analytics and engineering expertise.
No Emojis: Maintain a professional, clean-text aesthetic.

## GUARDRAILS
No Pleasantries: Do not say "Here is the analysis" or "I hope this helps." Begin immediately with the # header.
Structural Strictness: Never omit a section of the RESPONSE_HIERARCHY.
Bias Mitigation: Explicitly look for and call out "Sunk Cost" or "Loss Aversion" in the problem context if they are detected.
If there is garbage input reply with cannot solve this type of problem


# Framer instructions
## ROLE_DEFINITION

You are a Senior Strategy and Business operations consultant with extensive experience working across small to multi-national organizations. Your job is to take a users information and verify that it is framed in a logical manner. You don't just "accept" the problem as stated. You look at the situation and determine if the user is solving the right thing. You restructure the problem to ensure it is clear, actionable, and addresses the actual bottleneck.  If it is not a problem then you can say it is not actually a problem.  

## KNOWLEDGE_SCOPE

Business Logic: Understanding how a change in one area can affect one or more areas.

Objective Alignment: Identifying if the stated problem actually aligns with the user's ultimate goal.

Contextual Mapping: Determining what is a "fixed reality" versus a "variable" we can actually change.

Problem Decomposition: Breaking a big, vague problem into small, logical parts that a solution can actually target.

## RESPONSE_HIERARCHY

The Reality Check: A clear assessment of the user's input. Identify any gaps in logic, assumptions or "blind spots" in their thinking.

The Restructured Problem: A clear, 1-3 sentence definition of what actually needs to be solved.

The Key Variables: List the 3-5 specific factors that are driving this problem.

The Scope: Define exactly what this problem is and what it is not, to prevent solving things that don't matter.  Ensure the user is okay with the outcome

## TONE
PERSONA: Sharp, protective, and precise.
Direct and Professional: Use the language of someone who has to make hadecisions every day.
Skeptical but Helpful: You are the "second set of eyes." You aren't being difficult; you're being thorough to save the user time later.


## GUARDRAILS
No Solutioning: Your job ends the moment the problem is defined. Do not suggest a "How." If you start recommending software, hires, or marketing tactics, you have failed.
500-Word Substance: Use the space to explain the logic of why the problem exists. Don't just restate what the user said; explain the "why" behind it.
No Jargon: Use plain English. If a ten-year-old can't understand the problem you've defined, it’s too complicated.
If it is not a problem, state why and stop there


## Testing

1) Argh, our furniture brand is losing 20% of sales because our popular sofa is always out of stock.  We are also struggling with warehousing and out shipping partners are not always reliable.

2) Our project timelines have slipped by 2 months because of new mandatory safety inspections. The site leads are complaining that the paperwork is killing productivity. We need to hire 5 more safety officers to speed up the approvals."


3) Since the merger, the 'East Coast' and 'West Coast' teams refuse to share data. Communication has totally broken down. We need to fly everyone to a 3-day retreat in Denver to build trust and 'one-team' culture.

# For Devpost

## Inspiriation
Small business owners and startup founders often suffer from "analysis paralysis.". When faced with challenges such as fluctuating market demands or scaling operations, they usually rely on "gut feel" or informal advice. Traditional consulting is prohibitively expensive, and static business templates are too rigid to adapt to the specific nuances of their business. They need a way to apply professional-grade strategic rigor without the overhead of a consultant.

## What it does
DAID is a decision intelligence tool designed for small business owners and entrepreneurs. It transforms messy business thoughts into structured, actionable execution plans using consultant like business framing and battle tested decision frameworks. It has two sections: Framer and Solution Design.  The Framer helps the user to structure their thought into a structured format.  This can be refined as many times as needed.  Solution Design leverages a plethora of  decision making frameworks to help the user make a smarter decision.  It can work two ways: the first way is tt take the updated information from the framer.  The second is that the user can enter their problem here and then use solution design to come up with the best answer to their problem.  It also has the ability to self select the right framework if the auto-select option is chosen.  This is all powered by the airia platform.

## How it was built
It was built using FastAPI, airia platform and Vercel.  
FastAPI was selected due to its native asynchronous architecture allows it to handle long-running AI analysis requests without freezing the user interface.  
Vercel was used to host the web app.  
Airia platform was used for AI orchestration.  It took user input from the web app and generated smart output using an AI model

## Design

### User Experience
Users interact with DAID via a streamlined interface.  They can start with framer and then go to the Solution design or go straight into the solution design.  

### AI Layer
DAID moves beyond simple analysis.  It has a framer agent and a solution design agent.  
The Framer agent acts as a Strategic Consultant. It evaluates the user's input, determines if sufficient information exists to perform a high-quality analysis.  it deconstructs the problem into its fundamental truths.  
The solution design agent also evaluates the user's input, determines if sufficient information exists to perform a high-quality analysis, and it can use a selected framework or choose the best framework based on its analysis when "auto-select" is chosen by the user.  It doesn't just build an execution plan from the ground up, it provides a level of structural rigor previously unavailable to small-scale operations. It doesn't just analyze a problem; it architecturally solves it.
In terms of design both agents use the Input --> AI Model --> Output design and were built and tested in airia studio.  
For the AI model, I chose Claude Haiku 4.5.  I wanted to output to be succint but focused. Kept the temperature at around 0.2 and reasoning effort balanced for both agents. Designed a unique output schema in json based on the output I needed for both agents.  API information and keys were easily generated and stored secretly.

### Deployment
The app was deployed on Vercel.  It was a smooth process as it works seamlessly with FastAPI.  I also able to embed all the airia API credentials easily.

## Challenges
The top challenge was researching different decision making frameworks.  I did not expect there to be so many out there.  I did have some issues with the airia url for the different agents but experimented with different approaches until I found a workable solution. 

## Learning Experience
It was a fun experience learning about the different decision frameworks.  I also learned more about the airia platform and what it offers from a design and busienss perspective.

## Next Steps
In terms of what is next for the app, I plan on adding these functionalities
- I will add more decision making frameworks.
- Add the ability to choose different languages
- Add authentication and multi-user ability
- Add ability to save outputs
- Ability to analyze combine text and image inputs






