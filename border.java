import javax.swing.*;
import java.awt.BorderLayout;

public class Borderj extends JButton{
    Borderj(){
        setLayout (new BorderLayout (3,4));
        add(new JButton("east"),BorderLayout.EAST);
        add(new JButton("West"),BorderLayout.WEST);
        add(new JButton("Center"),BorderLayout.CENTER);
        add(new JButton("North"),BorderLayout.NORTH);
        add(new JButton("South"),BorderLayout.SOUTH);
    }
    public static void main(String[] args){
        JFrame frame = new JFrame();
        frame.setSize(500,500);
        frame.setVisible(true);
        frame.setTitle("BORDERLAY");
        frame.setLocationRelativeTo(null);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
}