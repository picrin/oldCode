import java.applet.*;
import java.awt.*;

public class DrawingLines extends Applet{
	int width, height;
	public void init(){
		this.width = getSize().width;
		this.height = getSize().height;
		setBackground(Color.black);
	}
	public void paint(Graphics g){
		g.setColor(Color.blue);
		for (int i = 0; i <= 10; i++){
			g.drawLine(this.width, this.height, i * width / 10, 0);
			g.drawCircle(this.width/2, this.height/2);
		}
	}
}
