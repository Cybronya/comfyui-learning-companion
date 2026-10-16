---
key: 视频生成/图生视频/Wan 2.2 x Multiple LoRA：一键多视角 MV，角色锁定，镜头瞬切！_1987350549395869697.json
name: Wan 2.2 x Multiple LoRA：一键多视角 MV，角色锁定，镜头瞬切！_1987350549395869697.json
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1987350549395869697.json
hash: 34d9bbde20668ded
coverage: 0.915663
learned_at: 2026-10-15 22:32:58
nodes: [UNETLoader, ModelSamplingAuraFlow, CFGNorm, VAEEncode, VAELoader, CLIPLoader, LoraLoaderModelOnly, SeedVR2ExtraArgs, SeedVR2, SeedVR2BlockSwap, LoraLoaderModelOnly, ConditioningZeroOut, CLIPLoader, PathchSageAttentionKJ, wanBlockSwap, PathchSageAttentionKJ, ModelSamplingSD3, ModelSamplingSD3, ModelPatchTorchSettings, ModelPatchTorchSettings, CLIPVisionLoader, wanBlockSwap, UNETLoader, UNETLoader, CLIPTextEncode, CLIPTextEncode, TextEncodeQwenImageEditPlus, easy showAnything, easy showAnything, MathExpression|pysssss, LoraLoaderModelOnly, easy cleanGpuUsed, ImageFromBatch, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, ImageFromBatch, ImageFromBatch, MathExpression|pysssss, VAELoader, easy showAnything, ImageFromBatch, Seed (rgthree), CLIPVisionEncode, KSampler, KSamplerAdvanced, KSamplerAdvanced, WanImageToVideo, easy imageListToImageBatch, VAEDecode, easy showAnything, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, MathExpression|pysssss, GetImageSizeAndCount, ImageFromBatch, easy imageListToImageBatch, ImageFromBatch, PreviewImage, MathExpression|pysssss, easy showAnything, MathExpression|pysssss, VHS_VideoCombine, JWInteger, easy promptLine, VAEDecode, easy cleanGpuUsed, VHS_VideoCombine, JWInteger, SDVN Any Show, DF_Get_image_size, SDVN Any Show, ImageScaleToTotalPixels, Film Grain, easy imageBatchToImageList, SaveImage, LoadAudio, LoadImage, AddNode, PreviewAny]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 10, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "randomize"}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Wan 2.2 x Multiple LoRA：一键多视角 MV，角色锁定，镜头瞬切！_1987350549395869697.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1987350549395869697.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（83 个）：
- `UNETLoader` ★核心
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `VAEEncode` ★核心
- `VAELoader`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `SeedVR2ExtraArgs`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `LoraLoaderModelOnly` ★核心
- `ConditioningZeroOut`
- `CLIPLoader`
- `PathchSageAttentionKJ`
- `wanBlockSwap`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `CLIPVisionLoader`
- `wanBlockSwap`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `TextEncodeQwenImageEditPlus`
- `easy showAnything`
- `easy showAnything`
- `MathExpression|pysssss`
- `LoraLoaderModelOnly` ★核心
- `easy cleanGpuUsed`
- `ImageFromBatch`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `ImageFromBatch`
- `ImageFromBatch`
- `MathExpression|pysssss`
- `VAELoader`
- `easy showAnything`
- `ImageFromBatch`
- `Seed (rgthree)`
- `CLIPVisionEncode`
- `KSampler` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `WanImageToVideo`
- `easy imageListToImageBatch`
- `VAEDecode` ★核心
- `easy showAnything`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `MathExpression|pysssss`
- `GetImageSizeAndCount`
- `ImageFromBatch`
- `easy imageListToImageBatch`
- `ImageFromBatch`
- `PreviewImage`
- `MathExpression|pysssss`
- `easy showAnything`
- `MathExpression|pysssss`
- `VHS_VideoCombine`
- `JWInteger`
- `easy promptLine`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `JWInteger`
- `SDVN Any Show`
- `DF_Get_image_size`
- `SDVN Any Show`
- `ImageScaleToTotalPixels`
- `Film Grain`
- `easy imageBatchToImageList`
- `SaveImage`
- `LoadAudio`
- `LoadImage`
- `AddNode`
- `PreviewAny`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `10`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **92%**（76/83）

**有卡**：`UNETLoader`、`ModelSamplingAuraFlow`、`CFGNorm`、`VAEEncode`、`VAELoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`SeedVR2ExtraArgs`、`SeedVR2`、`SeedVR2BlockSwap`、`ConditioningZeroOut`、`PathchSageAttentionKJ`、`wanBlockSwap`、`ModelSamplingSD3`、`ModelPatchTorchSettings`、`CLIPVisionLoader`、`CLIPTextEncode`、`TextEncodeQwenImageEditPlus`、`MathExpression|pysssss`、`easy cleanGpuUsed`、`ImageFromBatch`、`Seed (rgthree)`、`CLIPVisionEncode`、`KSampler`、`KSamplerAdvanced`、`WanImageToVideo`、`easy imageListToImageBatch`、`VAEDecode`、`VHS_VideoCombine`、`GetImageSizeAndCount`、`JWInteger`、`easy promptLine`、`SDVN Any Show`、`DF_Get_image_size`、`ImageScaleToTotalPixels`、`Film Grain`、`easy imageBatchToImageList`、`SaveImage`、`LoadAudio`、`LoadImage`、`AddNode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
