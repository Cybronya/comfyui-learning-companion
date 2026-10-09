# MiniMaxH3HybridLoader

## 节点类型

`MiniMaxH3HybridLoader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `base_model:COMBO`（2 次）
- `overlay_model:COMBO`（2 次）
- `overlay_preset:COMBO`（2 次）
- `block_range_start:INT`（2 次）
- `block_range_end:INT`（2 次）
- `final_adaln_from_overlay:BOOLEAN`（2 次）
- `custom_overlays:STRING`（2 次）
- `custom_base:STRING`（2 次）
- `weight_dtype:COMBO`（2 次）

## 输出

- `model:MODEL`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["minimax_h3_fl2va_pruned_bf16.safetensors", "minimax_h3_ref2va_pruned_bf16.safetensors", "block_range_adaln", 25, 49, f`（1 次）
- `["minimax_h3_fl2va_bf16.safetensors", "minimax_h3_ref2va_bf16.safetensors", "block_range_adaln", 25, 49, false, "", "", `（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
