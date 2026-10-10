---
key: 无AI味逼真质感文生图-Flux.1-Krea-Dev_1951090280026058754.json
name: 无AI味逼真质感文生图-Flux.1-Krea-Dev_1951090280026058754
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/无AI味逼真质感文生图-Flux.1-Krea-Dev_1951090280026058754.json
hash: 06ae0a646db70e8a
coverage: 0.818182
learned_at: 2026-10-10 20:59:50
nodes: [KSampler, VAEDecode, DualCLIPLoader, CLIPTextEncodeFlux, ConditioningZeroOut, SaveImage, CR SDXL Aspect Ratio, VAELoader, RH_Translator, UNETLoader, PrimitiveStringMultiline]
patterns: []
missing: [CR SDXL Aspect Ratio]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1060240504377534, "steps": 20}
discoveries: [次要节点 `CR SDXL Aspect Ratio` 仅有 Checkpoint 的通用知识，没有该节点自己的说明]
---

# 无AI味逼真质感文生图-Flux.1-Krea-Dev_1951090280026058754.json

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

覆盖率 **82%**（9/11）

**有卡**：`KSampler`、`VAEDecode`、`DualCLIPLoader`、`CLIPTextEncodeFlux`、`ConditioningZeroOut`、`SaveImage`、`VAELoader`、`RH_Translator`、`UNETLoader`

**缺卡**（1）：`CR SDXL Aspect Ratio`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、ConditioningZeroOut、CLIPTextEncodeFlux、DualCLIPLoader、SaveImage

## 学习发现

- 次要节点 `CR SDXL Aspect Ratio` 仅有 Checkpoint 的通用知识，没有该节点自己的说明
