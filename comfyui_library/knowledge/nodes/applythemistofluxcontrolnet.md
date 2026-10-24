# ApplyTheMistoFluxControlNet

## 节点类型

`ApplyTheMistoFluxControlNet`

## 分类

Conditioning

## 作用

ControlNet 控制类节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `controlnet:MistoFluxControlNet`（2 次）
- `image:IMAGE`（2 次）
- `resolution:INT`（1 次）
- `strength:FLOAT`（1 次）

## 输出

- `controlnet_condition:ControlNetCondition`（2 次）
- `cond_image:IMAGE`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[960, 0.5]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
