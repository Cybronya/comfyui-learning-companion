# HunyuanVideoFoley

## 节点类型

`HunyuanVideoFoley`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `images:IMAGE`（6 次）
- `text_prompt:STRING`（6 次）
- `guidance_scale:FLOAT`（6 次）
- `num_inference_steps:INT`（6 次）
- `sample_nums:INT`（6 次）
- `seed:INT`（6 次）
- `negative_prompt:STRING`（6 次）
- `fps:FLOAT`（6 次）
- `output_folder:STRING`（6 次）
- `filename_prefix:STRING`（6 次）

## 输出

- `video_frames:IMAGE`（6 次）
- `audio:AUDIO`（6 次）
- `status_message:STRING`（6 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["A person walks on frozen ice", 4.5, 50, 1, 882197747, "randomize", "Sharp sound, sharp flute sound, noise sound", 16, `（1 次）
- `["The camera is fixed, two little sparrows are chirping, it is raining heavily, and the sound of rain changes smoothly, `（1 次）
- `["The camera is fixed, two little sparrows are chirping, it is raining heavily, and the sound of rain changes smoothly, `（1 次）
- `["", 4.5, 50, 1, 3976808371, "randomize", "", 16, "hunyuan_foley", "foley_", false, 0]`（1 次）
- `["A person walks on frozen ice", 4.5, 50, 1, 3015995411, "randomize", "Sharp sound, sharp flute sound, noise sound", 16,`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
