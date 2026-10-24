# workflow/展示文本

## 节点类型

`workflow/展示文本`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `ref_image:IMAGE`（3 次）
- `文本:STRING`（3 次）
- `ShowText|pysssss text:STRING`（2 次）
- `ShowText|pysssss 2 text:STRING`（1 次）

## 输出

- `字符串:STRING`（5 次）
- `ShowText|pysssss 字符串:STRING`（3 次）
- `ShowText|pysssss 2 字符串:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["The title is \"Happy New Year\". Please provide a detailed description of this picture, but do not describe the style `（1 次）
- `["Please provide a detailed description of this image. If any characters in the image are familiar to you, such as celeb`（1 次）
- `["Please provide a detailed description of this image, but do not describe the style of the image, and if there are peop`（1 次）
- `[["The costume is a red, traditional-inspired jacket with intricate golden patterns, trimmed in soft white fur. The back`（1 次）
- `[[", (shinny skin, reflections on the skin, skin reflections:1.5)"], ["outdoor,model show,proscenium，Depth of field, bac`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
