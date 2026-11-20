---
key: 平台全量/FlashVSR高清放大+插帧 工作流最新版 林耀4.12_2043252298549301249.json
name: FlashVSR高清放大+插帧 工作流最新版 林耀4.12_2043252298549301249
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/FlashVSR高清放大+插帧 工作流最新版 林耀4.12_2043252298549301249.json
hash: 2b8c998fe646234f
coverage: 1
learned_at: 2026-11-14 00:27:15
nodes: [JWInteger, GetVideoComponents, GetVideoComponents, ImageFromBatch+, LayerUtility: ImageScaleByAspectRatio V2, FlashVSR_SM_Model, LoadVideo, JWInteger, FlashVSR_SM_KSampler, CreateVideo, RIFE VFI, MathExpression_UTK, SaveVideo, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": "randomize", "denoise": 11, "sampler_name": 2, "scheduler": 3.5, "seed": 1280, "steps": 384961141}
---

# 平台全量/FlashVSR高清放大+插帧 工作流最新版 林耀4.12_2043252298549301249.json

> 来源文件 `comfyui_library/workflows/平台全量/FlashVSR高清放大+插帧 工作流最新版 林耀4.12_2043252298549301249.json`

## 结构

**生成流程**：Sampling → Process → Output → Other

**节点**（14 个）：
- `JWInteger`
- `GetVideoComponents`
- `GetVideoComponents`
- `ImageFromBatch+`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `FlashVSR_SM_Model`
- `LoadVideo`
- `JWInteger`
- `FlashVSR_SM_KSampler` ★核心
- `CreateVideo`
- `RIFE VFI`
- `MathExpression_UTK`
- `SaveVideo`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `1280`
- `steps` = `384961141`
- `cfg` = `randomize`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`

## 知识

覆盖率 **100%**（14/14）

**有卡**：`JWInteger`、`GetVideoComponents`、`ImageFromBatch+`、`LayerUtility: ImageScaleByAspectRatio V2`、`FlashVSR_SM_Model`、`LoadVideo`、`FlashVSR_SM_KSampler`、`CreateVideo`、`RIFE VFI`、`MathExpression_UTK`、`SaveVideo`、`VHS_VideoCombine`

**用到的条目**：FlashVSR_SM_KSampler、SaveVideo、CreateVideo、FlashVSR_SM_Model、GetVideoComponents、ImageFromBatch+、JWInteger、LayerUtility: ImageScaleByAspectRatio V2
