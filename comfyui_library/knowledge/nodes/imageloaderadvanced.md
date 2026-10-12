# ImageLoaderAdvanced

## 节点类型

`ImageLoaderAdvanced`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:COMBO`（2 次）
- `mask_mode:COMBO`（2 次）
- `mask_blur:FLOAT`（2 次）
- `mask_strength:FLOAT`（2 次）
- `upload:IMAGEUPLOAD`（2 次）

## 输出

- `IMAGE:IMAGE`（2 次）
- `MASK:MASK`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["d781a51050f193d634e5a49f6d7c09ebca6fad1ade8183eb6e3f859d82a0dbd2.png", "alpha", 0, 1, "image"]`（1 次）
- `["f0dcb2bd10a8059ca4762955d18d40f9dc14b9f8b13fe415da2090a838d1db7e.png", "alpha", 0, 1, "image"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
