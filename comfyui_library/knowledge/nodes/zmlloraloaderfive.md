# ZmlLoraLoaderFive

## 节点类型

`ZmlLoraLoaderFive`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `模型:MODEL`（2 次）
- `CLIP:CLIP`（2 次）
- `lora_1_名称:COMBO`（2 次）
- `权重_1_强度:FLOAT`（2 次）
- `lora_2_名称:COMBO`（2 次）
- `权重_2_强度:FLOAT`（2 次）
- `lora_3_名称:COMBO`（2 次）
- `权重_3_强度:FLOAT`（2 次）
- `lora_4_名称:COMBO`（2 次）
- `权重_4_强度:FLOAT`（2 次）

## 输出

- `输出_模型:MODEL`（2 次）
- `输出_CLIP:CLIP`（2 次）
- `txt_内容:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["None", 1, "None", 1, "None", 1, "None", 1, "None", 1]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
