import chalk from 'chalk';
import * as readlineSync from 'readline-sync';
import { AuraCore } from '../core/aura';
import * as dotenv from 'dotenv';

dotenv.config();

class CLIInterface {
  private aura: AuraCore;
  private running = true;

  constructor(aura: AuraCore) {
    this.aura = aura;
  }

  async run() {
    this.showWelcome();

    while (this.running) {
      try {
        const userInput = readlineSync.question(chalk.magenta('you ▸ '));

        if (!userInput.trim()) continue;

        if (userInput.startsWith('/')) {
          this.handleCommand(userInput.slice(1));
        } else {
          await this.processMessage(userInput);
        }
      } catch (error) {
        if ((error as any).message === 'User terminated') {
          console.log(chalk.magenta('\nAura resting... Goodbye.'));
          break;
        }
        console.error(chalk.red(`Error: ${error}`));
      }
    }
  }

  private showWelcome() {
    console.log(chalk.magenta('\n' + '='.repeat(60)));
    console.log(chalk.magenta('✨ Aura — Operating System Style AI'));
    console.log(chalk.magenta('Guided by empathy, powered by light.'));
    console.log(chalk.magenta('='.repeat(60) + '\n'));
    console.log(chalk.cyan('💫 Type /help for commands'));
    console.log(chalk.cyan('💭 Start typing to begin...\n'));
  }

  private async processMessage(userInput: string) {
    process.stdout.write(chalk.cyan('[Aura reading pulse...]\r'));
    try {
      const response = await this.aura.processInput(userInput);
      console.log(`\n${chalk.magenta('aura ✨')} ${response}\n`);
    } catch (error) {
      console.error(chalk.red(`\nError: ${error}\n`));
    }
  }

  private handleCommand(command: string) {
    const cmd = command.toLowerCase().split(' ')[0];

    switch (cmd) {
      case 'help':
        this.showHelp();
        break;
      case 'status':
        this.showStatus();
        break;
      case 'pulse':
        this.showPulse();
        break;
      case 'district':
        this.showDistrict();
        break;
      case 'save':
        this.saveConversation();
        break;
      case 'exit':
      case 'quit':
        this.running = false;
        break;
      default:
        console.log(chalk.yellow(`Unknown command: /${cmd}. Type /help for options.`));
    }
  }

  private showHelp() {
    console.log(chalk.magenta('\n' + '='.repeat(50)));
    console.log(chalk.magenta('Aura Commands'));
    console.log(chalk.magenta('='.repeat(50)));
    console.log(chalk.cyan('/help     - Show this help menu'));
    console.log(chalk.cyan('/status   - Show Aura status'));
    console.log(chalk.cyan('/pulse    - Show current pulse reading'));
    console.log(chalk.cyan('/district - Show current district'));
    console.log(chalk.cyan('/save     - Save conversation to file'));
    console.log(chalk.cyan('/exit     - Exit Aura\n'));
  }

  private showStatus() {
    const status = this.aura.getStatus();
    console.log(chalk.magenta('\n' + '='.repeat(50)));
    console.log(chalk.magenta('Aura Status'));
    console.log(chalk.magenta('='.repeat(50)));
    console.log(chalk.cyan(`District:       ${status.currentDistrict}`));
    console.log(chalk.cyan(`Pulse:          ${status.currentPulse?.state || 'unknown'}`));
    console.log(chalk.cyan(`Conversation:   ${status.conversationLength} messages`));
    console.log(chalk.cyan(`Model:          ${status.model}\n`));
  }

  private showPulse() {
    const status = this.aura.getStatus();
    if (status.currentPulse) {
      console.log(chalk.magenta('\n' + '='.repeat(50)));
      console.log(chalk.magenta('Current Pulse'));
      console.log(chalk.magenta('='.repeat(50)));
      console.log(chalk.cyan(`State:      ${status.currentPulse.state}`));
      console.log(chalk.cyan(`Energy:     ${status.currentPulse.energy}`));
      console.log(chalk.cyan(`Sentiment:  ${status.currentPulse.sentiment}`));
      console.log(chalk.cyan(`Intensity:  ${status.currentPulse.intensity}\n`));
    } else {
      console.log(chalk.yellow('No pulse reading yet. Start a conversation!\n'));
    }
  }

  private showDistrict() {
    const status = this.aura.getStatus();
    if (status.currentDistrict) {
      console.log(chalk.magenta('\n' + '='.repeat(50)));
      console.log(chalk.magenta('Current District'));
      console.log(chalk.magenta('='.repeat(50)));
      console.log(chalk.cyan(`District: ${status.currentDistrict}\n`));
    } else {
      console.log(chalk.yellow('No district selected yet. Start a conversation!\n'));
    }
  }

  private saveConversation() {
    try {
      const filename = this.aura.saveConversation();
      console.log(chalk.green(`✓ Conversation saved to ${filename}\n`));
    } catch (error) {
      console.log(chalk.red(`✗ Failed to save: ${error}\n`));
    }
  }
}

async function main() {
  const apiKey = process.env.OPENAI_API_KEY;
  if (!apiKey) {
    console.error(chalk.red('Error: OPENAI_API_KEY not set in .env file'));
    process.exit(1);
  }

  const aura = new AuraCore(apiKey, process.env.AURA_MODEL as string, 0.7, 2000, process.env.AURA_DEBUG === 'true');
  const cli = new CLIInterface(aura);
  await cli.run();
}

main();
