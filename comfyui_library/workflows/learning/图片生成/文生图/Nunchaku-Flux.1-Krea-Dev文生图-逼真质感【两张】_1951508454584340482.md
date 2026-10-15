---
key: 图片生成/文生图/Nunchaku-Flux.1-Krea-Dev文生图-逼真质感【两张】_1951508454584340482.json
name: Nunchaku-Flux.1-Krea-Dev文生图-逼真质感【两张】_1951508454584340482
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Nunchaku-Flux.1-Krea-Dev文生图-逼真质感【两张】_1951508454584340482.json
hash: 0f12ead03746342b
coverage: 0.833333
learned_at: 2026-10-10 20:58:48
nodes: [UNETLoader, SaveImage, NunchakuFluxDiTLoader, CR SDXL Aspect Ratio, RH_Translator, KSampler, VAEDecode, DualCLIPLoader, VAELoader, CLIPTextEncode, ConditioningZeroOut, Text Multiline]
patterns: []
missing: [Text Multiline, CR SDXL Aspect Ratio]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 982866085529541, "steps": 20}
discoveries: [次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `CR SDXL Aspect Ratio` 仅有 Checkpoint 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/Nunchaku-Flux.1-Krea-Dev文生图-逼真质感【两张】_1951508454584340482.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Nunchaku-Flux.1-Krea-Dev文生图-逼真质感【两张】_1951508454584340482.json`

## 结构

**节点**（12 个）：
- `UNETLoader`
- `SaveImage`
- `NunchakuFluxDiTLoader`
- `CR SDXL Aspect Ratio`
- `RH_Translator`
- `KSampler`
- `VAEDecode`
- `DualCLIPLoader`
- `VAELoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Text Multiline`

## 关键参数

- `cfg` = `1`
- `denoise` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `982866085529541`
- `steps` = `20`

## 知识

覆盖率 **83%**（10/12）

**有卡**：`UNETLoader`、`SaveImage`、`NunchakuFluxDiTLoader`、`CR SDXL Aspect Ratio`、`RH_Translator`、`KSampler`、`VAEDecode`、`DualCLIPLoader`、`VAELoader`、`CLIPTextEncode`

**缺卡**（2）：`Text Multiline`、`CR SDXL Aspect Ratio`

## 学习发现

- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `CR SDXL Aspect Ratio` 仅有 Checkpoint 的通用知识，没有该节点自己的说明
