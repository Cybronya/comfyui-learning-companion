---
key: 视频生成/文生视频/MiniMax H3｜ControlNet Union  局部重绘专用工作流_2108263577818849282.json
name: MiniMax H3｜ControlNet Union  局部重绘专用工作流_2108263577818849282
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MiniMax H3｜ControlNet Union  局部重绘专用工作流_2108263577818849282.json
hash: afd937292fc9f4ab
coverage: 0.722826
learned_at: 2026-10-11 22:12:42
nodes: [CLIPLoader, VAELoader, VAELoader, UNETLoader, ModelPatchLoader, ImageScale, MiniMaxH3VDNModelComposerT8Advanced, MiniMaxH3VDNExecutionPlanT8Advanced, RandomNoise, SamplerCustomAdvanced, MiniMaxH3LearnedLatentUpscaleT8Advanced, MiniMaxH3VDNModelComposerT8Advanced, MiniMaxH3VDNRefinePlanT8Advanced, BasicGuider, RandomNoise, SamplerCustomAdvanced, MiniMaxH3TwoPassAudioAuditT8Advanced, MiniMaxH3AVDecodeT8, MiniMaxH3OutputTrimT8, MiniMaxH3SafeAVSaveT8Advanced, MarkdownNote, MarkdownNote, PrimitiveBoolean, PrimitiveInt, PrimitiveInt, ComfySwitchNode, ComfySwitchNode, MarkdownNote, MarkdownNote, AIO_Preprocessor, ComfySwitchNode, ComfySwitchNode, ComfySwitchNode, PointsEditor, GrowMask, ComfyMathExpression, ComfyMathExpression, MarkdownNote, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, PrimitiveInt, VHS_VideoInfoLoaded, MarkdownNote, MiniMaxH3DurationPlannerT8, PrimitiveFloat, BasicGuider, MiniMaxH3TwoPassLatentReconcileT8Advanced, PreviewAny, PrimitiveStringMultiline, VHS_LoadVideo, MaskPreview, MiniMaxH3FunControlNetApply, SeCModelLoader, SeCVideoSegmentation, MiniMaxH3ReferenceToVideo, MiniMaxH3ReferenceToVideo, MiniMaxH3OutputTrimT8, MiniMaxH3SafeAVSaveT8Advanced, CLIPLoader, VAELoader, VAELoader, UNETLoader, ImageScale, MiniMaxH3VDNModelComposerT8Advanced, MiniMaxH3VDNExecutionPlanT8Advanced, RandomNoise, SamplerCustomAdvanced, MiniMaxH3LearnedLatentUpscaleT8Advanced, MiniMaxH3VDNModelComposerT8Advanced, MiniMaxH3VDNRefinePlanT8Advanced, BasicGuider, RandomNoise, SamplerCustomAdvanced, MiniMaxH3TwoPassAudioAuditT8Advanced, MiniMaxH3AVDecodeT8, MiniMaxH3OutputTrimT8, MiniMaxH3SafeAVSaveT8Advanced, MarkdownNote, MarkdownNote, PrimitiveBoolean, PrimitiveInt, PrimitiveInt, ComfySwitchNode, ComfySwitchNode, MarkdownNote, MarkdownNote, AIO_Preprocessor, ComfySwitchNode, ComfySwitchNode, ComfySwitchNode, GrowMask, ComfyMathExpression, ComfyMathExpression, MarkdownNote, LoadImage, LoadImage, LoadImage, LoadImage, VHS_VideoInfoLoaded, MarkdownNote, MiniMaxH3DurationPlannerT8, BasicGuider, MiniMaxH3TwoPassLatentReconcileT8Advanced, PreviewAny, MiniMaxH3FunControlNetApply, SeCModelLoader, SeCVideoSegmentation, MiniMaxH3ReferenceToVideo, MiniMaxH3ReferenceToVideo, MiniMaxH3SafeAVSaveT8Advanced, CLIPLoader, VAELoader, VAELoader, UNETLoader, ModelPatchLoader, ImageScale, MiniMaxH3VDNModelComposerT8Advanced, MiniMaxH3VDNExecutionPlanT8Advanced, RandomNoise, SamplerCustomAdvanced, MiniMaxH3LearnedLatentUpscaleT8Advanced, MiniMaxH3VDNModelComposerT8Advanced, MiniMaxH3VDNRefinePlanT8Advanced, BasicGuider, RandomNoise, SamplerCustomAdvanced, MiniMaxH3TwoPassAudioAuditT8Advanced, MiniMaxH3AVDecodeT8, MiniMaxH3OutputTrimT8, MiniMaxH3SafeAVSaveT8Advanced, MarkdownNote, MarkdownNote, PrimitiveBoolean, PrimitiveInt, PrimitiveInt, ComfySwitchNode, ComfySwitchNode, MarkdownNote, MarkdownNote, AIO_Preprocessor, ComfySwitchNode, ComfySwitchNode, ComfySwitchNode, PointsEditor, GrowMask, ComfyMathExpression, ComfyMathExpression, MarkdownNote, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, PrimitiveInt, VHS_VideoInfoLoaded, MarkdownNote, MiniMaxH3DurationPlannerT8, PrimitiveFloat, BasicGuider, MiniMaxH3TwoPassLatentReconcileT8Advanced, PreviewAny, PrimitiveStringMultiline, VHS_LoadVideo, MaskPreview, MiniMaxH3FunControlNetApply, SeCModelLoader, SeCVideoSegmentation, MiniMaxH3ReferenceToVideo, MiniMaxH3ReferenceToVideo, MiniMaxH3OutputTrimT8, MiniMaxH3SafeAVSaveT8Advanced, PrimitiveInt, VHS_LoadVideo, ModelPatchLoader, MiniMaxH3OutputTrimT8, PrimitiveFloat, LoadImage, PrimitiveStringMultiline, PointsEditor, MaskPreview, SaveImage]
patterns: []
missing: []
parameters: {"controlnet_strength": 1.8}
---

