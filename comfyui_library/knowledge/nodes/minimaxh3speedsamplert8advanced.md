# MiniMaxH3SPEEDSamplerT8Advanced

## 节点类型

`MiniMaxH3SPEEDSamplerT8Advanced`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（1 次）
- `speed_plan:H3_T8_SPEED_PLAN`（1 次）
- `speed_source:H3_T8_SPEED_SOURCE`（1 次）
- `shift_audio:FLOAT`（1 次）
- `seed:INT`（1 次）
- `execution_scope:COMBO`（1 次）
- `dct_chunk_size:INT`（1 次）

## 输出

- `av_latent:LATENT`（1 次）
- `mux_audio:AUDIO`（1 次）
- `conditioned_prompt:STRING`（1 次）
- `media_map_json:STRING`（1 次）
- `report_json:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[3, 2608194001, "fixed", "turbo8_t2va_research_exp", 64]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
