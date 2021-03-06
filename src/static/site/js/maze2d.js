   /*

        Maze Generator pseudo-code

        1. Make the initial cell the current cell and mark it as visited
        2. While there are unvisited cells
            1. If the current cell has any neighbors which have not been visited
                1. Choose randomly one of the unvisited neighbors
                2. Push the chosen cell to the stack
                3. Remove the wall between the current cell and the chosen cell
                4. Make the chosen cell the current cell and mark it as visited
            2. Otherwise
                1. Pop a cell from the stack
                2. Make it the current cell
        */

        // class Maze {

        function Maze(dimension, x, y, cellSize) {
            this.x = x;
            this.y = y;
            this.map = [];
            this.visited = [];
            this.stack = [];
            this.cellSize = cellSize;
            this.begin = [];
            this.turnArounds = [];
            this.currentPosition = [0, 0];
            this.ballRadius = this.cellSize * 0.4;
            this.linesDrawn = [];

            for (var i=0; i<y; i++) {
                this.map.push( [] );
                this.visited.push( [] );
                for (var j=0; j<x; j++) {
                    this.map[i].push( [1,1,1,1] );
                    this.visited[i].push( false );
                }
            }

            this.generateMap();
        }

        Maze.prototype.unvisitedCellsExist = function() {
            for (var i=0; i<this.y; i++) {
                for (var j=0; j<this.x; j++) {
                    if (this.visited[i][j]) return true;
                }
            }
            return false;
        };

        Maze.prototype.chooseNeighbor = function(cx,cy) {
            var neighbors = [];
            var directions = [];
            if (cx > 0 && !this.visited[cy][cx-1]) 
                { neighbors.push( [cx-1, cy] ); directions.push('W'); }
            if (cx < this.x-1 && !this.visited[cy][cx+1]) 
                { neighbors.push( [cx+1, cy] ); directions.push('E'); }
            if (cy < this.y-1 && !this.visited[cy+1][cx]) 
                { neighbors.push( [cx, cy+1] ); directions.push('S'); }
            if (cy > 0 && !this.visited[cy-1][cx]) 
                { neighbors.push( [cx, cy-1] ); directions.push('N'); }
            if (neighbors.length) {
                r = Math.floor(Math.random()*neighbors.length);
                return [ neighbors[r], directions[r] ];
            } else return false;
        };

        Maze.prototype.removeWall = function(x1, y1, direction) { 
            switch (direction) {
                case 'N':
                    this.map[y1][x1][0] = 0;
                    this.map[y1-1][x1][2] = 0;
                break;
                case 'E':
                    this.map[y1][x1][1] = 0;
                    this.map[y1][x1+1][3] = 0;
                break;
                case 'S':
                    this.map[y1][x1][2] = 0;
                    this.map[y1+1][x1][0] = 0;
                break;
                case 'W':
                    this.map[y1][x1][3] = 0;
                    this.map[y1][x1-1][1] = 0;
                break;
            }
        };

        Maze.prototype.generateMap = function() {
            
            // choose initial cell
            var rx = Math.floor(Math.random()*this.x);
            var ry = Math.floor(Math.random()*this.y);

            this.begin = [rx, ry];

            var cx = rx;
            var cy = ry;
            var nx;
            var ny;

            this.visited[cy][cx] = true;

            var next;
            var nextDirection;

            // while there are still unvisited cells
            while (this.unvisitedCellsExist()) {
                if (this.chooseNeighbor(cx,cy)) {
                    
                    next = this.chooseNeighbor(cx,cy);
                    
                    nx = next[0][0];
                    ny = next[0][1];
                    
                    nextDirection = next[1];
                    this.stack.push( [nx, ny] );
                    this.removeWall(cx, cy, nextDirection);
                    this.visited[ny][nx] = true;

                    cx = nx;
                    cy = ny;
                
                } else if (this.stack.length) {

                    next = this.stack.pop();
                    cx = next[0];
                    cy = next[1];
                    this.turnArounds.push([cx, cy]);
                  
                } else break;
            }

            this.end = [cx, cy];
            this.map[0][0][3] = 0;
            this.map[this.y-1][this.x-1][1] = 0;

        };

        Maze.prototype.getClearRect = function(cx, cy) {
            var fx = cx * this.cellSize + (this.cellSize/2) - (this.ballRadius) - 1;
            var fy = cy * this.cellSize + (this.cellSize/2) - (this.ballRadius) - 1;
            return [fx,fy];
        };

        Maze.prototype.getBallCoords = function(nx, ny) {
            var bx = nx * this.cellSize + (this.cellSize/2);
            var by = ny * this.cellSize + (this.cellSize/2);
            return [bx,by];
        };

        Maze.prototype.clearBall = function() {
            var cl = this.getClearRect(this.currentPosition[0], this.currentPosition[1]);
            ctx.clearRect(cl[0], cl[1], this.ballRadius*2+2, this.ballRadius*2+2);
        };

        Maze.prototype.drawBall = function() {
            var ballCoords = this.getBallCoords(this.currentPosition[0], this.currentPosition[1]);
            ctx.beginPath();
            ctx.arc(ballCoords[0], ballCoords[1], this.ballRadius, 0, 2*Math.PI, false);
            ctx.fillStyle = 'green';
            ctx.fill();
            ctx.lineWidth = 1;
            ctx.strokeStyle = '#003300';
            ctx.stroke();
        };

        Maze.prototype.move = function(d) {
            var dx = d[0];
            var dy = d[1];
            this.clearBall();
            this.currentPosition = [this.currentPosition[0]+dx, this.currentPosition[1]+dy];
            this.drawBall();
        };

        Maze.prototype.lineIsDrawn = function(mt, lt) {
            for (var i=0; i<this.linesDrawn.length; i++) {
                if (this.linesDrawn[i][0][0] == mt[0] &&
                    this.linesDrawn[i][0][1] == mt[1] &&
                    this.linesDrawn[i][1][0] == lt[0] &&
                    this.linesDrawn[i][1][1] == lt[1]) {

                    return true;
                }
            }
            return false;
        };

        Maze.prototype.render = function(ctx) {
            
            var cell;
            var cx;
            var cy;

            ctx.moveTo(0,0);
            ctx.lineWidth = 1;
            ctx.strokeStyle = '#000000';
            
            for (var i=0; i<this.y; i++) {
                for (var j=0; j<this.x; j++) {
                    
                    ctx.beginPath();
                    cell = this.map[i][j];
                    cx = this.cellSize * j;
                    cy = this.cellSize * i;
                    var mt;
                    var lt;

                    if (cell[0]) {
                        mt = [cx, cy];
                        lt = [cx+this.cellSize, cy];
                        if (!this.lineIsDrawn(mt, lt)) {
                            this.linesDrawn.push([mt, lt]);
                            ctx.moveTo(mt[0], mt[1]);
                            ctx.lineTo(lt[0], lt[1]);
                            ctx.stroke();
                        }
                    } 
                    if (cell[1]) {
                        mt = [cx+this.cellSize, cy];
                        lt = [cx+this.cellSize, cy+this.cellSize];
                        if (!this.lineIsDrawn(mt, lt)) {
                            this.linesDrawn.push([mt, lt]);
                            ctx.moveTo(mt[0], mt[1]);
                            ctx.lineTo(lt[0], lt[1]);
                            ctx.stroke();
                        }
                    } 
                    if (cell[2]) {
                        mt = [cx+this.cellSize, cy+this.cellSize];
                        lt = [cx, cy+this.cellSize];
                        if (!this.lineIsDrawn(mt, lt)) {
                            this.linesDrawn.push([mt, lt]);
                            ctx.moveTo(mt[0], mt[1]);
                            ctx.lineTo(lt[0], lt[1]);
                            ctx.stroke();
                        }
                    }
                    if (cell[3]) {
                        mt = [cx, cy+this.cellSize];
                        lt = [cx, cy];
                        if (!this.lineIsDrawn(mt, lt)) {
                            this.linesDrawn.push([mt, lt]);
                            ctx.moveTo(mt[0], mt[1]);
                            ctx.lineTo(lt[0], lt[1]);
                            ctx.stroke();
                        }
                    }

                }
            }

            this.move([0,0]);

        };

        // } end class Maze

        /*
            MazeSolver pseudo-code

            1. start at the entrance
            2. while not at the exit
                1. push the current cell to visited
                2. if exists one or more directions that have not been visited
                    1. push the current cell to pathStack
                    2. choose any direction from those not visited
                    3. move in that direction
                    4. draw path from previous cell to chosen cell
                    5. make the chosen cell the current cell
                3. otherwise backtrack
                    1. pop the pathStack
                    2. remove line from currentCell to popped cell
                    3. do not remove popped cell from visited
        */

        // class MazeSolver {

        function MazeSolver(maze) {
            this.Maze = maze;
            this.position = [0, 0];
            this.pathStack = [];
            this.visited = [];
            this.Maze.clearBall();

            var self = this;
            this.solveStep = function() {
                self.moveForward();
            };
        }

        MazeSolver.prototype.getValidDirections = function(x,y) {
            
            var directions = [];
            
            if (!this.Maze.map[y][x][0]) 
                directions.push([0,-1]);
            if (!this.Maze.map[y][x][1] && (x!=this.Maze.x-1 || y!=this.Maze.y-1)) 
                directions.push([1,0]);
            if (!this.Maze.map[y][x][2]) 
                directions.push([0,1]);
            if (!this.Maze.map[y][x][3] && (x||y)) 
                directions.push([-1,0]);

            var validDirections = [];
            for (var i=0; i<directions.length; i++) {
                var tx = x+directions[i][0];
                var ty = y+directions[i][1];
                if (!this.isVisited(tx,ty)) {
                    validDirections.push(directions[i]);
                }
            }

            return validDirections;
        };

        MazeSolver.prototype.isVisited = function(x,y) {
            for (var i=0; i<this.visited.length; i++) {
                if (this.visited[i][0] == x && this.visited[i][1] == y) 
                    return true;
            }
            return false;
        };

        MazeSolver.prototype.isDeadEnd = function(x,y) {
            if (!this.getValidDirections(x,y).length)
                return true;
            return false;
        };

        MazeSolver.prototype.movePath = function(cx,cy,nx,ny) {
            ctx.lineWidth = 4;
            ctx.strokeStyle = '#5555ff';
            ctx.beginPath();

            ctx.moveTo(cx*this.Maze.cellSize+this.Maze.cellSize/2, 
                cy*this.Maze.cellSize+this.Maze.cellSize/2);
            ctx.lineTo(nx*this.Maze.cellSize+this.Maze.cellSize/2, 
                ny*this.Maze.cellSize+this.Maze.cellSize/2);
            ctx.stroke();
        };

        MazeSolver.prototype.clearPath = function(x,y) {
            ctx.clearRect(x*this.Maze.cellSize+2, y*this.Maze.cellSize+2, 
                this.Maze.cellSize-4, this.Maze.cellSize-4);
        };

        MazeSolver.prototype.isFinished = function() {
            if (this.position[0] == this.Maze.x-1 && this.position[1] == this.Maze.y-1)
                return true;
            return false;
        };

        MazeSolver.prototype.moveForward = function() {
            
            var cx = this.position[0];
            var cy = this.position[1];
            
            this.visited.push([cx,cy]);
            
            if (this.isFinished()) {
                console.log("FINISH");
                clearInterval(this.interval);
                return;
            }

            if (!this.isDeadEnd(cx,cy)) {
                this.pathStack.push([cx,cy]);
                var directions = this.getValidDirections(cx,cy);
                var randomDirection = Math.floor(Math.random()*directions.length);
                
                var nx = cx + directions[randomDirection][0];
                var ny = cy + directions[randomDirection][1];

                this.movePath(cx,cy,nx,ny);
                this.position = [nx,ny];

            } else { 
                this.backtrack();
            }
        };

        MazeSolver.prototype.backtrack = function() {
            var lastCell = this.pathStack.pop();
            this.clearPath(this.position[0], this.position[1]);
            this.position = [lastCell[0], lastCell[1]];
        };

        // } end class MazeSolver


        $(document).keydown(function(e) {
            
            var tx = Maze.currentPosition[0];
            var ty = Maze.currentPosition[1];

            switch (e.keyCode) {

                case 37: // left
                    if (!Maze.map[ty][tx][3]) Maze.move([-1,0]);
                break;
                case 38: // up
                    if (!Maze.map[ty][tx][0]) Maze.move([0,-1]);
                break;
                case 39: // right
                    if (!Maze.map[ty][tx][1]) Maze.move([1,0]);
                break;
                case 40: // down
                    if (!Maze.map[ty][tx][2]) Maze.move([0,1]);
                break;
                case 83: // 's' key
                    solver = new MazeSolver(Maze);
                    solver.interval = setInterval(solver.solveStep, 5);
                break;

            }
        });

        function solveMaze() {
            solver = new MazeSolver(Maze);
            solver.interval = setInterval(solver.solveStep, 5);
        }

        var Maze;
        var Canvas;
        var ctx;
        var solver;

        function start() {
            var cellSize = 25;

            Canvas = window.artboard.canvas;
            Canvas.width = $(window).width()-(cellSize*2);
            Canvas.height = $(window).height()-(cellSize*2)-20;

            var mx = Math.floor((Canvas.width) / cellSize);
            var my = Math.floor((Canvas.height) / cellSize);

            document.body.appendChild(Canvas);
            ctx = Canvas.getContext("2d");

            Maze = new Maze(2, mx, my, cellSize);
            Maze.render(ctx);

        }

