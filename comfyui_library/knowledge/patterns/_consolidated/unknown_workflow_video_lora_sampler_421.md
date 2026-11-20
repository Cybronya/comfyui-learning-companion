---
name: unknown_workflow_video_lora_sampler_421
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.707571
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, ComfyMathExpression, DrawBBoxes, ImageResizeKJv2, LTXVConcatAVLatent, LoadImage, LoraLoaderModelOnly, MVEx_MaskCleanup, MVEx_MaskToLatentSpace, MVEx_SubjectCrop, MVEx_SubjectUncrop, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, PreviewAnimation, RandomNoise, ResolutionSelector, SAM3_TrackPreview, SAM3_TrackToMask, SAM3_VideoTrack, SamplerCustomAdvanced, SetLatentNoiseMask, SolidMask, UNETLoader, VAEDecode, VAEDecodeAudio, VAEEncode, VAEEncodeAudio, VAELoader, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/Minimax_H3｜单人 & 多人中选一人替换｜+ 遮罩选人 + Character Swap V1.5 人物替换 LoRA_2106890082614603777.json, 平台全量/minimax_h3_角色替换_2113272648531800065.json, 数字人/数字人/minimax_h3_角色替换_2113147355452235777.json, 视频生成/图生视频/H3 Character Swap 1.5｜SAM 3.1 精准角色替换·VDN8 加速版_2113162325590102018.json, 视频生成/图生视频/H3 Character Swap 1.5｜SAM 3.1 精准角色替换·VDN8 加速版_2114606057728335873.json, 视频生成/图生视频/H3_Character_Swap_1.5｜SAM_3.1_精准角色替换·VDN8_加速版_2115232128324694017.json, 视频生成/图生视频/替换多人视频中的人物采用人物遮罩（简单提示词+h3_character_swap_mask）_2113250622324690946.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_421

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（平台全量/Minimax_H3｜单人 & 多人中选一人替换｜+ 遮罩选人 + Character Swap V1.5 人物替换 LoRA_2106890082614603777.json、平台全量/minimax_h3_角色替换_2113272648531800065.json、数字人/数字人/minimax_h3_角色替换_2113147355452235777.json、视频生成/图生视频/H3 Character Swap 1.5｜SAM 3.1 精准角色替换·VDN8 加速版_2113162325590102018.json、视频生成/图生视频/H3 Character Swap 1.5｜SAM 3.1 精准角色替换·VDN8 加速版_2114606057728335873.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：71%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ComfyMathExpression`
- `DrawBBoxes`
- `ImageResizeKJv2`
- `LTXVConcatAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MVEx_MaskCleanup`
- `MVEx_MaskToLatentSpace`
- `MVEx_SubjectCrop`
- `MVEx_SubjectUncrop`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `PreviewAnimation`
- `RandomNoise`
- `ResolutionSelector`
- `SAM3_TrackPreview`
- `SAM3_TrackToMask`
- `SAM3_VideoTrack`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SolidMask`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAEEncode`
- `VAEEncodeAudio`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ModelPreviewOverrideKJ` —— 6/7 个有
- `PrimitiveFloat` —— 6/7 个有
- `PrimitiveStringMultiline` —— 6/7 个有
- `ResizeImageMaskNode` —— 6/7 个有
- `BasicScheduler` —— 4/7 个有
- `GetNode` —— 4/7 个有
- `KSamplerSelect` —— 4/7 个有
- `ModelAttentionBackend` —— 4/7 个有
- `SetNode` —— 4/7 个有
- `MiniMaxH3VDNExecutionPlanT8Advanced` —— 3/7 个有
- `MiniMaxH3VDNModelComposerT8Advanced` —— 3/7 个有
- `Anything Everywhere3` —— 1/7 个有
- `BlockSparseAttention` —— 1/7 个有
- `Label (rgthree)` —— 1/7 个有
- `PrimitiveInt` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
