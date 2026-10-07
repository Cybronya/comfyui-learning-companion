# StoryDiffusion_CLIPTextEncode

## 节点类型

`StoryDiffusion_CLIPTextEncode`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `clip:CLIP`（3 次）
- `switch:DIFFCONDI`（3 次）
- `add_function:STORY_CONDITIONING`（3 次）
- `image:IMAGE`（3 次）
- `control_image:IMAGE`（3 次）
- `width:INT`（1 次）
- `height:INT`（1 次）
- `role_text:STRING`（1 次）
- `scene_text:STRING`（1 次）

## 输出

- `positive:CONDITIONING`（3 次）
- `negative:CONDITIONING`（3 次）
- `info:DIFFINFO`（3 次）
- `width:INT`（3 次）
- `height:INT`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1024, 1024, "[GoYounJung] a woman img, wearing a suit, black hair\n", "[GoYounJung] have breakfast by the window", ",be`（1 次）
- `[768, 768, "[Taylor] a woman img, wearing a white T-shirt, blue loose hair.\n[Lecun] a man img,wearing a suit,black hair`（1 次）
- `[768, 768, "[Taylor] a woman img, wearing a white T-shirt, blue loose hair.\n", "[Taylor] wake up in the bed ;", "best",`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
