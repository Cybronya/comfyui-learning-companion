# easy indexTTSGenerateSimple

## 节点类型

`easy indexTTSGenerateSimple`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `indextts_model:EASY_INDEXTTS_MODEL`（4 次）
- `reference_audio:AUDIO`（4 次）
- `reference_audios:AUDIOS`（4 次）
- `emotions:EASY_INDEXTTS_EMOTIONS`（4 次）
- `text:STRING`（4 次）
- `unload_model:BOOLEAN`（4 次）
- `seed:INT`（4 次）

## 输出

- `audio:AUDIO`（4 次）
- `seed:INT`（4 次）
- `subtitle:STRING`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["你是来拉屎的吧！", false, 4242950409, "fixed"]`（4 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
