---
key: 视频生成/图生视频/WAN2.2 Animate 动作迁移2.0版本_2027975235357646849.json
name: WAN2.2 Animate 动作迁移2.0版本_2027975235357646849.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2027975235357646849.json
hash: 7c7570daa863400f
coverage: 0.910256
learned_at: 2026-10-15 22:35:18
nodes: [PointsEditor, Any Switch (rgthree), Sam2Segmentation, LayerUtility: ImageBlend, DownloadAndLoadSAM2Model, GrowMask, BlockifyMask, easy int, MarkdownNote, Seed, easy int, SaveVideoRGBA, MarkdownNote, easy int, TorchCompileModelWanVideoV2, PathchSageAttentionKJ, easy int, easy ifElse, VAELoader, ModelSamplingSD3, easy ifElse, CLIPLoader, CLIPTextEncode, CLIPTextEncode, easy positive, CLIPVisionEncode, SimpleMath+, easy compare, easy lengthAnything, easy batchAnything, SimpleMath+, easy promptReplace, VAEDecode, TrimVideoLatent, GetImageRangeFromBatch, CLIPVisionLoader, easy int, UNETLoader, easy int, SimpleMath+, easy convertAnything, SimpleMath+, SimpleMathDual+, VHS_VideoInfo, easy compare, easy boolean, easy whileLoopEnd, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelPatchTorchSettings, Any Switch (rgthree), LoraLoaderModelOnly, KSampler, wanBlockSwap, DrawMaskOnImage, WanAnimateToVideo, Fast Groups Muter (rgthree), MathExpression|pysssss, MathExpression|pysssss, LoraLoaderModelOnly, VHS_LoadVideo, VHS_VideoCombine, GetImageSize, PoseAndFaceDetection, DrawViTPose, OnnxDetectionModelLoader, RHHiddenNodes, SaveVideoRGBA, SaveVideoRGBA, ImageConcatMulti, ImageConcatMulti, LoadImage, easy int, easy int, easy int, easy int, easy whileLoopStart, SaveVideoRGBA]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "sa_solver", "scheduler": "linear_quadratic", "seed": 998853928358357, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/WAN2.2 Animate 动作迁移2.0版本_2027975235357646849.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2027975235357646849.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（78 个）：
- `PointsEditor`
- `Any Switch (rgthree)`
- `Sam2Segmentation`
- `LayerUtility: ImageBlend`
- `DownloadAndLoadSAM2Model`
- `GrowMask`
- `BlockifyMask`
- `easy int`
- `MarkdownNote`
- `Seed`
- `easy int`
- `SaveVideoRGBA`
- `MarkdownNote`
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
- `KSampler` ★核心
- `wanBlockSwap`
- `DrawMaskOnImage`
- `WanAnimateToVideo`
- `Fast Groups Muter (rgthree)`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `LoraLoaderModelOnly` ★核心
- `VHS_LoadVideo`
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
- `LoadImage`
- `easy int`
- `easy int`
- `easy int`
- `easy int`
- `easy whileLoopStart`
- `SaveVideoRGBA`

## 关键参数

- `seed` = `998853928358357`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `linear_quadratic`
- `denoise` = `1`

## 知识

覆盖率 **91%**（71/78）

**有卡**：`PointsEditor`、`Sam2Segmentation`、`LayerUtility: ImageBlend`、`DownloadAndLoadSAM2Model`、`GrowMask`、`BlockifyMask`、`easy int`、`Seed`、`SaveVideoRGBA`、`TorchCompileModelWanVideoV2`、`PathchSageAttentionKJ`、`VAELoader`、`ModelSamplingSD3`、`CLIPLoader`、`CLIPTextEncode`、`easy positive`、`CLIPVisionEncode`、`SimpleMath+`、`easy compare`、`easy lengthAnything`、`easy batchAnything`、`easy promptReplace`、`VAEDecode`、`TrimVideoLatent`、`GetImageRangeFromBatch`、`CLIPVisionLoader`、`UNETLoader`、`easy convertAnything`、`SimpleMathDual+`、`VHS_VideoInfo`、`easy boolean`、`easy whileLoopEnd`、`LoraLoaderModelOnly`、`ModelPatchTorchSettings`、`KSampler`、`wanBlockSwap`、`DrawMaskOnImage`、`WanAnimateToVideo`、`MathExpression|pysssss`、`VHS_LoadVideo`、`VHS_VideoCombine`、`GetImageSize`、`PoseAndFaceDetection`、`DrawViTPose`、`OnnxDetectionModelLoader`、`RHHiddenNodes`、`ImageConcatMulti`、`LoadImage`、`easy whileLoopStart`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
