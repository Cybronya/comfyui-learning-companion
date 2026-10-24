---
key: 图片生成/图生图/最强动漫 Anima base v1.0 图生图 提示词扩写 自动匹配画师_2056557560999792641.json
name: 最强动漫 Anima base v1.0 图生图 提示词扩写 自动匹配画师_2056557560999792641
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/最强动漫 Anima base v1.0 图生图 提示词扩写 自动匹配画师_2056557560999792641.json
hash: 3c50a348c176ee55
coverage: 0.806452
learned_at: 2026-10-23 13:05:48
nodes: [CLIPLoader, VAELoader, SaveImage, llama_cpp_parameters, UNETLoader, Note, SaveImage, CLIPTextEncode, CLIPTextEncode, VAEDecode, VAEDecode, KSampler, CLIPTextEncode, PreviewAny, llama_cpp_model_loader, Note, LoraLoaderModelOnly, CLIPTextEncode, Seed_, KSampler, LayerUtility: ImageReelComposit, Note, Note, EmptyLatentImage, LayerUtility: ImageScaleByAspectRatio V2, Note, llama_cpp_instruct_adv, LoadImage, LayerUtility: ImageReel, CR Text, SaveImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1536, "sampler_name": "er_sde", "scheduler": "simple", "seed": 888, "steps": 12, "width": 1536}
---

# 图片生成/图生图/最强动漫 Anima base v1.0 图生图 提示词扩写 自动匹配画师_2056557560999792641.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/最强动漫 Anima base v1.0 图生图 提示词扩写 自动匹配画师_2056557560999792641.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（31 个）：
- `CLIPLoader`
- `VAELoader`
- `SaveImage`
- `llama_cpp_parameters`
- `UNETLoader` ★核心
- `Note`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `PreviewAny`
- `llama_cpp_model_loader`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `Seed_`
- `KSampler` ★核心
- `LayerUtility: ImageReelComposit`
- `Note`
- `Note`
- `EmptyLatentImage` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Note`
- `llama_cpp_instruct_adv`
- `LoadImage`
- `LayerUtility: ImageReel`
- `CR Text`
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `888`
- `steps` = `12`
- `cfg` = `1`
- `sampler_name` = `er_sde`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1536`
- `height` = `1536`
- `batch_size` = `1`

## 知识

覆盖率 **81%**（25/31）

**有卡**：`CLIPLoader`、`VAELoader`、`SaveImage`、`llama_cpp_parameters`、`UNETLoader`、`CLIPTextEncode`、`VAEDecode`、`KSampler`、`llama_cpp_model_loader`、`LoraLoaderModelOnly`、`Seed_`、`LayerUtility: ImageReelComposit`、`EmptyLatentImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`llama_cpp_instruct_adv`、`LoadImage`、`LayerUtility: ImageReel`、`CR Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage
