import TS1 from "./ts-1-priority-direction";
import TS2 from "./ts-2-execution-flow";
import TS3 from "./ts-3-research";
import TS4 from "./ts-4-synthesis";
import TS5 from "./ts-5-creative";
import TS6 from "./ts-6-troubleshoot";
import TS7 from "./ts-7-decision";
import TS8 from "./ts-8-reflection";

// Task System configurations
export const taskSystems = {
  TS1,
  TS2,
  TS3,
  TS4,
  TS5,
  TS6,
  TS7,
  TS8,
};

// Workflow configurations
export const workflows = {
  brainstorm: {
    name: "Brainstorm Workflow",
    description: "Transform ideas into actionable concepts",
    stages: 6,
    duration: "30-90 minutes",
    modules: ["TS5", "TS7", "TS4", "TS1", "TS2", "butterfly"],
    file: "brainstorm-workflow.md",
  },
  weekly_reset: {
    name: "Weekly Reset Workflow",
    description: "End-of-week reflection and planning",
    stages: 4,
    duration: "30-45 minutes",
    modules: ["TS8", "TS1", "weekly_reset_module"],
    file: "weekly-reset-workflow.md",
  },
  problem_solving: {
    name: "Problem-Solving Workflow",
    description: "Navigate stuck situations",
    stages: 5,
    duration: "20-45 minutes",
    modules: ["TS6", "TS7", "weather_module"],
    file: "problem-solving-workflow.md",
  },
  decision_making: {
    name: "Decision-Making Workflow",
    description: "Navigate complex choices",
    stages: 5,
    duration: "30-60 minutes",
    modules: ["TS7", "TS4", "TS1"],
    file: "decision-making-workflow.md",
  },
  focus_sprint: {
    name: "Focus Sprint Workflow",
    description: "Execute on high-priority tasks",
    stages: 5,
    duration: "45-90 minutes",
    modules: ["TS1", "TS2", "TS8"],
    file: "focus-sprint-workflow.md",
  },
};

export default {
  taskSystems,
  workflows,
};
