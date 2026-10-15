---
key: 图片生成/文生图/Nunchaku-Flux.1-Krea-Dev文生图-逼真质感【两张】_1951508454584340482.json
name: Nunchaku-Flux.1-Krea-Dev文生图-逼真质感【两张】_1951508454584340482
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Nunchaku-Flux.1-Krea-Dev文生图-逼真质感【两张】_1951508454584340482.json
hash: 0f12ead03746342b
coverage: 1
learned_at: 2026-10-15 22:26:52
nodes: [UNETLoader, SaveImage, NunchakuFluxDiTLoader, CR SDXL Aspect Ratio, RH_Translator, KSampler, VAEDecode, DualCLIPLoader, VAELoader, CLIPTextEncode, ConditioningZeroOut, Text Multiline]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 982866085529541, "steps": 20}
---

# 图片生成/文生图/Nunchaku-Flux.1-Krea-Dev文生图-逼真质感【两张】_1951508454584340482.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Nunchaku-Flux.1-Krea-Dev文生图-逼真质感【两张】_1951508454584340482.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（12 个）：
- `UNETLoader` ★核心
- `SaveImage`
- `NunchakuFluxDiTLoader`
- `CR SDXL Aspect Ratio`
- `RH_Translator`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `Text Multiline`

## 关键参数

- `seed` = `982866085529541`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（12/12）

**有卡**：`UNETLoader`、`SaveImage`、`NunchakuFluxDiTLoader`、`CR SDXL Aspect Ratio`、`RH_Translator`、`KSampler`、`VAEDecode`、`DualCLIPLoader`、`VAELoader`、`CLIPTextEncode`、`ConditioningZeroOut`、`Text Multiline`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、DualCLIPLoader、NunchakuFluxDiTLoader
