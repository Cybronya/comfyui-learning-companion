# CS-LTXSixGridDirector

## 节点类型

`CS-LTXSixGridDirector`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `model:MODEL`（3 次）
- `clip:CLIP`（3 次）
- `storyboard_images:IMAGE`（3 次）
- `audio_vae:VAE`（3 次）
- `optional_latent:LATENT`（3 次）
- `llm_response:STRING`（3 次）
- `global_prompt:STRING`（3 次）
- `duration_frames:INT`（3 次）
- `duration_seconds:FLOAT`（3 次）
- `timeline_data:STRING`（3 次）

## 输出

- `模型:MODEL`（3 次）
- `正向条件:CONDITIONING`（3 次）
- `视频潜空间:LATENT`（3 次）
- `音频潜空间:LATENT`（3 次）
- `引导数据:GUIDE_DATA`（3 次）
- `帧率:FLOAT`（3 次）
- `合成音频:AUDIO`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["近景侧面，黑衣湿发歌手站在巨大的演唱会舞台边缘，黑色防风外套被汗水和雾气压得发暗，耳返贴在湿发旁，他低着眼握住手麦，嘴唇停在话筒前却没有立刻发声；镜头从虚化的观众灯海缓慢推到他半张被侧光切开的脸，远处人群呼喊渐渐降下去，只剩低频音响余震`（1 次）
- `["中景定镜从客厅灯罩的暖光望向玄关，深色外套男子背着皮质斜挎包推门进来，手还停在门把上，肩膀带着一天的疲惫微微塌下；米色围裙女子站在厨房与餐厅交界处，灰色上衣外套着米色围裙，手指轻轻攥住围裙边，像是等了很久却没有催促，门轴轻响、楼道里的风`（1 次）
- `["夜晚的公寓门口，中景定镜，灰蓝衬衫男子外面套着深色夹克，肩上挂着黑色公文包，米色针织女子穿着浅色长外套、拎着帆布包跟在他身侧，两人从玄关走进客厅，落地窗外城市灯光细碎闪烁；灰蓝衬衫男子脚步先慢下来，回头看了她一眼，米色针织女子垂着眼没有`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
