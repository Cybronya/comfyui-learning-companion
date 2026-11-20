---
name: unknown_workflow_video_148
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.76
common_nodes: [CM_BoolBinaryOperation, CM_FloatBinaryCondition, CM_FloatBinaryOperation, CM_FloatToInt, CR Set Value On Boolean, GetImageSizeAndCount, GetNode, Image Comparer (rgthree), ImageFromBatch, ImpactCompare, ImpactFloat, Int, LayerUtility: PrintInfo, RIFE VFI, SetNode, Switch any [Crystools], VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, easy anythingIndexSwitch, easy anythingInversedSwitch, easy compare, easy imageSize, easy imageSizeBySide, easy showAnything]
problems: []
missing: []
members: [平台全量/视频-放大补帧-VOSR 2.0_2099096201214906370.json, 平台全量/视频-放大补帧-VideoUpScale_1973368359997845506.json, 平台全量/视频-放大补帧极速-RTX Video Super_2084956355777093633.json]
source: knowledge_consolidation
---

# unknown_workflow_video_148

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/视频-放大补帧-VOSR 2.0_2099096201214906370.json、平台全量/视频-放大补帧-VideoUpScale_1973368359997845506.json、平台全量/视频-放大补帧极速-RTX Video Super_2084956355777093633.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：76%

## 共有节点

全部 3 个 workflow 都包含：
- `CM_BoolBinaryOperation`
- `CM_FloatBinaryCondition`
- `CM_FloatBinaryOperation`
- `CM_FloatToInt`
- `CR Set Value On Boolean`
- `GetImageSizeAndCount`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageFromBatch`
- `ImpactCompare`
- `ImpactFloat`
- `Int`
- `LayerUtility: PrintInfo`
- `RIFE VFI`
- `SetNode`
- `Switch any [Crystools]`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `easy anythingIndexSwitch`
- `easy anythingInversedSwitch`
- `easy compare`
- `easy imageSize`
- `easy imageSizeBySide`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Video_Upscale_With_Model` —— 2/3 个有
- `RTXVideoSuperResolution` —— 1/3 个有
- `VOSR2ModelLoader` —— 1/3 个有
- `VOSR2Upscale` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
