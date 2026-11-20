---
key: 平台全量/logo设计-LOGO-图形LOGO-标志设计-创意LOGO平面设计 创意卡通logo设计 Qwen_2016402061209903106.json
name: logo设计-LOGO-图形LOGO-标志设计-创意LOGO平面设计 创意卡通logo设计 Qwen_2016402061209903106
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/logo设计-LOGO-图形LOGO-标志设计-创意LOGO平面设计 创意卡通logo设计 Qwen_2016402061209903106.json
hash: 18752450250dfb7f
coverage: 0.870968
learned_at: 2026-11-14 01:14:30
nodes: [KSampler, CLIPTextEncode, UNETLoader, CLIPLoader, VAELoader, ModelSamplingAuraFlow, Int, Int, Int, Int, Int, Int, ImpactSwitch, Int, Int, Int, Int, ImpactSwitch, Int, Int, Int, Int, LoraLoaderModelOnly, CLIPTextEncode, EmptyLatentImage, Text, Note, AILab_QwenVL, easy showAnything, SaveImage, VAEDecode]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 3.5, "denoise": 1, "height": 512, "sampler_name": "euler", "scheduler": "simple", "seed": 1051986075751196, "steps": 30, "width": 512}
---

# 平台全量/logo设计-LOGO-图形LOGO-标志设计-创意LOGO平面设计 创意卡通logo设计 Qwen_2016402061209903106.json

> 来源文件 `comfyui_library/workflows/平台全量/logo设计-LOGO-图形LOGO-标志设计-创意LOGO平面设计 创意卡通logo设计 Qwen_2016402061209903106.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（31 个）：
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `ModelSamplingAuraFlow`
- `Int`
- `Int`
- `Int`
- `Int`
- `Int`
- `Int`
- `ImpactSwitch`
- `Int`
- `Int`
- `Int`
- `Int`
- `ImpactSwitch`
- `Int`
- `Int`
- `Int`
- `Int`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `Text`
- `Note`
- `AILab_QwenVL`
- `easy showAnything`
- `SaveImage`
- `VAEDecode` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `1051986075751196`
- `steps` = `30`
- `cfg` = `3.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `512`
- `height` = `512`
- `batch_size` = `1`

## 知识

覆盖率 **87%**（27/31）

**有卡**：`KSampler`、`CLIPTextEncode`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`ModelSamplingAuraFlow`、`Int`、`LoraLoaderModelOnly`、`EmptyLatentImage`、`Text`、`AILab_QwenVL`、`SaveImage`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、EmptyLatentImage、UNETLoader
