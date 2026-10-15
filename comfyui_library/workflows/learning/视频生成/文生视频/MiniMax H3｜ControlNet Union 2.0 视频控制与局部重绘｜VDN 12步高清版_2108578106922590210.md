---
key: 视频生成/文生视频/MiniMax H3｜ControlNet Union 2.0 视频控制与局部重绘｜VDN 12步高清版_2108578106922590210.json
name: MiniMax H3｜ControlNet Union 2.0 视频控制与局部重绘｜VDN 12步高清版_2108578106922590210
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MiniMax H3｜ControlNet Union 2.0 视频控制与局部重绘｜VDN 12步高清版_2108578106922590210.json
hash: b0ade8ea2fe8f9d9
coverage: 0.702479
learned_at: 2026-10-15 22:46:09
nodes: [CLIPLoader, VAELoader, VAELoader, UNETLoader, ImageScale, MiniMaxH3VDNModelComposerT8Advanced, MiniMaxH3VDNExecutionPlanT8Advanced, RandomNoise, SamplerCustomAdvanced, MiniMaxH3LearnedLatentUpscaleT8Advanced, MiniMaxH3VDNModelComposerT8Advanced, MiniMaxH3VDNRefinePlanT8Advanced, BasicGuider, RandomNoise, SamplerCustomAdvanced, MiniMaxH3TwoPassAudioAuditT8Advanced, MiniMaxH3AVDecodeT8, MiniMaxH3OutputTrimT8, MarkdownNote, MarkdownNote, PrimitiveBoolean, PrimitiveInt, PrimitiveInt, ComfySwitchNode, ComfySwitchNode, MarkdownNote, MarkdownNote, ComfySwitchNode, ComfySwitchNode, ComfySwitchNode, PointsEditor, SeCVideoSegmentation, GrowMask, ComfyMathExpression, ComfyMathExpression, MarkdownNote, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, VHS_VideoInfoLoaded, MarkdownNote, PrimitiveFloat, BasicGuider, MiniMaxH3TwoPassLatentReconcileT8Advanced, PreviewAny, MiniMaxH3AudioConditioningT8, SeCModelLoader, MiniMaxH3AudioConditioningT8, MaskPreview, MiniMaxH3FunControlNetApply, PrimitiveInt, ModelPatchLoader, PrimitiveStringMultiline, CLIPLoader, VAELoader, VAELoader, UNETLoader, ImageScale, MiniMaxH3VDNModelComposerT8Advanced, MiniMaxH3VDNExecutionPlanT8Advanced, RandomNoise, SamplerCustomAdvanced, MiniMaxH3LearnedLatentUpscaleT8Advanced, MiniMaxH3VDNModelComposerT8Advanced, MiniMaxH3VDNRefinePlanT8Advanced, BasicGuider, RandomNoise, SamplerCustomAdvanced, MiniMaxH3TwoPassAudioAuditT8Advanced, MiniMaxH3AVDecodeT8, MiniMaxH3OutputTrimT8, MiniMaxH3SafeAVSaveT8Advanced, MarkdownNote, MarkdownNote, PrimitiveBoolean, PrimitiveInt, PrimitiveInt, ComfySwitchNode, ComfySwitchNode, MarkdownNote, MarkdownNote, ComfySwitchNode, ComfySwitchNode, ComfySwitchNode, PointsEditor, SeCVideoSegmentation, GrowMask, ComfyMathExpression, ComfyMathExpression, MarkdownNote, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, VHS_VideoInfoLoaded, MarkdownNote, MiniMaxH3DurationPlannerT8, PrimitiveFloat, BasicGuider, MiniMaxH3TwoPassLatentReconcileT8Advanced, PreviewAny, MiniMaxH3AudioConditioningT8, SeCModelLoader, MiniMaxH3AudioConditioningT8, MaskPreview, MiniMaxH3FunControlNetApply, PrimitiveInt, ModelPatchLoader, VHS_LoadVideo, AIO_Preprocessor, PrimitiveStringMultiline, PreviewImage, MiniMaxH3DurationPlannerT8, VHS_LoadVideo, MiniMaxH3SafeAVSaveT8Advanced, PreviewImage, AIO_Preprocessor, SaveImage]
patterns: []
missing: []
parameters: {"controlnet_strength": 1}
---

# 视频生成/文生视频/MiniMax H3｜ControlNet Union 2.0 视频控制与局部重绘｜VDN 12步高清版_2108578106922590210.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MiniMax H3｜ControlNet Union 2.0 视频控制与局部重绘｜VDN 12步高清版_2108578106922590210.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Process → Output → Other

