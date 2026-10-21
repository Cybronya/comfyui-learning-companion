---
key: 图片生成/文生图/Anima base v1.0 文生图 提示词扩写 自动匹配画师_2058751293228933122.json
name: Anima base v1.0 文生图 提示词扩写 自动匹配画师_2058751293228933122
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Anima base v1.0 文生图 提示词扩写 自动匹配画师_2058751293228933122.json
hash: dc21ceb196a92298
coverage: 0.851852
learned_at: 2026-10-19 23:02:11
nodes: [CLIPLoader, VAELoader, SaveImage, llama_cpp_parameters, UNETLoader, Note, SaveImage, CLIPTextEncode, VAEDecode, VAEDecode, KSampler, llama_cpp_instruct_adv, PreviewAny, llama_cpp_model_loader, Note, EmptyLatentImage, Note, LoraLoaderModelOnly, Seed_, KSampler, LayerUtility: ImageReelComposit, SaveImage, LayerUtility: ImageReel, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, CR Text]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1536, "sampler_name": "er_sde", "scheduler": "simple", "seed": 888, "steps": 12, "width": 1536}
---

# 图片生成/文生图/Anima base v1.0 文生图 提示词扩写 自动匹配画师_2058751293228933122.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Anima base v1.0 文生图 提示词扩写 自动匹配画师_2058751293228933122.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `CLIPLoader`
- `VAELoader`
- `SaveImage`
- `llama_cpp_parameters`
- `UNETLoader` ★核心
- `Note`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `llama_cpp_instruct_adv`
- `PreviewAny`
- `llama_cpp_model_loader`
- `Note`
- `EmptyLatentImage` ★核心
- `Note`
- `LoraLoaderModelOnly` ★核心
- `Seed_`
- `KSampler` ★核心
- `LayerUtility: ImageReelComposit`
- `SaveImage`
- `LayerUtility: ImageReel`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CR Text`

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

覆盖率 **85%**（23/27）

**有卡**：`CLIPLoader`、`VAELoader`、`SaveImage`、`llama_cpp_parameters`、`UNETLoader`、`CLIPTextEncode`、`VAEDecode`、`KSampler`、`llama_cpp_instruct_adv`、`llama_cpp_model_loader`、`EmptyLatentImage`、`LoraLoaderModelOnly`、`Seed_`、`LayerUtility: ImageReelComposit`、`LayerUtility: ImageReel`、`CR Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader
