package java.Command_Pattern;

import Command_Pattern.command.Command;
import Command_Pattern.command.NoCommand;

public class RemoteControl {
    Command[] onCommands;
    Command[] offCommands;

    public RemoteControl(){
        onCommands = new Command[2];
        offCommands = new Command[2];

        Command noCommand = new NoCommand();
        for (int i = 0; i < 2; i ++){
            onCommands[i] = noCommand;
            offCommands[i] = noCommand;
        }
    }

    public void setCommand(int slot, Command onCommand, Command offCommand){
        offCommands[slot] = offCommand;
        onCommands[slot] = onCommand;
    }

    public void onButtonWasPushed(int slot){
        onCommands[slot].execute();
    }

    public void offButtonWasPushed(int slot){
        offCommands[slot].execute();
    }

    public String toString(){
        StringBuffer stringBuff = new StringBuffer();
        stringBuff.append("\n------ Remote Control -------\n");
        for (int i = 0; i < onCommands.length; i++) {
            stringBuff.append("[slot " + i + "] " + onCommands[i].getClass().getName() 
            + " " + offCommands[i].getClass().getName() + "\n");
        }
        return stringBuff.toString();
    }
}