**节点**（121 个）：
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `UNETLoader` ★核心
- `ImageScale`
- `MiniMaxH3VDNModelComposerT8Advanced`
- `MiniMaxH3VDNExecutionPlanT8Advanced`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3LearnedLatentUpscaleT8Advanced`
- `MiniMaxH3VDNModelComposerT8Advanced`
- `MiniMaxH3VDNRefinePlanT8Advanced`
- `BasicGuider`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3TwoPassAudioAuditT8Advanced`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3OutputTrimT8`
- `MarkdownNote`
- `MarkdownNote`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `PrimitiveInt`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `MarkdownNote`
- `MarkdownNote`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `PointsEditor`
- `SeCVideoSegmentation`
- `GrowMask`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `MarkdownNote`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `VHS_VideoInfoLoaded`
- `MarkdownNote`
- `PrimitiveFloat`
- `BasicGuider`
- `MiniMaxH3TwoPassLatentReconcileT8Advanced`
- `PreviewAny`
- `MiniMaxH3AudioConditioningT8`
- `SeCModelLoader`
- `MiniMaxH3AudioConditioningT8`
- `MaskPreview`
- `MiniMaxH3FunControlNetApply` ★核心
- `PrimitiveInt`
- `ModelPatchLoader`
- `PrimitiveStringMultiline`
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `UNETLoader` ★核心
- `ImageScale`
- `MiniMaxH3VDNModelComposerT8Advanced`
- `MiniMaxH3VDNExecutionPlanT8Advanced`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3LearnedLatentUpscaleT8Advanced`
- `MiniMaxH3VDNModelComposerT8Advanced`
- `MiniMaxH3VDNRefinePlanT8Advanced`
- `BasicGuider`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3TwoPassAudioAuditT8Advanced`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3OutputTrimT8`
- `MiniMaxH3SafeAVSaveT8Advanced`
- `MarkdownNote`
- `MarkdownNote`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `PrimitiveInt`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `MarkdownNote`
- `MarkdownNote`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `PointsEditor`
- `SeCVideoSegmentation`
- `GrowMask`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `MarkdownNote`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `VHS_VideoInfoLoaded`
- `MarkdownNote`
- `MiniMaxH3DurationPlannerT8`
- `PrimitiveFloat`
- `BasicGuider`
- `MiniMaxH3TwoPassLatentReconcileT8Advanced`
- `PreviewAny`
- `MiniMaxH3AudioConditioningT8`
- `SeCModelLoader`
- `MiniMaxH3AudioConditioningT8`
- `MaskPreview`
- `MiniMaxH3FunControlNetApply` ★核心
- `PrimitiveInt`
- `ModelPatchLoader`
- `VHS_LoadVideo`
- `AIO_Preprocessor`
- `PrimitiveStringMultiline`
- `PreviewImage`
- `MiniMaxH3DurationPlannerT8`
- `VHS_LoadVideo`
- `MiniMaxH3SafeAVSaveT8Advanced`
- `PreviewImage`
- `AIO_Preprocessor`
- `SaveImage`

## 关键参数

- `controlnet_strength` = `1`

## 知识

覆盖率 **70%**（85/121）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`ImageScale`、`MiniMaxH3VDNModelComposerT8Advanced`、`MiniMaxH3VDNExecutionPlanT8Advanced`、`RandomNoise`、`SamplerCustomAdvanced`、`MiniMaxH3LearnedLatentUpscaleT8Advanced`、`MiniMaxH3VDNRefinePlanT8Advanced`、`BasicGuider`、`MiniMaxH3TwoPassAudioAuditT8Advanced`、`MiniMaxH3AVDecodeT8`、`MiniMaxH3OutputTrimT8`、`PrimitiveBoolean`、`PointsEditor`、`SeCVideoSegmentation`、`GrowMask`、`ComfyMathExpression`、`LoadImage`、`VHS_VideoInfoLoaded`、`MiniMaxH3TwoPassLatentReconcileT8Advanced`、`MiniMaxH3AudioConditioningT8`、`SeCModelLoader`、`MaskPreview`、`MiniMaxH3FunControlNetApply`、`ModelPatchLoader`、`MiniMaxH3SafeAVSaveT8Advanced`、`MiniMaxH3DurationPlannerT8`、`VHS_LoadVideo`、`AIO_Preprocessor`、`SaveImage`

**用到的条目**：VAELoader、CLIPLoader、SaveImage、LoadImage、UNETLoader、MiniMaxH3FunControlNetApply、SamplerCustomAdvanced、MiniMaxH3AVDecodeT8
