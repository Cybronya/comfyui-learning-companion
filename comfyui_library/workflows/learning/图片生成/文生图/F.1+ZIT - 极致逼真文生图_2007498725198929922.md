---
key: 图片生成/文生图/F.1+ZIT - 极致逼真文生图_2007498725198929922.json
name: F.1+ZIT - 极致逼真文生图_2007498725198929922
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/F.1+ZIT - 极致逼真文生图_2007498725198929922.json
hash: 878f2fe54c365b2d
coverage: 0.884615
learned_at: 2026-10-19 22:00:29
nodes: [BasicGuider, FluxGuidance, EmptyLatentImage, ModelSamplingFlux, BasicScheduler, ConditioningZeroOut, CLIPTextEncode, PrimitiveNode, PrimitiveNode, VAEDecode, VAEDecode, KSampler, RandomNoise, Image Comparer (rgthree), UNETLoader, LoraLoaderModelOnly, DualCLIPLoader, VAELoader, SamplerCustomAdvanced, CLIPTextEncode, KSamplerSelect, UNETLoader, CLIPLoader, LoraLoaderModelOnly, SaveImage, CR Text]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 0.18, "height": 1920, "sampler_name": "euler", "scheduler": "simple", "seed": 527852915460238, "steps": 10, "width": 1024}
---

# 图片生成/文生图/F.1+ZIT - 极致逼真文生图_2007498725198929922.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/F.1+ZIT - 极致逼真文生图_2007498725198929922.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（26 个）：
- `BasicGuider`
- `FluxGuidance`
- `EmptyLatentImage` ★核心
- `ModelSamplingFlux`
- `BasicScheduler`
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `PrimitiveNode`
- `PrimitiveNode`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `RandomNoise`
- `Image Comparer (rgthree)`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `SamplerCustomAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `KSamplerSelect` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `CR Text`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1024`
- `height` = `1920`
- `batch_size` = `1`
- `seed` = `527852915460238`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.18`

## 知识

覆盖率 **88%**（23/26）

**有卡**：`BasicGuider`、`FluxGuidance`、`EmptyLatentImage`、`ModelSamplingFlux`、`BasicScheduler`、`ConditioningZeroOut`、`CLIPTextEncode`、`VAEDecode`、`KSampler`、`RandomNoise`、`UNETLoader`、`LoraLoaderModelOnly`、`DualCLIPLoader`、`VAELoader`、`SamplerCustomAdvanced`、`KSamplerSelect`、`CLIPLoader`、`SaveImage`、`CR Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut
