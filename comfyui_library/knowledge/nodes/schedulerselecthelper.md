# SchedulerSelectHelper+

## 节点类型

`SchedulerSelectHelper+`

## 分类

Sampling

## 作用

调度器：控制去噪步长序列（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输出

- `STRING:STRING`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[false, false, false, false, false, true, false, false, false, false, false, false, false, false]`（2 次）
- `[false, false, false, false, true, false, false, false, false, false, false, false, false, false]`（1 次）
- `[false, false, false, true, false, false, false, false, false, false, false, false, false, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
