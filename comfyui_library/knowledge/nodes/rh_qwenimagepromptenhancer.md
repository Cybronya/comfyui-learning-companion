# RH_QwenImagePromptEnhancer

## 节点类型

`RH_QwenImagePromptEnhancer`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `prompt:STRING`（2 次）
- `language:COMBO`（2 次）
- `style:COMBO`（2 次）
- `quality_level:COMBO`（2 次）
- `custom_style:STRING`（2 次）
- `custom_quality:STRING`（2 次）

## 输出

- `enhanced_prompt:STRING`（2 次）
- `detected_language:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["一位穿着碧绿罗裙的中国古代美女，坐在湖边的亭子里，手托香腮，看着湖里的七彩鲤鱼发呆。", "auto", "realistic", "ultra", "", ""]`（1 次）
- `["a little cat", "auto", "none", "high", "", ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
