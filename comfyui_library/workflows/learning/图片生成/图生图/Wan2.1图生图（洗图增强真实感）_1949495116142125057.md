---
key: 图片生成/图生图/Wan2.1图生图（洗图增强真实感）_1949495116142125057.json
name: Wan2.1图生图（洗图增强真实感）_1949495116142125057
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.1图生图（洗图增强真实感）_1949495116142125057.json
hash: 49d14907baeb98fd
coverage: 0.857143
learned_at: 2026-10-23 11:27:51
nodes: [LayerColor: Brightness & Contrast, FilmGrain, VAEDecode, LayerUtility: ImageScaleByAspectRatio V2, KSampler, RH_Captioner, ImageScale, CLIPTextEncode, LoadImage, LoadImage, LoadImage, CLIPLoader, PrimitiveNode, VAELoader, Image Comparer (rgthree), PreviewImage, UNETLoader, VAEEncode, SaveImage, CLIPTextEncode, LoraLoader]
patterns: [image_to_image, lora]
missing: []
parameters: {"cfg": 1, "denoise": 0.5000000000000001, "lora_name": "Wan2.1_T2V_14B_FusionX_LoRA.safetensors", "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 110559553691710, "steps": 20, "strength_clip": 0.45000000000000007, "strength_model": 0.45000000000000007}
---

# 图片生成/图生图/Wan2.1图生图（洗图增强真实感）_1949495116142125057.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.1图生图（洗图增强真实感）_1949495116142125057.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `LayerColor: Brightness & Contrast`
- `FilmGrain`
- `VAEDecode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `KSampler` ★核心
- `RH_Captioner`
- `ImageScale`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CLIPLoader`
- `PrimitiveNode`
- `VAELoader`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `UNETLoader` ★核心
- `VAEEncode` ★核心
- `SaveImage`
- `CLIPTextEncode` ★核心
- `LoraLoader` ★核心

**识别到的模式**：image_to_image、lora

## 关键参数

- `seed` = `110559553691710`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `denoise` = `0.5000000000000001`
- `lora_name` = `Wan2.1_T2V_14B_FusionX_LoRA.safetensors`
- `strength_model` = `0.45000000000000007`
- `strength_clip` = `0.45000000000000007`

## 知识

覆盖率 **86%**（18/21）

**有卡**：`LayerColor: Brightness & Contrast`、`FilmGrain`、`VAEDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`KSampler`、`RH_Captioner`、`ImageScale`、`CLIPTextEncode`、`LoadImage`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`VAEEncode`、`SaveImage`、`LoraLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、VAEEncode
