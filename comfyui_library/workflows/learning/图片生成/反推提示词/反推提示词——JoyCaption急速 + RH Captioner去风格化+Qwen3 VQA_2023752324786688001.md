---
key: 图片生成/反推提示词/反推提示词——JoyCaption急速 + RH Captioner去风格化+Qwen3 VQA_2023752324786688001.json
name: 反推提示词——JoyCaption急速 + RH Captioner去风格化+Qwen3 VQA_2023752324786688001
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/反推提示词——JoyCaption急速 + RH Captioner去风格化+Qwen3 VQA_2023752324786688001.json
hash: 5321b2c5a5f5049b
coverage: 0.555556
learned_at: 2026-10-26 01:47:39
nodes: [PreviewAny, Note, SetNode, LayerUtility: JoyCaptionBeta1, GetNode, GetNode, AnySwitch, Qwen3_VQA_Plus, easy positive, PreviewAny, RH_Captioner, Fast Bypasser (rgthree), PreviewAny, Fast Groups Bypasser (rgthree), LayerUtility: LoadJoyCaptionBeta1Model, LoadImage, SaveImage, Qwen3_VQA_Plus]
patterns: []
missing: []
---

# 图片生成/反推提示词/反推提示词——JoyCaption急速 + RH Captioner去风格化+Qwen3 VQA_2023752324786688001.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/反推提示词——JoyCaption急速 + RH Captioner去风格化+Qwen3 VQA_2023752324786688001.json`

## 结构

**生成流程**：Output → Other

**节点**（18 个）：
- `PreviewAny`
- `Note`
- `SetNode`
- `LayerUtility: JoyCaptionBeta1`
- `GetNode`
- `GetNode`
- `AnySwitch`
- `Qwen3_VQA_Plus`
- `easy positive`
- `PreviewAny`
- `RH_Captioner`
- `Fast Bypasser (rgthree)`
- `PreviewAny`
- `Fast Groups Bypasser (rgthree)`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `LoadImage`
- `SaveImage`
- `Qwen3_VQA_Plus`

## 知识

覆盖率 **56%**（10/18）

**有卡**：`LayerUtility: JoyCaptionBeta1`、`AnySwitch`、`Qwen3_VQA_Plus`、`easy positive`、`RH_Captioner`、`Fast Bypasser (rgthree)`、`LayerUtility: LoadJoyCaptionBeta1Model`、`LoadImage`、`SaveImage`

**用到的条目**：LoadImage、SaveImage、AnySwitch、Qwen3_VQA_Plus、RH_Captioner、easy positive、Fast Bypasser (rgthree)、LayerUtility: JoyCaptionBeta1
