# CLIPVisionLoader

## 节点类型

`CLIPVisionLoader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `clip_name:COMBO`（3 次）

## 输出

- `CLIP_VISION:CLIP_VISION`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["dino_v3_vit_h.safetensors"]`（2 次）
- `["clip_vision_h.safetensors"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
