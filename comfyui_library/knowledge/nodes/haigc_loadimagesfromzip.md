# HAIGC_LoadImagesFromZip

## 节点类型

`HAIGC_LoadImagesFromZip`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `zip_file:COMBO`（1 次）

## 输出

- `图像:IMAGE`（1 次）
- `遮罩:MASK`（1 次）
- `提示词:STRING`（1 次）
- `视频:VIDEO`（1 次）
- `音频:AUDIO`（1 次）
- `文本:STRING`（1 次）
- `命名信息:*`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["81dd314d4efe4864f1ab3afdb51f0c20a0942b7dc878fa825b4592a9819bded9.zip", null]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
