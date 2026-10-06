# WanVideoNAG

## 节点类型

`WanVideoNAG`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `model:MODEL`（5 次）
- `conditioning:CONDITIONING`（5 次）
- `nag_scale:FLOAT`（5 次）
- `nag_alpha:FLOAT`（5 次）
- `nag_tau:FLOAT`（5 次）
- `input_type:COMBO`（5 次）
- `inplace:BOOLEAN`（5 次）

## 输出

- `model:MODEL`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[11, 0.25, 2.5, "default", false]`（5 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
