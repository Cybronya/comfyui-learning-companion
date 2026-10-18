# ManualRefCollage

## 节点类型

`ManualRefCollage`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `model:MODEL`（2 次）
- `clip:CLIP`（2 次）
- `image_1:IMAGE`（2 次）
- `image_2:IMAGE`（2 次）
- `image_3:IMAGE`（2 次）
- `image_4:IMAGE`（2 次）
- `image_5:IMAGE`（2 次）
- `video_frame:IMAGE`（2 次）
- `prompt:STRING`（2 次）
- `layout_json:STRING`（2 次）

## 输出

- `collage:IMAGE`（2 次）
- `alpha_mask:MASK`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["person", "{\"width\":1280,\"height\":1280,\"background\":\"black\",\"items\":[{\"x\":0.1,\"y\":0.72,\"scale\":0.52,\"z`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
