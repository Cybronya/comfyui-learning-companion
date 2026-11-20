---
name: unknown_workflow_generic_970
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.7255
common_nodes: [LoadAudio, Qwen3ASRLoader_DFT, Qwen3ASRTranscribe_DFT, easy saveText, easy showAnything]
problems: []
missing: []
members: [平台全量/Qwen3-ASR-音频SRT字幕生成_2100224707453874177.json, 平台全量/推理-音频提取字幕-Qwen3-ASR_2019238094452559874.json, 平台全量/语音识别文字--视频字幕SRT制作--Qwen3-ASR_2040740249474699265.json, 数字人/数字人/制作mv必备-音频转带时间文本制作--Qwen3-ASR_2094725013273403394.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_970

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/Qwen3-ASR-音频SRT字幕生成_2100224707453874177.json、平台全量/推理-音频提取字幕-Qwen3-ASR_2019238094452559874.json、平台全量/语音识别文字--视频字幕SRT制作--Qwen3-ASR_2040740249474699265.json、数字人/数字人/制作mv必备-音频转带时间文本制作--Qwen3-ASR_2094725013273403394.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：73%

## 共有节点

全部 4 个 workflow 都包含：
- `LoadAudio`
- `Qwen3ASRLoader_DFT`
- `Qwen3ASRTranscribe_DFT`
- `easy saveText`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `TranscribeSrt` —— 3/4 个有
- `Fast Groups Bypasser (rgthree)` —— 2/4 个有
- `Qwen3ASRLoader` —— 2/4 个有
- `Qwen3ASRTranscribe` —— 2/4 个有
- `VHS_LoadVideo` —— 2/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
