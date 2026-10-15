---
key: 图片生成/文生图/JoyCaption Beta One 反推提示词-flux文生图_1938602282357284865.json
name: JoyCaption Beta One 反推提示词-flux文生图_1938602282357284865
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/JoyCaption Beta One 反推提示词-flux文生图_1938602282357284865.json
hash: be7fb707b0107694
coverage: 0.866667
learned_at: 2026-10-15 22:26:35
nodes: [LayerUtility: LoadJoyCaptionBeta1Model, VAELoader, EmptySD3LatentImage, ShowText|pysssss, CLIPTextEncodeFlux, ConditioningZeroOut, VAEDecode, KSampler, LayerUtility: JoyCaptionBeta1, SaveImage, LoadImage, ShowText|pysssss, ArgosTranslateTextNode, UNETLoader, DualCLIPLoader]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 260417191096854, "steps": 10}
---

# 图片生成/文生图/JoyCaption Beta One 反推提示词-flux文生图_1938602282357284865.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/JoyCaption Beta One 反推提示词-flux文生图_1938602282357284865.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（15 个）：
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `VAELoader`
- `EmptySD3LatentImage`
- `ShowText|pysssss`
- `CLIPTextEncodeFlux` ★核心
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `LayerUtility: JoyCaptionBeta1`
- `SaveImage`
- `LoadImage`
- `ShowText|pysssss`
- `ArgosTranslateTextNode`
- `UNETLoader` ★核心
- `DualCLIPLoader`

## 关键参数

- `seed` = `260417191096854`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **87%**（13/15）

**有卡**：`LayerUtility: LoadJoyCaptionBeta1Model`、`VAELoader`、`EmptySD3LatentImage`、`CLIPTextEncodeFlux`、`ConditioningZeroOut`、`VAEDecode`、`KSampler`、`LayerUtility: JoyCaptionBeta1`、`SaveImage`、`LoadImage`、`ArgosTranslateTextNode`、`UNETLoader`、`DualCLIPLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、ConditioningZeroOut、LoadImage、CLIPTextEncodeFlux、DualCLIPLoader
