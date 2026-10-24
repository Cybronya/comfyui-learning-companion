# LoadImagesToBatch

## 节点类型

`LoadImagesToBatch`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `images:IMAGEBASE64`（2 次）

## 输出

- `IMAGE:IMAGE`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[{"base64": ["data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAzAAAATICAYAAADDbiDhAAAQAElEQVR4AeT9iZokOXKlC8rR6Pd/n7v07Z7b`（1 次）
- `[{"base64": ["data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAxcAAAR2CAYAAABOL0pNAAAQAElEQVR4Aey9B4BkR3E3/qvuN3lzuJxPd7rT`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
