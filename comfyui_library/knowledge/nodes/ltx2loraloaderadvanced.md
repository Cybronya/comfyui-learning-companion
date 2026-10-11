# LTX2LoraLoaderAdvanced

## 节点类型

`LTX2LoraLoaderAdvanced`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（2 次）
- `opt_lora_path:STRING`（2 次）
- `blocks:SELECTEDDITBLOCKS`（2 次）
- `lora_name:COMBO`（2 次）
- `strength_model:FLOAT`（2 次）
- `video:FLOAT`（2 次）
- `video_to_audio:FLOAT`（2 次）
- `audio:FLOAT`（2 次）
- `audio_to_video:FLOAT`（2 次）
- `other:FLOAT`（2 次）

## 输出

- `model:MODEL`（2 次）
- `rank:STRING`（2 次）
- `loaded_keys_info:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Best_FaceID_v1.0_LoRA.safetensors", 1.5, 1, 0, 0, 1, 1]`（1 次）
- `["ltx-2.3-ID-LoRA-TalkVid-3k-V1.0.safetensors", 1.5, 0, 1, 1, 0, 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
