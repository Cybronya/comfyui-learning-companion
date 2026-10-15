# BerniniScheduler

## 节点类型

`BerniniScheduler`

## 分类

Sampling

## 作用

调度器：控制去噪步长序列（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 6 个 workflow 中。

## 输入

- `sigmas:SIGMAS`（12 次）
- `scheduler:COMBO`（12 次）
- `steps:INT`（12 次）
- `shift:FLOAT`（12 次）
- `start_step:INT`（12 次）
- `end_step:INT`（12 次）
- `enhance_hf:BOOLEAN`（12 次）

## 输出

- `scheduler:WANVIDEOSCHEDULER`（12 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["euler", 8, 5, 0, 4, false]`（2 次）
- `["euler", 8, 5, 4, 1000, false]`（2 次）
- `["euler", 8, 5, 0, 4, false, "<img src='data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAoAAAAHgCAYAAAA10dzkAAAAOnRFWHRTb2`（1 次）
- `["euler", 8, 5, 4, 1000, false, "<img src='data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAoAAAAHgCAYAAAA10dzkAAAAOnRFWHR`（1 次）
- `["euler", 8, 5, 0, 4, false, "<img src='data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAoAAAAHgCAYAAAA10dzkAAAAOnRFWHRTb2`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
