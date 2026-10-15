---
key: 图片生成/文生图/Flux文生图+Wan2.1超真实洗图_1949521829412642817.json
name: Flux文生图+Wan2.1超真实洗图_1949521829412642817
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux文生图+Wan2.1超真实洗图_1949521829412642817.json
hash: 7a75b2dc40467d59
coverage: 0.848485
learned_at: 2026-10-10 20:58:37
nodes: [CLIPTextEncode, FilmGrain, VAELoader, KSampler, PrimitiveNode, CLIPTextEncode, RandomNoise, BasicGuider, KSamplerSelect, BasicScheduler, SamplerCustomAdvanced, VAEDecode, CLIPTextEncode, PreviewImage, GetImageSize, RH_Captioner, ImageScale, VAEEncode, RH_Translator, EmptyLatentImage, UNETLoader, DualCLIPLoader, VAELoader, UNETLoader, CLIPLoader, LoraLoader, LayerColor: Brightness & Contrast, LoadImage, LoadImage, VAEDecode, SaveImage, Image Comparer (rgthree), PreviewImage]
patterns: [text_to_image, image_to_image, lora]
missing: [LayerColor: Brightness & Contrast]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 0.5000000000000001, "height": 1536, "lora_name": "Wan2.1_T2V_14B_FusionX_LoRA.safetensors", "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 1011705246715296, "steps": 20, "strength_clip": 0.45000000000000007, "strength_model": 0.45000000000000007, "width": 1024}
discoveries: [次要节点 `LayerColor: Brightness & Contrast` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/Flux文生图+Wan2.1超真实洗图_1949521829412642817.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux文生图+Wan2.1超真实洗图_1949521829412642817.json`

## 结构

**节点**（33 个）：
- `CLIPTextEncode`
- `FilmGrain`
- `VAELoader`
- `KSampler`
- `PrimitiveNode`
- `CLIPTextEncode`
- `RandomNoise`
- `BasicGuider`
- `KSamplerSelect`
- `BasicScheduler`
- `SamplerCustomAdvanced`
- `VAEDecode`
- `CLIPTextEncode`
- `PreviewImage`
- `GetImageSize`
- `RH_Captioner`
- `ImageScale`
- `VAEEncode`
- `RH_Translator`
- `EmptyLatentImage`
- `UNETLoader`
- `DualCLIPLoader`
- `VAELoader`
- `UNETLoader`
- `CLIPLoader`
- `LoraLoader`
- `LayerColor: Brightness & Contrast`
- `LoadImage`
- `LoadImage`
- `VAEDecode`
- `SaveImage`
- `Image Comparer (rgthree)`
- `PreviewImage`

**识别到的模式**：text_to_image、image_to_image、lora

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `0.5000000000000001`
- `height` = `1536`
- `lora_name` = `Wan2.1_T2V_14B_FusionX_LoRA.safetensors`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `seed` = `1011705246715296`
- `steps` = `20`
- `strength_clip` = `0.45000000000000007`
- `strength_model` = `0.45000000000000007`
- `width` = `1024`

## 知识

覆盖率 **85%**（28/33）

**有卡**：`CLIPTextEncode`、`FilmGrain`、`VAELoader`、`KSampler`、`PrimitiveNode`、`RandomNoise`、`BasicGuider`、`KSamplerSelect`、`BasicScheduler`、`SamplerCustomAdvanced`、`VAEDecode`、`PreviewImage`、`GetImageSize`、`RH_Captioner`、`ImageScale`、`VAEEncode`、`RH_Translator`、`EmptyLatentImage`、`UNETLoader`、`DualCLIPLoader`、`CLIPLoader`、`LoraLoader`、`LayerColor: Brightness & Contrast`、`LoadImage`

**缺卡**（1）：`LayerColor: Brightness & Contrast`

## 学习发现

- 次要节点 `LayerColor: Brightness & Contrast` 知识库中没有该节点类型的任何知识
