# MiniMaxH3TwoPassAudioAuditT8Advanced

## 节点类型

`MiniMaxH3TwoPassAudioAuditT8Advanced`

## 分类

Audio

## 作用

音频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `second_pass_input:LATENT`（2 次）
- `second_pass_output:LATENT`（2 次）
- `expected_audio_strength:FLOAT`（2 次）
- `fail_on_locked_mismatch:BOOLEAN`（2 次）
- `locked_atol:FLOAT`（2 次）

## 输出

- `verified_av_latent:LATENT`（2 次）
- `report_json:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, true, 1e-05]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
