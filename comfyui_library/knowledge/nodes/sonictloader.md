# SONICTLoader

## 节点类型

`SONICTLoader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 7 个 workflow 中。

## 输入

- `model:MODEL`（7 次）

## 输出

- `model:MODEL_SONIC`（7 次）
- `dtype:DTYPE`（7 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["unet.pth", 1, true, "fp16"]`（6 次）
- `["unet.pth", 1.3, true, "fp16"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
