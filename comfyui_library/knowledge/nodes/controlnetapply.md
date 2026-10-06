# ControlNetApply

## 节点类型

`ControlNetApply`

## 分类

Conditioning

## 作用

ControlNet 控制类节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `conditioning:CONDITIONING`（3 次）
- `control_net:CONTROL_NET`（3 次）
- `image:IMAGE`（3 次）

## 输出

- `CONDITIONING:CONDITIONING`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0.45]`（2 次）
- `[0.3]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
