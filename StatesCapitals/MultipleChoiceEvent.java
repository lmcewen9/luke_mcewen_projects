package statescapitals;

import java.util.List;

import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import java.lang.Math;

public class MultipleChoice implements EventHandler<ActionEvent> {

    private StatesandCapitalsGuiForPeopleWhoAreBad gui;
    private Button buttonClicked;
    private Button otherButton1;
    private Button otherButton2;
    private Button otherButton3;
    private Button otherButton4;
    private Label label;
    private StatesandCapitals statescapitals;
    private Label score;
    private List<String> list;

    public MultipleChoice(Button buttonClicked, StatesandCapitalsGuiForPeopleWhoAreBad gui,
                             Button otherButton1, Button otherButton2,
                             Button otherButton3, Button otherButton4, Label label,
                              StatesandCapitals statescapitals, Label score, List<String> list){
        this.buttonClicked = buttonClicked;
        this.gui = gui;
        this.otherButton1 = otherButton1;
        this.otherButton2 = otherButton2;
        this.otherButton3 = otherButton3;
        this.otherButton4 = otherButton4;
        this.label = label;
        this.statescapitals = statescapitals;
        this.score = score;
        this.list = list;
    }

    @Override
    public void handle(ActionEvent event) {
        if(statescapitals.check(buttonClicked.getText(), gui.getCurrentState())){
            score.setText("Correct! Score=" + statescapitals.getScore());
        }
        else{
            score.setText("Incorrect! It was " + statescapitals.getCapital(gui.getCurrentState()) + ". Score=" + statescapitals.getScore());
        }

        if(list.isEmpty()){
            buttonClicked.setText("");
            otherButton1.setText("");
            otherButton2.setText("");
            otherButton3.setText("");
            otherButton4.setText("");
            buttonClicked.setOnAction(gui.exit());
            otherButton1.setOnAction(gui.exit());
            otherButton2.setOnAction(gui.exit());
            otherButton3.setOnAction(gui.exit());
            otherButton4.setOnAction(gui.exit());
            int percent = (int) Math.round((statescapitals.getScore()/50.0)*100.0);
            if (percent == 100)
                label.setText("Holy Fucking Shit! You got a 100%");
            else if (percent < 100 && percent > 80)
                label.setText("Great Job! You got a " + percent + "%");
            else if (percent > 50 && percent <= 80)
                label.setText("Good Job. You got a " + percent + "%");
            else
            label.setText("You Suck! You got a " + percent + "%");
        }
        else{
            String currentState = statescapitals.getState(list);
            gui.setCurrentState(currentState);
            label.setText("What is the capital of " + currentState + "?");

            List<String> randomStates = gui.fourRandom();
            List<Integer> randomNums = gui.randomNumbers();
            randomStates.add(statescapitals.getCapital(currentState));
            buttonClicked.setText(randomStates.get(randomNums.get(0)));
            otherButton1.setText(randomStates.get(randomNums.get(1)));
            otherButton2.setText(randomStates.get(randomNums.get(2)));
            otherButton3.setText(randomStates.get(randomNums.get(3)));
            otherButton4.setText(randomStates.get(randomNums.get(4)));
        }
    }   
}
