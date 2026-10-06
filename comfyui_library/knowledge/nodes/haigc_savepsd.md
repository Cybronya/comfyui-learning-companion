# HAIGC_SavePSD

## 节点类型

`HAIGC_SavePSD`

## 分类

Output

## 作用

输出类节点：把结果写到磁盘（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `图像:IMAGE`（3 次）
- `遮罩:MASK`（3 次）
- `图层数据:PSD_LAYERS`（3 次）
- `背景配置:HAIGC_BG_CONFIG`（3 次）
- `文件名前缀:STRING`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["不分层"]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
