---
name: unknown_workflow_generic_186
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.67
common_nodes: [LoadAudio, Qwen3ASRLoader, Qwen3ASRTranscribe, ShowText|pysssss]
problems: []
missing: []
members: [图片生成/文生图/SynVow_Qwen3ASR 多语言音频转文本_2018970445520838658.json, 平台全量/Qwen3 ASR HF 台词时间定位_2117469515138289666.json, 平台全量/Qwen3 ASR 提取声音文本_2117466524956057601.json, 平台全量/SynVow_Qwen3ASR 基础工作流_2018868859469570050.json, 平台全量/基于 Qwen3-ASR 与 Qwen3 ForcedAligner 的音频识别与时间戳字幕制作工作流_2019863556694482945.json, 平台全量/语音转成文字，多国语言都能转，操作简单_2019607973588377601.json, 平台全量/语音转文字+字幕_2112800043832012801.json, 平台全量/语音转文字- SynVow_Qwen3ASR 语音转文字基础工作流_2021814179719548930.json, 音频生成/音频生成/SynVow_Qwen3ASR 基础工作流_2019658132808536065.json, 音频生成/音频生成/SynVow_Qwen3ASR 基础工作流_2041507271208869889.json, 音频生成/音频生成/SynVow_Qwen3ASR 语音转文字_2022325449564622850.json, 音频生成/音频生成/SynVow_Qwen3ASR 语音转文字基础工作流_2020676844198039553.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_186

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/SynVow_Qwen3ASR 多语言音频转文本_2018970445520838658.json、平台全量/Qwen3 ASR HF 台词时间定位_2117469515138289666.json、平台全量/Qwen3 ASR 提取声音文本_2117466524956057601.json、平台全量/SynVow_Qwen3ASR 基础工作流_2018868859469570050.json、平台全量/基于 Qwen3-ASR 与 Qwen3 ForcedAligner 的音频识别与时间戳字幕制作工作流_2019863556694482945.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：67%

## 共有节点

全部 12 个 workflow 都包含：
- `LoadAudio`
- `Qwen3ASRLoader`
- `Qwen3ASRTranscribe`
- `ShowText|pysssss`

**可变部分**（部分 workflow 才有）：
- `Qwen3ForcedAlign` —— 11/12 个有
- `Qwen3ForcedAlignerLoader` —— 11/12 个有
- `easy saveText` —— 9/12 个有
- `LoadImage` —— 2/12 个有
- `SaveImage` —— 2/12 个有
- `SaveText` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
