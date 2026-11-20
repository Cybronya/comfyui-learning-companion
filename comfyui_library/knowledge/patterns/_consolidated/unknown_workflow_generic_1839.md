---
name: unknown_workflow_generic_1839
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.948
common_nodes: [CR Prompt Text, Fast Groups Bypasser (rgthree), LayerUtility: PurgeVRAM V2, LoadAudio, RunningHub_VoxCPM_Generate, RunningHub_VoxCPM_LoadModel, RunningHub_VoxCPM_MultiSpeaker_ListReference, SaveAudio, TDQwen3TTSModelLoader, TDQwen3TTSVoiceDesign]
problems: []
missing: []
members: [音频生成/音频生成/VOXCPM2语音设计_2067443898032680961.json, 音频生成/音频生成/极致人声！支持单人、多人音色设计+音频克隆！打造你的专属音色_2063265857324802049.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1839

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/VOXCPM2语音设计_2067443898032680961.json、音频生成/音频生成/极致人声！支持单人、多人音色设计+音频克隆！打造你的专属音色_2063265857324802049.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Prompt Text`
- `Fast Groups Bypasser (rgthree)`
- `LayerUtility: PurgeVRAM V2`
- `LoadAudio`
- `RunningHub_VoxCPM_Generate`
- `RunningHub_VoxCPM_LoadModel`
- `RunningHub_VoxCPM_MultiSpeaker_ListReference`
- `SaveAudio`
- `TDQwen3TTSModelLoader`
- `TDQwen3TTSVoiceDesign`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/2 个有
- `IndexTTS2Run` —— 1/2 个有
- `Label (rgthree)` —— 1/2 个有
- `PreviewAudio` —— 1/2 个有
- `Text Multiline` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
