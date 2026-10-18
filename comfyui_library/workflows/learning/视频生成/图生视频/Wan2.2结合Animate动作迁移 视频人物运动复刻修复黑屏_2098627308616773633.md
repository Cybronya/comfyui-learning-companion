---
key: 视频生成/图生视频/Wan2.2结合Animate动作迁移 视频人物运动复刻修复黑屏_2098627308616773633.json
name: Wan2.2结合Animate动作迁移 视频人物运动复刻修复黑屏_2098627308616773633
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2结合Animate动作迁移 视频人物运动复刻修复黑屏_2098627308616773633.json
hash: 582f19fedfb2d7ba
coverage: 0.915094
learned_at: 2026-10-17 01:44:49
nodes: [PointsEditor, Any Switch (rgthree), Sam2Segmentation, LayerUtility: ImageBlend, DownloadAndLoadSAM2Model, GrowMask, BlockifyMask, easy int, Seed, easy int, SaveVideoRGBA, easy int, easy int, TorchCompileModelWanVideoV2, PathchSageAttentionKJ, easy int, easy ifElse, VAELoader, ModelSamplingSD3, easy ifElse, CLIPLoader, CLIPTextEncode, CLIPTextEncode, easy positive, CLIPVisionEncode, SimpleMath+, easy compare, easy lengthAnything, easy batchAnything, SimpleMath+, easy promptReplace, VAEDecode, TrimVideoLatent, GetImageRangeFromBatch, CLIPVisionLoader, easy int, UNETLoader, easy whileLoopStart, easy int, SimpleMath+, easy convertAnything, SimpleMath+, SimpleMathDual+, VHS_VideoInfo, easy compare, easy boolean, easy whileLoopEnd, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelPatchTorchSettings, Any Switch (rgthree), LoraLoaderModelOnly, easy int, easy int, KSampler, wanBlockSwap, DrawMaskOnImage, WanAnimateToVideo, Fast Groups Muter (rgthree), MathExpression|pysssss, MathExpression|pysssss, LoraLoaderModelOnly, easy int, VHS_LoadVideo, LoadImage, VHS_VideoCombine, GetImageSize, PoseAndFaceDetection, DrawViTPose, OnnxDetectionModelLoader, RHHiddenNodes, SaveVideoRGBA, SaveVideoRGBA, ImageConcatMulti, ImageConcatMulti, SaveVideoRGBA, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPLoader, CLIPTextEncode, JjkText, EmptyLatentImage, solarL_SaveImagesToZip, VAEDecode, VAELoader, Note, SaveImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Wan2.2结合Animate动作迁移 视频人物运动复刻修复黑屏_2098627308616773633.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Wan2.2结合Animate动作迁移 视频人物运动复刻修复黑屏_2098627308616773633.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（106 个）：
- `PointsEditor`
- `Any Switch (rgthree)`
- `Sam2Segmentation`
- `LayerUtility: ImageBlend`
- `DownloadAndLoadSAM2Model`
- `GrowMask`
- `BlockifyMask`
- `easy int`
- `Seed`
- `easy int`
- `SaveVideoRGBA`
- `easy int`
- `easy int`
- `TorchCompileModelWanVideoV2`
- `PathchSageAttentionKJ`
- `easy int`
- `easy ifElse`
- `VAELoader`
- `ModelSamplingSD3`
- `easy ifElse`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `easy positive`
- `CLIPVisionEncode`
- `SimpleMath+`
- `easy compare`
- `easy lengthAnything`
- `easy batchAnything`
- `SimpleMath+`
- `easy promptReplace`
- `VAEDecode` ★核心
- `TrimVideoLatent`
- `GetImageRangeFromBatch`
- `CLIPVisionLoader`
- `easy int`
- `UNETLoader` ★核心
- `easy whileLoopStart`
- `easy int`
- `SimpleMath+`
- `easy convertAnything`
- `SimpleMath+`
- `SimpleMathDual+`
- `VHS_VideoInfo`
- `easy compare`
- `easy boolean`
- `easy whileLoopEnd`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelPatchTorchSettings`
- `Any Switch (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `easy int`
- `easy int`
- `KSampler` ★核心
- `wanBlockSwap`
- `DrawMaskOnImage`
- `WanAnimateToVideo`
- `Fast Groups Muter (rgthree)`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `LoraLoaderModelOnly` ★核心
- `easy int`
- `VHS_LoadVideo`
- `LoadImage`
- `VHS_VideoCombine`
- `GetImageSize`
- `PoseAndFaceDetection`
- `DrawViTPose`
- `OnnxDetectionModelLoader`
- `RHHiddenNodes`
- `SaveVideoRGBA`
- `SaveVideoRGBA`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `SaveVideoRGBA`
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
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `JjkText`
- `EmptyLatentImage` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `VAELoader`
- `Note`
- `SaveImage`

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

覆盖率 **92%**（97/106）

**有卡**：`PointsEditor`、`Sam2Segmentation`、`LayerUtility: ImageBlend`、`DownloadAndLoadSAM2Model`、`GrowMask`、`BlockifyMask`、`easy int`、`Seed`、`SaveVideoRGBA`、`TorchCompileModelWanVideoV2`、`PathchSageAttentionKJ`、`VAELoader`、`ModelSamplingSD3`、`CLIPLoader`、`CLIPTextEncode`、`easy positive`、`CLIPVisionEncode`、`SimpleMath+`、`easy compare`、`easy lengthAnything`、`easy batchAnything`、`easy promptReplace`、`VAEDecode`、`TrimVideoLatent`、`GetImageRangeFromBatch`、`CLIPVisionLoader`、`UNETLoader`、`easy whileLoopStart`、`easy convertAnything`、`SimpleMathDual+`、`VHS_VideoInfo`、`easy boolean`、`easy whileLoopEnd`、`LoraLoaderModelOnly`、`ModelPatchTorchSettings`、`KSampler`、`wanBlockSwap`、`DrawMaskOnImage`、`WanAnimateToVideo`、`MathExpression|pysssss`、`VHS_LoadVideo`、`LoadImage`、`VHS_VideoCombine`、`GetImageSize`、`PoseAndFaceDetection`、`DrawViTPose`、`OnnxDetectionModelLoader`、`RHHiddenNodes`、`ImageConcatMulti`、`EmptyLatentImage`、`solarL_SaveImagesToZip`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
