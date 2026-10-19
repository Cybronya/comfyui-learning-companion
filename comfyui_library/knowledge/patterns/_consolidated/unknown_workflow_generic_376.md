---
name: unknown_workflow_generic_376
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.97225
common_nodes: [CR Prompt Text, LoadAudio, Qwen3TTSModelLoader, Qwen3TTSVoiceClone, SaveAudio]
problems: []
missing: []
members: [音频生成/音频生成/Qwen3 TTS语音克隆V1_2014526902039486466.json, 音频生成/音频生成/Qwen3 TTS语音克隆_2014714896633569282.json, 音频生成/音频生成/Qwen3+TTS+声音复刻_2014723999279878146.json, 音频生成/音频生成/通义qwen3 TTS语音克隆工作流_2015320768132947969.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_376

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（音频生成/音频生成/Qwen3 TTS语音克隆V1_2014526902039486466.json、音频生成/音频生成/Qwen3 TTS语音克隆_2014714896633569282.json、音频生成/音频生成/Qwen3+TTS+声音复刻_2014723999279878146.json、音频生成/音频生成/通义qwen3 TTS语音克隆工作流_2015320768132947969.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 4 个 workflow 都包含：
- `CR Prompt Text`
- `LoadAudio`
- `Qwen3TTSModelLoader`
- `Qwen3TTSVoiceClone`
- `SaveAudio`

**可变部分**（部分 workflow 才有）：
- `AudioSeparation` —— 1/4 个有
- `Label (rgthree)` —— 1/4 个有
- `MuyeLoadImage` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
