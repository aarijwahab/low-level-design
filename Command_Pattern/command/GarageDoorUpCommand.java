package Command_Pattern.command;

import Command_Pattern.device.GarageDoor;

public class GarageDoorUpCommand implements Command {
    GarageDoor garageDoor = new GarageDoor();

    public GarageDoorUpCommand(GarageDoor garageDoor){
        this.garageDoor = garageDoor;
    }

    public void execute(){
        garageDoor.up();
    }
    
}
