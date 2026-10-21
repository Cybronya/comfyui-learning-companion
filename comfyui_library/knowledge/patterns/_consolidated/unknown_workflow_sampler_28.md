---
name: unknown_workflow_sampler_28
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.939
common_nodes: [Apply Whisper, FB_Qwen3TTSDialogueInference, FB_Qwen3TTSRoleBank, FB_Qwen3TTSVoiceClonePrompt, Fast Groups Bypasser (rgthree), LayerUtility: PurgeVRAM V2, LoadAudio, MelBandRoFormerModelLoader, MelBandRoFormerSampler, Qwen3TTSModelLoader, Qwen3TTSVoiceClone, Qwen3TTSVoiceDesign, SaveAudio]
problems: []
missing: []
members: [音频生成/音频生成/Qwen3-TTS克隆音色（单人克隆_多人对话）_2016078134889684993.json, 音频生成/音频生成/Qwen3-TTS多人对话声音编辑_2017122770886336514.json, 音频生成/音频生成/千问3tts音色克隆+音色设计+多人物对话_2020707913525891073.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_28

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（音频生成/音频生成/Qwen3-TTS克隆音色（单人克隆_多人对话）_2016078134889684993.json、音频生成/音频生成/Qwen3-TTS多人对话声音编辑_2017122770886336514.json、音频生成/音频生成/千问3tts音色克隆+音色设计+多人物对话_2020707913525891073.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 3 个 workflow 都包含：
- `Apply Whisper`
- `FB_Qwen3TTSDialogueInference`
- `FB_Qwen3TTSRoleBank`
- `FB_Qwen3TTSVoiceClonePrompt`
- `Fast Groups Bypasser (rgthree)`
- `LayerUtility: PurgeVRAM V2`
- `LoadAudio`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `Qwen3TTSModelLoader`
- `Qwen3TTSVoiceClone`
- `Qwen3TTSVoiceDesign`
- `SaveAudio`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 2/3 个有
- `CR Text` —— 2/3 个有
- `Qwen3TTSCustomVoice` —— 2/3 个有
- `ShowText|pysssss` —— 2/3 个有
- `VRAMReserver` —— 2/3 个有
- `CR Prompt Text` —— 1/3 个有
- `FB_Qwen3TTSVoiceDesign` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
