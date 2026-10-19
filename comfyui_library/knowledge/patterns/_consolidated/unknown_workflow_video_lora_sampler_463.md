---
name: unknown_workflow_video_lora_sampler_463
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.887
common_nodes: [CreateCFGScheduleFloatList, GetImageSizeAndCount, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, Text Multiline]
members: [图片生成/文生图/1971322210470281217.json, 视频生成/图生视频/1952544816922071041.json, 视频生成/图生视频/1975384215250448386.json, 视频生成/图生视频/2053486047740350466.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_463

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/1971322210470281217.json、视频生成/图生视频/1952544816922071041.json、视频生成/图生视频/1975384215250448386.json、视频生成/图生视频/2053486047740350466.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 4 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `GetImageSizeAndCount`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
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
- `INTConstant` —— 3/4 个有
- `ImageResizeKJv2` —— 3/4 个有
- `Fast Groups Bypasser (rgthree)` —— 2/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `easy seed` —— 2/4 个有
- `Label (rgthree)` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `RH_Nano_Banana_Image2Image` —— 1/4 个有
- `RIFE VFI` —— 1/4 个有
- `SaveImage` —— 1/4 个有
- `Seed (rgthree)` —— 1/4 个有
- `Text` —— 1/4 个有
- `Text Multiline` —— 1/4 个有
- `WanVideoTeaCache` —— 1/4 个有
- `easy int` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2、Text Multiline
