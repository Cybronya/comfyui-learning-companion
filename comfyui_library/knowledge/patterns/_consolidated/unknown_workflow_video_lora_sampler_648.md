---
name: unknown_workflow_video_lora_sampler_648
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.58225
common_nodes: [GetImageSizeAndCount, GetNode, JjkText, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, Primitive integer [Crystools], SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoMagCache, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/首尾帧-FusionX_VACE_放大_补帧_1933343489382096898.json, 平台全量/一键图转2K高清动态壁纸 +旋转_1984282159491989505.json, 平台全量/姿态模仿-FusionX_VACE_1935209988690477058.json, 视频生成/图生视频/一键将图像转换为2K高清动态壁纸_1930433955672264705.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_648

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/首尾帧-FusionX_VACE_放大_补帧_1933343489382096898.json、平台全量/一键图转2K高清动态壁纸 +旋转_1984282159491989505.json、平台全量/姿态模仿-FusionX_VACE_1935209988690477058.json、视频生成/图生视频/一键将图像转换为2K高清动态壁纸_1930433955672264705.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：58%

## 共有节点

全部 4 个 workflow 都包含：
- `GetImageSizeAndCount`
- `GetNode`
- `JjkText`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `Primitive integer [Crystools]`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoMagCache`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere3` —— 3/4 个有
- `LoadAudio` —— 3/4 个有
- `RIFE VFI` —— 3/4 个有
- `SimpleMath+` —— 3/4 个有
- `TextCombinerTwo` —— 3/4 个有
- `Video_Upscale_With_Model` —— 3/4 个有
- `WanVideoVACEStartToEndFrame` —— 3/4 个有
- `easy showAnything` —— 3/4 个有
- `RH_Captioner` —— 2/4 个有
- `RH_Prompter` —— 2/4 个有
- `Anything Everywhere` —— 1/4 个有
- `DWPreprocessor` —— 1/4 个有
- `ImageBlend` —— 1/4 个有
- `ImageFromBatch+` —— 1/4 个有
- `ImageListToImageBatch` —— 1/4 个有
- `ImageResizeKJv2` —— 1/4 个有
- `ImageScale` —— 1/4 个有
- `ImpactImageBatchToImageList` —— 1/4 个有
- `LayerUtility: PurgeVRAM` —— 1/4 个有
- `ReActorFaceSwap` —— 1/4 个有
- `VHS_LoadVideo` —— 1/4 个有
- `VHS_VideoInfo` —— 1/4 个有
- `WanVideoTorchCompileSettings` —— 1/4 个有
- `Zoe-DepthMapPreprocessor` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
