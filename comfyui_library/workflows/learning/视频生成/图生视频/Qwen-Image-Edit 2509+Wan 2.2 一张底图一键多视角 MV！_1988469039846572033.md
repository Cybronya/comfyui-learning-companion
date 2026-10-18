---
key: 视频生成/图生视频/Qwen-Image-Edit 2509+Wan 2.2 一张底图一键多视角 MV！_1988469039846572033.json
name: Qwen-Image-Edit 2509+Wan 2.2 一张底图一键多视角 MV！_1988469039846572033.json
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Qwen-Image-Edit 2509+Wan 2.2 一张底图一键多视角 MV！_1988469039846572033.json
hash: 98fb154abfd23e1a
coverage: 0.885057
learned_at: 2026-10-15 22:33:02
nodes: [MathExpression|pysssss, MathExpression|pysssss, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, SaveImage, PreviewImage, SDVN Any Show, MathExpression|pysssss, ImageFromBatch, easy showAnything, MathExpression|pysssss, ImageFromBatch, easy showAnything, MathExpression|pysssss, ImageFromBatch, easy showAnything, ImageFromBatch, MathExpression|pysssss, easy showAnything, ImageFromBatch, MathExpression|pysssss, GetImageSizeAndCount, MathExpression|pysssss, easy showAnything, PreviewAny, AddNode, easy imageListToImageBatch, ImageFromBatch, VAELoader, CLIPLoader, VAEEncode, ImageScaleToTotalPixels, UNETLoader, LoraLoaderModelOnly, TextEncodeQwenImageEditPlus, LoraLoaderModelOnly, ConditioningZeroOut, ModelSamplingAuraFlow, CFGNorm, LoraLoaderModelOnly, VAEDecode, easy cleanGpuUsed, KSampler, SeedVR2BlockSwap, SeedVR2ExtraArgs, easy imageListToImageBatch, SeedVR2, Film Grain, UNETLoader, UNETLoader, wanBlockSwap, wanBlockSwap, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelSamplingSD3, ModelSamplingSD3, ModelPatchTorchSettings, SDVN Any Show, VAEDecode, CLIPLoader, VAELoader, CLIPVisionLoader, CLIPVisionEncode, easy imageBatchToImageList, CLIPTextEncode, CLIPTextEncode, Seed (rgthree), DF_Get_image_size, WanImageToVideo, ModelPatchTorchSettings, KSamplerAdvanced, easy cleanGpuUsed, KSamplerAdvanced, easy promptLine, LoadAudio, VHS_VideoCombine, VHS_VideoCombine, JWInteger, JWInteger, Note, Note, LoadImage, LoadImage, Note]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 10, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "randomize"}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Qwen-Image-Edit 2509+Wan 2.2 一张底图一键多视角 MV！_1988469039846572033.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1988469039846572033.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（87 个）：
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `SaveImage`
- `PreviewImage`
- `SDVN Any Show`
- `MathExpression|pysssss`
- `ImageFromBatch`
- `easy showAnything`
- `MathExpression|pysssss`
- `ImageFromBatch`
- `easy showAnything`
- `MathExpression|pysssss`
- `ImageFromBatch`
- `easy showAnything`
- `ImageFromBatch`
- `MathExpression|pysssss`
- `easy showAnything`
- `ImageFromBatch`
- `MathExpression|pysssss`
- `GetImageSizeAndCount`
- `MathExpression|pysssss`
- `easy showAnything`
- `PreviewAny`
- `AddNode`
- `easy imageListToImageBatch`
- `ImageFromBatch`
- `VAELoader`
- `CLIPLoader`
- `VAEEncode` ★核心
- `ImageScaleToTotalPixels`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `TextEncodeQwenImageEditPlus`
- `LoraLoaderModelOnly` ★核心
- `ConditioningZeroOut`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `KSampler` ★核心
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `easy imageListToImageBatch`
- `SeedVR2`
- `Film Grain`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `wanBlockSwap`
- `wanBlockSwap`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `ModelPatchTorchSettings`
- `SDVN Any Show`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `easy imageBatchToImageList`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Seed (rgthree)`
- `DF_Get_image_size`
- `WanImageToVideo`
- `ModelPatchTorchSettings`
- `KSamplerAdvanced` ★核心
- `easy cleanGpuUsed`
- `KSamplerAdvanced` ★核心
- `easy promptLine`
- `LoadAudio`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `JWInteger`
- `JWInteger`
- `Note`
- `Note`
- `LoadImage`
- `LoadImage`
- `Note`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `10`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **89%**（77/87）

**有卡**：`MathExpression|pysssss`、`VHS_VideoCombine`、`SaveImage`、`SDVN Any Show`、`ImageFromBatch`、`GetImageSizeAndCount`、`AddNode`、`easy imageListToImageBatch`、`VAELoader`、`CLIPLoader`、`VAEEncode`、`ImageScaleToTotalPixels`、`UNETLoader`、`LoraLoaderModelOnly`、`TextEncodeQwenImageEditPlus`、`ConditioningZeroOut`、`ModelSamplingAuraFlow`、`CFGNorm`、`VAEDecode`、`easy cleanGpuUsed`、`KSampler`、`SeedVR2BlockSwap`、`SeedVR2ExtraArgs`、`SeedVR2`、`Film Grain`、`wanBlockSwap`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`ModelPatchTorchSettings`、`CLIPVisionLoader`、`CLIPVisionEncode`、`easy imageBatchToImageList`、`CLIPTextEncode`、`Seed (rgthree)`、`DF_Get_image_size`、`WanImageToVideo`、`KSamplerAdvanced`、`easy promptLine`、`LoadAudio`、`JWInteger`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
