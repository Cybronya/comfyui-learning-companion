# workflow/CLIP文本编码器

## 节点类型

`workflow/CLIP文本编码器`

## 分类

Conditioning

## 作用

CLIP/条件相关节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `CLIP:CLIP`（1 次）
- `CLIPTextEncode clip:CLIP`（1 次）
- `CLIPTextEncode 2 clip:CLIP`（1 次）

## 输出

- `条件:CONDITIONING`（1 次）
- `CLIPTextEncode 条件:CONDITIONING`（1 次）
- `CLIPTextEncode 3 条件:CONDITIONING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["yun，3D， A colorful,(Purple:0.8), vibrant  poster, Deep orange gradient Metal material device，car，There are fun decorat`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
