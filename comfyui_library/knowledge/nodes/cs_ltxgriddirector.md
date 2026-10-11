# CS-LTXGridDirector

## 节点类型

`CS-LTXGridDirector`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `model:MODEL`（4 次）
- `clip:CLIP`（4 次）
- `storyboard_images:IMAGE`（4 次）
- `audio_vae:VAE`（4 次）
- `optional_latent:LATENT`（4 次）
- `llm_response:STRING`（4 次）
- `global_prompt:STRING`（4 次）
- `duration_frames:INT`（4 次）
- `duration_seconds:FLOAT`（4 次）
- `timeline_data:STRING`（4 次）

## 输出

- `模型:MODEL`（4 次）
- `正向条件:CONDITIONING`（4 次）
- `视频潜空间:LATENT`（4 次）
- `音频潜空间:LATENT`（4 次）
- `引导数据:GUIDE_DATA`（4 次）
- `帧率:FLOAT`（4 次）
- `合成音频:AUDIO`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["This is a continuous six-shot whimsical fantasy comedy sequence set at the same glowing riverside milk tea stall durin`（1 次）
- `["正面词：电影感真人摄影，现代都市剧照，便服日常装，都市室内与街市场景，自然光与暖黄室内光，浅景深，35mm镜头质感，无文字无水印无边框。第一个镜头（对应3x3九宫格从左上至右下区域）：左上，中景，李强穿蓝色旧T恤坐在单人床边，一手握着彩`（1 次）
- `["正面词：电影感真人摄影，现代都市剧照，便服日常装，都市室内与街市场景，自然光与暖黄室内光，浅景深，35mm镜头质感，无文字无水印无边框。第一个镜头（对应3x3九宫格从左上至右下区域）：左上，中景，李强穿蓝色旧T恤坐在单人床边，一手握着彩`（1 次）
- `["中景定镜，宫殿长廊被暖黄灯笼照出斑驳柱影，黑金长袍男子立在左侧柱间，衣纹暗绣在光里微微发亮，白衣簪花女子站在右侧廊柱后，双手拢在袖中，眼神避开他又忍不住回望，两人隔着一排石柱保持距离，像是刚在无人处停下脚步；镜头从女子低垂的发饰慢慢横移`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
