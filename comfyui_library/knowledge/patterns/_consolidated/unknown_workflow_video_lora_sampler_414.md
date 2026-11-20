---
name: unknown_workflow_video_lora_sampler_414
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.948
common_nodes: [CreateCFGScheduleFloatList, GetImageSizeAndCount, GrowMaskWithBlur, INTConstant, ImageCompositeMasked, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, MaskToImage, SolidMask, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader, easy imageRemBg]
problems: []
missing: []
members: [平台全量/2.2Fun-VACE+视频角色替换+无限长度_1967853401608454146.json, 平台全量/wan2.2官方 VACE 视频人物替换 KJ版【推荐】_1967866150157713410.json, 视频生成/图生视频/Aiwood全网首发2.2Fun-VACE+Controlnet+视频角色替换+首尾帧_1966481669362495490.json, 视频生成/图生视频/Wan2.2-VACE首尾帧视频+动态参考+角色替换_1988214470772178945.json, 视频生成/图生视频/Wan2.2_Fun-VACE_首尾帧+动作控制+视频角色替换_1967688435714711553.json, 视频生成/图生视频/wan2.2官方 VACE 视频人物替换电商版3.0_1968972312815026177.json, 视频生成/图生视频/极简——KJ版 wan2.2模型VACE 视频人物替换_1968955207906385921.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_414

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（平台全量/2.2Fun-VACE+视频角色替换+无限长度_1967853401608454146.json、平台全量/wan2.2官方 VACE 视频人物替换 KJ版【推荐】_1967866150157713410.json、视频生成/图生视频/Aiwood全网首发2.2Fun-VACE+Controlnet+视频角色替换+首尾帧_1966481669362495490.json、视频生成/图生视频/Wan2.2-VACE首尾帧视频+动态参考+角色替换_1988214470772178945.json、视频生成/图生视频/Wan2.2_Fun-VACE_首尾帧+动作控制+视频角色替换_1967688435714711553.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 7 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `GetImageSizeAndCount`
- `GrowMaskWithBlur`
- `INTConstant`
- `ImageCompositeMasked`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MaskToImage`
- `SolidMask`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`
- `easy imageRemBg`

**可变部分**（部分 workflow 才有）：
- `ImageConcatMulti` —— 6/7 个有
- `WanVideoTorchCompileSettings` —— 6/7 个有
- `DownloadAndLoadSAM2Model` —— 4/7 个有
- `PointsEditor` —— 4/7 个有
- `PreviewImage` —— 4/7 个有
- `Sam2Segmentation` —— 4/7 个有
- `DWPreprocessor` —— 3/7 个有
- `ImageFromBatch+` —— 3/7 个有
- `ImpactInt` —— 3/7 个有
- `LayerMask: SAM2VideoUltra` —— 3/7 个有
- `LayerMask: SegmentAnythingUltra V2` —— 3/7 个有
- `PrimitiveInt` —— 3/7 个有
- `SimpleMath+` —— 3/7 个有
- `WanVideoVACEStartToEndFrame` —— 3/7 个有
- `CR Text` —— 2/7 个有
- `Anything Everywhere` —— 1/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有
- `Fast Groups Muter (rgthree)` —— 1/7 个有
- `GetNode` —— 1/7 个有
- `Label (rgthree)` —— 1/7 个有
- `Note Plus (mtb)` —— 1/7 个有
- `SetNode` —— 1/7 个有
- `WanVideoContextOptions` —— 1/7 个有
- `easy showAnything` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
