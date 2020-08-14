#! /usr/bin/python3

from flask import Flask,render_template,request, flash
import requests
import json


app = Flask(__name__)
app.secret_key = 'coses'


labels = [
    'Take Out', 'Take Out (expected)',
    'Groceries', 'Groceries (expected)',
    'Entertainment', 'Entertainment (expected)',
    'Misc', 'Misc (expected)'
]

@app.route('/')
def main():
    return render_template('welcome.html')

@app.route('/get_goals')
def goals():
    return render_template('goals.html')

@app.route('/set_goals', methods = ["POST"])
def set_goals():
    req = request.form
    print(req)
    # budg = req.get("t1")
    # print("==========")
    # print("HELLO")
    # type(req.get("t1"))
    # # req.get("t1")
    # print("==========")
    budg = int(req.get("t1"))
    # print("==========")
    # print("==========")
    dining = int(req.get("t2"))
    groceries = int(req.get("t3"))
    ent = int(req.get("t4"))
    misc = int(req.get("t5"))
    if(dining+groceries+ent+misc>100):
        flash('Your percentages added up to more than 100%! Please try again')
        return render_template('goals.html')
    if(dining+groceries+ent+misc<100):
        flash('Your percentages added up to less than 100%! Please try again')
        return render_template('goals.html')
    SPENT = 0
    values = []
    # goal_list = []
    values.append(SPENT)
    values.append(int(budg * (dining/100)))
    goal_dining= (int(budg * (dining/100)))
    values.append(SPENT)
    values.append(int(budg * (groceries/100)))
    goal_groc = (int(budg * (groceries/100)))
    values.append(SPENT)
    values.append(int(budg * (ent/100)))
    goal_ent = (int(budg * (ent/100)))
    values.append(SPENT)
    values.append(int(budg * (misc/100)))
    goal_misc= (int(budg * (misc/100)))
    bar_labels=labels
    maxy = max(values)
    # maxy = budg
    return render_template('graphs.html',title='Monthly Expenses', max=maxy, labels=bar_labels, values=values, budg = budg, dining = SPENT, groceries = SPENT,ent = SPENT, misc = SPENT,goal_dining = goal_dining, goal_groc = goal_groc, goal_ent = goal_ent, goal_misc = goal_misc )
@app.route('/update_spending', methods=["POST"])
def update_spending():
    req = request.form
    print("========")
    print(req)
    print("========")
    budg = int(req.get("budg"))
    d = int(req.get("old_dining"))
    g = int(req.get("old_groceries"))
    e = int(req.get("old_ent"))
    m = int(req.get("old_misc"))
    d_goal = int(req.get("goal_dining"))
    g_goal = int(req.get("goal_groceries"))
    e_goal = int(req.get("goal_ent"))
    m_goal = int(req.get("goal_misc"))
    if(req.get("takeout")== "takeout"):
        d = d + int(req.get("amount"))
    if(req.get("groceries")== "groceries"):
        g = g + int(req.get("amount"))
    if(req.get("ent")== "ent"):
        e = e + int(req.get("amount"))
    if(req.get("misc")== "misc"):
        m = m + int(req.get("amount"))
    values = []
    values.append(d)
    values.append(d_goal)
    values.append(g)
    values.append(g_goal)
    values.append(e)
    values.append(e_goal)
    values.append(m)
    values.append(m_goal)
    for i in values:
        print(i)
    maxy = max(values)
    bar_labels=labels
    if(d> d_goal):
        flash('You exceeded your dining out goal! No more take out!')
    if(g> g_goal):
        flash("You exceeded your groceries goal! Somebody's been mighty hungry!")
    if(e> e_goal):
        flash('You exceeded your entertainment goal! Stop watching TV and do some work!')
    if(m> m_goal):
        flash('You exceeded your misc goal! What are you spending your money on?')
    return render_template('graphs.html',title='Monthly Expenses', max=maxy, labels=bar_labels, values=values, budg = budg, dining = d, groceries = g,ent = e, misc = m,goal_dining = d_goal, goal_groc = g_goal, goal_ent = e_goal, goal_misc = m_goal )
if __name__ == '__main__':
    app.debug = True
    app.run()
