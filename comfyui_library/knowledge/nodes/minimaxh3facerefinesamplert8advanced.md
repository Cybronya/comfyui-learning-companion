# MiniMaxH3FaceRefineSamplerT8Advanced

## 节点类型

`MiniMaxH3FaceRefineSamplerT8Advanced`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（2 次）
- `av_latent:LATENT`（2 次）
- `steps:INT`（2 次）
- `denoise:FLOAT`（2 次）
- `shift_video:FLOAT`（2 次）
- `shift_audio:FLOAT`（2 次）
- `sampler_name:COMBO`（2 次）
- `scheduler:COMBO`（2 次）

## 输出

- `model:MODEL`（2 次）
- `sampler:SAMPLER`（2 次）
- `sigmas:SIGMAS`（2 次）
- `report_json:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[12, 0.45, 12, 3, "dual_clock_euler", "native_flow"]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
