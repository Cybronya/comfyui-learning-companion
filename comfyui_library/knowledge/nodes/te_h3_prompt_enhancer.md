# TE_H3_Prompt_Enhancer

## 节点类型

`TE_H3_Prompt_Enhancer`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `H3参考素材:TE_H3_REFERENCES`（1 次）
- `输入提示词:STRING`（1 次）
- `任务类型:COMBO`（1 次）
- `视频时长:FLOAT`（1 次）
- `参考素材说明:STRING`（1 次）
- `增强方式:COMBO`（1 次）
- `api_key:STRING`（1 次）
- `api_base_url:STRING`（1 次）
- `model:STRING`（1 次）
- `max_output_tokens:INT`（1 次）

## 输出

- `增强提示词(API):STRING`（1 次）
- `提示词模版(本地):STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["两个剑客激烈打斗,镜头表现力强,动作迅速", "全参考模式(Reference to Video)", 5, "", "本地模板", "", "", "", 4096, 0.6, 300, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
