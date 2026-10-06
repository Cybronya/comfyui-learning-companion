# LayerUtility: ImageReel

## 节点类型

`LayerUtility: ImageReel`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 16 个 workflow 中。

## 输入

- `image1:IMAGE`（36 次）
- `image2:IMAGE`（36 次）
- `image3:IMAGE`（36 次）
- `image4:IMAGE`（36 次）
- `image1_text:STRING`（36 次）
- `image2_text:STRING`（36 次）
- `image3_text:STRING`（36 次）
- `image4_text:STRING`（36 次）
- `reel_height:INT`（36 次）
- `border:INT`（36 次）

## 输出

- `reel:Reel`（36 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["画风参考", "原图", "结果图", "image4", 1280, 32]`（6 次）
- `["original", "Final Effect", "image3", "image4", 2048, 32]`（5 次）
- `["原图", "细节程度：高（高细节）", "细节程度：平衡（偏平滑）", "image4", 2048, 32]`（5 次）
- `["原图光影", "去噪后光影", "平滑细节", "image4", 2048, 32]`（5 次）
- `["原图", "润图后", "细节程度：平衡（偏平滑）", "image4", 2048, 32]`（5 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
