---
key: 图片生成/文生图/Pornmaster_krea2_t2i_Raw+Turbo_2098728229115879426.json
name: Pornmaster_krea2_t2i_Raw+Turbo_2098728229115879426
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Pornmaster_krea2_t2i_Raw+Turbo_2098728229115879426.json
hash: 5b8c2ed4254eeacd
coverage: 0.916667
learned_at: 2026-10-20 01:34:53
nodes: [Note, VAELoader, CLIPTextEncode, CLIPLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSamplerAdvanced, LoraLoaderModelOnly, Note, VAEDecode, UNETLoader, EmptyLatentImage, Int, Int, CLIPTextEncode, SaveImage, CompressImages]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 8, "denoise": "simple", "height": 1216, "sampler_name": 1.5, "scheduler": "euler", "seed": "enable", "steps": "randomize", "width": 832}
---

# 图片生成/文生图/Pornmaster_krea2_t2i_Raw+Turbo_2098728229115879426.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Pornmaster_krea2_t2i_Raw+Turbo_2098728229115879426.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `Note`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `EmptyLatentImage` ★核心
- `Int`
- `Int`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `CompressImages`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1.5`
- `scheduler` = `euler`
- `denoise` = `simple`
- `width` = `832`
- `height` = `1216`
- `batch_size` = `1`

## 知识

覆盖率 **92%**（22/24）

**有卡**：`VAELoader`、`CLIPTextEncode`、`CLIPLoader`、`LoraLoaderModelOnly`、`KSamplerAdvanced`、`VAEDecode`、`UNETLoader`、`EmptyLatentImage`、`Int`、`SaveImage`、`CompressImages`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader、KSamplerAdvanced
