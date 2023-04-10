package statescapitals;

import java.util.List;

import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

public class StatesandCapitalsGUI extends Application {

    private StatesandCapitals game;

    public Label labelFactory(String state, List<String> list){
        Label label = new Label("What is the capital of " + state + "?");
        label.setPadding(new Insets(70));
        label.setAlignment(Pos.CENTER);
        list.remove(state);
        return label;
    }

    @Override
    public void start(Stage stage) throws Exception {
        game = new StatesandCapitals();
        List<String> list = game.toArray();
        VBox vbox = new VBox();

        String currentState = game.getState(list);
        Label question = labelFactory(currentState, list);

        TextField answer = new TextField();

        Button check = new Button("Check");
        check.setMaxHeight(Double.POSITIVE_INFINITY);
        check.setMaxWidth(Double.POSITIVE_INFINITY);

        Label result = new Label("Score=0");
        result.setMaxHeight(Double.POSITIVE_INFINITY);
        result.setMaxWidth(Double.POSITIVE_INFINITY);

        CheckChange event = new CheckChange(question, currentState, list, answer, game, result, check);
        check.setOnAction(event);
        answer.setOnAction(event);

        Button exit = new Button("Exit");
        exit.setMaxHeight(Double.POSITIVE_INFINITY);
        exit.setMaxWidth(Double.POSITIVE_INFINITY);
        exit.setOnAction(e -> System.exit(0));
        vbox.getChildren().addAll(question, answer, check, result, exit);

        Scene scene = new Scene(vbox);
        stage.setTitle("States and Capitals");
        stage.setScene(scene);
        stage.show();
    }
    
    public static void main(String[] args){
        launch(args);
    }
}
