# workflow>clip文本编码

## 节点类型

`workflow>clip文本编码`

## 分类

Conditioning

## 作用

CLIP/条件相关节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `CLIP:CLIP`（1 次）
- `CLIPTextEncode clip:CLIP`（1 次）
- `text:STRING`（1 次）
- `CLIPTextEncode text:STRING`（1 次）

## 输出

- `条件:CONDITIONING`（1 次）
- `CLIPTextEncode 条件:CONDITIONING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["blurry， nsfw,NSFW,(NSFW:2),legs apart, paintings, sketches, (worst quality:2), (low quality:2), (normal quality:2), lo`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
