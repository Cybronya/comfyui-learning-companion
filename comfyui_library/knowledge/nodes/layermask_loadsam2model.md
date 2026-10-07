# LayerMask: LoadSAM2Model

## 节点类型

`LayerMask: LoadSAM2Model`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `sam2_model:COMBO`（4 次）
- `precision:COMBO`（4 次）
- `device:COMBO`（4 次）

## 输出

- `sam2_model:LS_SAM2_MODEL`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["sam2_hiera_base_plus.safetensors", "fp16", "cuda"]`（4 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
