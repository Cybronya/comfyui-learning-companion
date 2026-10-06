# TextEncodeQwenImageEditPlus

## 节点类型

`TextEncodeQwenImageEditPlus`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 15 个 workflow 中。

## 输入

- `clip:CLIP`（19 次）
- `vae:VAE`（19 次）
- `image1:IMAGE`（19 次）
- `image2:IMAGE`（19 次）
- `image3:IMAGE`（19 次）
- `prompt:STRING`（19 次）

## 输出

- `CONDITIONING:CONDITIONING`（19 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[""]`（10 次）
- `["woman standing on a rooftop edge, oversized olive green coat, dramatic low side angle, distant gaze, cloudy evening sk`（3 次）
- `["Next Scene: 创建一个正视图，纯白色背景上的全身姿势，一致的照明和风格，没有背景噪音，没有阴影"]`（3 次）
- `["动漫转写实真人"]`（1 次）
- `["改为“深圳书香苑”"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
