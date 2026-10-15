---
key: 图片生成/文生图/JoyCaption Beta One 反推提示词-flux文生图_1938602282357284865.json
name: JoyCaption Beta One 反推提示词-flux文生图_1938602282357284865
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/JoyCaption Beta One 反推提示词-flux文生图_1938602282357284865.json
hash: be7fb707b0107694
coverage: 0.733333
learned_at: 2026-10-10 20:58:41
nodes: [LayerUtility: LoadJoyCaptionBeta1Model, VAELoader, EmptySD3LatentImage, ShowText|pysssss, CLIPTextEncodeFlux, ConditioningZeroOut, VAEDecode, KSampler, LayerUtility: JoyCaptionBeta1, SaveImage, LoadImage, ShowText|pysssss, ArgosTranslateTextNode, UNETLoader, DualCLIPLoader]
patterns: []
missing: [LayerUtility: JoyCaptionBeta1, LayerUtility: LoadJoyCaptionBeta1Model]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 260417191096854, "steps": 10}
discoveries: [次要节点 `LayerUtility: JoyCaptionBeta1` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: LoadJoyCaptionBeta1Model` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/JoyCaption Beta One 反推提示词-flux文生图_1938602282357284865.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/JoyCaption Beta One 反推提示词-flux文生图_1938602282357284865.json`

## 结构

**节点**（15 个）：
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `VAELoader`
- `EmptySD3LatentImage`
- `ShowText|pysssss`
- `CLIPTextEncodeFlux`
- `ConditioningZeroOut`
- `VAEDecode`
- `KSampler`
- `LayerUtility: JoyCaptionBeta1`
- `SaveImage`
- `LoadImage`
- `ShowText|pysssss`
- `ArgosTranslateTextNode`
- `UNETLoader`
- `DualCLIPLoader`

## 关键参数

- `cfg` = `1`
- `denoise` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `260417191096854`
- `steps` = `10`

## 知识

覆盖率 **73%**（11/15）

**有卡**：`LayerUtility: LoadJoyCaptionBeta1Model`、`VAELoader`、`EmptySD3LatentImage`、`ShowText|pysssss`、`CLIPTextEncodeFlux`、`ConditioningZeroOut`、`VAEDecode`、`KSampler`、`LayerUtility: JoyCaptionBeta1`、`SaveImage`、`LoadImage`

**缺卡**（2）：`LayerUtility: JoyCaptionBeta1`、`LayerUtility: LoadJoyCaptionBeta1Model`

## 学习发现

- 次要节点 `LayerUtility: JoyCaptionBeta1` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: LoadJoyCaptionBeta1Model` 知识库中没有该节点类型的任何知识
