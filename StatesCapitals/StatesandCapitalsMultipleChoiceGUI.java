package statescapitals;

import javafx.event.EventHandler;
import javafx.event.ActionEvent;
import java.util.LinkedList;
import java.util.List;
import java.util.Random;

import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.layout.HBox;
import javafx.scene.layout.Priority;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

public class StatesandCapitalsGuiForPeopleWhoAreBad extends Application{

    private static StatesandCapitals game = new StatesandCapitals();
    private static List<String> entireList = game.toArray();
    private static Random random = new Random();
    private static String currentState;

    public List<Integer> randomNumbers(){
        List<Integer> randomList = new LinkedList<>();
        while (randomList.size() < 5){
            int k = random.nextInt(5);
            if(!(randomList.contains(k))){
                randomList.add(k);
            }
        }
        return randomList;
    }

    public List<String> fourRandom(){
        List<String> tmp = new LinkedList<>();
        entireList.remove(currentState);
        while (tmp.size() < 4){
            int i = random.nextInt(entireList.size());
            if(!(tmp.contains(game.getCapital(entireList.get(i)))))
                tmp.add(game.getCapital(entireList.get(i)));
        }
        entireList.add(currentState);
        return tmp;
    }

    public Button buttonFactory(String capital){
        Button button = new Button(capital);
        button.setMaxSize(Double.MAX_VALUE, Double.MAX_VALUE);
        HBox.setHgrow(button, Priority.ALWAYS);
        return button;
    }

    public EventHandler<ActionEvent> exit(){
        return e -> System.exit(0);
    }

    public void setCurrentState(String state){currentState = state;}
    public String getCurrentState(){return currentState;}

    @Override
    public void start(Stage stage) throws Exception {
        VBox vbox = new VBox();
        List<String> currentList = game.toArray();

        currentState = game.getState(currentList);
        Label question = new Label("What is the capital of " + currentState + "?");
        question.setMaxSize(500, 400);
        question.setPadding(new Insets(70));
        question.setAlignment(Pos.CENTER);

        HBox hbox = new HBox();

        List<String> fourRandomStart = fourRandom();
        fourRandomStart.add(game.getCapital(currentState));

        List<Integer> randomNumbers = randomNumbers();
        Button button1 = buttonFactory(fourRandomStart.get(randomNumbers.get(0)));
        Button button2 = buttonFactory(fourRandomStart.get(randomNumbers.get(1)));
        Button button3 = buttonFactory(fourRandomStart.get(randomNumbers.get(2)));
        Button button4 = buttonFactory(fourRandomStart.get(randomNumbers.get(3)));
        Button button5 = buttonFactory(fourRandomStart.get(randomNumbers.get(4)));

        Label result = new Label("Score=0");
        result.setMaxSize(200, 40);

        Button exit = new Button("Exit");
        exit.setMaxSize(40, 40);
        exit.setOnAction(exit());
        button1.setOnAction(new MultipleChoice(button1, this, button2, button3, button4, button5, question, game, result, currentList));
        button2.setOnAction(new MultipleChoice(button2, this, button1, button3, button4, button5, question, game, result, currentList));
        button3.setOnAction(new MultipleChoice(button3, this, button1, button2, button4, button5, question, game, result, currentList));
        button4.setOnAction(new MultipleChoice(button4, this, button1, button2, button3, button5, question, game, result, currentList));
        button5.setOnAction(new MultipleChoice(button5, this, button1, button2, button3, button4, question, game, result, currentList));
        hbox.getChildren().addAll(button1, button2, button3, button4, button5);
        vbox.getChildren().addAll(question, hbox, result, exit);

        Scene scene = new Scene(vbox);
        stage.setTitle("States and Capitals");
        stage.setScene(scene);
        stage.show();   
    }

    public static void main(String[] args){
        launch(args);
    }
}