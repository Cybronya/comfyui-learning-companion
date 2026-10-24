# LHSTW30M_BatchLoadImageList

## 节点类型

`LHSTW30M_BatchLoadImageList`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `path:STRING`（1 次）
- `image_limit:INT`（1 次）
- `start_index:INT`（1 次）
- `always_load:BOOLEAN`（1 次）
- `sort_method:COMBO`（1 次）

## 输出

- `图像:IMAGE`（1 次）
- `遮罩:MASK`（1 次）
- `文件路径:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["C:\\Users\\ASUS\\Desktop\\测试", 100, 0, false, "None"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
