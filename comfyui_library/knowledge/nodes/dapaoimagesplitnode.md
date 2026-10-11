# DapaoImageSplitNode

## 节点类型

`DapaoImageSplitNode`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `🖼️ 输入图像:IMAGE`（1 次）
- `↕️ 分割行数:INT`（1 次）
- `↔️ 分割列数:INT`（1 次）
- `🟢 启用模型放大:BOOLEAN`（1 次）
- `🧠 放大模型:COMBO`（1 次）
- `🔍 放大倍数:FLOAT`（1 次）
- `📏 最长边限制:INT`（1 次）
- `🧪 缩放插值:COMBO`（1 次）

## 输出

- `🧩 分割图像批次:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[3, 3, false, "1x-ITF-SkinDiffDetail-Lite-v1.pth", 1, 0, "lanczos"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
