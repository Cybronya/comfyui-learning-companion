# QwenTE_ImageInfer

## 节点类型

`QwenTE_ImageInfer`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `qwen模型:QWENLLAMA`（1 次）
- `图片:IMAGE`（1 次）
- `输入模式:COMBO`（1 次）
- `提示词:STRING`（1 次）
- `系统提示词:STRING`（1 次）
- `最多帧数:INT`（1 次）
- `最大边长:INT`（1 次）
- `最大生成token:INT`（1 次）
- `温度:FLOAT`（1 次）
- `top_p:FLOAT`（1 次）

## 输出

- `文本:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["文本", "", "", 24, 1024, 4096, 0.7, 0.9, 20, 1, 0, 0, 466022094287289, "randomize", false, true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
