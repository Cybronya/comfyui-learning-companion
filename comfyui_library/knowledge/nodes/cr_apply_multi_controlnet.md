# CR Apply Multi-ControlNet

## 节点类型

`CR Apply Multi-ControlNet`

## 分类

Conditioning

## 作用

ControlNet 控制类节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `base_positive:CONDITIONING`（2 次）
- `base_negative:CONDITIONING`（2 次）
- `controlnet_stack:CONTROL_NET_STACK`（2 次）

## 输出

- `base_pos:CONDITIONING`（2 次）
- `base_neg:CONDITIONING`（2 次）
- `show_help:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["On"]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
