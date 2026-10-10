# DownloadAndLoadNLFModel

## 节点类型

`DownloadAndLoadNLFModel`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `url:COMBO`（1 次）
- `warmup:BOOLEAN`（1 次）

## 输出

- `nlf_model:NLFMODEL`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["https://github.com/isarandi/nlf/releases/download/v0.3.2/nlf_l_multi_0.3.2.torchscript", true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
