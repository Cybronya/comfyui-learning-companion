---
key: 视频生成/图生视频/LTX-2.5-图生视频-数字人唱歌_对口型-可上传音频_2096779577384329217.json
name: LTX-2.5-图生视频-数字人唱歌_对口型-可上传音频_2096779577384329217
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX-2.5-图生视频-数字人唱歌_对口型-可上传音频_2096779577384329217.json
hash: c4a84cae5a5ae502
coverage: 0.595041
learned_at: 2026-10-17 01:27:58
nodes: [CLIPTextEncode, CLIPTextEncode, PrimitiveFloat, LTXVPreprocess, EmptyLTXVLatentVideo, LTXVImgToVideoInplace, GetNode, GetNode, SamplerCustomAdvanced, GetNode, GetNode, SetNode, SetNode, easy int, GetNode, LTXVSeparateAVLatent, LTXVImgToVideoInplace, LTXVLatentUpsampler, SamplerCustomAdvanced, LTXVSeparateAVLatent, GetNode, LTXVSpatioTemporalTiledVAEDecode, LTXVAudioVAEDecode, GetNode, SetNode, SetNode, CreateVideo, GetNode, WanVideoImageResizeToClosest, ImageScaleBy, GetImageSize, GetNode, easy int, easy int, KSamplerSelect, RandomNoise, ResizeImagesByLongerEdge, SetNode, UNETLoader, SetNode, VAELoader, SetNode, SetNode, SetNode, PrimitiveInt, LTXVGemmaEnhancePrompt, VAELoader, CLIPLoader, LatentUpscaleModelLoader, KSamplerSelect, SolidMask, SetNode, MathExpression|pysssss, SetNode, MelBandRoFormerModelLoader, MelBandRoFormerSampler, GetNode, easy int, SetNode, TrimAudioDuration, SetLatentNoiseMask, LTXVAudioVAEEncode, GetNode, Audio Duration (mtb), ImageResizeKJv2, EmptyImage, SetNode, GetNode, SetNode, GetNode, GetNode, DF_Int_to_Float, DF_Int_to_Float, MathExpression|pysssss, DF_Int_to_Float, SetNode, easy ifElse, GetNode, easy boolean, SetNode, SetNode, GetNode, LTXVConcatAVLatent, LTXVEmptyLatentAudio, GetNode, easy ifElse, GetNode, KSamplerSelect, GetNode, ManualSigmas, KSamplerSelect, ManualSigmas, LTXVConcatAVLatent, ManualSigmas, KSamplerSelect, ManualSigmas, KSamplerSelect, easy float, GetNode, GetNode, SetNode, ImpactExecutionOrderController, LTXVConditioning, LTXVDualCFGGuider, GetNode, GetNode, GetNode, RandomNoise, LTXVDualCFGGuider, CFGGuider, GetNode, easy float, LTXVScheduler, SaveVideo, PrimitiveStringMultiline, LoraLoaderModelOnly, CFGGuider, LoadImage, LoadAudio, easy int, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 121}
---

# 视频生成/图生视频/LTX-2.5-图生视频-数字人唱歌_对口型-可上传音频_2096779577384329217.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX-2.5-图生视频-数字人唱歌_对口型-可上传音频_2096779577384329217.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（121 个）：
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `PrimitiveFloat`
- `LTXVPreprocess`
- `EmptyLTXVLatentVideo`
- `LTXVImgToVideoInplace`
- `GetNode`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `easy int`
- `GetNode`
- `LTXVSeparateAVLatent`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `GetNode`
- `LTXVSpatioTemporalTiledVAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `SetNode`
- `SetNode`
- `CreateVideo`
- `GetNode`
- `WanVideoImageResizeToClosest`
- `ImageScaleBy`
- `GetImageSize`
- `GetNode`
- `easy int`
- `easy int`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SetNode`
- `UNETLoader` ★核心
- `SetNode`
- `VAELoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `PrimitiveInt`
- `LTXVGemmaEnhancePrompt`
- `VAELoader`
- `CLIPLoader`
- `LatentUpscaleModelLoader`
- `KSamplerSelect` ★核心
- `SolidMask`
- `SetNode`
- `MathExpression|pysssss`
- `SetNode`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler` ★核心
- `GetNode`
- `easy int`
- `SetNode`
- `TrimAudioDuration`
- `SetLatentNoiseMask`
- `LTXVAudioVAEEncode` ★核心
- `GetNode`
- `Audio Duration (mtb)`
- `ImageResizeKJv2`
- `EmptyImage`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `DF_Int_to_Float`
- `DF_Int_to_Float`
- `MathExpression|pysssss`
- `DF_Int_to_Float`
- `SetNode`
- `easy ifElse`
- `GetNode`
- `easy boolean`
- `SetNode`
- `SetNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `LTXVEmptyLatentAudio` ★核心
- `GetNode`
- `easy ifElse`
- `GetNode`
- `KSamplerSelect` ★核心
- `GetNode`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `easy float`
- `GetNode`
- `GetNode`
- `SetNode`
- `ImpactExecutionOrderController`
- `LTXVConditioning`
- `LTXVDualCFGGuider`
- `GetNode`
- `GetNode`
- `GetNode`
- `RandomNoise`
- `LTXVDualCFGGuider`
- `CFGGuider`
- `GetNode`
- `easy float`
- `LTXVScheduler`
- `SaveVideo`
- `PrimitiveStringMultiline`
- `LoraLoaderModelOnly` ★核心
- `CFGGuider`
- `LoadImage`
- `LoadAudio`
- `easy int`
- `PrimitiveStringMultiline`

## 关键参数

- `width` = `121`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **60%**（72/121）

**有卡**：`CLIPTextEncode`、`LTXVPreprocess`、`EmptyLTXVLatentVideo`、`LTXVImgToVideoInplace`、`SamplerCustomAdvanced`、`easy int`、`LTXVSeparateAVLatent`、`LTXVLatentUpsampler`、`LTXVSpatioTemporalTiledVAEDecode`、`LTXVAudioVAEDecode`、`CreateVideo`、`WanVideoImageResizeToClosest`、`ImageScaleBy`、`GetImageSize`、`KSamplerSelect`、`RandomNoise`、`ResizeImagesByLongerEdge`、`UNETLoader`、`VAELoader`、`LTXVGemmaEnhancePrompt`、`CLIPLoader`、`LatentUpscaleModelLoader`、`SolidMask`、`MathExpression|pysssss`、`MelBandRoFormerModelLoader`、`MelBandRoFormerSampler`、`TrimAudioDuration`、`SetLatentNoiseMask`、`LTXVAudioVAEEncode`、`Audio Duration (mtb)`、`ImageResizeKJv2`、`EmptyImage`、`DF_Int_to_Float`、`easy boolean`、`LTXVConcatAVLatent`、`LTXVEmptyLatentAudio`、`ManualSigmas`、`easy float`、`ImpactExecutionOrderController`、`LTXVConditioning`、`LTXVDualCFGGuider`、`CFGGuider`、`LTXVScheduler`、`SaveVideo`、`LoraLoaderModelOnly`、`LoadImage`、`LoadAudio`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、CFGGuider、KSamplerSelect
