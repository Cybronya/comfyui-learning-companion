# CLIPTextEncodePixArtAlpha

## 节点类型

`CLIPTextEncodePixArtAlpha`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `clip:CLIP`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）
- `text:STRING`（1 次）

## 输出

- `CONDITIONING:CONDITIONING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1024, 1024, "图像1的衣服穿在图像3的模特身上，与图像2的模特站在一起，在图像2的场景中。"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
