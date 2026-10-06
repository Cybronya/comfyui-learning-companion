# RH_RhartImageG25FlareImageToImage

## 节点类型

`RH_RhartImageG25FlareImageToImage`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `image1:IMAGE`（5 次）
- `image2:IMAGE`（5 次）
- `image3:IMAGE`（5 次）
- `image4:IMAGE`（5 次）
- `image5:IMAGE`（5 次）
- `image6:IMAGE`（5 次）
- `image7:IMAGE`（5 次）
- `image8:IMAGE`（5 次）
- `image9:IMAGE`（5 次）
- `image10:IMAGE`（5 次）

## 输出

- `image:IMAGE`（5 次）
- `url:STRING`（5 次）
- `response:STRING`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Apply image 2's lighting (direction, color temperature, contrast, light spots) to image 1. Keep image 1's composition,`（2 次）
- `["Apply image 1's lighting to image 2. Keep image 2's composition, subject, pose, scene and content. Re-light only: repr`（1 次）
- `["Make image 1's tiger run through image 2's snowy mountain scene. Keep image 1's tiger's shape, fur color and posture d`（1 次）
- `["", "16:9", "1k", false, 2031632758, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
