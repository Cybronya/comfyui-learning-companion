---
name: unknown_workflow_video_147
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.768333
common_nodes: [CM_BoolBinaryOperation, CM_FloatBinaryCondition, CM_FloatBinaryOperation, CM_FloatToInt, CR Set Value On Boolean, GetImageSizeAndCount, GetNode, Image Comparer (rgthree), ImageFromBatch, ImpactCompare, ImpactFloat, Int, LayerUtility: PrintInfo, RIFE VFI, SetNode, Switch any [Crystools], VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, easy anythingIndexSwitch, easy anythingInversedSwitch, easy compare, easy imageSize, easy imageSizeBySide, easy showAnything]
problems: []
missing: []
members: [平台全量/视频-放大补帧-Astra 星光_2110232088627736577.json, 平台全量/视频-放大补帧-FlashVSR-wankj_1979575823420264449.json, 平台全量/视频-放大补帧-FlashVSR1.1-Smthem_1982480634318864386.json]
source: knowledge_consolidation
---

# unknown_workflow_video_147

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/视频-放大补帧-Astra 星光_2110232088627736577.json、平台全量/视频-放大补帧-FlashVSR-wankj_1979575823420264449.json、平台全量/视频-放大补帧-FlashVSR1.1-Smthem_1982480634318864386.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：77%

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
- `ImageConcatMulti` —— 2/3 个有
- `Astra` —— 1/3 个有
- `CreateVideo` —— 1/3 个有
- `FlashVSR_SM_KSampler` —— 1/3 个有
- `FlashVSR_SM_Model` —— 1/3 个有
- `GetVideoComponents` —— 1/3 个有
- `ImageScaleBy` —— 1/3 个有
- `LoadWanVideoT5TextEncoder` —— 1/3 个有
- `MathExpression|pysssss` —— 1/3 个有
- `MemoryCleaner` —— 1/3 个有
- `WanVideoAddFlashVSRInput` —— 1/3 个有
- `WanVideoDecode` —— 1/3 个有
- `WanVideoEmptyEmbeds` —— 1/3 个有
- `WanVideoExtraModelSelect` —— 1/3 个有
- `WanVideoFlashVSRDecoderLoader` —— 1/3 个有
- `WanVideoModelLoader` —— 1/3 个有
- `WanVideoSampler` —— 1/3 个有
- `WanVideoTextEncode` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6.3197e+08 | - | 1 | 100% |
| Prompt 约束强度(CFG) | randomize | - | 1 | 100% |
| 采样算法 | 2 | - | 1 | 100% |
| 调度器 | 3.5 | - | 1 | 100% |
| 重绘幅度 | 11 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 风险：采样步数 观测到 6.3197e+08，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
- 风险：重绘幅度 观测到 11，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
