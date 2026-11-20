---
name: unknown_workflow_video_lora_sampler_811
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.991
common_nodes: [CreateCFGScheduleFloatList, INTConstant, ImageResizeKJv2, LoadImage, SimpleMath+, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/Wan2.2 VACE 视频动作迁移_1979193024913772546.json, 平台全量/Wan2.2 VACE视频人物替换_1979515366428807170.json, 平台全量/Wan2.2-VACE视频物品重绘_1981639602450644994.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_811

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/Wan2.2 VACE 视频动作迁移_1979193024913772546.json、平台全量/Wan2.2 VACE视频人物替换_1979515366428807170.json、平台全量/Wan2.2-VACE视频物品重绘_1981639602450644994.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 3 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `ImageResizeKJv2`
- `LoadImage`
- `SimpleMath+`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageCompositeMasked` —— 2/3 个有
- `MaskToImage` —— 2/3 个有
- `SolidMask` —— 2/3 个有
- `DWPreprocessor` —— 1/3 个有
- `GrowMask` —— 1/3 个有
- `GrowMaskWithBlur` —— 1/3 个有
- `ImageFromBatch+` —— 1/3 个有
- `LayerMask: SAM2VideoUltra` —— 1/3 个有
- `LayerMask: SegmentAnythingUltra V2` —— 1/3 个有
- `PixelPerfectResolution` —— 1/3 个有
- `PointsEditor` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `SeCModelLoader` —— 1/3 个有
- `SeCVideoSegmentation` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
