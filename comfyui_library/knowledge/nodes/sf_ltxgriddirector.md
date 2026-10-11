# SF-LTXGridDirector

## 节点类型

`SF-LTXGridDirector`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `model:MODEL`（2 次）
- `clip:CLIP`（2 次）
- `storyboard_images:IMAGE`（2 次）
- `audio_vae:VAE`（2 次）
- `optional_latent:LATENT`（2 次）
- `llm_response:STRING`（2 次）
- `global_prompt:STRING`（2 次）
- `duration_frames:INT`（2 次）
- `duration_seconds:FLOAT`（2 次）
- `timeline_data:STRING`（2 次）

## 输出

- `模型:MODEL`（2 次）
- `正向条件:CONDITIONING`（2 次）
- `视频潜空间:LATENT`（2 次）
- `音频潜空间:LATENT`（2 次）
- `引导数据:GUIDE_DATA`（2 次）
- `帧率:FLOAT`（2 次）
- `合成音频:AUDIO`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["正面词：第一个镜头，左上，中景，2秒，远山夕阳压在亭檐下，青袍男子站在石桌旁，袖口被山风轻轻掀起，紫衣女子背对着他望向山路，发间银饰在暮色里微微晃动，桌上放着一个系紧的蓝布小包，像是刚被取出又迟迟无人打开；镜头以全景定住亭子、石凳和蜿蜒`（1 次）
- `["正面词：第一个镜头，左上，中景，3秒，沈昭宁闭眼站立，呼吸平稳，偶尔有细微的皱眉，光线从左侧透进，檀香气味若有若无。[旁白：\"沈昭宁，沈府嫡长女。\"]\n。第二个镜头，右上，近景，3秒，缓慢向前推进至脸部近景，她眉头微微颤动，嘴角向`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
