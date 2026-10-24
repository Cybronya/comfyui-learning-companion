# ZML_LoadImageFromPath

## 节点类型

`ZML_LoadImageFromPath`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `文件夹路径:STRING`（4 次）
- `索引模式:COMBO`（4 次）
- `图像索引:INT`（4 次）
- `正规化:COMBO`（4 次）
- `读取文本块:COMBO`（4 次）

## 输出

- `图像路径:STRING`（6 次）
- `图像数量:INT`（6 次）
- `图像列表:IMAGE`（4 次）
- `文本块:STRING`（4 次）
- `Name:STRING`（4 次）
- `宽:INT`（2 次）
- `高:INT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "固定索引", 0, "正规", "禁用"]`（3 次）
- `["F:\\服装测试", "固定索引", 4, "正规", "禁用"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
