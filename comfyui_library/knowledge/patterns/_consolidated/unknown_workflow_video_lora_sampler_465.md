---
name: unknown_workflow_video_lora_sampler_465
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.9045
common_nodes: [CreateCFGScheduleFloatList, GetImageSizeAndCount, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, Text Multiline]
members: [图片生成/文生图/1971322210470281217.json, 图片生成/文生图/FFGO：自定义Wan2.2视频内容，用视频首帧提高主角背景一致性_1995962307618488322.json, 视频生成/图生视频/1994305244540715009.json, 视频生成/图生视频/1993311574968434690.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_465

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/1971322210470281217.json、图片生成/文生图/FFGO：自定义Wan2.2视频内容，用视频首帧提高主角背景一致性_1995962307618488322.json、视频生成/图生视频/1994305244540715009.json、视频生成/图生视频/1993311574968434690.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 4 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AILab_ImageStitch` —— 3/4 个有
- `INTConstant` —— 3/4 个有
- `ImageFromBatch+` —— 3/4 个有
- `ImageStitch` —— 3/4 个有
- `RMBG` —— 3/4 个有
- `SaveImage` —— 3/4 个有
- `RH_Nano_Banana2_Image2Image` —— 2/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `Label (rgthree)` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/4 个有
- `RH_Nano_Banana_Image2Image` —— 1/4 个有
- `Text` —— 1/4 个有
- `Text Multiline` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2、Text Multiline
