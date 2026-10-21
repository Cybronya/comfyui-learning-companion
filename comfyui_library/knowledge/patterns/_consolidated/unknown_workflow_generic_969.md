---
name: unknown_workflow_generic_969
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [FB_Qwen3TTSDialogueInference, FB_Qwen3TTSRoleBank, FB_Qwen3TTSVoiceClonePrompt, FB_Qwen3TTSVoiceDesign, LayerUtility: PurgeVRAM V2, LoadAudio, SaveAudio, VRAMReserver, WhisperSTT]
problems: []
missing: []
members: [音频生成/音频生成/Qwen3 TTS多角色配音-漫剧利器_2015358867147857922.json, 音频生成/音频生成/Qwen3 TTS多角色配音V2（声音克隆版）_2015094220624764929.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_969

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/Qwen3 TTS多角色配音-漫剧利器_2015358867147857922.json、音频生成/音频生成/Qwen3 TTS多角色配音V2（声音克隆版）_2015094220624764929.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `FB_Qwen3TTSDialogueInference`
- `FB_Qwen3TTSRoleBank`
- `FB_Qwen3TTSVoiceClonePrompt`
- `FB_Qwen3TTSVoiceDesign`
- `LayerUtility: PurgeVRAM V2`
- `LoadAudio`
- `SaveAudio`
- `VRAMReserver`
- `WhisperSTT`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 1/2 个有
- `Label (rgthree)` —— 1/2 个有
- `ShowText` —— 1/2 个有
- `Text` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
