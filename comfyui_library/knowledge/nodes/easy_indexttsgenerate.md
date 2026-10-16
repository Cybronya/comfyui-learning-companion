# easy indexTTSGenerate

## 节点类型

`easy indexTTSGenerate`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `indextts_model:EASY_INDEXTTS_MODEL`（2 次）
- `reference_audio:AUDIO`（2 次）
- `reference_audios:AUDIOS`（2 次）
- `emotions:EASY_INDEXTTS_EMOTIONS`（2 次）
- `text:STRING`（2 次）
- `unload_model:BOOLEAN`（2 次）
- `do_sample:BOOLEAN`（2 次）
- `temperature:FLOAT`（2 次）
- `top_p:FLOAT`（2 次）
- `top_k:INT`（2 次）

## 输出

- `audio:AUDIO`（2 次）
- `seed:INT`（2 次）
- `subtitle:STRING`（2 次）
- `subtitle_text:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["[s1] 测试", false, false, 0.1, 0.9000000000000001, 30, 3, 10, 0, 1815, 120, 1242452022, "randomize", 1.0000000000000002]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
