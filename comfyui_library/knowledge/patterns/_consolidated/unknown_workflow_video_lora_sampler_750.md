---
name: unknown_workflow_video_lora_sampler_750
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.463
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, Fast Groups Bypasser (rgthree), GetNode, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, ModelAttentionBackend, ModelPreviewOverrideKJ, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/H3 mask替换人物_2099484034475847682.json, 视频生成/文生视频/minimax h3六宫生视频_2085919188304093186.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_750

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/H3 mask替换人物_2099484034475847682.json、视频生成/文生视频/minimax h3六宫生视频_2085919188304093186.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：46%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 1/2 个有
- `CR Prompt Text` —— 1/2 个有
- `CheckpointLoaderSimple` —— 1/2 个有
- `ImageAndMaskPreview` —— 1/2 个有
- `ImageResizeKJv2` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有
- `SAM3_TrackPreview` —— 1/2 个有
- `SAM3_TrackToMask` —— 1/2 个有
- `SAM3_VideoTrack` —— 1/2 个有
- `VHS_LoadVideo` —— 1/2 个有
- `取色器_孤海` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
