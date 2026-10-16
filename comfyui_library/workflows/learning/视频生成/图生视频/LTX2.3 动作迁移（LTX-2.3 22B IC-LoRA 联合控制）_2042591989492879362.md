---
key: 视频生成/图生视频/LTX2.3 动作迁移（LTX-2.3 22B IC-LoRA 联合控制）_2042591989492879362.json
name: LTX2.3 动作迁移（LTX-2.3 22B IC-LoRA 联合控制）_2042591989492879362.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2042591989492879362.json
hash: a8dcef00602ad66d
coverage: 0.469027
learned_at: 2026-10-15 22:36:28
nodes: [GetNode, ModelPatchTorchSettings, LTXVChunkFeedForward, SetNode, Anything Everywhere, SetNode, RandomNoise, PathchSageAttentionKJ, GetNode, GetNode, PrimitiveBoolean, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, LTXAddVideoICLoRAGuide, VAEDecodeTiled, GetNode, GetNode, PrimitiveInt, CannyEdgePreprocessor, GetNode, GetNode, GetNode, GetNode, ComfyMathExpression, GetNode, LTXVImgToVideoConditionOnly, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, LTXVConditioning, SetNode, PrimitiveInt, PrimitiveInt, ComfyMathExpression, SetNode, PrimitiveInt, GetNode, GetNode, ComfyMathExpression, LTXVPreprocess, SetNode, Note, LayerUtility: ImageScaleByAspectRatio V2, Note, SetNode, easy showAnything, VAELoaderKJ, DualCLIPLoader, LatentUpscaleModelLoader, UNETLoader, VAELoaderKJ, SetNode, SetNode, CFGGuider, GetNode, GetNode, GetNode, SamplerCustomAdvanced, KSamplerSelect, GetNode, ManualSigmas, GetNode, GetNode, LTXVSeparateAVLatent, GetNode, GetNode, GetNode, LTXVLatentUpsampler, LTXVImgToVideoInplace, ManualSigmas, KSamplerSelect, RandomNoise, CFGGuider, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVAudioVAEDecode, LTXVCropGuides, LTXVSeparateAVLatent, easy cleanGpuUsed, LoadImage, CLIPTextEncode, LTX2_NAG, SetNode, Note, GetNode, GetNode, LTXVConcatAVLatent, DepthAnythingPreprocessor, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, VHS_VideoCombine, SetNode, SetNode, ComfyMathExpression, CLIPTextEncode, PrimitiveInt, ResizeImageMaskNode, DWPreprocessor, easy cleanGpuUsed, easy showAnything, GetImageSize, easy showAnything, easy showAnything, GetNode, VHS_LoadVideo, LTXICLoRALoaderModelOnly]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3 动作迁移（LTX-2.3 22B IC-LoRA 联合控制）_2042591989492879362.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2042591989492879362.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（113 个）：
- `GetNode`
- `ModelPatchTorchSettings`
- `LTXVChunkFeedForward`
- `SetNode`
- `Anything Everywhere`
- `SetNode`
- `RandomNoise`
- `PathchSageAttentionKJ`
- `GetNode`
- `GetNode`
- `PrimitiveBoolean`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `LTXAddVideoICLoRAGuide`
- `VAEDecodeTiled` ★核心
- `GetNode`
- `GetNode`
- `PrimitiveInt`
- `CannyEdgePreprocessor`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ComfyMathExpression`
- `GetNode`
- `LTXVImgToVideoConditionOnly`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `LTXVConditioning`
- `SetNode`
- `PrimitiveInt`
- `PrimitiveInt`
- `ComfyMathExpression`
- `SetNode`
- `PrimitiveInt`
- `GetNode`
- `GetNode`
- `ComfyMathExpression`
- `LTXVPreprocess`
- `SetNode`
- `Note`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Note`
- `SetNode`
- `easy showAnything`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `LatentUpscaleModelLoader`
- `UNETLoader` ★核心
- `VAELoaderKJ`
- `SetNode`
- `SetNode`
- `CFGGuider`
- `GetNode`
- `GetNode`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `GetNode`
- `ManualSigmas`
- `GetNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `CFGGuider`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `easy cleanGpuUsed`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `LTX2_NAG`
- `SetNode`
- `Note`
- `GetNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `DepthAnythingPreprocessor`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `SetNode`
- `SetNode`
- `ComfyMathExpression`
- `CLIPTextEncode` ★核心
- `PrimitiveInt`
- `ResizeImageMaskNode`
- `DWPreprocessor`
- `easy cleanGpuUsed`
- `easy showAnything`
- `GetImageSize`
- `easy showAnything`
- `easy showAnything`
- `GetNode`
- `VHS_LoadVideo`
- `LTXICLoRALoaderModelOnly` ★核心

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **47%**（53/113）

**有卡**：`ModelPatchTorchSettings`、`LTXVChunkFeedForward`、`RandomNoise`、`PathchSageAttentionKJ`、`PrimitiveBoolean`、`LTXAddVideoICLoRAGuide`、`VAEDecodeTiled`、`CannyEdgePreprocessor`、`ComfyMathExpression`、`LTXVImgToVideoConditionOnly`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`LTXVConditioning`、`LTXVPreprocess`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAELoaderKJ`、`DualCLIPLoader`、`LatentUpscaleModelLoader`、`UNETLoader`、`CFGGuider`、`SamplerCustomAdvanced`、`KSamplerSelect`、`ManualSigmas`、`LTXVSeparateAVLatent`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`LTXVConcatAVLatent`、`LTXVAudioVAEDecode`、`LTXVCropGuides`、`easy cleanGpuUsed`、`LoadImage`、`CLIPTextEncode`、`LTX2_NAG`、`DepthAnythingPreprocessor`、`VHS_VideoCombine`、`ResizeImageMaskNode`、`DWPreprocessor`、`GetImageSize`、`VHS_LoadVideo`、`LTXICLoRALoaderModelOnly`

**用到的条目**：CLIPTextEncode、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、DepthAnythingPreprocessor、CannyEdgePreprocessor、CFGGuider、KSamplerSelect
