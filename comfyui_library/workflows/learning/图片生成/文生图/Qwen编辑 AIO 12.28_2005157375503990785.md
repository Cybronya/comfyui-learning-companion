---
key: 图片生成/文生图/Qwen编辑 AIO 12.28_2005157375503990785.json
name: Qwen编辑 AIO 12.28_2005157375503990785
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen编辑 AIO 12.28_2005157375503990785.json
hash: 9dfd9278b86b5995
coverage: 0.706522
learned_at: 2026-10-19 22:00:55
nodes: [IO_clear_cache, LayerUtility: PurgeVRAM V2, easy cleanGpuUsed, Image Blank, VAEDecode, ImageBlend, PreviewImage, LotusSampler, Switch image [Crystools], PreviewImage, LoadImage, Anything Everywhere3, AILab_MaskEnhancer, KSampler, AILab_MaskOverlay, QwenEditAdaptiveLongestEdge, QwenEditAdaptiveLongestEdge, SetNode, QwenEditAdaptiveLongestEdge, SetNode, QwenEditAdaptiveLongestEdge, SDPoseOODProcessor, QwenEditAdaptiveLongestEdge, QwenEditAdaptiveLongestEdge, QwenEditAdaptiveLongestEdge, PreviewImage, ImagePadForOutpaint, LoadImage, LoadImage, ImageGenResolutionFromImage, DepthAnythingV2Preprocessor, LoadLotusModel, VAELoader, VAEEncode, TextEncodeQwenImageEditPlusCustom_lrzjason, QwenEditConfigPreparer, QwenEditConfigPreparer, QwenEditConfigPreparer, QwenEditConfigPreparer, QwenEditConfigPreparer, QwenEditConfigPreparer, SetNode, QwenEditConfigPreparer, SDPoseOODLoader, LoadImage, VAEDecode, GetNode, ImageUpscaleWithModel, PreviewImage, UpscaleModelLoader, SetNode, SetNode, SetNode, SetNode, easy positive, easy positive, easy positive, GetNode, GetNode, easy imageColorMatch, GetNode, GetNode, easy positive, LoadImage, LoadImage, CheckpointLoaderSimple, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPLoader, easy positive, EmptyLatentImage, GetNode, GetNode, GetNode, GetNode, AILab_ImageStitch, PreviewImage, SetNode, SaveImage, LoadImage, ImageLoaderPlus, MultiplePathsInputPlus, Qwen3_VQA_Plus, easy positive, easy promptConcat, easy positive, easy showAnything, ProcessString, easy promptLine, ShowText|pysssss, Fast Groups Bypasser (rgthree), Image Comparer (rgthree)]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "e6093d0b626b2a046868f0fc1b5b98962608194df5d2dcbd3f2f737401897c47.safetensors", "denoise": 1, "height": 1720, "sampler_name": "euler_ancestral", "scheduler": "beta57", "seed": 123321123321, "steps": 4, "width": 1280}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen编辑 AIO 12.28_2005157375503990785.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen编辑 AIO 12.28_2005157375503990785.json`

## 结构

**生成流程**：Model → Encode → Latent → Sampling → Decode → Process → Output → Other

**节点**（92 个）：
- `IO_clear_cache`
- `LayerUtility: PurgeVRAM V2`
- `easy cleanGpuUsed`
- `Image Blank`
- `VAEDecode` ★核心
- `ImageBlend`
- `PreviewImage`
- `LotusSampler` ★核心
- `Switch image [Crystools]`
- `PreviewImage`
- `LoadImage`
- `Anything Everywhere3`
- `AILab_MaskEnhancer`
- `KSampler` ★核心
- `AILab_MaskOverlay`
- `QwenEditAdaptiveLongestEdge`
- `QwenEditAdaptiveLongestEdge`
- `SetNode`
- `QwenEditAdaptiveLongestEdge`
- `SetNode`
- `QwenEditAdaptiveLongestEdge`
- `SDPoseOODProcessor`
- `QwenEditAdaptiveLongestEdge`
- `QwenEditAdaptiveLongestEdge`
- `QwenEditAdaptiveLongestEdge`
- `PreviewImage`
- `ImagePadForOutpaint`
- `LoadImage`
- `LoadImage`
- `ImageGenResolutionFromImage`
- `DepthAnythingV2Preprocessor`
- `LoadLotusModel`
- `VAELoader`
- `VAEEncode` ★核心
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `QwenEditConfigPreparer`
- `QwenEditConfigPreparer`
- `QwenEditConfigPreparer`
- `QwenEditConfigPreparer`
- `QwenEditConfigPreparer`
- `QwenEditConfigPreparer`
- `SetNode`
- `QwenEditConfigPreparer`
- `SDPoseOODLoader`
- `LoadImage`
- `VAEDecode` ★核心
- `GetNode`
- `ImageUpscaleWithModel`
- `PreviewImage`
- `UpscaleModelLoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `easy positive`
- `easy positive`
- `easy positive`
- `GetNode`
- `GetNode`
- `easy imageColorMatch`
- `GetNode`
- `GetNode`
- `easy positive`
- `LoadImage`
- `LoadImage`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `easy positive`
- `EmptyLatentImage` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `AILab_ImageStitch`
- `PreviewImage`
- `SetNode`
- `SaveImage`
- `LoadImage`
- `ImageLoaderPlus`
- `MultiplePathsInputPlus`
- `Qwen3_VQA_Plus`
- `easy positive`
- `easy promptConcat`
- `easy positive`
- `easy showAnything`
- `ProcessString`
- `easy promptLine`
- `ShowText|pysssss`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `123321123321`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `beta57`
- `denoise` = `1`
- `checkpoint` = `e6093d0b626b2a046868f0fc1b5b98962608194df5d2dcbd3f2f737401897c47.safetensors`
- `width` = `1280`
- `height` = `1720`
- `batch_size` = `1`

## 知识

覆盖率 **71%**（65/92）

**有卡**：`IO_clear_cache`、`LayerUtility: PurgeVRAM V2`、`easy cleanGpuUsed`、`Image Blank`、`VAEDecode`、`ImageBlend`、`LotusSampler`、`Switch image [Crystools]`、`LoadImage`、`AILab_MaskEnhancer`、`KSampler`、`AILab_MaskOverlay`、`QwenEditAdaptiveLongestEdge`、`SDPoseOODProcessor`、`ImagePadForOutpaint`、`ImageGenResolutionFromImage`、`DepthAnythingV2Preprocessor`、`LoadLotusModel`、`VAELoader`、`VAEEncode`、`TextEncodeQwenImageEditPlusCustom_lrzjason`、`QwenEditConfigPreparer`、`SDPoseOODLoader`、`ImageUpscaleWithModel`、`UpscaleModelLoader`、`easy positive`、`easy imageColorMatch`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`CLIPLoader`、`EmptyLatentImage`、`AILab_ImageStitch`、`SaveImage`、`ImageLoaderPlus`、`MultiplePathsInputPlus`、`Qwen3_VQA_Plus`、`easy promptConcat`、`ProcessString`、`easy promptLine`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
