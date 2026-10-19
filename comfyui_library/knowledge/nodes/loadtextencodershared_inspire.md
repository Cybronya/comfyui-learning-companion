# LoadTextEncoderShared //Inspire

## 节点类型

`LoadTextEncoderShared //Inspire`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model_name1:COMBO`（1 次）
- `model_name2:COMBO`（1 次）
- `model_name3:COMBO`（1 次）
- `type:COMBO`（1 次）
- `key_opt:STRING`（1 次）
- `mode:COMBO`（1 次）
- `device:COMBO`（1 次）

## 输出

- `clip:CLIP`（1 次）
- `cache key:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["qwen_2.5_vl_7b.safetensors", "None", "None", "stable_diffusion", "", "Auto", "default"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
