---
key: 图片生成/图生图/Anima+V1.0 图生图 二次元手绘风 anima_base 卡通动漫角色Q版可爱动画风_2057338559039885313.json
name: Anima+V1.0 图生图 二次元手绘风 anima_base 卡通动漫角色Q版可爱动画风_2057338559039885313
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Anima+V1.0 图生图 二次元手绘风 anima_base 卡通动漫角色Q版可爱动画风_2057338559039885313.json
hash: 11ac34e0d72bc477
coverage: 0.933333
learned_at: 2026-10-23 10:51:08
nodes: [UNETLoader, CLIPLoader, VAEDecode, EmptyLatentImage, CR Prompt Text, CLIPTextEncode, CLIPTextEncode, ConcatTextOfUtils, KSampler, Florence2ModelLoader, Florence2Run, VAELoader, easy showAnything, LoadImage, SaveImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 1080, "sampler_name": "er_sde", "scheduler": "beta", "seed": 237925664789044, "steps": 40, "width": 1920}
---

# 图片生成/图生图/Anima+V1.0 图生图 二次元手绘风 anima_base 卡通动漫角色Q版可爱动画风_2057338559039885313.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Anima+V1.0 图生图 二次元手绘风 anima_base 卡通动漫角色Q版可爱动画风_2057338559039885313.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（15 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `CR Prompt Text`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ConcatTextOfUtils`
- `KSampler` ★核心
- `Florence2ModelLoader`
- `Florence2Run`
- `VAELoader`
- `easy showAnything`
- `LoadImage`
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1920`
- `height` = `1080`
- `batch_size` = `1`
- `seed` = `237925664789044`
- `steps` = `40`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **93%**（14/15）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAEDecode`、`EmptyLatentImage`、`CR Prompt Text`、`CLIPTextEncode`、`ConcatTextOfUtils`、`KSampler`、`Florence2ModelLoader`、`Florence2Run`、`VAELoader`、`LoadImage`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage、UNETLoader
