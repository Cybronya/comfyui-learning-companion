# RunningHub OmniWeaving Sampler(TIV2V)

## 节点类型

`RunningHub OmniWeaving Sampler(TIV2V)`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `pipeline:RH_OmniWeaving_Pipeline`（1 次）
- `condition_video:VIDEO`（1 次）
- `ref_image:IMAGE`（1 次）
- `prompt:STRING`（1 次）
- `video_length:INT`（1 次）
- `num_inference_steps:INT`（1 次）
- `seed:INT`（1 次）
- `target_resolution:COMBO`（1 次）
- `fps:INT`（1 次）

## 输出

- `video:VIDEO`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Replace the man in the video with the man in the image.", 81, 20, 621801659735109, "randomize", "480p", 16]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
