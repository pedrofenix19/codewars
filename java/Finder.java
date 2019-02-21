public class Finder {

    private class Point{
        int x;
        int y;

        public Point(int x, int y){
            this.x = x;
            this.y = y;
        }

        public String toString(){
            return "(" + this.x + "," + this.y + ")";
        }
    }
    
    static boolean pathFinder(String maze) {
        // Your code here!!
        return false;
    }

    public static void main(String[] args){
        Point hola = new Point(1,2);
        System.out.println(hola);

        String a = ".W.\n"+
                 ".W.\n"+
                 "...",
               
             b = ".W.\n"+
                 ".W.\n"+
                 "W..",
               
             c = "......\n"+
                 "......\n"+
                 "......\n"+
                 "......\n"+
                 "......\n"+
                 "......",
               
             d = "......\n"+
                 "......\n"+
                 "......\n"+
                 "......\n"+
                 ".....W\n"+
                 "....W.";

        System.out.println(a + "\n" + Finder.pathFinder(a) + "\n");
        System.out.println(b + "\n" + Finder.pathFinder(b) + "\n");
        System.out.println(c + "\n" + Finder.pathFinder(c) + "\n");
        System.out.println(d + "\n" + Finder.pathFinder(d) + "\n");
    }
}