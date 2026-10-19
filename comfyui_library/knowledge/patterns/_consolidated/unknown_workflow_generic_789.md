---
name: unknown_workflow_generic_789
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7915
common_nodes: [Fast Groups Bypasser (rgthree), LoadAudio, SaveAudio, TDQwen3TTSCustomVoice, TDQwen3TTSModelLoader, TDQwen3TTSVoiceClone, TDQwen3TTSVoiceDesign]
problems: []
missing: []
members: [音频生成/音频生成/CG迷-Qwen3 TTS音色克隆工作流_2016079119808729090.json, 音频生成/音频生成/Qwen3-TTS_2015449559899574274.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_789

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/CG迷-Qwen3 TTS音色克隆工作流_2016079119808729090.json、音频生成/音频生成/Qwen3-TTS_2015449559899574274.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：79%

## 共有节点

全部 2 个 workflow 都包含：
- `Fast Groups Bypasser (rgthree)`
- `LoadAudio`
- `SaveAudio`
- `TDQwen3TTSCustomVoice`
- `TDQwen3TTSModelLoader`
- `TDQwen3TTSVoiceClone`
- `TDQwen3TTSVoiceDesign`

**可变部分**（部分 workflow 才有）：
- `Apply Whisper` —— 1/2 个有
- `AudioSpeedShift` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
