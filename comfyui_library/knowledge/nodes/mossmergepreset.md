# MOSSMergePreset

## 节点类型

`MOSSMergePreset`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 25 个 workflow 中。

## 输入

- `base_model:MODEL`（25 次）
- `sft_model:MODEL`（25 次）
- `preset:COMBO`（25 次）
- `strength:FLOAT`（25 次）
- `merge_info:STRING`（25 次）
- `m_video_embedder:FLOAT`（25 次）
- `m_text_proj:FLOAT`（25 次）
- `m_text_block0:FLOAT`（25 次）
- `m_text_block1:FLOAT`（25 次）
- `m_time:FLOAT`（25 次）

## 输出

- `MODEL:MODEL`（25 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Balanced", 1, "Balanced | strength 1.00\nvideo_embedder=0.20  text_proj=0.20  text_blocks=0.16/0.16\ntime_embedding=0.`（18 次）
- `["Base-preserve", 1, "Base-preserve | strength 1.00\nvideo_embedder=0.12  text_proj=0.12  text_blocks=0.10/0.10\ntime_em`（3 次）
- `["Balanced", 0.45, "Balanced | strength 0.45\nvideo_embedder=0.09  text_proj=0.09  text_blocks=0.07/0.07\ntime_embedding`（2 次）
- `["SFT-detail", 1, "SFT-detail | strength 1.00\nvideo_embedder=0.30  text_proj=0.30  text_blocks=0.24/0.24\ntime_embeddin`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
