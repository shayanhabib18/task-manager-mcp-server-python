from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Task-Manager-MCP")

tasks = []


@mcp.tool()
def addTask(title: str):
    task = {
        "task_id": len(tasks) + 1,
        "title": title,
        "isCompleted": False
    }

    tasks.append(task)

    return task


@mcp.tool()
def list_tasks():
    return tasks


@mcp.tool()
def complete_task(taskid: int):
    for i in tasks:
        if i["task_id"] == taskid:
            i["isCompleted"] = True
            return i


@mcp.tool()
def delete_task(taskid:int):
    for i in tasks:
        if i["task_id"]==taskid:
            tasks.remove(i)
            return i

if __name__ == "__main__":
    mcp.run()