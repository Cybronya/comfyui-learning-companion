---
key: 视频生成/图生视频/LTX2.3邪修采样多参人物场景分镜短剧_2046143007354789890.json
name: LTX2.3邪修采样多参人物场景分镜短剧_2046143007354789890.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3邪修采样多参人物场景分镜短剧_2046143007354789890.json
hash: bbae6a575c4c2837
coverage: 0.904762
learned_at: 2026-10-15 22:36:55
nodes: [ModelPatchTorchSettings, LTXVConditioning, RandomNoise, LTXVConcatAVLatent, PrimitiveInt, LTXVChunkFeedForward, LatentUpscaleModelLoader, PathchSageAttentionKJ, LTXVConcatAVLatent, SamplerCustomAdvanced, Reroute, TrimAudioDuration, LTXVSeparateAVLatent, RandomNoise, CFGGuider, VAEDecodeTiled, KSamplerSelect, KSamplerSelect, SamplerCustomAdvanced, ManualSigmas, CLIPTextEncode, ManualSigmas, CLIPTextEncode, CFGGuider, PrimitiveFloat, VHS_VideoCombine, LayerUtility: ImageScaleByAspectRatio V2, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, LoadImage, RandomNoise, easy indexAnything, easy indexAnything, easy indexAnything, easy indexAnything, easy indexAnything, SetNode, easy promptReplace, SetNode, GetNode, EmptyImage, easy promptLine, easy indexAnything, LoadImage, LoadImage, LoadImage, LoadImage, SetNode, PrimitiveInt, ImageResizeKJv2, ImageResizeKJv2, SetNode, easy convertAnything, easy promptLine, ComfyMathExpression, easy imageRemBg, easy imageRemBg, PreviewImage, GetNode, easy indexAnything, INTConstant, easy indexAnything, LoadImage, easy indexAnything, INTConstant, INTConstant, INTConstant, INTConstant, CM_IntToFloat, INTConstant, ShowText|pysssss, easy indexAnything, CR Text Concatenate, easy positive, easy promptLine, easy indexAnything, ImageResizeKJv2, easy imageRemBg, LayerUtility: NumberCalculatorV2, INTConstant, LayerUtility: NumberCalculatorV2, LayerUtility: NumberCalculatorV2, CFGGuider, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, LTXVConditioning, LayerUtility: NumberCalculatorV2, LayerUtility: NumberCalculatorV2, LayerUtility: NumberCalculatorV2, LayerUtility: NumberCalculatorV2, INTConstant, Reroute, BasicScheduler, SplitSigmas, SplitSigmas, LTXVImgToVideoInplace, VAEDecodeTiled, VHS_VideoCombine, LTXVImgToVideoInplace, easy promptList, PrimitiveInt, INTConstant, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, VAELoaderKJ, VAELoaderKJ, DualCLIPLoader, LTXVPreprocess, LTXVAddGuideMulti, ImageAddMulti, UNETLoader, GetImagesFromBatchIndexed, ImageBatchMulti, easy indexAnything, RegexExtract, RegexExtract, RegexExtract, easy promptReplace, easy promptLine, LoraLoaderModelOnly, CheckpointLoaderSimple, BasicScheduler, RTXVideoSuperResolution, LTXVAddGuideMulti, ManualSigmas, SamplerCustomAdvanced, LTXVAudioVAEDecode, ImageFromBatch, ImageFromBatch, LTXVSeparateAVLatent, LTXVLatentUpsampler, EmptyLTXVLatentVideo, CM_FloatToInt, LTXVEmptyLatentAudio, INTConstant, easy positive, easy positive, ImageResizeKJv2]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3邪修采样多参人物场景分镜短剧_2046143007354789890.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2046143007354789890.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（147 个）：
- `ModelPatchTorchSettings`
- `LTXVConditioning`
- `RandomNoise`
- `LTXVConcatAVLatent`
- `PrimitiveInt`
- `LTXVChunkFeedForward`
- `LatentUpscaleModelLoader`
- `PathchSageAttentionKJ`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `Reroute`
- `TrimAudioDuration`
- `LTXVSeparateAVLatent`
- `RandomNoise`
- `CFGGuider`
- `VAEDecodeTiled` ★核心
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `ManualSigmas`
- `CLIPTextEncode` ★核心
- `ManualSigmas`
- `CLIPTextEncode` ★核心
- `CFGGuider`
- `PrimitiveFloat`
- `VHS_VideoCombine`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `LoadImage`
- `RandomNoise`
- `easy indexAnything`
- `easy indexAnything`
- `easy indexAnything`
- `easy indexAnything`
- `easy indexAnything`
- `SetNode`
- `easy promptReplace`
- `SetNode`
- `GetNode`
- `EmptyImage`
- `easy promptLine`
- `easy indexAnything`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `SetNode`
- `PrimitiveInt`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `SetNode`
- `easy convertAnything`
- `easy promptLine`
- `ComfyMathExpression`
- `easy imageRemBg`
- `easy imageRemBg`
- `PreviewImage`
- `GetNode`
- `easy indexAnything`
- `INTConstant`
- `easy indexAnything`
- `LoadImage`
- `easy indexAnything`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `CM_IntToFloat`
- `INTConstant`
- `ShowText|pysssss`
- `easy indexAnything`
- `CR Text Concatenate`
- `easy positive`
- `easy promptLine`
- `easy indexAnything`
- `ImageResizeKJv2`
- `easy imageRemBg`
- `LayerUtility: NumberCalculatorV2`
- `INTConstant`
- `LayerUtility: NumberCalculatorV2`
- `LayerUtility: NumberCalculatorV2`
- `CFGGuider`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `LTXVConditioning`
- `LayerUtility: NumberCalculatorV2`
- `LayerUtility: NumberCalculatorV2`
- `LayerUtility: NumberCalculatorV2`
- `LayerUtility: NumberCalculatorV2`
- `INTConstant`
- `Reroute`
- `BasicScheduler`
- `SplitSigmas`
- `SplitSigmas`
- `LTXVImgToVideoInplace`
- `VAEDecodeTiled` ★核心
- `VHS_VideoCombine`
- `LTXVImgToVideoInplace`
- `easy promptList`
- `PrimitiveInt`
- `INTConstant`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoaderKJ`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `LTXVPreprocess`
- `LTXVAddGuideMulti`
- `ImageAddMulti`
- `UNETLoader` ★核心
- `GetImagesFromBatchIndexed`
- `ImageBatchMulti`
- `easy indexAnything`
- `RegexExtract`
- `RegexExtract`
- `RegexExtract`
- `easy promptReplace`
- `easy promptLine`
- `LoraLoaderModelOnly` ★核心
- `CheckpointLoaderSimple` ★核心
- `BasicScheduler`
- `RTXVideoSuperResolution`
- `LTXVAddGuideMulti`
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `LTXVAudioVAEDecode` ★核心
- `ImageFromBatch`
- `ImageFromBatch`
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `EmptyLTXVLatentVideo`
- `CM_FloatToInt`
- `LTXVEmptyLatentAudio` ★核心
- `INTConstant`
- `easy positive`
- `easy positive`
- `ImageResizeKJv2`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **90%**（133/147）

**有卡**：`ModelPatchTorchSettings`、`LTXVConditioning`、`RandomNoise`、`LTXVConcatAVLatent`、`LTXVChunkFeedForward`、`LatentUpscaleModelLoader`、`PathchSageAttentionKJ`、`SamplerCustomAdvanced`、`TrimAudioDuration`、`LTXVSeparateAVLatent`、`CFGGuider`、`VAEDecodeTiled`、`KSamplerSelect`、`ManualSigmas`、`CLIPTextEncode`、`VHS_VideoCombine`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageResizeKJv2`、`LoadImage`、`easy indexAnything`、`easy promptReplace`、`EmptyImage`、`easy promptLine`、`easy convertAnything`、`ComfyMathExpression`、`easy imageRemBg`、`INTConstant`、`CM_IntToFloat`、`CR Text Concatenate`、`easy positive`、`LayerUtility: NumberCalculatorV2`、`BasicScheduler`、`SplitSigmas`、`LTXVImgToVideoInplace`、`easy promptList`、`LoraLoaderModelOnly`、`VAELoaderKJ`、`DualCLIPLoader`、`LTXVPreprocess`、`LTXVAddGuideMulti`、`ImageAddMulti`、`UNETLoader`、`GetImagesFromBatchIndexed`、`ImageBatchMulti`、`RegexExtract`、`CheckpointLoaderSimple`、`RTXVideoSuperResolution`、`LTXVAudioVAEDecode`、`ImageFromBatch`、`LTXVLatentUpsampler`、`EmptyLTXVLatentVideo`、`CM_FloatToInt`、`LTXVEmptyLatentAudio`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect
