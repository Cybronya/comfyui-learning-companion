# JoyAI_Image_ENCODER

## 节点类型

`JoyAI_Image_ENCODER`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `clip:CLIP`（7 次）
- `image:IMAGE`（7 次）
- `prompt:STRING`（7 次）
- `infer_device:COMBO`（7 次）
- `save_emb:BOOLEAN`（7 次）

## 输出

- `positive:CONDITIONING`（7 次）
- `negative:CONDITIONING`（7 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["女人在海边玩水，保持五官100%不变", "cuda", true]`（4 次）
- `["同一位蓝发赛博机械少女在阳光下的草原中奔跑，保留原角色的五官、蓝粉渐变双马尾、机械耳侧装置、颈部连接结构和金属身体，不改变人物身份。背景替换并扩展为真实开阔草原场景，草地、空气透视、地平线和天空自然协调。人物动作呈现奔跑状态，发丝与马尾`（2 次）
- `["把图像1角色衣服改成黑色", "cuda", false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
