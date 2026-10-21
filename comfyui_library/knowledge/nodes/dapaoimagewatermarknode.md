# DapaoImageWatermarkNode

## 节点类型

`DapaoImageWatermarkNode`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `🖼️ 输入图像:IMAGE`（1 次）
- `🖼️ 水印图像:IMAGE`（1 次）
- `😶‍🌫️ 水印遮罩:MASK`（1 次）
- `📝 水印文本:STRING`（1 次）
- `🔤 水印字体:COMBO`（1 次）
- `🔠 水印大小百分比:INT`（1 次）
- `🫥 水印不透明度:INT`（1 次）
- `🖼️ 水印混合模式:COMBO`（1 次）
- `↔️ 水平位置:COMBO`（1 次）
- `↕️ 垂直位置:COMBO`（1 次）

## 输出

- `🖼️ 水印图像:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Hello AI", "默认字体", 30, 80, "正常", "靠右", "靠下", 2, 2, "#FFFFFF", false, 0, 10, false, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
