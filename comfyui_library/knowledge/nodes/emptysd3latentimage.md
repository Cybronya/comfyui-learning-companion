# EmptySD3LatentImage

## 节点类型

`EmptySD3LatentImage`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 12 个 workflow 中。

## 输入

- `width:INT`（12 次）
- `height:INT`（12 次）
- `batch_size:INT`（12 次）

## 输出

- `LATENT:LATENT`（12 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1024, 1024, 1]`（4 次）
- `[1024, 1536, 1]`（3 次）
- `[1328, 1328, 1]`（2 次）
- `[1280, 1568, 1]`（1 次）
- `[864, 1152, 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
