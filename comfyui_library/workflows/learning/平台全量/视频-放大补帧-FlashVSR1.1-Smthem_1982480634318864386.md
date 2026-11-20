---
key: 平台全量/视频-放大补帧-FlashVSR1.1-Smthem_1982480634318864386.json
name: 视频-放大补帧-FlashVSR1.1-Smthem_1982480634318864386
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/视频-放大补帧-FlashVSR1.1-Smthem_1982480634318864386.json
hash: d36216e5824eafec
coverage: 0.745763
learned_at: 2026-11-14 02:34:20
nodes: [easy imageSize, LayerUtility: PrintInfo, easy showAnything, VHS_VideoInfoLoaded, Note, Note, Note, easy showAnything, ImpactCompare, easy imageSizeBySide, easy anythingIndexSwitch, easy anythingIndexSwitch, CR Set Value On Boolean, CM_FloatBinaryCondition, CM_BoolBinaryOperation, easy showAnything, ImpactFloat, ImageFromBatch, ImageFromBatch, GetImageSizeAndCount, easy anythingInversedSwitch, GetImageSizeAndCount, CR Set Value On Boolean, easy anythingInversedSwitch, GetImageSizeAndCount, Image Comparer (rgthree), CM_FloatBinaryOperation, Switch any [Crystools], CM_FloatBinaryCondition, CM_BoolBinaryOperation, GetImageSizeAndCount, GetImageSizeAndCount, easy compare, GetImageSizeAndCount, VHS_VideoCombine, Note, Note, Int, Int, ImageConcatMulti, SetNode, SetNode, GetNode, GetImageSizeAndCount, CM_FloatToInt, VHS_VideoCombine, ImpactFloat, FlashVSR_SM_KSampler, GetImageSizeAndCount, easy showAnything, easy showAnything, GetImageSizeAndCount, GetNode, CM_FloatToInt, FlashVSR_SM_Model, RIFE VFI, VHS_LoadVideo, MemoryCleaner, GetImageSizeAndCount]
patterns: []
missing: []
parameters: {"cfg": "randomize", "denoise": 11, "sampler_name": 2, "scheduler": 3.5, "seed": 1280, "steps": 631970344}
---

# 平台全量/视频-放大补帧-FlashVSR1.1-Smthem_1982480634318864386.json

> 来源文件 `comfyui_library/workflows/平台全量/视频-放大补帧-FlashVSR1.1-Smthem_1982480634318864386.json`

## 结构

**生成流程**：Sampling → Process → Other

**节点**（59 个）：
- `easy imageSize`
- `LayerUtility: PrintInfo`
- `easy showAnything`
- `VHS_VideoInfoLoaded`
- `Note`
- `Note`
- `Note`
- `easy showAnything`
- `ImpactCompare`
- `easy imageSizeBySide`
- `easy anythingIndexSwitch`
- `easy anythingIndexSwitch`
- `CR Set Value On Boolean`
- `CM_FloatBinaryCondition`
- `CM_BoolBinaryOperation`
- `easy showAnything`
- `ImpactFloat`
- `ImageFromBatch`
- `ImageFromBatch`
- `GetImageSizeAndCount`
- `easy anythingInversedSwitch`
- `GetImageSizeAndCount`
- `CR Set Value On Boolean`
- `easy anythingInversedSwitch`
- `GetImageSizeAndCount`
- `Image Comparer (rgthree)`
- `CM_FloatBinaryOperation`
- `Switch any [Crystools]`
- `CM_FloatBinaryCondition`
- `CM_BoolBinaryOperation`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `easy compare`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `Note`
- `Note`
- `Int`
- `Int`
- `ImageConcatMulti`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `CM_FloatToInt`
- `VHS_VideoCombine`
- `ImpactFloat`
- `FlashVSR_SM_KSampler` ★核心
- `GetImageSizeAndCount`
- `easy showAnything`
- `easy showAnything`
- `GetImageSizeAndCount`
- `GetNode`
- `CM_FloatToInt`
- `FlashVSR_SM_Model`
- `RIFE VFI`
- `VHS_LoadVideo`
- `MemoryCleaner`
- `GetImageSizeAndCount`

## 关键参数

- `seed` = `1280`
- `steps` = `631970344`
- `cfg` = `randomize`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`

## 知识

覆盖率 **75%**（44/59）

**有卡**：`easy imageSize`、`LayerUtility: PrintInfo`、`VHS_VideoInfoLoaded`、`ImpactCompare`、`easy imageSizeBySide`、`easy anythingIndexSwitch`、`CR Set Value On Boolean`、`CM_FloatBinaryCondition`、`CM_BoolBinaryOperation`、`ImpactFloat`、`ImageFromBatch`、`GetImageSizeAndCount`、`easy anythingInversedSwitch`、`CM_FloatBinaryOperation`、`Switch any [Crystools]`、`easy compare`、`VHS_VideoCombine`、`Int`、`ImageConcatMulti`、`CM_FloatToInt`、`FlashVSR_SM_KSampler`、`FlashVSR_SM_Model`、`RIFE VFI`、`VHS_LoadVideo`、`MemoryCleaner`

**用到的条目**：FlashVSR_SM_KSampler、easy imageSize、easy imageSizeBySide、GetImageSizeAndCount、CM_BoolBinaryOperation、CM_FloatBinaryOperation、CM_FloatToInt、CR Set Value On Boolean
