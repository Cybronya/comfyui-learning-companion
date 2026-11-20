---
name: unknown_workflow_generic_407
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.647857
common_nodes: [LoadAudio, easy saveText]
problems: []
missing: []
members: [图片生成/反推提示词/Qwen3音频转文字_2031992191672913921.json, 平台全量/Qwen3-ASR 基础工作流_2018514781723959298.json, 平台全量/Qwen3-ASR 声音转文字工作流_2019355146672676866.json, 平台全量/Qwen3-ASR 语音转文字_2018619396305981442.json, 平台全量/Qwen3-ASR 语音转文本_2018697983029682177.json, 平台全量/Qwen3-ASR+SynVow_ 语音转文字_2018621289543507969.json, 音频生成/音频生成/音频+文本的高可用字幕生成工作流_2026261585597042689.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_407

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/反推提示词/Qwen3音频转文字_2031992191672913921.json、平台全量/Qwen3-ASR 基础工作流_2018514781723959298.json、平台全量/Qwen3-ASR 声音转文字工作流_2019355146672676866.json、平台全量/Qwen3-ASR 语音转文字_2018619396305981442.json、平台全量/Qwen3-ASR 语音转文本_2018697983029682177.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：65%

## 共有节点

全部 7 个 workflow 都包含：
- `LoadAudio`
- `easy saveText`

**可变部分**（部分 workflow 才有）：
- `PreviewAny` —— 6/7 个有
- `Qwen3ASRLoader_DFT` —— 6/7 个有
- `Qwen3ASRTranscribe_DFT` —— 6/7 个有
- `Qwen3ForcedAlign` —— 2/7 个有
- `Qwen3ForcedAlignerLoader` —— 2/7 个有
- `ShowText|pysssss` —— 2/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
