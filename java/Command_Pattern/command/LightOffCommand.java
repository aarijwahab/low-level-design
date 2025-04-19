package java.Command_Pattern.command;

import Command_Pattern.device.Light;

public class LightOffCommand implements Command {
    Light light;
    public LightOffCommand(Light light){
        this.light = light;
    }

    public void execute(){
        light.off();
    }
}
