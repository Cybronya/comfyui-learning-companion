---
key: 图片生成/文生图/Wan2.1 文生图+图像高清修复_1945356782250414081.json
name: Wan2.1 文生图+图像高清修复_1945356782250414081.json
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.1 文生图+图像高清修复_1945356782250414081.json
hash: f25b826fbb5b0226
coverage: 0.782609
learned_at: 2026-10-07 22:52:37
nodes: [UNETLoader, CLIPLoader, MarkdownNote, MarkdownNote, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, EmptyLatentImage, CLIPTextEncode, SaveImage, VAEDecode, KSampler, LoadImage, VAEEncode, ImageScale, LayerUtility: ImageScaleRestore V2, UpscaleModelLoader, ShowText|pysssss, JJC_JoyCaption, ImageUpscaleWithModel, RH_Translator, VAELoader, Image Comparer (rgthree)]
patterns: [text_to_image, image_to_image]
missing: [LayerUtility: ImageScaleRestore V2]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 0.10000000000000002, "height": 1920, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 1234571656, "steps": 10, "width": 1024}
discoveries: [次要节点 `LayerUtility: ImageScaleRestore V2` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/Wan2.1 文生图+图像高清修复_1945356782250414081.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1945356782250414081.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `MarkdownNote`
- `MarkdownNote`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `LoadImage`
- `VAEEncode` ★核心
- `ImageScale`
- `LayerUtility: ImageScaleRestore V2`
- `UpscaleModelLoader`
- `ShowText|pysssss`
- `JJC_JoyCaption`
- `ImageUpscaleWithModel`
- `RH_Translator`
- `VAELoader`
- `Image Comparer (rgthree)`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `width` = `1024`
- `height` = `1920`
- `batch_size` = `1`
- `seed` = `1234571656`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `0.10000000000000002`

## 知识

覆盖率 **78%**（18/23）

**有卡**：`UNETLoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`EmptyLatentImage`、`SaveImage`、`VAEDecode`、`KSampler`、`LoadImage`、`VAEEncode`、`ImageScale`、`UpscaleModelLoader`、`JJC_JoyCaption`、`ImageUpscaleWithModel`、`RH_Translator`、`VAELoader`

**缺卡**（1）：`LayerUtility: ImageScaleRestore V2`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 学习发现

- 次要节点 `LayerUtility: ImageScaleRestore V2` 知识库中没有该节点类型的任何知识
