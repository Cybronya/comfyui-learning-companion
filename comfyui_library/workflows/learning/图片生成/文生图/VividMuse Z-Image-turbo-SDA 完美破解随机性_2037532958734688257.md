---
key: 图片生成/文生图/VividMuse Z-Image-turbo-SDA 完美破解随机性_2037532958734688257.json
name: VividMuse Z-Image-turbo-SDA 完美破解随机性_2037532958734688257
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/VividMuse Z-Image-turbo-SDA 完美破解随机性_2037532958734688257.json
hash: 03edff3b0f41f09f
coverage: 0.933333
learned_at: 2026-10-21 02:55:20
nodes: [VAELoader, CLIPTextEncode, ConditioningZeroOut, UNETLoader, VAELoader, EmptyLatentImage, CLIPLoader, CLIPLoader, KSamplerAdvanced, UNETLoader, CLIPLoader, VAELoader, CLIPTextEncode, ConditioningZeroOut, LoraLoaderModelOnly, VAEDecode, VAEDecode, KSamplerAdvanced, KSamplerAdvanced, PrimitiveStringMultiline, UNETLoader, LoraLoaderModelOnly, VAEDecode, CLIPTextEncode, ConditioningZeroOut, easy promptList, SaveImage, SaveImage, SaveImage, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
parameters: {"batch_size": 4, "cfg": 8, "denoise": "FlowMatchEulerDiscreteScheduler", "height": 2048, "sampler_name": 1, "scheduler": "lcm", "seed": "enable", "steps": "randomize", "width": 1536}
---

# 图片生成/文生图/VividMuse Z-Image-turbo-SDA 完美破解随机性_2037532958734688257.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/VividMuse Z-Image-turbo-SDA 完美破解随机性_2037532958734688257.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（30 个）：
- `VAELoader`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `UNETLoader` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `CLIPLoader`
- `CLIPLoader`
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `PrimitiveStringMultiline`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `easy promptList`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`

## 关键参数

- `width` = `1536`
- `height` = `2048`
- `batch_size` = `4`
- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `FlowMatchEulerDiscreteScheduler`

## 知识

覆盖率 **93%**（28/30）

**有卡**：`VAELoader`、`CLIPTextEncode`、`ConditioningZeroOut`、`UNETLoader`、`EmptyLatentImage`、`CLIPLoader`、`KSamplerAdvanced`、`LoraLoaderModelOnly`、`VAEDecode`、`easy promptList`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、UNETLoader
