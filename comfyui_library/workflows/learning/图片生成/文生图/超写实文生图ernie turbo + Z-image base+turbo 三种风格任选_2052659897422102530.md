---
key: 图片生成/文生图/超写实文生图ernie turbo + Z-image base+turbo 三种风格任选_2052659897422102530.json
name: 超写实文生图ernie turbo + Z-image base+turbo 三种风格任选_2052659897422102530
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/超写实文生图ernie turbo + Z-image base+turbo 三种风格任选_2052659897422102530.json
hash: f3a44709578093b6
coverage: 0.803922
learned_at: 2026-10-21 03:02:59
nodes: [VAELoader, CLIPTextEncode, UNETLoader, ModelSamplingAuraFlow, VAEDecode, Note, Int, KSamplerAdvanced, CLIPTextEncode, CLIPLoader, CLIPTextEncode, InversionDemoLazyIndexSwitch, KSamplerAdvanced, Text, Int, CR Text, RH_LLMAPI_Pro_Node, RH_LLMAPI_NODE, CLIPLoader, VAELoader, CLIPTextEncode, CLIPTextEncode, easy showAnything, PreviewImage, ModelSamplingAuraFlow, VAEDecode, PreviewImage, VAEEncode, VAEDecode, KSamplerAdvanced, LoraLoaderModelOnly, Note, Note, Note, Note, Int, Int, Int, Note, InversionDemoLazyIndexSwitch, Note, Int, CheckpointLoaderSimple, UNETLoader, LoraLoaderModelOnly, VAELoader, SaveImage, Int, CheckpointLoaderSimple, EmptyLatentImage, CR Text]
patterns: []
missing: []
parameters: {"batch_size": 2, "cfg": 8, "checkpoint": "redcraft_ernieRedmix.safetensors", "denoise": "simple", "height": 1536, "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize", "width": 960}
---

# 图片生成/文生图/超写实文生图ernie turbo + Z-image base+turbo 三种风格任选_2052659897422102530.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/超写实文生图ernie turbo + Z-image base+turbo 三种风格任选_2052659897422102530.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Output → Other

**节点**（51 个）：
- `VAELoader`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `ModelSamplingAuraFlow`
- `VAEDecode` ★核心
- `Note`
- `Int`
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `InversionDemoLazyIndexSwitch`
- `KSamplerAdvanced` ★核心
- `Text`
- `Int`
- `CR Text`
- `RH_LLMAPI_Pro_Node`
- `RH_LLMAPI_NODE`
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `easy showAnything`
- `PreviewImage`
- `ModelSamplingAuraFlow`
- `VAEDecode` ★核心
- `PreviewImage`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`
- `Note`
- `Note`
- `Note`
- `Int`
- `Int`
- `Int`
- `Note`
- `InversionDemoLazyIndexSwitch`
- `Note`
- `Int`
- `CheckpointLoaderSimple` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `SaveImage`
- `Int`
- `CheckpointLoaderSimple` ★核心
- `EmptyLatentImage` ★核心
- `CR Text`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`
- `checkpoint` = `redcraft_ernieRedmix.safetensors`
- `width` = `960`
- `height` = `1536`
- `batch_size` = `2`

## 知识

覆盖率 **80%**（41/51）

**有卡**：`VAELoader`、`CLIPTextEncode`、`UNETLoader`、`ModelSamplingAuraFlow`、`VAEDecode`、`Int`、`KSamplerAdvanced`、`CLIPLoader`、`InversionDemoLazyIndexSwitch`、`Text`、`CR Text`、`RH_LLMAPI_Pro_Node`、`RH_LLMAPI_NODE`、`VAEEncode`、`LoraLoaderModelOnly`、`CheckpointLoaderSimple`、`SaveImage`、`EmptyLatentImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage
