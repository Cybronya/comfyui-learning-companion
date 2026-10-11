# JoyAI_Echo_SM_Clip

## 节点类型

`JoyAI_Echo_SM_Clip`

## 分类

Conditioning

## 作用

CLIP/条件相关节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 9 个 workflow 中。

## 输入

- `clip:COMBO`（10 次）
- `gguf:COMBO`（10 次）
- `connector:COMBO`（10 次）
- `infer_device:COMBO`（10 次）

## 输出

- `clip:CLIP`（10 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["none", "gemma-3-12b-it-qat-Q4_0.gguf", "connector.safetensors", "cuda"]`（10 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
