# FlowMatchEulerDiscreteScheduler (Custom)

## 节点类型

`FlowMatchEulerDiscreteScheduler (Custom)`

## 分类

Sampling

## 作用

调度器：控制去噪步长序列（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `steps:INT`（2 次）
- `start_at_step:INT`（2 次）
- `end_at_step:INT`（2 次）
- `base_image_seq_len:INT`（2 次）
- `base_shift:FLOAT`（2 次）
- `invert_sigmas:COMBO`（2 次）
- `max_image_seq_len:INT`（2 次）
- `max_shift:FLOAT`（2 次）
- `num_train_timesteps:INT`（2 次）
- `shift:FLOAT`（2 次）

## 输出

- `sigmas:SIGMAS`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[8, 0, 9999, 512, 1.0000000000000002, "disable", 2048, 1.15, 1000, 3, 0, "disable", "exponential", "disable", "disable",`（1 次）
- `[9, 0, 1000, 512, 1.0000000000000002, "disable", 2048, 1.1500000000000001, 1000, 3.0000000000000004, 0, "disable", "expo`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
