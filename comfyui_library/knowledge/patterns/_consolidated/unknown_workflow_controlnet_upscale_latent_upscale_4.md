---
name: unknown_workflow_controlnet_upscale_latent_upscale_4
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.702333
common_nodes: [AIO_Preprocessor, BasicGuider, CLIPLoader, ComfyMathExpression, ComfySwitchNode, GrowMask, ImageScale, MaskPreview, MiniMaxH3AVDecodeT8, MiniMaxH3FunControlNetApply, MiniMaxH3LearnedLatentUpscaleT8Advanced, MiniMaxH3OutputTrimT8, MiniMaxH3SafeAVSaveT8Advanced, MiniMaxH3TwoPassAudioAuditT8Advanced, MiniMaxH3TwoPassLatentReconcileT8Advanced, MiniMaxH3VDNExecutionPlanT8Advanced, MiniMaxH3VDNModelComposerT8Advanced, MiniMaxH3VDNRefinePlanT8Advanced, ModelPatchLoader, PointsEditor, PreviewAny, PrimitiveBoolean, PrimitiveFloat, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SaveImage, SeCModelLoader, SeCVideoSegmentation, UNETLoader, VAELoader, VHS_LoadVideo, VHS_VideoInfoLoaded]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax H3｜ControlNet Union  局部重绘专用工作流_2108263577818849282.json, 视频生成/文生视频/MiniMax H3｜ControlNet Union 2.0 视频控制与局部重绘·音频驱动数字人｜VDN 12步高清版_2106627537043550210.json, 视频生成/文生视频/MiniMax H3｜ControlNet Union 2.0 视频控制与局部重绘｜VDN 12步高清版_2108578106922590210.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_upscale_latent_upscale_4

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3｜ControlNet Union  局部重绘专用工作流_2108263577818849282.json、视频生成/文生视频/MiniMax H3｜ControlNet Union 2.0 视频控制与局部重绘·音频驱动数字人｜VDN 12步高清版_2106627537043550210.json、视频生成/文生视频/MiniMax H3｜ControlNet Union 2.0 视频控制与局部重绘｜VDN 12步高清版_2108578106922590210.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：70%

## 共有节点

全部 3 个 workflow 都包含：
- `AIO_Preprocessor`
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `GrowMask`
- `ImageScale`
- `MaskPreview`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3FunControlNetApply`
- `MiniMaxH3LearnedLatentUpscaleT8Advanced`
- `MiniMaxH3OutputTrimT8`
- `MiniMaxH3SafeAVSaveT8Advanced`
- `MiniMaxH3TwoPassAudioAuditT8Advanced`
- `MiniMaxH3TwoPassLatentReconcileT8Advanced`
- `MiniMaxH3VDNExecutionPlanT8Advanced`
- `MiniMaxH3VDNModelComposerT8Advanced`
- `MiniMaxH3VDNRefinePlanT8Advanced`
- `ModelPatchLoader`
- `PointsEditor`
- `PreviewAny`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SeCModelLoader`
- `SeCVideoSegmentation`
- `UNETLoader`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoInfoLoaded`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 2/3 个有
- `MiniMaxH3DurationPlannerT8` —— 2/3 个有
- `MiniMaxH3ReferenceToVideo` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `AudioSeparation` —— 1/3 个有
- `LTXVAudioVAEEncode` —— 1/3 个有
- `LTXVConcatAVLatent` —— 1/3 个有
- `LoadAudio` —— 1/3 个有
- `MiniMaxH3AudioConditioningT8` —— 1/3 个有
- `MiniMaxH3AudioWindowT8` —— 1/3 个有
- `SetLatentNoiseMask` —— 1/3 个有
- `SolidMask` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 1 | 1 - 1.8 | 3 | 70% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 1，观测区间 1 - 1.8，3 个样本
