---
name: unknown_workflow_generic_1856
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.843
common_nodes: [LoadAudio, SaveAudioMP3, TDQwen3TTSCustomVoice, TDQwen3TTSModelLoader, TDQwen3TTSVoiceClone, TDQwen3TTSVoiceDesign]
problems: []
missing: []
members: [音频生成/音频生成/【Supermate】 QWEN3 TTS TD节点工作流_2015819820255682561.json, 音频生成/音频生成/真人配音_Qwen3-TD-TTS_2036601489619161089.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1856

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/【Supermate】 QWEN3 TTS TD节点工作流_2015819820255682561.json、音频生成/音频生成/真人配音_Qwen3-TD-TTS_2036601489619161089.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `LoadAudio`
- `SaveAudioMP3`
- `TDQwen3TTSCustomVoice`
- `TDQwen3TTSModelLoader`
- `TDQwen3TTSVoiceClone`
- `TDQwen3TTSVoiceDesign`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `Fast Groups Muter (rgthree)` —— 1/2 个有
- `Label (rgthree)` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
