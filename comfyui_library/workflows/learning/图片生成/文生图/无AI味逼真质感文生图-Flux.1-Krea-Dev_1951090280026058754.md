---
key: 图片生成/文生图/无AI味逼真质感文生图-Flux.1-Krea-Dev_1951090280026058754.json
name: 无AI味逼真质感文生图-Flux.1-Krea-Dev_1951090280026058754
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/无AI味逼真质感文生图-Flux.1-Krea-Dev_1951090280026058754.json
hash: 06ae0a646db70e8a
coverage: 0.909091
learned_at: 2026-10-15 22:28:52
nodes: [KSampler, VAEDecode, DualCLIPLoader, CLIPTextEncodeFlux, ConditioningZeroOut, SaveImage, CR SDXL Aspect Ratio, VAELoader, RH_Translator, UNETLoader, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1060240504377534, "steps": 20}
---

# 图片生成/文生图/无AI味逼真质感文生图-Flux.1-Krea-Dev_1951090280026058754.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/无AI味逼真质感文生图-Flux.1-Krea-Dev_1951090280026058754.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（11 个）：
- `KSampler` ★核心
- `VAEDecode` ★核心
- `DualCLIPLoader`
- `CLIPTextEncodeFlux` ★核心
- `ConditioningZeroOut`
- `SaveImage`
- `CR SDXL Aspect Ratio`
- `VAELoader`
- `RH_Translator`
- `UNETLoader` ★核心
- `PrimitiveStringMultiline`

## 关键参数

- `seed` = `1060240504377534`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **91%**（10/11）

**有卡**：`KSampler`、`VAEDecode`、`DualCLIPLoader`、`CLIPTextEncodeFlux`、`ConditioningZeroOut`、`SaveImage`、`CR SDXL Aspect Ratio`、`VAELoader`、`RH_Translator`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、ConditioningZeroOut、CLIPTextEncodeFlux、DualCLIPLoader、CR SDXL Aspect Ratio
