# CLIPTextEncodeBREAK

## 节点类型

`CLIPTextEncodeBREAK`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `clip:CLIP`（2 次）
- `text:STRING`（2 次）

## 输出

- `CONDITIONING:CONDITIONING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["masterpiece, 8k, anime cel shading, 1girl, Audrey Hall(正义小姐,诡秘之主), long golden curly hair, emerald green eyes, elegant`（1 次）
- `["lowres, bad anatomy, bad hands, extra fingers, missing fingers, deformed limbs, disfigured face, blurry, ugly, mutated`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
