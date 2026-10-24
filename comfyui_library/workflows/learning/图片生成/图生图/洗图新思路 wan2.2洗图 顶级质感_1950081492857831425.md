---
key: 图片生成/图生图/洗图新思路 wan2.2洗图 顶级质感_1950081492857831425.json
name: 洗图新思路 wan2.2洗图 顶级质感_1950081492857831425
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/洗图新思路 wan2.2洗图 顶级质感_1950081492857831425.json
hash: e175ce43af0fbdc1
coverage: 0.733333
learned_at: 2026-10-23 13:12:09
nodes: [CLIPTextEncode, VAELoader, SaveImage, CLIPLoader, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, VAEEncode, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, Reroute, PDImageResizeV2, LoadImage, RH_LLMAPI_NODE, VAEDecode, ttN concat, RH_Captioner, easy showAnything, LoraLoader, PreviewImage, MarkdownNote, EmptyHunyuanLatentVideo, CLIPTextEncode, UNETLoader, LoraLoader, LoraLoader, LayerUtility: SaveImagePlusV2, ModelSamplingSD3, KSampler]
patterns: [image_to_image, lora]
missing: []
parameters: {"cfg": 3.5, "denoise": 0.30000000000000004, "lora_name": "Wan2.1_T2V_14B_FusionX_LoRA.safetensors", "sampler_name": "euler", "scheduler": "simple", "seed": 1234567911, "steps": 20, "strength_clip": 0.4000000000000001, "strength_model": 0.4000000000000001}
---

# 图片生成/图生图/洗图新思路 wan2.2洗图 顶级质感_1950081492857831425.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/洗图新思路 wan2.2洗图 顶级质感_1950081492857831425.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `CLIPTextEncode` ★核心
- `VAELoader`
- `SaveImage`
- `CLIPLoader`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `VAEEncode` ★核心
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `Reroute`
- `PDImageResizeV2`
- `LoadImage`
- `RH_LLMAPI_NODE`
- `VAEDecode` ★核心
- `ttN concat`
- `RH_Captioner`
- `easy showAnything`
- `LoraLoader` ★核心
- `PreviewImage`
- `MarkdownNote`
- `EmptyHunyuanLatentVideo`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `LayerUtility: SaveImagePlusV2`
- `ModelSamplingSD3`
- `KSampler` ★核心

**识别到的模式**：image_to_image、lora

## 关键参数

- `lora_name` = `Wan2.1_T2V_14B_FusionX_LoRA.safetensors`
- `strength_model` = `0.4000000000000001`
- `strength_clip` = `0.4000000000000001`
- `seed` = `1234567911`
- `steps` = `20`
- `cfg` = `3.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.30000000000000004`

## 知识

覆盖率 **73%**（22/30）

**有卡**：`CLIPTextEncode`、`VAELoader`、`SaveImage`、`CLIPLoader`、`VAEEncode`、`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`、`PDImageResizeV2`、`LoadImage`、`RH_LLMAPI_NODE`、`VAEDecode`、`ttN concat`、`RH_Captioner`、`LoraLoader`、`EmptyHunyuanLatentVideo`、`UNETLoader`、`LayerUtility: SaveImagePlusV2`、`ModelSamplingSD3`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、VAEEncode
