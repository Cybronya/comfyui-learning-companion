---
key: 视频生成/图生视频/MiniMax H3 ControlNet Union局部重绘专用工作流 精准控制改图_2109171442880442369.json
name: MiniMax H3 ControlNet Union局部重绘专用工作流 精准控制改图_2109171442880442369
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMax H3 ControlNet Union局部重绘专用工作流 精准控制改图_2109171442880442369.json
hash: 36093ecfd961bf77
coverage: 0.811224
learned_at: 2026-10-17 22:49:45
nodes: [CLIPLoader, VAELoader, VAELoader, UNETLoader, ModelPatchLoader, ImageScale, MiniMaxH3VDNModelComposerT8Advanced, MiniMaxH3VDNExecutionPlanT8Advanced, RandomNoise, SamplerCustomAdvanced, MiniMaxH3LearnedLatentUpscaleT8Advanced, MiniMaxH3VDNModelComposerT8Advanced, MiniMaxH3VDNRefinePlanT8Advanced, BasicGuider, RandomNoise, SamplerCustomAdvanced, MiniMaxH3TwoPassAudioAuditT8Advanced, MiniMaxH3AVDecodeT8, MiniMaxH3OutputTrimT8, MiniMaxH3SafeAVSaveT8Advanced, PrimitiveBoolean, PrimitiveInt, PrimitiveInt, ComfySwitchNode, ComfySwitchNode, AIO_Preprocessor, ComfySwitchNode, ComfySwitchNode, ComfySwitchNode, PointsEditor, GrowMask, ComfyMathExpression, ComfyMathExpression, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, PrimitiveInt, VHS_VideoInfoLoaded, MiniMaxH3DurationPlannerT8, PrimitiveFloat, BasicGuider, MiniMaxH3TwoPassLatentReconcileT8Advanced, PreviewAny, PrimitiveStringMultiline, VHS_LoadVideo, MaskPreview, MiniMaxH3FunControlNetApply, SeCModelLoader, SeCVideoSegmentation, MiniMaxH3ReferenceToVideo, MiniMaxH3ReferenceToVideo, MiniMaxH3OutputTrimT8, MiniMaxH3SafeAVSaveT8Advanced, CLIPLoader, VAELoader, VAELoader, UNETLoader, ImageScale, MiniMaxH3VDNModelComposerT8Advanced, MiniMaxH3VDNExecutionPlanT8Advanced, RandomNoise, SamplerCustomAdvanced, MiniMaxH3LearnedLatentUpscaleT8Advanced, MiniMaxH3VDNModelComposerT8Advanced, MiniMaxH3VDNRefinePlanT8Advanced, BasicGuider, RandomNoise, SamplerCustomAdvanced, MiniMaxH3TwoPassAudioAuditT8Advanced, MiniMaxH3AVDecodeT8, MiniMaxH3OutputTrimT8, MiniMaxH3SafeAVSaveT8Advanced, PrimitiveBoolean, PrimitiveInt, PrimitiveInt, ComfySwitchNode, ComfySwitchNode, AIO_Preprocessor, ComfySwitchNode, ComfySwitchNode, ComfySwitchNode, GrowMask, ComfyMathExpression, ComfyMathExpression, LoadImage, LoadImage, LoadImage, LoadImage, VHS_VideoInfoLoaded, MiniMaxH3DurationPlannerT8, BasicGuider, MiniMaxH3TwoPassLatentReconcileT8Advanced, PreviewAny, MiniMaxH3FunControlNetApply, SeCModelLoader, SeCVideoSegmentation, MiniMaxH3ReferenceToVideo, MiniMaxH3ReferenceToVideo, MiniMaxH3SafeAVSaveT8Advanced, CLIPLoader, VAELoader, VAELoader, UNETLoader, ModelPatchLoader, ImageScale, MiniMaxH3VDNModelComposerT8Advanced, MiniMaxH3VDNExecutionPlanT8Advanced, RandomNoise, SamplerCustomAdvanced, MiniMaxH3LearnedLatentUpscaleT8Advanced, MiniMaxH3VDNModelComposerT8Advanced, MiniMaxH3VDNRefinePlanT8Advanced, BasicGuider, RandomNoise, SamplerCustomAdvanced, MiniMaxH3TwoPassAudioAuditT8Advanced, MiniMaxH3AVDecodeT8, MiniMaxH3OutputTrimT8, MiniMaxH3SafeAVSaveT8Advanced, PrimitiveBoolean, PrimitiveInt, PrimitiveInt, ComfySwitchNode, ComfySwitchNode, AIO_Preprocessor, ComfySwitchNode, ComfySwitchNode, ComfySwitchNode, PointsEditor, GrowMask, ComfyMathExpression, ComfyMathExpression, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, PrimitiveInt, VHS_VideoInfoLoaded, MiniMaxH3DurationPlannerT8, PrimitiveFloat, BasicGuider, MiniMaxH3TwoPassLatentReconcileT8Advanced, PreviewAny, PrimitiveStringMultiline, VHS_LoadVideo, MaskPreview, MiniMaxH3FunControlNetApply, SeCModelLoader, SeCVideoSegmentation, MiniMaxH3ReferenceToVideo, MiniMaxH3ReferenceToVideo, MiniMaxH3OutputTrimT8, MiniMaxH3SafeAVSaveT8Advanced, PrimitiveInt, VHS_LoadVideo, ModelPatchLoader, MiniMaxH3OutputTrimT8, PrimitiveFloat, LoadImage, PrimitiveStringMultiline, PointsEditor, MaskPreview, SaveImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note, SaveImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "controlnet_strength": 1.8, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/MiniMax H3 ControlNet Union局部重绘专用工作流 精准控制改图_2109171442880442369.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMax H3 ControlNet Union局部重绘专用工作流 精准控制改图_2109171442880442369.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（196 个）：
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
- `PrimitiveBoolean`
- `PrimitiveInt`
- `PrimitiveInt`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `AIO_Preprocessor`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `PointsEditor`
- `GrowMask`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PrimitiveInt`
- `VHS_VideoInfoLoaded`
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
- `PrimitiveBoolean`
- `PrimitiveInt`
- `PrimitiveInt`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `AIO_Preprocessor`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `GrowMask`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `VHS_VideoInfoLoaded`
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
- `PrimitiveBoolean`
- `PrimitiveInt`
- `PrimitiveInt`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `AIO_Preprocessor`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `PointsEditor`
- `GrowMask`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PrimitiveInt`
- `VHS_VideoInfoLoaded`
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
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `Note`
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `controlnet_strength` = `1.8`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **81%**（159/196）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`ModelPatchLoader`、`ImageScale`、`MiniMaxH3VDNModelComposerT8Advanced`、`MiniMaxH3VDNExecutionPlanT8Advanced`、`RandomNoise`、`SamplerCustomAdvanced`、`MiniMaxH3LearnedLatentUpscaleT8Advanced`、`MiniMaxH3VDNRefinePlanT8Advanced`、`BasicGuider`、`MiniMaxH3TwoPassAudioAuditT8Advanced`、`MiniMaxH3AVDecodeT8`、`MiniMaxH3OutputTrimT8`、`MiniMaxH3SafeAVSaveT8Advanced`、`PrimitiveBoolean`、`AIO_Preprocessor`、`PointsEditor`、`GrowMask`、`ComfyMathExpression`、`LoadImage`、`VHS_VideoInfoLoaded`、`MiniMaxH3DurationPlannerT8`、`MiniMaxH3TwoPassLatentReconcileT8Advanced`、`VHS_LoadVideo`、`MaskPreview`、`MiniMaxH3FunControlNetApply`、`SeCModelLoader`、`SeCVideoSegmentation`、`MiniMaxH3ReferenceToVideo`、`SaveImage`、`LoraLoaderModelOnly`、`KSampler`、`EmptyLatentImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、SaveImage、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
