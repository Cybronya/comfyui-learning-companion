# ModelMergeMOSSImage

## 节点类型

`ModelMergeMOSSImage`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model1:MODEL`（1 次）
- `model2:MODEL`（1 次）
- `video_embedder.:FLOAT`（1 次）
- `text_embedder.proj.:FLOAT`（1 次）
- `text_embedder.blocks.0.:FLOAT`（1 次）
- `text_embedder.blocks.1.:FLOAT`（1 次）
- `time_embedding.:FLOAT`（1 次）
- `shared_block_modulation.:FLOAT`（1 次）
- `layers.0.:FLOAT`（1 次）
- `layers.1.:FLOAT`（1 次）

## 输出

- `MODEL:MODEL`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0.12, 0.3, 0.24, 0.24, 0.24, 0.2, 0.08, 0.08, 0.08, 0.08, 0.08, 0.08, 0.08, 0.08, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
