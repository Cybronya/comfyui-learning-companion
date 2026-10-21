---
name: unknown_workflow_video_lora_sampler_479
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.938
common_nodes: [CreateCFGScheduleFloatList, INTConstant, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, PrimitiveInt, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVACEStartToEndFrame, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1966481669362495490.json, 视频生成/图生视频/1967843382921953282.json, 视频生成/图生视频/1988214470772178945.json, 视频生成/图生视频/1967688435714711553.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_479

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/1966481669362495490.json、视频生成/图生视频/1967843382921953282.json、视频生成/图生视频/1988214470772178945.json、视频生成/图生视频/1967688435714711553.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 4 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PrimitiveInt`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVACEStartToEndFrame`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `DWPreprocessor` —— 3/4 个有
- `DownloadAndLoadSAM2Model` —— 3/4 个有
- `GetImageSizeAndCount` —— 3/4 个有
- `GrowMaskWithBlur` —— 3/4 个有
- `ImageCompositeMasked` —— 3/4 个有
- `ImageConcatMulti` —— 3/4 个有
- `MaskToImage` —— 3/4 个有
- `PointsEditor` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `Sam2Segmentation` —— 3/4 个有
- `SolidMask` —— 3/4 个有
- `VHS_LoadVideo` —— 3/4 个有
- `VHS_VideoInfo` —— 3/4 个有
- `easy imageRemBg` —— 3/4 个有
- `Anything Everywhere` —— 1/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `Fast Groups Muter (rgthree)` —— 1/4 个有
- `GetNode` —— 1/4 个有
- `Label (rgthree)` —— 1/4 个有
- `SetNode` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
