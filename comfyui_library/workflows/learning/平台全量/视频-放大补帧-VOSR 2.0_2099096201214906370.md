---
key: 平台全量/视频-放大补帧-VOSR 2.0_2099096201214906370.json
name: 视频-放大补帧-VOSR 2.0_2099096201214906370
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/视频-放大补帧-VOSR 2.0_2099096201214906370.json
hash: 4e0a46b2d059af0b
coverage: 0.764706
learned_at: 2026-11-14 02:34:21
nodes: [easy imageSize, GetImageSizeAndCount, LayerUtility: PrintInfo, easy showAnything, SetNode, VHS_VideoInfoLoaded, Note, Note, Note, easy showAnything, ImpactCompare, easy imageSizeBySide, GetImageSizeAndCount, CR Set Value On Boolean, RIFE VFI, CM_FloatBinaryCondition, CM_BoolBinaryOperation, easy showAnything, ImpactFloat, ImageFromBatch, ImageFromBatch, CR Set Value On Boolean, GetImageSizeAndCount, Image Comparer (rgthree), GetNode, CM_FloatBinaryOperation, Switch any [Crystools], CM_FloatBinaryCondition, CM_BoolBinaryOperation, SetNode, GetImageSizeAndCount, GetImageSizeAndCount, easy compare, GetImageSizeAndCount, VHS_VideoCombine, Note, Note, Int, Int, easy anythingIndexSwitch, GetImageSizeAndCount, VHS_LoadVideo, easy anythingInversedSwitch, ImpactFloat, CM_FloatToInt, CM_FloatToInt, VOSR2ModelLoader, easy anythingInversedSwitch, easy anythingIndexSwitch, GetImageSizeAndCount, VOSR2Upscale]
patterns: []
missing: []
---

# 平台全量/视频-放大补帧-VOSR 2.0_2099096201214906370.json

> 来源文件 `comfyui_library/workflows/平台全量/视频-放大补帧-VOSR 2.0_2099096201214906370.json`

## 结构

**生成流程**：Model → Process → Other

**节点**（51 个）：
- `easy imageSize`
- `GetImageSizeAndCount`
- `LayerUtility: PrintInfo`
- `easy showAnything`
- `SetNode`
- `VHS_VideoInfoLoaded`
- `Note`
- `Note`
- `Note`
- `easy showAnything`
- `ImpactCompare`
- `easy imageSizeBySide`
- `GetImageSizeAndCount`
- `CR Set Value On Boolean`
- `RIFE VFI`
- `CM_FloatBinaryCondition`
- `CM_BoolBinaryOperation`
- `easy showAnything`
- `ImpactFloat`
- `ImageFromBatch`
- `ImageFromBatch`
- `CR Set Value On Boolean`
- `GetImageSizeAndCount`
- `Image Comparer (rgthree)`
- `GetNode`
- `CM_FloatBinaryOperation`
- `Switch any [Crystools]`
- `CM_FloatBinaryCondition`
- `CM_BoolBinaryOperation`
- `SetNode`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `easy compare`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `Note`
- `Note`
- `Int`
- `Int`
- `easy anythingIndexSwitch`
- `GetImageSizeAndCount`
- `VHS_LoadVideo`
- `easy anythingInversedSwitch`
- `ImpactFloat`
- `CM_FloatToInt`
- `CM_FloatToInt`
- `VOSR2ModelLoader`
- `easy anythingInversedSwitch`
- `easy anythingIndexSwitch`
- `GetImageSizeAndCount`
- `VOSR2Upscale`

## 知识

覆盖率 **76%**（39/51）

**有卡**：`easy imageSize`、`GetImageSizeAndCount`、`LayerUtility: PrintInfo`、`VHS_VideoInfoLoaded`、`ImpactCompare`、`easy imageSizeBySide`、`CR Set Value On Boolean`、`RIFE VFI`、`CM_FloatBinaryCondition`、`CM_BoolBinaryOperation`、`ImpactFloat`、`ImageFromBatch`、`CM_FloatBinaryOperation`、`Switch any [Crystools]`、`easy compare`、`VHS_VideoCombine`、`Int`、`easy anythingIndexSwitch`、`VHS_LoadVideo`、`easy anythingInversedSwitch`、`CM_FloatToInt`、`VOSR2ModelLoader`、`VOSR2Upscale`

**用到的条目**：VOSR2Upscale、easy imageSize、easy imageSizeBySide、GetImageSizeAndCount、CM_BoolBinaryOperation、CM_FloatBinaryOperation、CM_FloatToInt、CR Set Value On Boolean
