/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package test;

import java.awt.Point;
import java.util.ArrayList;

/**
 *
 * @author user
 */
public class BackTracking {
    //Properties
    private static int cordinateX = 0;
    private static int cordinateY = 0;
    private static Point point = new Point(-1,-1);
    //This is a cross road property 
    //used the determine a cross road in 
    //the walking
    private Point cr = new Point(-1,-1);
    
     /**moveX()
     * this method walks through the x axis
     * path to find the route
     * @param maze
     * @param path */
    public void moveX(int[][] maze, ArrayList<Point> path){    
        if(BackTracking.cordinateX < maze[0].length && maze[BackTracking.cordinateY][BackTracking.cordinateX] == 1){
            if(!point.equals(new Point(BackTracking.cordinateX,BackTracking.cordinateY))){
                point = new Point(BackTracking.cordinateX,BackTracking.cordinateY);                
                path.add(new Point(BackTracking.cordinateX,BackTracking.cordinateY));
            }
            BackTracking.cordinateX++;
            this.moveX(maze, path);
        }else if(BackTracking.cordinateX < maze[0].length && maze[BackTracking.cordinateY][BackTracking.cordinateX] == 0){
             BackTracking.cordinateX--;
             if(this.cr.equals(new Point(BackTracking.cordinateX,BackTracking.cordinateY))){
                maze[BackTracking.cordinateY][BackTracking.cordinateX] = 0;
                path.remove(new Point(BackTracking.cordinateX,BackTracking.cordinateY));
               
             }else{
                this.cr = new Point(BackTracking.cordinateX,BackTracking.cordinateY);
                point = this.cr;
             }
            this.moveY(maze, path);
        }else if(BackTracking.cordinateY != maze.length - 1 && BackTracking.cordinateX == maze[0].length - 1 && maze[BackTracking.cordinateY][BackTracking.cordinateX] == 1){
            this.moveY(maze, path);
        }
    }
    
    /**moveY()
     * this method walks through the y axis
     * path to find the route
     * @param maze
     * @param path */
    private void moveY(int[][] maze, ArrayList<Point> path){    
        
        if(BackTracking.cordinateY < maze.length - 1 && maze[BackTracking.cordinateY][BackTracking.cordinateX] == 1){
            if(!point.equals(new Point(BackTracking.cordinateX,BackTracking.cordinateY))){
                point = new Point(BackTracking.cordinateX,BackTracking.cordinateY);
                path.add(new Point(BackTracking.cordinateX,BackTracking.cordinateY));
            }
            BackTracking.cordinateY++;
            this.moveY(maze, path);
        }else if(maze[BackTracking.cordinateY][BackTracking.cordinateX] == 0 && BackTracking.cordinateY != maze.length - 1 ){
            BackTracking.cordinateY--;
            if(this.cr.equals(new Point(BackTracking.cordinateX,BackTracking.cordinateY))){
                maze[BackTracking.cordinateY][BackTracking.cordinateX] = 0;
                path.remove(new Point(BackTracking.cordinateX,BackTracking.cordinateY));
                
             }else{
                this.cr = new Point(BackTracking.cordinateX,BackTracking.cordinateY);
                point = this.cr;
            }
            this.moveX(maze, path);
        }else if(BackTracking.cordinateY == maze.length - 1 && BackTracking.cordinateX != maze[0].length){
            this.moveX(maze, path);
            
        }
    }
}
