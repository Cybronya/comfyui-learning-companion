---
key: 视频生成/图生视频/数字人唱歌对口型可上传音频｜LTX-2.5角色一致性图生视频工作流_2088154505077678082.json
name: 数字人唱歌对口型可上传音频｜LTX-2.5角色一致性图生视频工作流_2088154505077678082
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/数字人唱歌对口型可上传音频｜LTX-2.5角色一致性图生视频工作流_2088154505077678082.json
hash: 0a548e311c7aa445
coverage: 0.641892
learned_at: 2026-10-16 21:28:11
nodes: [CLIPTextEncode, CLIPTextEncode, PrimitiveFloat, LTXVPreprocess, EmptyLTXVLatentVideo, LTXVImgToVideoInplace, GetNode, GetNode, SamplerCustomAdvanced, GetNode, GetNode, SetNode, SetNode, easy int, GetNode, LTXVSeparateAVLatent, LTXVImgToVideoInplace, LTXVLatentUpsampler, SamplerCustomAdvanced, LTXVSeparateAVLatent, GetNode, LTXVSpatioTemporalTiledVAEDecode, LTXVAudioVAEDecode, GetNode, SetNode, SetNode, CreateVideo, GetNode, WanVideoImageResizeToClosest, ImageScaleBy, GetImageSize, GetNode, easy int, easy int, KSamplerSelect, RandomNoise, ResizeImagesByLongerEdge, SetNode, UNETLoader, SetNode, VAELoader, SetNode, SetNode, SetNode, PrimitiveInt, LTXVGemmaEnhancePrompt, VAELoader, CLIPLoader, LatentUpscaleModelLoader, KSamplerSelect, SolidMask, SetNode, MathExpression|pysssss, SetNode, MelBandRoFormerModelLoader, MelBandRoFormerSampler, GetNode, easy int, SetNode, TrimAudioDuration, SetLatentNoiseMask, LTXVAudioVAEEncode, GetNode, Audio Duration (mtb), ImageResizeKJv2, EmptyImage, SetNode, GetNode, SetNode, GetNode, GetNode, DF_Int_to_Float, DF_Int_to_Float, MathExpression|pysssss, DF_Int_to_Float, SetNode, easy ifElse, GetNode, easy boolean, SetNode, SetNode, GetNode, LTXVConcatAVLatent, LTXVEmptyLatentAudio, GetNode, easy ifElse, GetNode, KSamplerSelect, GetNode, ManualSigmas, KSamplerSelect, ManualSigmas, LTXVConcatAVLatent, ManualSigmas, KSamplerSelect, ManualSigmas, KSamplerSelect, easy float, GetNode, GetNode, SetNode, ImpactExecutionOrderController, LTXVConditioning, LTXVDualCFGGuider, GetNode, GetNode, GetNode, RandomNoise, LTXVDualCFGGuider, CFGGuider, GetNode, easy float, LTXVScheduler, SaveVideo, PrimitiveStringMultiline, PrimitiveStringMultiline, easy int, LoadAudio, LoraLoaderModelOnly, CFGGuider, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, JjkText, solarL_SaveImagesToZip, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note, LoadImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/数字人唱歌对口型可上传音频｜LTX-2.5角色一致性图生视频工作流_2088154505077678082.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/数字人唱歌对口型可上传音频｜LTX-2.5角色一致性图生视频工作流_2088154505077678082.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（148 个）：
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
- `PrimitiveStringMultiline`
- `easy int`
- `LoadAudio`
- `LoraLoaderModelOnly` ★核心
- `CFGGuider`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `JjkText`
- `solarL_SaveImagesToZip`
- `CLIPTextEncode` ★核心
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
- `Note`
- `LoadImage`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **64%**（95/148）

**有卡**：`CLIPTextEncode`、`LTXVPreprocess`、`EmptyLTXVLatentVideo`、`LTXVImgToVideoInplace`、`SamplerCustomAdvanced`、`easy int`、`LTXVSeparateAVLatent`、`LTXVLatentUpsampler`、`LTXVSpatioTemporalTiledVAEDecode`、`LTXVAudioVAEDecode`、`CreateVideo`、`WanVideoImageResizeToClosest`、`ImageScaleBy`、`GetImageSize`、`KSamplerSelect`、`RandomNoise`、`ResizeImagesByLongerEdge`、`UNETLoader`、`VAELoader`、`LTXVGemmaEnhancePrompt`、`CLIPLoader`、`LatentUpscaleModelLoader`、`SolidMask`、`MathExpression|pysssss`、`MelBandRoFormerModelLoader`、`MelBandRoFormerSampler`、`TrimAudioDuration`、`SetLatentNoiseMask`、`LTXVAudioVAEEncode`、`Audio Duration (mtb)`、`ImageResizeKJv2`、`EmptyImage`、`DF_Int_to_Float`、`easy boolean`、`LTXVConcatAVLatent`、`LTXVEmptyLatentAudio`、`ManualSigmas`、`easy float`、`ImpactExecutionOrderController`、`LTXVConditioning`、`LTXVDualCFGGuider`、`CFGGuider`、`LTXVScheduler`、`SaveVideo`、`LoadAudio`、`LoraLoaderModelOnly`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`solarL_SaveImagesToZip`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
