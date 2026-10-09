# MiniMaxH3EasyLoader

## 节点类型

`MiniMaxH3EasyLoader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `fl2va_model:COMBO`（1 次）
- `ref2va_model:COMBO`（1 次）
- `text_encoder:COMBO`（1 次）
- `video_vae:COMBO`（1 次）
- `audio_vae:COMBO`（1 次）

## 输出

- `h3_bundle:MINIMAX_H3_BUNDLE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["minimax_h3_hybrid_fl2va_ref2va_b25-49-int8.safetensors", "minimax_h3_hybrid_fl2va_ref2va_b25-49-int8.safetensors", "qw`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
