# DoubaoImageGenerator

## 节点类型

`DoubaoImageGenerator`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `image1:IMAGE`（3 次）
- `image2:IMAGE`（3 次）
- `image3:IMAGE`（3 次）
- `image4:IMAGE`（3 次）
- `image5:IMAGE`（3 次）
- `image6:IMAGE`（3 次）
- `image_batch:IMAGE`（3 次）
- `mode:COMBO`（3 次）
- `prompt:STRING`（3 次）
- `api_key:STRING`（3 次）

## 输出

- `images:IMAGE`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["multi_img2img", "将图1的卡通人物溶入到图2的环境中，站在汽车旁边，保持人物、背景和汽车构图不变", "", "doubao-seedream-4-0-250828", 2048, 2048, 4, true, 120,`（1 次）
- `["img2imgs", "生成图1中角色和一个带着红色发夹的女士在咖啡厅的图像，近景，", "", "doubao-seedream-4-0-250828", 2048, 2048, 4, true, 120, true, 4]`（1 次）
- `["text2img", "发光轮廓，由精致流动的光线线条构成，有着柔和的曲线与优美的形状，在深色背景上散发着明亮的白色光芒，风格空灵简约，属于未来主义光绘，对比度高，有柔和的光影效果，飘渺梦幻的拖影，小王子手拿着玫瑰花。", "", "d`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
