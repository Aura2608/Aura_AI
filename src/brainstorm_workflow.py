#!/usr/bin/env python3
"""
Brainstorming Module Extension for Aura
Activates the 6-stage brainstorming workflow
"""

from typing import Dict, List
from aura_core import AuraCore


class BrainstormingWorkflow:
    """6-stage brainstorming workflow for creative ideation."""
    
    STAGES = {
        1: {
            'name': 'Idea Seed',
            'duration': '5-10 min',
            'purpose': 'Capture the core concept',
            'prompts': [
                'What is the core concept?',
                'What problem does it solve?',
                'What excites you about it?',
                'Who would benefit most?'
            ]
        },
        2: {
            'name': 'Expansion',
            'duration': '10-15 min',
            'purpose': 'Generate multiple angles and possibilities',
            'modules': ['butterfly', 'TS-5'],
            'techniques': [
                'Perspective Shifting',
                'Constraint Reversal',
                'Adjacent Possibilities',
                'Yes, And Principle'
            ]
        },
        3: {
            'name': 'Exploration',
            'duration': '15-20 min',
            'purpose': 'Dive deep into promising angles',
            'modules': ['butterfly'],
            'focus_areas': [
                'Divergent Thinking',
                'Target User Mapping',
                'Feature Ideation'
            ]
        },
        4: {
            'name': 'Evaluation',
            'duration': '10-15 min',
            'purpose': 'Test against reality and feasibility',
            'modules': ['TS-7'],
            'frameworks': [
                'Reality Check (Feasibility/Desirability/Viability)',
                'Risk Assessment',
                'Competitive Landscape'
            ]
        },
        5: {
            'name': 'Integration',
            'duration': '10 min',
            'purpose': 'Synthesize insights into coherent concept',
            'modules': ['TS-4'],
            'outputs': [
                'Core Concept',
                'Target User',
                'Primary Value',
                'Key Features',
                'Business Model',
                'Next Steps'
            ]
        },
        6: {
            'name': 'Action Planning',
            'duration': '10 min',
            'purpose': 'Convert ideas into concrete steps',
            'modules': ['TS-1', 'TS-2'],
            'deliverables': [
                'MVP Features',
                'Validation Plan',
                'First Steps (1-2 weeks)'
            ]
        }
    }
    
    def __init__(self, aura: AuraCore):
        self.aura = aura
        self.stage = 0
        self.session_data = {
            'seed_idea': None,
            'expansions': [],
            'evaluated_ideas': [],
            'final_concept': None,
            'action_plan': None
        }
    
    def start(self) -> str:
        """Start the brainstorming workflow."""
        self.stage = 1
        
        response = f"""
✨ Aura is entering Creative District | Butterfly Module activated

🦋 Welcome to the Brainstorming Workflow

We're about to embark on a 6-stage creative journey:

1️⃣  SEED (5-10 min)        → Capture your core idea
2️⃣  EXPANSION (10-15 min)  → Generate multiple angles
3️⃣  EXPLORATION (15-20 min) → Dive into promising directions
4️⃣  EVALUATION (10-15 min)  → Test against reality
5️⃣  INTEGRATION (10 min)    → Synthesize into clear concept
6️⃣  ACTION (10 min)         → Create concrete next steps

Total time: 60-90 minutes for a complete session
(You can adjust pace as we go)

Let's begin with Stage 1: IDEA SEED

Tell me about your idea:
- What's the core concept?
- What problem does it solve?
- What excites you most about it?
"""
        return response
    
    def process_stage(self, user_input: str) -> str:
        """Process user input for current stage."""
        
        if self.stage == 1:
            return self._process_seed(user_input)
        elif self.stage == 2:
            return self._process_expansion(user_input)
        elif self.stage == 3:
            return self._process_exploration(user_input)
        elif self.stage == 4:
            return self._process_evaluation(user_input)
        elif self.stage == 5:
            return self._process_integration(user_input)
        elif self.stage == 6:
            return self._process_action(user_input)
        else:
            return "Brainstorm session complete! Use /save to save your work."
    
    def _process_seed(self, user_input: str) -> str:
        """Stage 1: Process seed idea."""
        self.session_data['seed_idea'] = user_input
        self.stage = 2
        
        return f"""
✨ Great seed: "{user_input}"

I've captured your core idea. Now let's expand it.

═════════════════════════════════════════
🦋 STAGE 2: EXPANSION (10-15 minutes)
═════════════════════════════════════════

Let's view this from multiple perspectives:

👨‍💼 ENTREPRENEUR lens:
  How would this scale? What's the business model?
  
🎨 DESIGNER lens:
  What would the experience feel like?
  
⚙️  ENGINEER lens:
  What's technically possible?
  
👤 CUSTOMER lens:
  How would this improve their life?
  
🤔 CRITIC lens:
  What could go wrong? What's missing?

Which perspective interests you most?
Or shall I explore all of them?
"""
    
    def _process_expansion(self, user_input: str) -> str:
        """Stage 2: Process expansion input."""
        self.session_data['expansions'].append(user_input)
        self.stage = 3
        
        return f"""
🦋 Excellent expansion thinking!

═════════════════════════════════════════
🌊 STAGE 3: EXPLORATION (15-20 minutes)
═════════════════════════════════════════

Now let's dive deep. Based on what resonates most, 
let's explore variations:

What are 5-10 different ways this could work?

 Examples:
 - The straightforward version
 - The premium version
 - The freemium version
 - The AI-powered version
 - The community-driven version

For each variation, consider:
- Who would use it?
- What problem does it solve for them?
- How is it different from alternatives?

Share your top 2-3 variations:
"""
    
    def _process_exploration(self, user_input: str) -> str:
        """Stage 3: Process exploration."""
        self.stage = 4
        
        return f"""
🌊 Powerful variations! You've opened up the possibilities.

═════════════════════════════════════════
🎯 STAGE 4: EVALUATION (10-15 minutes)
═════════════════════════════════════════

Now let's test your strongest idea against reality.

For your most promising variation, rate these (1-10):

FEASIBILITY:
  ▪ Technical feasibility (Can we build it?)
  ▪ Do we have resources?
  ▪ Timeline?
  ▪ Cost?

DESIRABILITY:
  ▪ Does it solve a real problem? (1-10)
  ▪ Would people use it? (1-10)
  ▪ Is there competition? How is this different?

VIABILITY:
  ▪ Long-term sustainable? (1-10)
  ▪ Business model viable? (1-10)
  ▪ Can we scale?

Share your ratings. I'll calculate a viability score.
"""
    
    def _process_evaluation(self, user_input: str) -> str:
        """Stage 4: Process evaluation."""
        self.session_data['evaluated_ideas'].append(user_input)
        self.stage = 5
        
        return f"""
🎯 Realistic assessment. That's the honest evaluation we need.

═════════════════════════════════════════
🔮 STAGE 5: INTEGRATION (10 minutes)
═════════════════════════════════════════

Let's synthesize everything into a clear concept:

For your strongest idea, define:

1. CORE CONCEPT (1 sentence)
   What is this at its essence?
   
2. TARGET USER (2-3 sentences)
   Who is this for? Why do they need it?
   
3. PRIMARY VALUE (2-3 sentences)
   What problem does it solve? How is it different?
   
4. KEY FEATURES (3-5 bullets)
   What makes it work?
   
5. BUSINESS MODEL (1-2 sentences)
   How does it make money?

Share what you have so far, and I'll help refine it:
"""
    
    def _process_integration(self, user_input: str) -> str:
        """Stage 5: Process integration."""
        self.session_data['final_concept'] = user_input
        self.stage = 6
        
        return f"""
🔮 Excellent synthesis! Your concept is taking shape.

═════════════════════════════════════════
🚀 STAGE 6: ACTION PLANNING (10 minutes)
═════════════════════════════════════════

Now let's convert this into concrete action.

What's your MVP (Minimum Viable Product)?

Define:

1. MUST-HAVE FEATURES (for launch)
   - Feature 1
   - Feature 2
   - Feature 3
   
2. VALIDATION PLAN
   What needs to be true for this to work?
   How will you test each assumption?
   
3. FIRST STEPS (Next 1-2 weeks)
   - What's the one thing you'll do first?
   - Who will you talk to?
   - What will you build/research?

Share your action plan, and I'll help you refine it:
"""
    
    def _process_action(self, user_input: str) -> str:
        """Stage 6: Process action planning."""
        self.session_data['action_plan'] = user_input
        self.stage = 7
        
        return f"""
✨ BRAINSTORMING COMPLETE!

You now have:
✅ A clear concept
✅ Target user identified
✅ MVP scope defined
✅ Validation strategy
✅ First steps planned

Here's what I recommend:

1. REVIEW TODAY
   Read through this entire brainstorm.
   
2. SLEEP ON IT
   Give your mind time to process.
   
3. VALIDATE TOMORROW
   Start step 1 of your action plan.
   Talk to potential users.
   Get feedback.
   
4. ITERATE
   Adjust based on what you learn.
   Pivot if needed. That's normal.
   
5. BUILD
   Once validated, start building!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💾 Use /save to save your full brainstorm session.

📈 You've taken your idea from raw concept to actionable plan.
That's the power of structured brainstorming.

Ready to execute? What's your first action?
"""
    
    def get_summary(self) -> Dict:
        """Get brainstorm session summary."""
        return {
            'seed_idea': self.session_data['seed_idea'],
            'expansions': self.session_data['expansions'],
            'evaluated_ideas': self.session_data['evaluated_ideas'],
            'final_concept': self.session_data['final_concept'],
            'action_plan': self.session_data['action_plan'],
            'completed': self.stage >= 7
        }
