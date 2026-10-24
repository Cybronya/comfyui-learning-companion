---
name: unknown_workflow_lora_sampler_unet_313
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.5445
common_nodes: [AudioCrop, BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, ComfySwitchNode, CreateVideo, GetNode, KSamplerSelect, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveBoolean, PrimitiveFloat, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_LoadVideo, easy minimaxH3AudioLock]
problems: []
missing: []
members: [视频生成/图生视频/Minimax多帧插入或者视频续写_2102590341739274241.json, 视频生成/图生视频/Minmax多参考生成视频R2V_2084668436755599362.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_313

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/Minimax多帧插入或者视频续写_2102590341739274241.json、视频生成/图生视频/Minmax多参考生成视频R2V_2084668436755599362.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：54%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioCrop`
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `CreateVideo`
- `GetNode`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_LoadVideo`
- `easy minimaxH3AudioLock`

**可变部分**（部分 workflow 才有）：
- `AudioConcat` —— 1/2 个有
- `ColorMatchV2` —— 1/2 个有
- `GetImageRangeFromBatch` —— 1/2 个有
- `INTConstant` —— 1/2 个有
- `Image Batch` —— 1/2 个有
- `ImageAddNoise` —— 1/2 个有
- `ImageFromBatch` —— 1/2 个有
- `ImageScale` —— 1/2 个有
- `MiniMaxH3AddGuide` —— 1/2 个有
- `TrimAudioDuration` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
