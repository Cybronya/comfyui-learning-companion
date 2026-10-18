# T8_IndexTTS25_TextPreview

## 节点类型

`T8_IndexTTS25_TextPreview`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `model:T8_INDEXTTS25_MODEL`（3 次）
- `sampling:T8_INDEXTTS25_SAMPLING`（3 次）
- `text:STRING`（3 次）
- `language:COMBO`（3 次）

## 输出

- `原样文本:STRING`（3 次）
- `分段与停顿预览 JSON:STRING`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["而那个将来会权倾天下、将我完全控制的男人，此刻还只是我一时兴起抢回来的……马奴", "ZH"]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
