---
name: unknown_workflow_generic_1101
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.785667
common_nodes: [Qwen3ASRLoader_DFT, Qwen3ASRTranscribe_DFT, VHS_LoadVideo, easy saveText, easy showAnything]
problems: []
missing: []
members: [图片生成/反推提示词/视频提取台词  mikez_2061823132499005441.json, 平台全量/推理-视频提取字幕(音频)-Qwen3-ASR_2019238102878920705.json, 音频生成/音频生成/视频提取字幕 音频提取字幕 视频转文字 音频转文字 语音转文字_2115481137740079105.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1101

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/反推提示词/视频提取台词  mikez_2061823132499005441.json、平台全量/推理-视频提取字幕(音频)-Qwen3-ASR_2019238102878920705.json、音频生成/音频生成/视频提取字幕 音频提取字幕 视频转文字 音频转文字 语音转文字_2115481137740079105.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 3 个 workflow 都包含：
- `Qwen3ASRLoader_DFT`
- `Qwen3ASRTranscribe_DFT`
- `VHS_LoadVideo`
- `easy saveText`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `PreviewAudio` —— 2/3 个有
- `SaveImage` —— 1/3 个有
- `ttN textOutput` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
