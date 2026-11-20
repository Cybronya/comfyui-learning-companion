---
key: 平台全量/Seedance 2.0-首尾帧获取+视频高清修复_2021599529472106498.json
name: Seedance 2.0-首尾帧获取+视频高清修复_2021599529472106498
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Seedance 2.0-首尾帧获取+视频高清修复_2021599529472106498.json
hash: 5ba0db42bb5ad525
coverage: 0.9375
learned_at: 2026-11-14 01:00:15
nodes: [ImageFromBatch+, GetVideoComponents, GetVideoComponents, SaveVideo, LayerUtility: ImageScaleByAspectRatio V2, FlashVSR_SM_Model, CreateVideo, FlashVSR_SM_KSampler, GetImageSizeAndCount, ImageFromBatch+, ImageFromBatch+, SaveImage, SaveImage, LoadVideo, JWInteger, MarkdownNote]
patterns: []
missing: []
parameters: {"cfg": "randomize", "denoise": 11, "sampler_name": 2, "scheduler": 3.5, "seed": 1280, "steps": 1047454449}
---

# 平台全量/Seedance 2.0-首尾帧获取+视频高清修复_2021599529472106498.json

> 来源文件 `comfyui_library/workflows/平台全量/Seedance 2.0-首尾帧获取+视频高清修复_2021599529472106498.json`

## 结构

**生成流程**：Sampling → Process → Output → Other

**节点**（16 个）：
- `ImageFromBatch+`
- `GetVideoComponents`
- `GetVideoComponents`
- `SaveVideo`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `FlashVSR_SM_Model`
- `CreateVideo`
- `FlashVSR_SM_KSampler` ★核心
- `GetImageSizeAndCount`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `SaveImage`
- `SaveImage`
- `LoadVideo`
- `JWInteger`
- `MarkdownNote`

## 关键参数

- `seed` = `1280`
- `steps` = `1047454449`
- `cfg` = `randomize`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`

## 知识

覆盖率 **94%**（15/16）

**有卡**：`ImageFromBatch+`、`GetVideoComponents`、`SaveVideo`、`LayerUtility: ImageScaleByAspectRatio V2`、`FlashVSR_SM_Model`、`CreateVideo`、`FlashVSR_SM_KSampler`、`GetImageSizeAndCount`、`SaveImage`、`LoadVideo`、`JWInteger`

**用到的条目**：FlashVSR_SM_KSampler、GetImageSizeAndCount、SaveImage、SaveVideo、CreateVideo、FlashVSR_SM_Model、GetVideoComponents、ImageFromBatch+
