---
key: 图片生成/文生图/ernie turbo + Z-image base+turbo 三阶采样 多样性超写实 文生图 图生图洗图_2044650703913750529.json
name: ernie turbo + Z-image base+turbo 三阶采样 多样性超写实 文生图 图生图洗图_2044650703913750529
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/ernie turbo + Z-image base+turbo 三阶采样 多样性超写实 文生图 图生图洗图_2044650703913750529.json
hash: 8f8f1ce3c6ef0528
coverage: 0.818182
learned_at: 2026-10-19 22:45:57
nodes: [VAELoader, CLIPTextEncode, UNETLoader, ModelSamplingAuraFlow, VAEDecode, Note, Int, KSamplerAdvanced, CLIPLoader, Int, CLIPTextEncode, CLIPTextEncode, PreviewImage, VAEEncode, VAEDecode, KSamplerAdvanced, Note, Note, Note, Note, Int, CLIPTextEncode, CheckpointLoaderSimple, Int, Int, CLIPTextEncode, CLIPLoader, KSamplerAdvanced, ModelSamplingAuraFlow, VAEDecode, InversionDemoLazyIndexSwitch, CR Text, CR Text, SaveImage, InversionDemoLazyIndexSwitch, easy showAnything, UNETLoader, LoraLoaderModelOnly, VAELoader, VAELoader, EmptyLatentImage, CR Text, Int, Text, Text, Note, LoraLoaderModelOnly, LoraLoaderModelOnly, CheckpointLoaderSimple, Note, PreviewImage, LoadImage, Int, RH_LLMAPI_Pro_Node, RH_LLMAPI_Pro_Node]
patterns: []
missing: []
parameters: {"batch_size": 6, "cfg": 3, "checkpoint": "redcraft_ernieRedmix.safetensors", "denoise": "simple", "height": 1536, "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize", "width": 1024}
---

# 图片生成/文生图/ernie turbo + Z-image base+turbo 三阶采样 多样性超写实 文生图 图生图洗图_2044650703913750529.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/ernie turbo + Z-image base+turbo 三阶采样 多样性超写实 文生图 图生图洗图_2044650703913750529.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Output → Other

**节点**（55 个）：
- `VAELoader`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `ModelSamplingAuraFlow`
- `VAEDecode` ★核心
- `Note`
- `Int`
- `KSamplerAdvanced` ★核心
- `CLIPLoader`
- `Int`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `Note`
- `Note`
- `Note`
- `Note`
- `Int`
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `Int`
- `Int`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `KSamplerAdvanced` ★核心
- `ModelSamplingAuraFlow`
- `VAEDecode` ★核心
- `InversionDemoLazyIndexSwitch`
- `CR Text`
- `CR Text`
- `SaveImage`
- `InversionDemoLazyIndexSwitch`
- `easy showAnything`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `CR Text`
- `Int`
- `Text`
- `Text`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CheckpointLoaderSimple` ★核心
- `Note`
- `PreviewImage`
- `LoadImage`
- `Int`
- `RH_LLMAPI_Pro_Node`
- `RH_LLMAPI_Pro_Node`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `3`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`
- `checkpoint` = `redcraft_ernieRedmix.safetensors`
- `width` = `1024`
- `height` = `1536`
- `batch_size` = `6`

## 知识

覆盖率 **82%**（45/55）

**有卡**：`VAELoader`、`CLIPTextEncode`、`UNETLoader`、`ModelSamplingAuraFlow`、`VAEDecode`、`Int`、`KSamplerAdvanced`、`CLIPLoader`、`VAEEncode`、`CheckpointLoaderSimple`、`InversionDemoLazyIndexSwitch`、`CR Text`、`SaveImage`、`LoraLoaderModelOnly`、`EmptyLatentImage`、`Text`、`LoadImage`、`RH_LLMAPI_Pro_Node`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage
