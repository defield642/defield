import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import javax.swing.event.*;
public class SwingThread extends JFrame implements ActionListener {
private static int count = 0;
public SwingThread(String title) {
super(title);
JButton incrementButton = new JButton("increment");
incrementButton.addActionListener(this);
Container contentPane = getContentPane();
contentPane.add(incrementButton);
}
public void actionPerformed(ActionEvent evt) {
count = 0;
}
// Main entry point
public static void main(String[] args) {
JFrame frame = new SwingThread("Swing Thread Demo");
// Java idiom for handling window closing events
frame.addWindowListener(new WindowAdapter() {
public void windowClosing(WindowEvent e) {
System.exit(0);
}
} );
// pack() will resize the frame to its preferred size
// which is calculated by adding up the preferred size
// of the components within the frame.
frame.pack();
/
while (true) {
System.out.println(count);
count++;
try {
java.lang.Thread.sleep(1 * 1000); // Wait 1 second
}
catch (java.lang.InterruptedException e) {}
}
}
}