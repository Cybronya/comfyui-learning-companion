# LlamaServeDocH3OmniGenerate

## 节点类型

`LlamaServeDocH3OmniGenerate`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `server_config:LLAMA_SERVER_CONFIG`（2 次）
- `ref_images.ref_image_0:IMAGE`（2 次）
- `ref_videos.ref_video_0:IMAGE`（2 次）
- `ref_video_audios.ref_video_audio_0:AUDIO`（2 次）
- `ref_audios.ref_audio_0:AUDIO`（2 次）
- `mode:COMBO`（2 次）
- `raw_prompt:STRING`（2 次）
- `duration:INT`（2 次）
- `resolution:COMBO`（2 次）
- `max_tokens:INT`（2 次）

## 输出

- `text:STRING`（2 次）
- `performance_json:STRING`（2 次）
- `groups:MMX_DIR_GROUP`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["I2AV", "以<Picture 1> 作为首帧，小狗跑向镜头", 5, "16:9", 2048, 0.2, 20, 0.9, 0.05, 1.05, 652290846707590, "randomize", "off", fal`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
