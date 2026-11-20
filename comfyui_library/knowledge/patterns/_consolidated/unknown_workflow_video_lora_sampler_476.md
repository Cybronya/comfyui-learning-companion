---
name: unknown_workflow_video_lora_sampler_476
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.734833
common_nodes: [CR Text, CreateCFGScheduleFloatList, GetNode, ImageResizeKJ, ImpactSwitch, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoScheduler, WanVideoSetBlockSwap, WanVideoSigmaToStep, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/Wan2.2 Fun VACE 多图融合_1966783248779128833.json, 图片生成/图生图/Wan2.2 Fun VACE 首尾帧_1966773011640692738.json, 平台全量/Wan2.2-Vace-姿势_深度参考转绘_1983820329074270209.json, 视频生成/图生视频/Wan2.2 Fun VACE 姿势深度参考转绘_1966804556082556930.json, 视频生成/图生视频/视频人物替换 Wan2.2  24G显存可以跑_1966922362283233281.json, 视频生成/图生视频/通义万相wan2.2Fun VACE视频转绘（美女跳舞姿势参考）_1967206218295074817.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_476

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Wan2.2 Fun VACE 多图融合_1966783248779128833.json、图片生成/图生图/Wan2.2 Fun VACE 首尾帧_1966773011640692738.json、平台全量/Wan2.2-Vace-姿势_深度参考转绘_1983820329074270209.json、视频生成/图生视频/Wan2.2 Fun VACE 姿势深度参考转绘_1966804556082556930.json、视频生成/图生视频/视频人物替换 Wan2.2  24G显存可以跑_1966922362283233281.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：73%

## 共有节点

全部 6 个 workflow 都包含：
- `CR Text`
- `CreateCFGScheduleFloatList`
- `GetNode`
- `ImageResizeKJ`
- `ImpactSwitch`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoScheduler`
- `WanVideoSetBlockSwap`
- `WanVideoSigmaToStep`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 5/6 个有
- `PreviewImage` —— 5/6 个有
- `AIO_Preprocessor` —— 4/6 个有
- `AddLabel` —— 4/6 个有
- `DepthAnything_V2` —— 4/6 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 4/6 个有
- `EmptyImage` —— 4/6 个有
- `ImageConcatMulti` —— 4/6 个有
- `VHS_LoadVideo` —— 4/6 个有
- `VHS_VideoInfo` —— 4/6 个有
- `Primitive integer [Crystools]` —— 3/6 个有
- `ImageConcanate` —— 2/6 个有
- `MathExpression|pysssss` —— 2/6 个有
- `RH_LLMAPI_NODE` —— 2/6 个有
- `ImageResizeKJv2` —— 1/6 个有
- `InspyrenetRembg` —— 1/6 个有
- `LayerUtility: ImageRemoveAlpha` —— 1/6 个有
- `WanVideoVACEStartToEndFrame` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有
- `easy showAnything` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
