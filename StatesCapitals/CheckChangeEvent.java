package statescapitals;

import java.util.List;

import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;

public class CheckChange implements EventHandler<ActionEvent> {

    private Label label;
    private String currentState;
    private List<String> list;
    private TextField textField;
    private StatesandCapitals game;
    private Label score;
    private Button button;

    public CheckChange(Label label, String currentState, List<String> list, TextField textField, StatesandCapitals game, Label score, Button button){
        this.label = label;
        this.currentState = currentState;
        this.list = list;
        this.textField = textField;
        this.game = game;
        this.score = score;
        this.button = button;
    }

    @Override
    public void handle(ActionEvent event) {
        if(game.check(textField.getText(), currentState)){
            score.setText("Correct! Score=" + game.getScore());
        }
        else{
            score.setText("Incorrect! It was " + game.getCapital(currentState) + ". Score=" + game.getScore());
        }

        textField.setText("");
        
        if (list.isEmpty()){
            textField.setOnAction(e -> System.exit(0));
            button.setOnAction(e -> System.exit(0));
            double percent = game.getScore()/50.0;
            if (percent == 1)
                label.setText("Holy Fucking Shit! You got a 100%");
            else if (percent < 1 && percent > .80)
                label.setText("Great Job! You got a " + percent + "%");
            else if (percent > .50 && percent <= .80)
                label.setText("Good Job! You got a " + percent + "%");
            else
            label.setText("You Suck! You got a " + percent + "%");
        }
        else{
            currentState = game.getState(list);
            label.setText("What is the capital of " + currentState + "?");
        }
    }
    
}
