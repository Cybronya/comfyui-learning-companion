# DapaoImageLayoutNode

## 节点类型

`DapaoImageLayoutNode`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `📸 基准图片:IMAGE`（3 次）
- `🖼️ 批次图片:IMAGE`（3 次）
- `📁 使用文件夹:BOOLEAN`（3 次）
- `📂 图片文件夹路径:STRING`（3 次）
- `🎯 排列方向:COMBO`（3 次）
- `📐 基准图尺寸模式:COMBO`（3 次）
- `📏 基准图最长边:INT`（3 次）
- `📐 布局模式:COMBO`（3 次）
- `📊 列数:INT`（3 次）
- `📏 行数:INT`（3 次）

## 输出

- `🖼️ 排列图像:IMAGE`（3 次）
- `ℹ️ 布局信息:STRING`（3 次）
- `📊 总图片数:INT`（3 次）
- `📐 网格尺寸:INT`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[false, "", "左右排列", "默认", 1024, "固定列数", 2, 2, 256, 10, "智能瀑布流", "白色", 20, false, "黑色", 2]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
