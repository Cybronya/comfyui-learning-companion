---
key: 图片生成/文生图/千问编辑All In One 12.1_1997564330105323522.json
name: 千问编辑All In One 12.1_1997564330105323522
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/千问编辑All In One 12.1_1997564330105323522.json
hash: 2128a7000ce7d478
coverage: 0.74359
learned_at: 2026-10-19 21:47:37
nodes: [QwenEditAdaptiveLongestEdge, GetNode, QwenEditAdaptiveLongestEdge, GetNode, QwenEditAdaptiveLongestEdge, QwenEditAdaptiveLongestEdge, GetNode, GetNode, IO_clear_cache, easy cleanGpuUsed, SDPoseOODLoader, GetNode, SetNode, QwenEditConfigPreparer, SDPoseOODProcessor, MultiplePathsInput, ImageGenResolutionFromImage, GetNode, GetNode, QwenEditAdaptiveLongestEdge, QwenEditConfigPreparer, Image Blank, SetNode, QwenEditConfigPreparer, VAELoader, VAEEncode, ImageAndMaskPreview, SetNode, LoadImage, ImagePadForOutpaint, QwenEditConfigPreparer, LoadLotusModel, SetNode, PreviewImage, PreviewImage, RMBG, SetNode, PreviewImage, SetNode, QwenEditConfigPreparer, easy positive, Anything Everywhere3, QwenEditAdaptiveLongestEdge, ImageAndMaskPreview, Mask Fill Holes, LoadImage, SetNode, QwenEditAdaptiveLongestEdge, LoadImage, LotusSampler, PreviewImage, easy positive, VAEDecode, DepthAnythingV2Preprocessor, QwenEditConfigPreparer, ImageBlend, ImageLoader, QwenEditConfigPreparer, Qwen3_VQA, easy showAnything, easy positive, easy positive, TextEncodeQwenImageEditPlusCustom_lrzjason, LoadImage, LoadImage, EmptyLatentImage, ImageUpscaleWithModel, LayerUtility: PurgeVRAM V2, KSampler, LoadImage, CheckpointLoaderSimple, LoraLoaderModelOnly, LoraLoaderModelOnly, EmptyLatentImage, UpscaleModelLoader, easy positive, VAEDecode, SaveImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "Qwen-Rapid-AIO-NSFW-v10.2.safetensors", "denoise": 1, "height": 832, "sampler_name": "euler", "scheduler": "beta57", "seed": 720256556940365, "steps": 5, "width": 1280}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/千问编辑All In One 12.1_1997564330105323522.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/千问编辑All In One 12.1_1997564330105323522.json`

## 结构

**生成流程**：Model → Encode → Latent → Sampling → Decode → Process → Output → Other

**节点**（78 个）：
- `QwenEditAdaptiveLongestEdge`
- `GetNode`
- `QwenEditAdaptiveLongestEdge`
- `GetNode`
- `QwenEditAdaptiveLongestEdge`
- `QwenEditAdaptiveLongestEdge`
- `GetNode`
- `GetNode`
- `IO_clear_cache`
- `easy cleanGpuUsed`
- `SDPoseOODLoader`
- `GetNode`
- `SetNode`
- `QwenEditConfigPreparer`
- `SDPoseOODProcessor`
- `MultiplePathsInput`
- `ImageGenResolutionFromImage`
- `GetNode`
- `GetNode`
- `QwenEditAdaptiveLongestEdge`
- `QwenEditConfigPreparer`
- `Image Blank`
- `SetNode`
- `QwenEditConfigPreparer`
- `VAELoader`
- `VAEEncode` ★核心
- `ImageAndMaskPreview`
- `SetNode`
- `LoadImage`
- `ImagePadForOutpaint`
- `QwenEditConfigPreparer`
- `LoadLotusModel`
- `SetNode`
- `PreviewImage`
- `PreviewImage`
- `RMBG`
- `SetNode`
- `PreviewImage`
- `SetNode`
- `QwenEditConfigPreparer`
- `easy positive`
- `Anything Everywhere3`
- `QwenEditAdaptiveLongestEdge`
- `ImageAndMaskPreview`
- `Mask Fill Holes`
- `LoadImage`
- `SetNode`
- `QwenEditAdaptiveLongestEdge`
- `LoadImage`
- `LotusSampler` ★核心
- `PreviewImage`
- `easy positive`
- `VAEDecode` ★核心
- `DepthAnythingV2Preprocessor`
- `QwenEditConfigPreparer`
- `ImageBlend`
- `ImageLoader`
- `QwenEditConfigPreparer`
- `Qwen3_VQA`
- `easy showAnything`
- `easy positive`
- `easy positive`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `LoadImage`
- `LoadImage`
- `EmptyLatentImage` ★核心
- `ImageUpscaleWithModel`
- `LayerUtility: PurgeVRAM V2`
- `KSampler` ★核心
- `LoadImage`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `EmptyLatentImage` ★核心
- `UpscaleModelLoader`
- `easy positive`
- `VAEDecode` ★核心
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `width` = `1280`
- `height` = `832`
- `batch_size` = `1`
- `seed` = `720256556940365`
- `steps` = `5`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta57`
- `denoise` = `1`
- `checkpoint` = `Qwen-Rapid-AIO-NSFW-v10.2.safetensors`

## 知识

覆盖率 **74%**（58/78）

**有卡**：`QwenEditAdaptiveLongestEdge`、`IO_clear_cache`、`easy cleanGpuUsed`、`SDPoseOODLoader`、`QwenEditConfigPreparer`、`SDPoseOODProcessor`、`MultiplePathsInput`、`ImageGenResolutionFromImage`、`Image Blank`、`VAELoader`、`VAEEncode`、`ImageAndMaskPreview`、`LoadImage`、`ImagePadForOutpaint`、`LoadLotusModel`、`RMBG`、`easy positive`、`Mask Fill Holes`、`LotusSampler`、`VAEDecode`、`DepthAnythingV2Preprocessor`、`ImageBlend`、`ImageLoader`、`Qwen3_VQA`、`TextEncodeQwenImageEditPlusCustom_lrzjason`、`EmptyLatentImage`、`ImageUpscaleWithModel`、`LayerUtility: PurgeVRAM V2`、`KSampler`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`UpscaleModelLoader`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、EmptyLatentImage、LoadImage、DepthAnythingV2Preprocessor

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
