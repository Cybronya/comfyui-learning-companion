# KarrasScheduler

## 节点类型

`KarrasScheduler`

## 分类

Sampling

## 作用

调度器：控制去噪步长序列（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `steps:INT`（5 次）
- `sigma_max:FLOAT`（5 次）
- `sigma_min:FLOAT`（5 次）
- `rho:FLOAT`（5 次）

## 输出

- `SIGMAS:SIGMAS`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[8, 0.99, 0.08, 0.3]`（1 次）
- `[6, 1, 0.08, 0.32]`（1 次）
- `[5, 1, 0.2, 0.7]`（1 次）
- `[3, 0.17, 0.06, 0.6]`（1 次）
- `[3, 0.22, 0.06, 0.5]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
