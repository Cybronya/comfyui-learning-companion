# Project Knowledge Rules


# 1. Knowledge Categories


项目知识分为：


## Workflow Knowledge


包含：


- workflow json
- workflow metadata
- workflow explanation



---


## Node Knowledge


包含：


- node name
- node function
- input
- output
- usage



---


## Model Knowledge


包含：


- model
- architecture
- requirement
- compatibility



---


## Experience Knowledge


来自：


memory


例如：

```
tested
failed
recommended
```



---


# 2. Knowledge Relationship


建立关系：

```
Workflow

    ↓

uses

    ↓

Node



Workflow

    ↓

requires

    ↓

Model



Workflow

    ↓

has

    ↓

Experience



Node

    ↓

supports

    ↓

Model
```


---


# 3. Knowledge Index


维护：


project_index.json


记录：


- asset count
- category
- location
- update time


---


# 4. Update Rules


新增资源：

执行：

```
scan

    ↓

analyze

    ↓

index

    ↓

update
```


---


# 5. Knowledge Quality


状态：


## Verified

人工确认。


## Analyzed

Agent 分析。


## Unknown

未知。
