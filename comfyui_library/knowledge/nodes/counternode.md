# CounterNode

## 节点类型

`CounterNode`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `trigger:*`（1 次）
- `counter_id:STRING`（1 次）
- `start_value:INT`（1 次）
- `increment:INT`（1 次）
- `reset:COMBO`（1 次）
- `max_value:INT`（1 次）
- `restart_on_max:COMBO`（1 次）
- `abort_on_max:COMBO`（1 次）
- `seed:INT`（1 次）
- `usage_notes:STRING`（1 次）

## 输出

- `计数值:INT`（1 次）
- `信息:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["lora_angle", 0, 1, "否", 9, "是", "否", 361140746611555, "randomize", "计数器节点\n配合【运行】按钮旁边的批次数量，效果更好，这样【超过上限重新计数】和【超过上限中止运行`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
