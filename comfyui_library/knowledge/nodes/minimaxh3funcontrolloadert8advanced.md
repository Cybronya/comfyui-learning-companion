# MiniMaxH3FunControlLoaderT8Advanced

## 节点类型

`MiniMaxH3FunControlLoaderT8Advanced`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `control_net_name:COMBO`（2 次）

## 输出

- `control_net:H3_T8_FUN_CONTROL`（2 次）
- `report_json:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["MiniMax-H3-Fun-Controlnet-Union.safetensors"]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
