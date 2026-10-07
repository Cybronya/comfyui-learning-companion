# ByteDance2ReferenceNodeV2

## 节点类型

`ByteDance2ReferenceNodeV2`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 11 个 workflow 中。

## 输入

- `model.reference_images.image_1:IMAGE`（11 次）
- `model.reference_videos.video_1:VIDEO`（11 次）
- `model.reference_audios.audio_1:AUDIO`（11 次）
- `model.reference_assets.asset_1:STRING`（11 次）
- `model.reference_images.image_2:IMAGE`（8 次）
- `model.reference_images.image_3:IMAGE`（4 次）
- `model.reference_videos.video_2:VIDEO`（2 次）
- `model.prompt:STRING`（2 次）
- `model.reference_assets.asset_2:STRING`（1 次）

## 输出

- `VIDEO:VIDEO`（11 次）
- `draft_task_id:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Seedance 2.0 Mini", "Shot 1: Medium close-up, three-quarter angle. The model holds the bottle from @Image 1 in her rig`（1 次）
- `["Seedance 2.0", "fast-paced fashion showcase video, fisheye lens extreme wide-angle distortion, glitch transitions and `（1 次）
- `["Seedance 2.0", "Using the attached character as the subject, generate a continuous cycling sequence where the environm`（1 次）
- `["Seedance 2.5", "Use @asset_1 as a reference character. A young person with curly auburn hair floats underwater, eyes g`（1 次）
- `["Seedance 2.5 Draft", "Photoreal cinematic sci-fi action fashion film, 5 seconds, a high-end techwear campaign crossed `（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
