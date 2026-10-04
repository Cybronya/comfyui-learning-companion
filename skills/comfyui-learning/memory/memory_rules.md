# Memory Rules


# 1. Memory Creation


只有满足：

- 可重复使用
- 对未来有帮助
- 用户确认


才保存。


---


# 2. Workflow Memory Rules


保存：


- workflow_name
- location
- category
- models
- nodes
- test_status
- notes


例如：

```
Wan animation workflow

Test:
success

GPU:
RTX4090

VRAM:
22GB
```


---


# 3. Experiment Memory


记录实验：

```
Experiment

    ↓

Change

    ↓

Result

    ↓

Conclusion
```


例如：

```
Model:
Wan2.1

Change:
FP16 -> INT8

Result:
VRAM 下降

Conclusion:
质量可接受
```


---


# 4. User Learning Memory


记录：

用户已经掌握的内容。


例如：

```
User understands:
latent concept

Needs learning:
attention mechanism
```


---


# 5. Memory Quality


Memory 分级：


## Confirmed


用户验证。


## Generated


Agent 推测。


## Temporary


暂存。


---


# 6. Memory Update


旧信息不能直接覆盖。


保留：


- history
- timestamp
- source
