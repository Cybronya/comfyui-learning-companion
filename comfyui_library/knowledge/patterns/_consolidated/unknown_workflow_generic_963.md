---
name: unknown_workflow_generic_963
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.7385
common_nodes: [Qwen3ASRLoader_DFT, Qwen3ASRTranscribe_DFT, TranscribeSrt, VHS_LoadVideo, easy boolean, easy ifElse, easy saveText, easy showAnything]
problems: []
missing: []
members: [平台全量/ASR-Qwen3-语音识别-字幕生成-SRT_2018484882946658306.json, 平台全量/语音识别-字幕生成-SRT_2052389211482927106.json, 音频生成/音频生成/Qwen3-ASR-SRT字幕生成_2071425658730930178.json, 音频生成/音频生成/Qwen3-ASR-SRT字幕生成_2075846413833035777.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_963

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/ASR-Qwen3-语音识别-字幕生成-SRT_2018484882946658306.json、平台全量/语音识别-字幕生成-SRT_2052389211482927106.json、音频生成/音频生成/Qwen3-ASR-SRT字幕生成_2071425658730930178.json、音频生成/音频生成/Qwen3-ASR-SRT字幕生成_2075846413833035777.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：74%

## 共有节点

全部 4 个 workflow 都包含：
- `Qwen3ASRLoader_DFT`
- `Qwen3ASRTranscribe_DFT`
- `TranscribeSrt`
- `VHS_LoadVideo`
- `easy boolean`
- `easy ifElse`
- `easy saveText`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 2/4 个有
- `PrimitiveBoolean` —— 2/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
