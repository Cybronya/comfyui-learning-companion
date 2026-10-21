---
name: unknown_workflow_generic_1000
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.965
common_nodes: [Apply Whisper, Bjornulf_IfElse, CR Text, EmptyAudio, FB_Qwen3TTSConfig, FB_Qwen3TTSDialogueInference, FB_Qwen3TTSRoleBank, FB_Qwen3TTSVoiceClone, FB_Qwen3TTSVoiceClonePrompt, FB_Qwen3TTSVoiceDesign, ImpactSwitch, Int, LazySwitch1way, LoadAudio, Qwen3TTSVoicePresets, SaveAudioMP3, TrimAudioDuration, easy compare]
problems: []
missing: []
members: [音频生成/音频生成/qwen3 tts-声音克隆_创建声音-整合版_2028677768417906689.json, 音频生成/音频生成/声音克隆_创建声音-整合版（健祥）_2031904106389966849.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1000

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/qwen3 tts-声音克隆_创建声音-整合版_2028677768417906689.json、音频生成/音频生成/声音克隆_创建声音-整合版（健祥）_2031904106389966849.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：96%

## 共有节点

全部 2 个 workflow 都包含：
- `Apply Whisper`
- `Bjornulf_IfElse`
- `CR Text`
- `EmptyAudio`
- `FB_Qwen3TTSConfig`
- `FB_Qwen3TTSDialogueInference`
- `FB_Qwen3TTSRoleBank`
- `FB_Qwen3TTSVoiceClone`
- `FB_Qwen3TTSVoiceClonePrompt`
- `FB_Qwen3TTSVoiceDesign`
- `ImpactSwitch`
- `Int`
- `LazySwitch1way`
- `LoadAudio`
- `Qwen3TTSVoicePresets`
- `SaveAudioMP3`
- `TrimAudioDuration`
- `easy compare`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
