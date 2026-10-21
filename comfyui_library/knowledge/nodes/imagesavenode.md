# ImageSaveNode_孤海

## 节点类型

`ImageSaveNode_孤海`

## 分类

Output

## 作用

输出类节点：把结果写到磁盘（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `图像输入:IMAGE`（1 次）
- `文件名前缀:STRING`（1 次）
- `文件名分隔符:STRING`（1 次）
- `文件名自动序号:COMBO`（1 次）
- `文件名序号位数:INT`（1 次）
- `dpi:INT`（1 次）
- `质量:INT`（1 次）
- `使用原始文件名:BOOLEAN`（1 次）
- `图片格式:STRING`（1 次）

## 输出

- `图像输出:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["排版", "_", "末尾", 2, 2, 100, false, "jpg"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
