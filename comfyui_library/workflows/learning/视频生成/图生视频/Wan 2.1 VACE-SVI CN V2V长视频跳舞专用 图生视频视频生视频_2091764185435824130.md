---
key: 视频生成/图生视频/Wan 2.1 VACE-SVI CN V2V长视频跳舞专用 图生视频视频生视频_2091764185435824130.json
name: Wan 2.1 VACE-SVI CN V2V长视频跳舞专用 图生视频视频生视频_2091764185435824130
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan 2.1 VACE-SVI CN V2V长视频跳舞专用 图生视频视频生视频_2091764185435824130.json
hash: f28fbff1cdfde895
coverage: 0.535484
learned_at: 2026-10-16 22:30:46
nodes: [CLIPTextEncode, WanVaceToVideo, INTConstant, INTConstant, TrimVideoLatent, VAEDecode, LayerUtility: PurgeVRAM, GetImageRangeFromBatch, SetNode, ImageResizeKJv2, LayerUtility: PurgeVRAM, GetNode, VAEDecode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVaceToVideo, KSampler, TrimVideoLatent, SetNode, SetNode, WanVideoVACEStartToEndFrame, GetNode, MathExpression|pysssss, VHS_VideoCombine, MathExpression|pysssss, INTConstant, GetNode, GetNode, ImageFromBatch, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, DWPreprocessor, MathExpression|pysssss, GetNode, ImageResizeKJv2, GetNode, INTConstant, ModelSamplingSD3, ModelSamplingSD3, INTConstant, FloatConstant, GetNode, GetNode, GetNode, easy forLoopStart, easy forLoopEnd, VHS_GetImageCount, MathExpression|pysssss, ImageBatchMulti, VHS_GetImageCount, MathExpression|pysssss, easy showAnything, VHS_VideoCombine, KSampler, VHS_GetImageCount, easy showAnything, easy showAnything, GetNode, PreviewImage, PreviewImage, Reroute, GetNode, PathchSageAttentionKJ, UnetLoaderGGUF, UNETLoader, CLIPLoader, GetNode, GetNode, LoadImage, VAELoader, CLIPTextEncode, TorchCompileModelWanVideoV2, Power Lora Loader (rgthree), GetNode, FloatConstant, VHS_VideoInfo, wanBlockSwap, INTConstant, MaskToImage, Reroute, GetNode, GetImageRangeFromBatch, GetNode, ImageColorMatch+, easy showAnything, VHS_GetImageCount, SetNode, GetNode, GetNode, PreviewImage, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, ImageColorMatch+, GetNode, VHS_VideoCombine, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, VHS_LoadVideo, DWPreprocessor, SetNode, GetImageRangeFromBatch, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, JjkText, solarL_SaveImagesToZip, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Wan 2.1 VACE-SVI CN V2V长视频跳舞专用 图生视频视频生视频_2091764185435824130.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Wan 2.1 VACE-SVI CN V2V长视频跳舞专用 图生视频视频生视频_2091764185435824130.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（155 个）：
- `CLIPTextEncode` ★核心
- `WanVaceToVideo`
- `INTConstant`
- `INTConstant`
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM`
- `GetImageRangeFromBatch`
- `SetNode`
- `ImageResizeKJv2`
- `LayerUtility: PurgeVRAM`
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVaceToVideo`
- `KSampler` ★核心
- `TrimVideoLatent`
- `SetNode`
- `SetNode`
- `WanVideoVACEStartToEndFrame`
- `GetNode`
- `MathExpression|pysssss`
- `VHS_VideoCombine`
- `MathExpression|pysssss`
- `INTConstant`
- `GetNode`
- `GetNode`
- `ImageFromBatch`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `DWPreprocessor`
- `MathExpression|pysssss`
- `GetNode`
- `ImageResizeKJv2`
- `GetNode`
- `INTConstant`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `INTConstant`
- `FloatConstant`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy forLoopStart`
- `easy forLoopEnd`
- `VHS_GetImageCount`
- `MathExpression|pysssss`
- `ImageBatchMulti`
- `VHS_GetImageCount`
- `MathExpression|pysssss`
- `easy showAnything`
- `VHS_VideoCombine`
- `KSampler` ★核心
- `VHS_GetImageCount`
- `easy showAnything`
- `easy showAnything`
- `GetNode`
- `PreviewImage`
- `PreviewImage`
- `Reroute`
- `GetNode`
- `PathchSageAttentionKJ`
- `UnetLoaderGGUF` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `GetNode`
- `GetNode`
- `LoadImage`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `TorchCompileModelWanVideoV2`
- `Power Lora Loader (rgthree)`
- `GetNode`
- `FloatConstant`
- `VHS_VideoInfo`
- `wanBlockSwap`
- `INTConstant`
- `MaskToImage`
- `Reroute`
- `GetNode`
- `GetImageRangeFromBatch`
- `GetNode`
- `ImageColorMatch+`
- `easy showAnything`
- `VHS_GetImageCount`
- `SetNode`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `ImageColorMatch+`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `VHS_LoadVideo`
- `DWPreprocessor`
- `SetNode`
- `GetImageRangeFromBatch`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
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

**识别到的模式**：text_to_image

## 关键参数

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

覆盖率 **54%**（83/155）

**有卡**：`CLIPTextEncode`、`WanVaceToVideo`、`INTConstant`、`TrimVideoLatent`、`VAEDecode`、`LayerUtility: PurgeVRAM`、`GetImageRangeFromBatch`、`ImageResizeKJv2`、`KSampler`、`WanVideoVACEStartToEndFrame`、`MathExpression|pysssss`、`VHS_VideoCombine`、`ImageFromBatch`、`DWPreprocessor`、`ModelSamplingSD3`、`FloatConstant`、`easy forLoopStart`、`easy forLoopEnd`、`VHS_GetImageCount`、`ImageBatchMulti`、`PathchSageAttentionKJ`、`UnetLoaderGGUF`、`UNETLoader`、`CLIPLoader`、`LoadImage`、`VAELoader`、`TorchCompileModelWanVideoV2`、`Power Lora Loader (rgthree)`、`VHS_VideoInfo`、`wanBlockSwap`、`MaskToImage`、`ImageColorMatch+`、`VHS_LoadVideo`、`EmptyLatentImage`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 3 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
