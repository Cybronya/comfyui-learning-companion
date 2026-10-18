# T8MuLaCoverGenerate

## 节点类型

`T8MuLaCoverGenerate`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `model:MULACOVER_MODEL`（2 次）
- `condition:MULACOVER_CONDITION`（2 次）
- `lyrics:STRING`（2 次）
- `style_tags:STRING`（2 次）
- `duration_seconds:INT`（2 次）
- `cfg_scale:FLOAT`（2 次）
- `temperature:FLOAT`（2 次）
- `topk:INT`（2 次）
- `seed:INT`（2 次）
- `decode_seed:INT`（2 次）

## 输出

- `audio:AUDIO`（2 次）
- `output_info:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "topic:[love]; genre:[pop]; instrument:[piano, strings, drums]; mood:[warm]", 30, 1.5, 1, 250, 955290940447221, "ra`（1 次）
- `["[Verse]\n", "topic:[unspecified]; genre:[pop]; instrument:[piano, strings, drums]; mood:[warm]", 30, 1.500000000000000`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
