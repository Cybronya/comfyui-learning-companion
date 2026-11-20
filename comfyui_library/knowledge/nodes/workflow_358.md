# workflow>翻译工作流

## 节点类型

`workflow>翻译工作流`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `图像:IMAGE`（1 次）
- `PreviewImage images:IMAGE`（1 次）
- `图像缩放V2_孤海 图像:IMAGE`（1 次）
- `遮罩:MASK`（1 次）
- `image1:IMAGE`（1 次）
- `image2:IMAGE`（1 次）
- `image3:IMAGE`（1 次）
- `image4:IMAGE`（1 次）
- `image5:IMAGE`（1 次）
- `image6:IMAGE`（1 次）

## 输出

- `image_urls:STRING`（1 次）
- `images:IMAGE`（1 次）
- `宽度:INT`（1 次）
- `高度:INT`（1 次）
- `遮罩:MASK`（1 次）
- `PreviewImage image_urls:STRING`（1 次）
- `PreviewImage images:IMAGE`（1 次）
- `image_url:STRING`（1 次）
- `response:STRING`（1 次）
- `图像:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["#ffffff", 0, 2048, 2048, "自定义宽高", 2048, "Lanczos", "填充_自定颜色", "居中", "总是", "把图片中的语言翻译成日语，其他所有内容都保持不变", 1065964652, "ran`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
