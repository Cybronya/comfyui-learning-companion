# AuKModelsLoader_Doc

## 节点类型

`AuKModelsLoader_Doc`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `model_name:COMBO`（4 次）
- `qwen_name:COMBO`（4 次）
- `memory_mode:COMBO`（4 次）
- `dtype:COMBO`（4 次）
- `device:COMBO`（4 次）
- `sequential_cfg:BOOLEAN`（4 次）

## 输出

- `engine:AUK_ENGINE_Doc`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["AuK/auk_base.safetensors", "Qwen2.5-Omni-3B", "balanced", "bf16", "cuda:0", true]`（4 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
