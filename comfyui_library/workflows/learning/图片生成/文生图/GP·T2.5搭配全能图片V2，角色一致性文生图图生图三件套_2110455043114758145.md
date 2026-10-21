---
key: 图片生成/文生图/GP·T2.5搭配全能图片V2，角色一致性文生图图生图三件套_2110455043114758145.json
name: GP·T2.5搭配全能图片V2，角色一致性文生图图生图三件套_2110455043114758145
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/GP·T2.5搭配全能图片V2，角色一致性文生图图生图三件套_2110455043114758145.json
hash: b4281519b61866b9
coverage: 0.877551
learned_at: 2026-10-21 02:52:33
nodes: [LoadImage, LoadImage, SaveImage, RH_RhartImageG2ImageToImage, RH_Nano_Banana2_Gemini31Flash, LoadImage, SaveImage, LoadImage, SaveImage, easy int, SeedVR2, SeedVR2BlockSwap, SaveImage, LoadImage, Image Comparer (rgthree), LoadImage, SaveImage, RH_RhartImageG25SunburstImageToImage, RH_RhartImageNNb21ImageToImage, JjkText, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/GP·T2.5搭配全能图片V2，角色一致性文生图图生图三件套_2110455043114758145.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/GP·T2.5搭配全能图片V2，角色一致性文生图图生图三件套_2110455043114758145.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（49 个）：
- `LoadImage`
- `LoadImage`
- `SaveImage`
- `RH_RhartImageG2ImageToImage`
- `RH_Nano_Banana2_Gemini31Flash`
- `LoadImage`
- `SaveImage`
- `LoadImage`
- `SaveImage`
- `easy int`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `SaveImage`
- `LoadImage`
- `Image Comparer (rgthree)`
- `LoadImage`
- `SaveImage`
- `RH_RhartImageG25SunburstImageToImage`
- `RH_RhartImageNNb21ImageToImage`
- `JjkText`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `JjkText`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `VAELoader`
- `solarL_SaveImagesToZip`
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **88%**（43/49）

**有卡**：`LoadImage`、`SaveImage`、`RH_RhartImageG2ImageToImage`、`RH_Nano_Banana2_Gemini31Flash`、`easy int`、`SeedVR2`、`SeedVR2BlockSwap`、`RH_RhartImageG25SunburstImageToImage`、`RH_RhartImageNNb21ImageToImage`、`UNETLoader`、`LoraLoaderModelOnly`、`KSampler`、`CLIPTextEncode`、`CLIPLoader`、`VAEDecode`、`EmptyLatentImage`、`VAELoader`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
