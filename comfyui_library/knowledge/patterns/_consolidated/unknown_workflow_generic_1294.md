---
name: unknown_workflow_generic_1294
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.809667
common_nodes: [FB_Qwen3TTSDialogueInference, FB_Qwen3TTSRoleBank, FB_Qwen3TTSVoiceClonePrompt, LayerUtility: PurgeVRAM V2, LoadAudio, SaveAudio, ShowText|pysssss, WhisperSTT]
problems: []
missing: []
members: [平台全量/Qwen3 TTS 多角色克隆配音_1943412030600867841.json, 音频生成/音频生成/Qwen3 TTS 多角色克隆配音 音色参考  Qwen3 TTS 声音克隆_2017873840382152706.json, 音频生成/音频生成/Qwen3 TTS全套-语音设计+克隆+多角配音_2015623768873373697.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1294

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/Qwen3 TTS 多角色克隆配音_1943412030600867841.json、音频生成/音频生成/Qwen3 TTS 多角色克隆配音 音色参考  Qwen3 TTS 声音克隆_2017873840382152706.json、音频生成/音频生成/Qwen3 TTS全套-语音设计+克隆+多角配音_2015623768873373697.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 3 个 workflow 都包含：
- `FB_Qwen3TTSDialogueInference`
- `FB_Qwen3TTSRoleBank`
- `FB_Qwen3TTSVoiceClonePrompt`
- `LayerUtility: PurgeVRAM V2`
- `LoadAudio`
- `SaveAudio`
- `ShowText|pysssss`
- `WhisperSTT`

**可变部分**（部分 workflow 才有）：
- `Apply Whisper` —— 2/3 个有
- `AudioCrop` —— 2/3 个有
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `Qwen3TTSModelLoader` —— 2/3 个有
- `Qwen3TTSVoiceClone` —— 2/3 个有
- `CR Prompt Text` —— 1/3 个有
- `FB_Qwen3TTSVoiceDesign` —— 1/3 个有
- `PreviewAny` —— 1/3 个有
- `Qwen3TTSVoiceDesign` —— 1/3 个有
- `RH_LLMAPI_Pro_Node` —— 1/3 个有
- `Text` —— 1/3 个有
- `VRAMReserver` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