# 视频生成/文生视频/MiniMax H3｜ControlNet Union  局部重绘专用工作流_2108263577818849282.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MiniMax H3｜ControlNet Union  局部重绘专用工作流_2108263577818849282.json`

## 结构

**生成流程**：Model → Control → Sampling → Process → Output → Other

**节点**（184 个）：
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `UNETLoader` ★核心
- `ModelPatchLoader`
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
- `AIO_Preprocessor`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `PointsEditor`
- `GrowMask`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `MarkdownNote`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PrimitiveInt`
- `VHS_VideoInfoLoaded`
- `MarkdownNote`
- `MiniMaxH3DurationPlannerT8`
- `PrimitiveFloat`
- `BasicGuider`
- `MiniMaxH3TwoPassLatentReconcileT8Advanced`
- `PreviewAny`
- `PrimitiveStringMultiline`
- `VHS_LoadVideo`
- `MaskPreview`
- `MiniMaxH3FunControlNetApply` ★核心
- `SeCModelLoader`
- `SeCVideoSegmentation`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3OutputTrimT8`
- `MiniMaxH3SafeAVSaveT8Advanced`
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
- `AIO_Preprocessor`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `GrowMask`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `MarkdownNote`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `VHS_VideoInfoLoaded`
- `MarkdownNote`
- `MiniMaxH3DurationPlannerT8`
- `BasicGuider`
- `MiniMaxH3TwoPassLatentReconcileT8Advanced`
- `PreviewAny`
- `MiniMaxH3FunControlNetApply` ★核心
- `SeCModelLoader`
- `SeCVideoSegmentation`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SafeAVSaveT8Advanced`
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `UNETLoader` ★核心
- `ModelPatchLoader`
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
- `AIO_Preprocessor`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `PointsEditor`
- `GrowMask`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `MarkdownNote`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PrimitiveInt`
- `VHS_VideoInfoLoaded`
- `MarkdownNote`
- `MiniMaxH3DurationPlannerT8`
- `PrimitiveFloat`
- `BasicGuider`
- `MiniMaxH3TwoPassLatentReconcileT8Advanced`
- `PreviewAny`
- `PrimitiveStringMultiline`
- `VHS_LoadVideo`
- `MaskPreview`
- `MiniMaxH3FunControlNetApply` ★核心
- `SeCModelLoader`
- `SeCVideoSegmentation`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3OutputTrimT8`
- `MiniMaxH3SafeAVSaveT8Advanced`
- `PrimitiveInt`
- `VHS_LoadVideo`
- `ModelPatchLoader`
- `MiniMaxH3OutputTrimT8`
- `PrimitiveFloat`
- `LoadImage`
- `PrimitiveStringMultiline`
- `PointsEditor`
- `MaskPreview`
- `SaveImage`

## 关键参数

- `controlnet_strength` = `1.8`

## 知识

覆盖率 **72%**（133/184）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`ModelPatchLoader`、`ImageScale`、`MiniMaxH3VDNModelComposerT8Advanced`、`MiniMaxH3VDNExecutionPlanT8Advanced`、`RandomNoise`、`SamplerCustomAdvanced`、`MiniMaxH3LearnedLatentUpscaleT8Advanced`、`MiniMaxH3VDNRefinePlanT8Advanced`、`BasicGuider`、`MiniMaxH3TwoPassAudioAuditT8Advanced`、`MiniMaxH3AVDecodeT8`、`MiniMaxH3OutputTrimT8`、`MiniMaxH3SafeAVSaveT8Advanced`、`PrimitiveBoolean`、`AIO_Preprocessor`、`PointsEditor`、`GrowMask`、`ComfyMathExpression`、`LoadImage`、`VHS_VideoInfoLoaded`、`MiniMaxH3DurationPlannerT8`、`MiniMaxH3TwoPassLatentReconcileT8Advanced`、`VHS_LoadVideo`、`MaskPreview`、`MiniMaxH3FunControlNetApply`、`SeCModelLoader`、`SeCVideoSegmentation`、`MiniMaxH3ReferenceToVideo`、`SaveImage`

**用到的条目**：VAELoader、CLIPLoader、SaveImage、LoadImage、UNETLoader、MiniMaxH3FunControlNetApply、SamplerCustomAdvanced、MiniMaxH3AVDecodeT8
