package Command_Pattern;

import java.rmi.Remote;

import Command_Pattern.command.GarageDoorDownCommand;
import Command_Pattern.command.GarageDoorUpCommand;
import Command_Pattern.command.LightOffCommand;
import Command_Pattern.command.LightOnCommand;
import Command_Pattern.device.GarageDoor;
import Command_Pattern.device.Light;

public class RemoteLoader {
    public static void main(String[] args){
        // Create the remote control
        RemoteControl remoteControl = new RemoteControl();

        Light light = new Light();
        LightOnCommand lightOnCommand = new LightOnCommand(light);
        LightOffCommand lightOffCommand = new LightOffCommand(light);
        GarageDoor garageDoor = new GarageDoor();
        GarageDoorUpCommand garageDoorUpCommand = new GarageDoorUpCommand(garageDoor);
        GarageDoorDownCommand garageDoorDownCommand = new GarageDoorDownCommand(garageDoor);

        // Fill up the slot with the command
        remoteControl.setCommand(0, lightOnCommand, lightOffCommand);
        remoteControl.setCommand(1, garageDoorUpCommand, garageDoorDownCommand);

        // Print the remote control
        System.out.println(remoteControl);

        // Execute the command
        remoteControl.onButtonWasPushed(1);
        remoteControl.offButtonWasPushed(1);

        // Execute the command
        remoteControl.onButtonWasPushed(0);
        remoteControl.offButtonWasPushed(0);

    }
    
}
