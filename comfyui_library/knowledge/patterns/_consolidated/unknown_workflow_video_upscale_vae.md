---
name: unknown_workflow_video_upscale_vae
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.53625
common_nodes: [1hew_SaveVideo, CR Prompt Text, DF_Integer, GetNode, LayerUtility: PurgeVRAM, LoadImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoSource]
problems: []
missing: []
members: [视频生成/图生视频/多图（最多支持9张）+文生视频happyhorse 1.0_2049414589812580354.json, 视频生成/图生视频/超强Happyhorse1.0 快乐马图生视频+放大工作流_2048771078763323394.json, 视频生成/文生视频/真香！多图（最多支持9张）+文生视频Seedance2.0 Fast_2047909181948174338.json, 视频生成/文生视频/赞！Happyhorse1.0 快乐马文+图生视频（视频1080_2K_4K放大）_2049126884318912513.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_vae

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/多图（最多支持9张）+文生视频happyhorse 1.0_2049414589812580354.json、视频生成/图生视频/超强Happyhorse1.0 快乐马图生视频+放大工作流_2048771078763323394.json、视频生成/文生视频/真香！多图（最多支持9张）+文生视频Seedance2.0 Fast_2047909181948174338.json、视频生成/文生视频/赞！Happyhorse1.0 快乐马文+图生视频（视频1080_2K_4K放大）_2049126884318912513.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：54%

## 共有节点

全部 4 个 workflow 都包含：
- `1hew_SaveVideo`
- `CR Prompt Text`
- `DF_Integer`
- `GetNode`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoSource`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `RH_AlibabaHappyhorse10ImageToVideo` —— 2/4 个有
- `Fast Groups Muter (rgthree)` —— 1/4 个有
- `JjkText` —— 1/4 个有
- `RH_AlibabaHappyhorse10ReferenceToVideo` —— 1/4 个有
- `RH_AlibabaHappyhorse10TextToVideo` —— 1/4 个有
- `RH_BytedanceSeedance20GlobalFastMultimodalVideo` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
