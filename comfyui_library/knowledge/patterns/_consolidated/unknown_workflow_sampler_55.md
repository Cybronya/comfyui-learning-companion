---
name: unknown_workflow_sampler_55
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 1
common_nodes: [Apply Whisper, FB_Qwen3TTSDialogueInference, FB_Qwen3TTSRoleBank, FB_Qwen3TTSVoiceClonePrompt, LayerUtility: PurgeVRAM V2, LoadAudio, MelBandRoFormerModelLoader, MelBandRoFormerSampler, SaveAudio]
problems: []
missing: []
members: [图片生成/文生图/Qwen3-TTS多人对话_2015350699822944258.json, 音频生成/音频生成/Qwen3 TTS-多人音频对话_2060685586805121025.json, 音频生成/音频生成/Qwen3-TTS多人对话_2057792545501048834.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_55

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Qwen3-TTS多人对话_2015350699822944258.json、音频生成/音频生成/Qwen3 TTS-多人音频对话_2060685586805121025.json、音频生成/音频生成/Qwen3-TTS多人对话_2057792545501048834.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 3 个 workflow 都包含：
- `Apply Whisper`
- `FB_Qwen3TTSDialogueInference`
- `FB_Qwen3TTSRoleBank`
- `FB_Qwen3TTSVoiceClonePrompt`
- `LayerUtility: PurgeVRAM V2`
- `LoadAudio`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `SaveAudio`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/3 个有
- `FB_Qwen3TTSVoiceDesign` —— 1/3 个有
- `VRAMReserver` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
