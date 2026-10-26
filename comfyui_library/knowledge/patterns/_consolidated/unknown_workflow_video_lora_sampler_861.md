---
name: unknown_workflow_video_lora_sampler_861
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.5235
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, GetNode, H3SigmaRefiner, KSamplerSelect, LayerColor: Brightness & Contrast, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, PrimitiveFloat, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SetNode, SolAttnPatch, TrimAudioDuration, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/Minimax 单采打戏_2095742874632675330.json, 视频生成/图生视频/MinimaxH3 长视频生成~_2095477683223355393.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_861

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/Minimax 单采打戏_2095742874632675330.json、视频生成/图生视频/MinimaxH3 长视频生成~_2095477683223355393.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：52%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `GetNode`
- `H3SigmaRefiner`
- `KSamplerSelect`
- `LayerColor: Brightness & Contrast`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `PrimitiveFloat`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `SolAttnPatch`
- `TrimAudioDuration`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `FrameInterpolate` —— 1/2 个有
- `FrameInterpolationModelLoader` —— 1/2 个有
- `GetImageRangeFromBatch` —— 1/2 个有
- `ImageFromBatch` —— 1/2 个有
- `LayerUtility: PurgeVRAM V2` —— 1/2 个有
- `MiniMaxH3AddGuide` —— 1/2 个有
- `RTXVideoSuperResolution` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
