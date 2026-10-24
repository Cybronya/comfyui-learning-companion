# APISR_ModelLoader_Zho

## 节点类型

`APISR_ModelLoader_Zho`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `apisr_model:COMBO`（1 次）

## 输出

- `pipe:APISRMODEL`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["4x_APISR_GRL_GAN_generator.pth"]`（2 次）
- `["2x_APISR_RRDB_GAN_generator.pth"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
