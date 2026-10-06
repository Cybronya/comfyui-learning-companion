# BasicScheduler

## 节点类型

`BasicScheduler`

## 分类

Sampling

## 作用

调度器：控制去噪步长序列（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 53 个 workflow 中。

## 输入

- `model:MODEL`（66 次）
- `scheduler:COMBO`（66 次）
- `steps:INT`（66 次）
- `denoise:FLOAT`（66 次）

## 输出

- `SIGMAS:SIGMAS`（66 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["beta", 30, 1]`（14 次）
- `["simple", 2, 1]`（6 次）
- `["beta", 4, 1]`（5 次）
- `["beta", 8, 1]`（5 次）
- `["simple", 8, 1]`（5 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
