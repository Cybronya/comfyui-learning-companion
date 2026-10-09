# WanVideoSchedulerv2

## 节点类型

`WanVideoSchedulerv2`

## 分类

Sampling

## 作用

调度器：控制去噪步长序列（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `sigmas:SIGMAS`（1 次）
- `scheduler:COMBO`（1 次）
- `steps:INT`（1 次）
- `shift:FLOAT`（1 次）
- `start_step:INT`（1 次）
- `end_step:INT`（1 次）
- `enhance_hf:BOOLEAN`（1 次）

## 输出

- `scheduler:WANVIDEOSCHEDULER`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["euler", 10, 12, 0, -1, false, "<img src='data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAoAAAAHgCAYAAAA10dzkAAAAOnRFWHR`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
