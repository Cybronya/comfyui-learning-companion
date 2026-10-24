# LoadLayeredControlV2Pipe

## 节点类型

`LoadLayeredControlV2Pipe`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 6 个 workflow 中。

## 输入

- `offload:BOOLEAN`（6 次）
- `v2_lora:COMBO`（6 次）

## 输出

- `pipe:LayeredControlV2Pipe`（6 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[true, "Qwen-Image-Layered-Control-V2.safetensors"]`（6 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
