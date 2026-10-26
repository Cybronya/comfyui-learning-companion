---
name: unknown_workflow_video_lora_sampler_535
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.63925
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, ComfyMathExpression, ImageResizeKJv2, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, ModelPreviewOverrideKJ, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SAM3_TrackPreview, SAM3_TrackToMask, SAM3_VideoTrack, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [数字人/数字人/minimax_h3_角色替换_2113147355452235777.json, 视频生成/图生视频/H3 Character Swap 1.5｜SAM 3.1 精准角色替换·VDN8 加速版_2113162325590102018.json, 视频生成/图生视频/H3 mask替换人物_2099484034475847682.json, 视频生成/图生视频/替换多人视频中的人物采用人物遮罩（简单提示词+h3_character_swap_mask）_2113250622324690946.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_535

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（数字人/数字人/minimax_h3_角色替换_2113147355452235777.json、视频生成/图生视频/H3 Character Swap 1.5｜SAM 3.1 精准角色替换·VDN8 加速版_2113162325590102018.json、视频生成/图生视频/H3 mask替换人物_2099484034475847682.json、视频生成/图生视频/替换多人视频中的人物采用人物遮罩（简单提示词+h3_character_swap_mask）_2113250622324690946.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：64%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ComfyMathExpression`
- `ImageResizeKJv2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `ModelPreviewOverrideKJ`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SAM3_TrackPreview`
- `SAM3_TrackToMask`
- `SAM3_VideoTrack`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 3/4 个有
- `DrawBBoxes` —— 3/4 个有
- `GetNode` —— 3/4 个有
- `KSamplerSelect` —— 3/4 个有
- `LTXVConcatAVLatent` —— 3/4 个有
- `MVEx_MaskCleanup` —— 3/4 个有
- `MVEx_MaskToLatentSpace` —— 3/4 个有
- `MVEx_SubjectCrop` —— 3/4 个有
- `MVEx_SubjectUncrop` —— 3/4 个有
- `ModelAttentionBackend` —— 3/4 个有
- `PreviewAnimation` —— 3/4 个有
- `ResizeImageMaskNode` —— 3/4 个有
- `SetLatentNoiseMask` —— 3/4 个有
- `SetNode` —— 3/4 个有
- `SolidMask` —— 3/4 个有
- `VAEEncode` —— 3/4 个有
- `VAEEncodeAudio` —— 3/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `ImageAndMaskPreview` —— 1/4 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/4 个有
- `MiniMaxH3VDNExecutionPlanT8Advanced` —— 1/4 个有
- `MiniMaxH3VDNModelComposerT8Advanced` —— 1/4 个有
- `取色器_孤海` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
