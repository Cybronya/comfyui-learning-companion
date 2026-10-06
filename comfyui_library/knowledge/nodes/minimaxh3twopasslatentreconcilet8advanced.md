# MiniMaxH3TwoPassLatentReconcileT8Advanced

## 节点类型

`MiniMaxH3TwoPassLatentReconcileT8Advanced`

## 分类

Latent

## 作用

latent 空间处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 14 个 workflow 中。

## 输入

- `learned_latent:LATENT`（14 次）
- `highres_template:LATENT`（14 次）
- `positive:CONDITIONING`（14 次）
- `audio_policy:COMBO`（14 次）
- `second_pass_audio_source:COMBO`（14 次）
- `second_pass_audio_strength:FLOAT`（14 次）

## 输出

- `av_latent:LATENT`（14 次）
- `positive:CONDITIONING`（14 次）
- `report_json:STRING`（14 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["auto", "legacy_policy", 0]`（14 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
