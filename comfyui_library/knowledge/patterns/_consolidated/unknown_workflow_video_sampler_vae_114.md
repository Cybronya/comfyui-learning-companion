---
name: unknown_workflow_video_sampler_vae_114
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.729
common_nodes: [CM_IntToFloat, Fast Bypasser (rgthree), GetImageRangeFromBatch, Int, JjkText, LBMSampler, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadLBMModel, MathExpression|pysssss, RHHiddenNodes, RH_Translator, VHS_LoadVideo, VHS_VideoCombine, WanVideoApplyNAG, WanVideoBlockSwap, WanVideoDecode, WanVideoSampler, WanVideoTextEncodeSingle, WanVideoVACEEncode, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/WAN2.2 视频外扩_1959928047594057729.json, 平台全量/视频外扩_1957304317273370625.json, 平台全量/视频换主体_1956907566207832065.json, 平台全量/视频换背景_1957091072990175234.json, 平台全量/视频迁移＋对口型_1958243804514041857.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_114

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/WAN2.2 视频外扩_1959928047594057729.json、平台全量/视频外扩_1957304317273370625.json、平台全量/视频换主体_1956907566207832065.json、平台全量/视频换背景_1957091072990175234.json、平台全量/视频迁移＋对口型_1958243804514041857.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：73%

## 共有节点

全部 5 个 workflow 都包含：
- `CM_IntToFloat`
- `Fast Bypasser (rgthree)`
- `GetImageRangeFromBatch`
- `Int`
- `JjkText`
- `LBMSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadLBMModel`
- `MathExpression|pysssss`
- `RHHiddenNodes`
- `RH_Translator`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoApplyNAG`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoSampler`
- `WanVideoTextEncodeSingle`
- `WanVideoVACEEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Bjornulf_ShowInt` —— 4/5 个有
- `LayerMask: RemBgUltra` —— 4/5 个有
- `LayerUtility: ImageRemoveAlpha` —— 4/5 个有
- `RH_Captioner` —— 4/5 个有
- `GrowMask` —— 3/5 个有
- `InvertMask` —— 3/5 个有
- `LayerMask: SegmentAnythingUltra V2` —— 3/5 个有
- `LayerUtility: ImageOpacity` —— 3/5 个有
- `LoadImage` —— 3/5 个有
- `MaskBlur+` —— 3/5 个有
- `MaskToImage` —— 3/5 个有
- `PreviewImage` —— 3/5 个有
- `WanVideoImageResizeToClosest` —— 3/5 个有
- `ImagePadForOutpaintMasked` —— 2/5 个有
- `Pick From Batch (mtb)` —— 2/5 个有
- `PrimitiveInt` —— 2/5 个有
- `ImageCompositeMasked` —— 1/5 个有
- `ImpactSwitch` —— 1/5 个有
- `Masks Combine Regions` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
