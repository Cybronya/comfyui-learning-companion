---
name: unknown_workflow_generic_828
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [Apply Whisper, LoadAudio, Qwen3TTSModelLoader, Qwen3TTSVoiceClone, SaveAudio]
problems: []
missing: []
members: [音频生成/音频生成/Qwen3 TTS语音复刻（阿里最新开源）_2014610323709366274.json, 音频生成/音频生成/Qwen3TTS 终极声音克隆_2018636171651321857.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_828

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/Qwen3 TTS语音复刻（阿里最新开源）_2014610323709366274.json、音频生成/音频生成/Qwen3TTS 终极声音克隆_2018636171651321857.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `Apply Whisper`
- `LoadAudio`
- `Qwen3TTSModelLoader`
- `Qwen3TTSVoiceClone`
- `SaveAudio`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 1/2 个有
- `LayerUtility: TextBox` —— 1/2 个有
- `ShowAnything|Mie` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
