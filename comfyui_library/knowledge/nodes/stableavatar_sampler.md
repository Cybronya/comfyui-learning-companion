# StableAvatar_Sampler

## 节点类型

`StableAvatar_Sampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL_PIPE_SA`（1 次）
- `emb:MODEL_EMB_E`（1 次）
- `seed:INT`（1 次）
- `cfg:FLOAT`（1 次）
- `sample_text_guide_scale:FLOAT`（1 次）
- `sample_audio_guide_scale:FLOAT`（1 次）
- `steps:INT`（1 次）
- `overlap_window_length:INT`（1 次）
- `overlapping_weight_scheme:COMBO`（1 次）

## 输出

- `latent:LATENT`（1 次）
- `frame_rate:FLOAT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[223937763, "randomize", 6, 3, 5, 25, 9, "uniform"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
