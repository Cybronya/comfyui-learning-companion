---
key: 图片生成/文生图/Flux.1 Krea Dev文生图【逼真质感 无AI味】_1951177482479280130.json
name: Flux.1 Krea Dev文生图【逼真质感 无AI味】_1951177482479280130
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux.1 Krea Dev文生图【逼真质感 无AI味】_1951177482479280130.json
hash: 266c0d79403eb5b5
coverage: 0.85
learned_at: 2026-10-15 22:26:25
nodes: [easy compare, Int, RH_Translator, RH_LLMAPI_NODE, Note, DualCLIPLoader, UNETLoader, Note, Int, CLIPTextEncode, VAELoader, ConditioningZeroOut, KSampler, VAEDecode, easy ifElse, SaveImage, Display Any (rgthree), CR Text, CR SDXL Aspect Ratio, Int]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 534550369502419, "steps": 20}
---

# 图片生成/文生图/Flux.1 Krea Dev文生图【逼真质感 无AI味】_1951177482479280130.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux.1 Krea Dev文生图【逼真质感 无AI味】_1951177482479280130.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（20 个）：
- `easy compare`
- `Int`
- `RH_Translator`
- `RH_LLMAPI_NODE`
- `Note`
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `Note`
- `Int`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `ConditioningZeroOut`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `easy ifElse`
- `SaveImage`
- `Display Any (rgthree)`
- `CR Text`
- `CR SDXL Aspect Ratio`
- `Int`

## 关键参数

- `seed` = `534550369502419`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **85%**（17/20）

**有卡**：`easy compare`、`Int`、`RH_Translator`、`RH_LLMAPI_NODE`、`DualCLIPLoader`、`UNETLoader`、`CLIPTextEncode`、`VAELoader`、`ConditioningZeroOut`、`KSampler`、`VAEDecode`、`SaveImage`、`Display Any (rgthree)`、`CR Text`、`CR SDXL Aspect Ratio`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、DualCLIPLoader、CR SDXL Aspect Ratio
