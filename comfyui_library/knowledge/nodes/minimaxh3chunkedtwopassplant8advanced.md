# MiniMaxH3ChunkedTwoPassPlanT8Advanced

## 节点类型

`MiniMaxH3ChunkedTwoPassPlanT8Advanced`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model_name:COMBO`（1 次）
- `target_width:INT`（1 次）
- `target_height:INT`（1 次）
- `temporal_chunk_frames:INT`（1 次）
- `temporal_overlap_frames:INT`（1 次）
- `anchor_strength:FLOAT`（1 次）
- `tile_width:INT`（1 次）
- `tile_height:INT`（1 次）
- `spatial_overlap:INT`（1 次）
- `spatial_fade:INT`（1 次）

## 输出

- `plan:T8_H3_CHUNKED_TWO_PASS_PLAN`（1 次）
- `report_json:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["hunyuanvideo15_latent_upsampler_1080p.safetensors", 1280, 704, 136, 17, 0.999, 512, 512, 128, 32, 256, "smoothstep", "`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
