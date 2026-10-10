---
key: 视频生成/图生视频/MiniMax H3｜ControlNet Union 2.0 视频控制与局部重绘·音频驱动数字人｜VDN 12步高清版_2106627537043550210.json
name: MiniMax H3｜ControlNet Union 2.0 视频控制与局部重绘·音频驱动数字人｜VDN 12步高清版_2106627537043550210
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMax H3｜ControlNet Union 2.0 视频控制与局部重绘·音频驱动数字人｜VDN 12步高清版_2106627537043550210.json
hash: a504058f5e82cd10
coverage: 0.681818
learned_at: 2026-10-10 22:53:17
nodes: [PrimitiveFloat, CLIPLoader, VAELoader, VAELoader, UNETLoader, ModelPatchLoader, ImageScale, MiniMaxH3FunControlNetApply, MiniMaxH3VDNModelComposerT8Advanced, MiniMaxH3VDNExecutionPlanT8Advanced, BasicGuider, RandomNoise, SamplerCustomAdvanced, MiniMaxH3VDNModelComposerT8Advanced, MiniMaxH3TwoPassLatentReconcileT8Advanced, MiniMaxH3VDNRefinePlanT8Advanced, BasicGuider, RandomNoise, SamplerCustomAdvanced, MiniMaxH3TwoPassAudioAuditT8Advanced, MiniMaxH3AVDecodeT8, MiniMaxH3OutputTrimT8, MarkdownNote, LoadAudio, MarkdownNote, PrimitiveBoolean, PrimitiveInt, PrimitiveInt, ComfySwitchNode, ComfySwitchNode, MarkdownNote, MarkdownNote, AIO_Preprocessor, ComfySwitchNode, ComfySwitchNode, ComfySwitchNode, SeCModelLoader, PointsEditor, SeCVideoSegmentation, GrowMask, MaskPreview, PrimitiveInt, ComfyMathExpression, ComfyMathExpression, MarkdownNote, AudioSeparation, LTXVAudioVAEEncode, SolidMask, SetLatentNoiseMask, LTXVConcatAVLatent, MarkdownNote, MarkdownNote, MiniMaxH3ReferenceToVideo, ComfySwitchNode, VHS_VideoInfoLoaded, PreviewAny, PrimitiveBoolean, easy showAnything, MiniMaxH3AudioWindowT8, VHS_LoadVideo, PrimitiveStringMultiline, MiniMaxH3SafeAVSaveT8Advanced, PreviewImage, MiniMaxH3LearnedLatentUpscaleT8Advanced, MiniMaxH3ReferenceToVideo, SaveImage]
patterns: []
missing: []
parameters: {"controlnet_strength": 1}
---

# 视频生成/图生视频/MiniMax H3｜ControlNet Union 2.0 视频控制与局部重绘·音频驱动数字人｜VDN 12步高清版_2106627537043550210.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMax H3｜ControlNet Union 2.0 视频控制与局部重绘·音频驱动数字人｜VDN 12步高清版_2106627537043550210.json`

## 结构

**生成流程**：Model → Encode → Control → Sampling → Process → Output → Other

**节点**（66 个）：
- `PrimitiveFloat`
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `UNETLoader` ★核心
- `ModelPatchLoader`
- `ImageScale`
- `MiniMaxH3FunControlNetApply` ★核心
- `MiniMaxH3VDNModelComposerT8Advanced`
- `MiniMaxH3VDNExecutionPlanT8Advanced`
- `BasicGuider`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3VDNModelComposerT8Advanced`
- `MiniMaxH3TwoPassLatentReconcileT8Advanced`
- `MiniMaxH3VDNRefinePlanT8Advanced`
- `BasicGuider`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3TwoPassAudioAuditT8Advanced`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3OutputTrimT8`
- `MarkdownNote`
- `LoadAudio`
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
- `SeCModelLoader`
- `PointsEditor`
- `SeCVideoSegmentation`
- `GrowMask`
- `MaskPreview`
- `PrimitiveInt`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `MarkdownNote`
- `AudioSeparation`
- `LTXVAudioVAEEncode` ★核心
- `SolidMask`
- `SetLatentNoiseMask`
- `LTXVConcatAVLatent`
- `MarkdownNote`
- `MarkdownNote`
- `MiniMaxH3ReferenceToVideo`
- `ComfySwitchNode`
- `VHS_VideoInfoLoaded`
- `PreviewAny`
- `PrimitiveBoolean`
- `easy showAnything`
- `MiniMaxH3AudioWindowT8`
- `VHS_LoadVideo`
- `PrimitiveStringMultiline`
- `MiniMaxH3SafeAVSaveT8Advanced`
- `PreviewImage`
- `MiniMaxH3LearnedLatentUpscaleT8Advanced`
- `MiniMaxH3ReferenceToVideo`
- `SaveImage`

## 关键参数

- `controlnet_strength` = `1`

## 知识

覆盖率 **68%**（45/66）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`ModelPatchLoader`、`ImageScale`、`MiniMaxH3FunControlNetApply`、`MiniMaxH3VDNModelComposerT8Advanced`、`MiniMaxH3VDNExecutionPlanT8Advanced`、`BasicGuider`、`RandomNoise`、`SamplerCustomAdvanced`、`MiniMaxH3TwoPassLatentReconcileT8Advanced`、`MiniMaxH3VDNRefinePlanT8Advanced`、`MiniMaxH3TwoPassAudioAuditT8Advanced`、`MiniMaxH3AVDecodeT8`、`MiniMaxH3OutputTrimT8`、`LoadAudio`、`PrimitiveBoolean`、`AIO_Preprocessor`、`SeCModelLoader`、`PointsEditor`、`SeCVideoSegmentation`、`GrowMask`、`MaskPreview`、`ComfyMathExpression`、`AudioSeparation`、`LTXVAudioVAEEncode`、`SolidMask`、`SetLatentNoiseMask`、`LTXVConcatAVLatent`、`MiniMaxH3ReferenceToVideo`、`VHS_VideoInfoLoaded`、`MiniMaxH3AudioWindowT8`、`VHS_LoadVideo`、`MiniMaxH3SafeAVSaveT8Advanced`、`MiniMaxH3LearnedLatentUpscaleT8Advanced`、`SaveImage`

**用到的条目**：VAELoader、CLIPLoader、SaveImage、UNETLoader、MiniMaxH3FunControlNetApply、SamplerCustomAdvanced、LTXVConcatAVLatent、SetLatentNoiseMask
