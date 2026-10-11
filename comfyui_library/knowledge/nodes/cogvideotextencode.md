# CogVideoTextEncode

## 节点类型

`CogVideoTextEncode`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `clip:CLIP`（8 次）
- `prompt:STRING`（8 次）
- `strength:FLOAT`（8 次）
- `force_offload:BOOLEAN`（8 次）

## 输出

- `conditioning:CONDITIONING`（8 次）
- `clip:CLIP`（8 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["The video is not of a high quality, it has a low resolution. Watermark present in eachframe. Strange motion trajectory`（2 次）
- `["", 1, true]`（2 次）
- `["A garden comes to life as a kaleidoscope of butterflies flutters amidst the blossoms, their delicate wings casting sha`（1 次）
- `["Forward camera push, giant mecha Gundam walking on city street, cinematic shot, realistic texture, dynamic perspective`（1 次）
- `["一个美女在跳舞", 1, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
