# HAIGC_ImagesToPPTX

## 节点类型

`HAIGC_ImagesToPPTX`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `图像列表:IMAGE`（1 次）
- `文件名前缀:STRING`（1 次）
- `幻灯片尺寸:COMBO`（1 次）
- `填充方式:COMBO`（1 次）
- `边距(px@96DPI):INT`（1 次）
- `图片格式:COMBO`（1 次）
- `JPEG质量:INT`（1 次）

## 输出

- `ZIP相对路径:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["ppt/HAIGC", "首图尺寸(96DPI)", "适应(留白)", 50, "PNG", 92]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
