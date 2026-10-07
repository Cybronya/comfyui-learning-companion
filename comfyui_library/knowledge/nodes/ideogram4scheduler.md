# Ideogram4Scheduler

## 节点类型

`Ideogram4Scheduler`

## 分类

Sampling

## 作用

调度器：控制去噪步长序列（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `steps:INT`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）
- `mu:FLOAT`（1 次）
- `std:FLOAT`（1 次）

## 输出

- `SIGMAS:SIGMAS`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[20, 1024, 1024, 0.5, 1.75]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
