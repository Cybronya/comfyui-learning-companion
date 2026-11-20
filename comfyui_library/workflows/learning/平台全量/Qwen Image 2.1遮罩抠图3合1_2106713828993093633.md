---
key: 平台全量/Qwen Image 2.1遮罩抠图3合1_2106713828993093633.json
name: Qwen Image 2.1遮罩抠图3合1_2106713828993093633
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen Image 2.1遮罩抠图3合1_2106713828993093633.json
hash: 1b68c51187bd2320
coverage: 0.794872
learned_at: 2026-11-14 00:50:08
nodes: [UNETLoader, VAELoader, EmptyLatentImage, VAEDecode, ComfySwitchNode, QwenImage21Cache, CLIPLoader, easy showAnything, LoadImage, BBOXToBoundingBoxKJ, SAM3_Detect, CheckpointLoaderSimple, InvertMask, MaskToImage, PreviewImage, ImageMaskPreview_Guhai, PreviewImage, ImageMaskPreview_Guhai, PreviewImage, GetImageSize, TextEncodeQwenImage21, CR Prompt Text, CR Prompt Text, Note, Fast Groups Bypasser (rgthree), 孤海注释, MaskToImage, ZML_AnyTypeSwitchFive, CR Prompt Text, StringMergeNode, BatchImagesNode, CLIPLoader, MuyeTextEditOutput, TextGenerate, KSampler, ImageTransformKJ, SaveImage, easy cleanGpuUsed, SaveImageAdvanced]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "sam3.1_multiplex_fp16.safetensors", "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 956859685200321, "steps": 30, "width": 1024}
---

# 平台全量/Qwen Image 2.1遮罩抠图3合1_2106713828993093633.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen Image 2.1遮罩抠图3合1_2106713828993093633.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（39 个）：
- `UNETLoader` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `ComfySwitchNode`
- `QwenImage21Cache`
- `CLIPLoader`
- `easy showAnything`
- `LoadImage`
- `BBOXToBoundingBoxKJ`
- `SAM3_Detect`
- `CheckpointLoaderSimple` ★核心
- `InvertMask`
- `MaskToImage`
- `PreviewImage`
- `ImageMaskPreview_Guhai`
- `PreviewImage`
- `ImageMaskPreview_Guhai`
- `PreviewImage`
- `GetImageSize`
- `TextEncodeQwenImage21`
- `CR Prompt Text`
- `CR Prompt Text`
- `Note`
- `Fast Groups Bypasser (rgthree)`
- `孤海注释`
- `MaskToImage`
- `ZML_AnyTypeSwitchFive`
- `CR Prompt Text`
- `StringMergeNode`
- `BatchImagesNode`
- `CLIPLoader`
- `MuyeTextEditOutput`
- `TextGenerate`
- `KSampler` ★核心
- `ImageTransformKJ`
- `SaveImage`
- `easy cleanGpuUsed`
- `SaveImageAdvanced`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `checkpoint` = `sam3.1_multiplex_fp16.safetensors`
- `seed` = `956859685200321`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **79%**（31/39）

**有卡**：`UNETLoader`、`VAELoader`、`EmptyLatentImage`、`VAEDecode`、`QwenImage21Cache`、`CLIPLoader`、`LoadImage`、`BBOXToBoundingBoxKJ`、`SAM3_Detect`、`CheckpointLoaderSimple`、`InvertMask`、`MaskToImage`、`ImageMaskPreview_Guhai`、`GetImageSize`、`TextEncodeQwenImage21`、`CR Prompt Text`、`ZML_AnyTypeSwitchFive`、`StringMergeNode`、`BatchImagesNode`、`MuyeTextEditOutput`、`TextGenerate`、`KSampler`、`ImageTransformKJ`、`SaveImage`、`easy cleanGpuUsed`、`SaveImageAdvanced`

**用到的条目**：KSampler、TextEncodeQwenImage21、VAEDecode、VAELoader、CheckpointLoaderSimple、UNETLoader、CLIPLoader、EmptyLatentImage
