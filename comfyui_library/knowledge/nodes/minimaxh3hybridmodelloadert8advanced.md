# MiniMaxH3HybridModelLoaderT8Advanced

## 节点类型

`MiniMaxH3HybridModelLoaderT8Advanced`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `hybrid_artifact:H3_T8_HYBRID_ARTIFACT`（2 次）
- `vram_policy:H3_T8_VRAM_POLICY`（2 次）
- `quality_base:COMBO`（1 次）
- `mode:COMBO`（1 次）
- `weight_dtype:COMBO`（1 次）

## 输出

- `model:MODEL`（2 次）
- `report_json:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["minimax_h3_fl2va_pruned_int8_convrot.safetensors", "base_only", "default"]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
