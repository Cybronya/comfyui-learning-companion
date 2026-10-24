---
key: 图片生成/图生图/🈚️基础图生图_洗图-Wan2.2-native-Lightx-1080p_1952482785493749762.json
name: 🈚️基础图生图_洗图-Wan2.2-native-Lightx-1080p_1952482785493749762
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/🈚️基础图生图_洗图-Wan2.2-native-Lightx-1080p_1952482785493749762.json
hash: 6ce260b19008d839
coverage: 0.555556
learned_at: 2026-10-23 13:38:44
nodes: [CLIPTextEncode, VAELoader, SetNode, SetNode, CLIPTextEncode, GetNode, ApplySageAttention, ApplySageAttention, SetNode, SetNode, SetNode, GetNode, GetNode, SetNode, UpscaleModelLoader, PreviewImage, GetNode, LayerUtility: ImageScaleByAspectRatio V2, GetNode, ModelSamplingSD3, ModelSamplingSD3, LoraLoaderModelOnly, UNETLoader, LatentPixelScale, SetNode, easy seed, GetNode, ImageSmartSharpen+, SetNode, easy showAnything, LoadJanusModel, wanBlockSwap, wanBlockSwap, JanusImage2Text, LoraLoaderModelOnly, LoraLoaderModelOnly, GetNode, GetNode, GetNode, GetNode, VAEDecode, LayerUtility: TextJoin, KSampler, UNETLoader, GetNode, UnetLoaderGGUF, CLIPLoader, SetNode, SetNode, LoadImage, LoraLoaderModelOnly, SaveImage, Image Comparer (rgthree), Manual XY Entry Info, GetNode, KSampler, RebatchLatents, GetNode, RepeatLatentBatch, VAEEncode, GetNode, CR Text, GetNode]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.7000000000000002, "sampler_name": "heun", "scheduler": "beta", "seed": 442257947380223, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/🈚️基础图生图_洗图-Wan2.2-native-Lightx-1080p_1952482785493749762.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/🈚️基础图生图_洗图-Wan2.2-native-Lightx-1080p_1952482785493749762.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（63 个）：
- `CLIPTextEncode` ★核心
- `VAELoader`
- `SetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `ApplySageAttention`
- `ApplySageAttention`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `UpscaleModelLoader`
- `PreviewImage`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LatentPixelScale`
- `SetNode`
- `easy seed`
- `GetNode`
- `ImageSmartSharpen+`
- `SetNode`
- `easy showAnything`
- `LoadJanusModel`
- `wanBlockSwap`
- `wanBlockSwap`
- `JanusImage2Text`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `LayerUtility: TextJoin`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `GetNode`
- `UnetLoaderGGUF` ★核心
- `CLIPLoader`
- `SetNode`
- `SetNode`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `Manual XY Entry Info`
- `GetNode`
- `KSampler` ★核心
- `RebatchLatents`
- `GetNode`
- `RepeatLatentBatch`
- `VAEEncode` ★核心
- `GetNode`
- `CR Text`
- `GetNode`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `442257947380223`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `heun`
- `scheduler` = `beta`
- `denoise` = `0.7000000000000002`

## 知识

覆盖率 **56%**（35/63）

**有卡**：`CLIPTextEncode`、`VAELoader`、`ApplySageAttention`、`UpscaleModelLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`ModelSamplingSD3`、`LoraLoaderModelOnly`、`UNETLoader`、`LatentPixelScale`、`easy seed`、`ImageSmartSharpen+`、`LoadJanusModel`、`wanBlockSwap`、`JanusImage2Text`、`VAEDecode`、`LayerUtility: TextJoin`、`KSampler`、`UnetLoaderGGUF`、`CLIPLoader`、`LoadImage`、`SaveImage`、`Manual XY Entry Info`、`RebatchLatents`、`RepeatLatentBatch`、`VAEEncode`、`CR Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
