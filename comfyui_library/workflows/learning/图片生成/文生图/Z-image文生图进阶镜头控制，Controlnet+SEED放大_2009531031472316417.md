---
key: 图片生成/文生图/Z-image文生图进阶镜头控制，Controlnet+SEED放大_2009531031472316417.json
name: Z-image文生图进阶镜头控制，Controlnet+SEED放大_2009531031472316417
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-image文生图进阶镜头控制，Controlnet+SEED放大_2009531031472316417.json
hash: 1e0b016ff0668848
coverage: 0.90625
learned_at: 2026-10-19 22:01:06
nodes: [Note, LoadImage, AIO_Preprocessor, ModelPatchLoader, LoadImage, QwenImageDiffsynthControlnet, CLIPLoader, Text Multiline, CR Prompt List, Note, Note, LayerUtility: PurgeVRAM V2, SeedVR2BlockSwap, SeedVR2ExtraArgs, LayerUtility: PurgeVRAM, SeedVR2GGUF, ImageResize+, VAELoader, VAEEncode, UNETLoader, UNETLoader, SaveImage, VAEDecode, KSampler, LayerUtility: TextJoin, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, CR Text, FlexLoraLoaderModelOnly, SaveImage, VNCCS_VisualPositionControl]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 4, "cfg": 1, "denoise": 1, "height": 1504, "sampler_name": "euler", "scheduler": "simple", "seed": 973253720806813, "steps": 9, "width": 1000}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Z-image文生图进阶镜头控制，Controlnet+SEED放大_2009531031472316417.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-image文生图进阶镜头控制，Controlnet+SEED放大_2009531031472316417.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（32 个）：
- `Note`
- `LoadImage`
- `AIO_Preprocessor`
- `ModelPatchLoader`
- `LoadImage`
- `QwenImageDiffsynthControlnet`
- `CLIPLoader`
- `Text Multiline`
- `CR Prompt List`
- `Note`
- `Note`
- `LayerUtility: PurgeVRAM V2`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `LayerUtility: PurgeVRAM`
- `SeedVR2GGUF`
- `ImageResize+`
- `VAELoader`
- `VAEEncode` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `LayerUtility: TextJoin`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `EmptyLatentImage` ★核心
- `CR Text`
- `FlexLoraLoaderModelOnly` ★核心
- `SaveImage`
- `VNCCS_VisualPositionControl`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `seed` = `973253720806813`
- `steps` = `9`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1000`
- `height` = `1504`
- `batch_size` = `4`

## 知识

覆盖率 **91%**（29/32）

**有卡**：`LoadImage`、`AIO_Preprocessor`、`ModelPatchLoader`、`QwenImageDiffsynthControlnet`、`CLIPLoader`、`Text Multiline`、`CR Prompt List`、`LayerUtility: PurgeVRAM V2`、`SeedVR2BlockSwap`、`SeedVR2ExtraArgs`、`LayerUtility: PurgeVRAM`、`SeedVR2GGUF`、`ImageResize+`、`VAELoader`、`VAEEncode`、`UNETLoader`、`SaveImage`、`VAEDecode`、`KSampler`、`LayerUtility: TextJoin`、`CLIPTextEncode`、`ConditioningZeroOut`、`EmptyLatentImage`、`CR Text`、`FlexLoraLoaderModelOnly`、`VNCCS_VisualPositionControl`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
