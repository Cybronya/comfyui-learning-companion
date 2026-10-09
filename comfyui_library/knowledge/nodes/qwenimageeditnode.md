# QwenImageEditNode

## 节点类型

`QwenImageEditNode`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（3 次）
- `prompt:STRING`（3 次）
- `api_token:STRING`（3 次）
- `model:STRING`（3 次）
- `negative_prompt:STRING`（3 次）
- `width:INT`（3 次）
- `height:INT`（3 次）
- `steps:INT`（3 次）
- `guidance:FLOAT`（3 次）
- `seed:INT`（3 次）

## 输出

- `edited_image:IMAGE`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["把女孩的衣服变成红色，其他都不变，尤其要保持人物面部特征不变", "", "Qwen/Qwen-Image-Edit", "", 512, 512, 40, 7, 1256873458, "randomize"]`（1 次）
- `["左图的女生换上右图的粉色T恤", "", "Qwen/Qwen-Image-Edit-2509", "", 512, 512, 40, 4, 1626395607, "randomize"]`（1 次）
- `["把女孩的衣服变成红色，其他都不变，尤其要保持人物面部特征不变", "", "Qwen/Qwen-Image-Edit-2509", "", 512, 512, 40, 7, 806154545, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
