---
key: 图片生成/文生图/RealQwenImage1.0真实人像出图_2012887003628572673.json
name: RealQwenImage1.0真实人像出图_2012887003628572673
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/RealQwenImage1.0真实人像出图_2012887003628572673.json
hash: d047c99492a64a1f
coverage: 0.9375
learned_at: 2026-10-19 22:15:19
nodes: [UNETLoader, INTConstant, INTConstant, LoraLoaderModelOnly, INTConstant, CLIPLoader, SaveImage, CLIPTextEncode, CLIPTextEncode, EmptyLatentImage, ModelSamplingAuraFlow, KSampler, VAEDecode, VAELoader, Seed (rgthree), PrimitiveStringMultiline]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1.2, "denoise": 1, "height": 1824, "sampler_name": "euler", "scheduler": "simple", "seed": 121125480055509, "steps": 12, "width": 1024}
---

# 图片生成/文生图/RealQwenImage1.0真实人像出图_2012887003628572673.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/RealQwenImage1.0真实人像出图_2012887003628572673.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（16 个）：
- `UNETLoader` ★核心
- `INTConstant`
- `INTConstant`
- `LoraLoaderModelOnly` ★核心
- `INTConstant`
- `CLIPLoader`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `ModelSamplingAuraFlow`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `VAELoader`
- `Seed (rgthree)`
- `PrimitiveStringMultiline`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1024`
- `height` = `1824`
- `batch_size` = `1`
- `seed` = `121125480055509`
- `steps` = `12`
- `cfg` = `1.2`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **94%**（15/16）

**有卡**：`UNETLoader`、`INTConstant`、`LoraLoaderModelOnly`、`CLIPLoader`、`SaveImage`、`CLIPTextEncode`、`EmptyLatentImage`、`ModelSamplingAuraFlow`、`KSampler`、`VAEDecode`、`VAELoader`、`Seed (rgthree)`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader
