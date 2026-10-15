# Yusu-LTXDirector

## 节点类型

`Yusu-LTXDirector`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `model:MODEL`（3 次）
- `clip:CLIP`（3 次）
- `audio_vae:VAE`（3 次）
- `optional_latent:LATENT`（3 次）
- `global_prompt:STRING`（3 次）
- `duration_frames:INT`（3 次）
- `duration_seconds:FLOAT`（3 次）
- `timeline_data:STRING`（3 次）
- `local_prompts:STRING`（3 次）
- `segment_lengths:STRING`（3 次）

## 输出

- `model:MODEL`（3 次）
- `positive:CONDITIONING`（3 次）
- `video_latent:LATENT`（3 次）
- `audio_latent:LATENT`（3 次）
- `guide_data:GUIDE_DATA`（3 次）
- `frame_rate:FLOAT`（3 次）
- `combined_audio:AUDIO`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["美女主播讲话", 900, 18, "{\"segments\":[{\"id\":\"17809118128933xghr\",\"start\":0,\"length\":300,\"prompt\":\"过肩近景，酒红色短褐女子的`（1 次）
- `["", 96, 4, "{\"segments\":[{\"id\":\"1780914218720uz58p\",\"start\":0,\"length\":96,\"prompt\":\"中近景镜头。\\n苏念念坐回餐桌旁，右手紧握`（1 次）
- `["美女主播讲话", 600, 20, "{\"segments\":[{\"id\":\"1780977172693ira8t\",\"start\":0,\"length\":120,\"prompt\":\"8K ultra HD, `（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
