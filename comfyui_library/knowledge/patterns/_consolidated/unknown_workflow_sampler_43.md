---
name: unknown_workflow_sampler_43
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.785
common_nodes: [CR Text, CR Text Replace, GetTextFromJson, Light-Tool: DeserializeJsonString, PreviewAny, PurgeVRAM_UTK, Qwen3TTSModelLoader, Qwen3TTSVoiceDesign, RHLLMChatNode, SaveAudio, easy showAnything, 孤海注释]
problems: []
missing: []
members: [音频生成/音频生成/Comfyui 基础知识09：声音生成和处理-工具集_2075252484909654017.json, 音频生成/音频生成/声音声纹设计专用流 （一次出两个）_2074903538848845826.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_43

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/Comfyui 基础知识09：声音生成和处理-工具集_2075252484909654017.json、音频生成/音频生成/声音声纹设计专用流 （一次出两个）_2074903538848845826.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：78%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Text`
- `CR Text Replace`
- `GetTextFromJson`
- `Light-Tool: DeserializeJsonString`
- `PreviewAny`
- `PurgeVRAM_UTK`
- `Qwen3TTSModelLoader`
- `Qwen3TTSVoiceDesign`
- `RHLLMChatNode`
- `SaveAudio`
- `easy showAnything`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `AFL:AudioSeparateDemucs4Stem` —— 1/2 个有
- `AudioAdjustVolume` —— 1/2 个有
- `AudioCombine` —— 1/2 个有
- `LoadAudioUI` —— 1/2 个有
- `MelBandRoFormerModelLoader` —— 1/2 个有
- `MelBandRoFormerSampler` —— 1/2 个有
- `PreviewAudio` —— 1/2 个有
- `SaveAudioAdvanced` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
