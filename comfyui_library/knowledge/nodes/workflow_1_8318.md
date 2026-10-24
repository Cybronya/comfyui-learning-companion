# workflow>保留图1背景

## 节点类型

`workflow>保留图1背景`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `source_path:PATH`（2 次）
- `image:IMAGE`（2 次）
- `文本1:STRING`（2 次）
- `文本2:STRING`（2 次）
- `text:STRING`（2 次）
- `seed:INT`（2 次）
- `attention:COMBO`（2 次）
- `Qwen3_VQA text:STRING`（2 次）
- `model:COMBO`（2 次）
- `quantization:COMBO`（2 次）

## 输出

- `显示帮助:STRING`（2 次）
- `字符串:*`（2 次）
- `CR Text Concatenate 显示帮助:STRING`（2 次）
- `output:*`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["让图像1中的人物摆出与图像2中人物完全相同的姿势。绝对不能更改图像1中人物的风格和衣服，发型，脸部，背景。调整视角和拍摄角度，使其与图像2完全一致。去除图2背景，换为图1背景", 1909, "randomize", "eager", `（1 次）
- `["让图像1中的人物摆出与图像2中人物完全相同的姿势。绝对不能更改图像1中人物的风格和衣服，发型，脸部，背景。调整视角和拍摄角度，使其与图像2完全一致。保留图2背景", 876, "randomize", "eager", "描述背景，不要`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
