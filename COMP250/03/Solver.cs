using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public static class Solver
{
    class Node
    {
        public Node parent;
        public GameState.Action incomingAction;
        public GameState state; 
    }

    static List<GameState.Action> allActions = new List<GameState.Action>{
        GameState.Action.Up,
        GameState.Action.Down,
        GameState.Action.Left,
        GameState.Action.Right
    };

    public static List<GameState.Action> Solve(GameState state)
    {
        System.Diagnostics.Stopwatch stopwatch = System.Diagnostics.Stopwatch.StartNew();

        Node root = new Node
        { 
            parent = null, 
            incomingAction = GameState.Action.None, 
            state = state
        };

        Queue<Node> q = new Queue<Node>();
        q.Enqueue(root);

        HashSet<GameState> seenStates = new HashSet<GameState>();
        seenStates.Add(state);

        while (true)
        {
            if (stopwatch.Elapsed.Seconds > 10)
            {
                Debug.LogError("Solver timed out");
                return new List<GameState.Action>();
            }

            Node node = q.Dequeue();

            foreach (GameState.Action action in allActions)
            {
                if (node.state.IsActionAvailable(action))
                {
                    var nextState = node.state.Copy();
                    nextState.DoAction(action);
                    if (nextState.IsSolved)
                    {
                        List<GameState.Action> result = new List<GameState.Action>();
                        result.Add(action);
                        for (; node != null; node = node.parent)
                            result.Insert(0, node.incomingAction);
                        
                        return result;
                    }
                    else if (!seenStates.Contains(nextState))
                    {
                        seenStates.Add(nextState);
                        Node child = new Node
                        {
                            parent = node,
                            incomingAction = action,
                            state = nextState
                        };

                        q.Enqueue(child);
                    }
                }
            }
        }
    }
}
