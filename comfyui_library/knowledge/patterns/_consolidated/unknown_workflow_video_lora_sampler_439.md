---
name: unknown_workflow_video_lora_sampler_439
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9502
common_nodes: [INTConstant, LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1962882725575364609.json, 视频生成/图生视频/1972581199266906114.json, 视频生成/图生视频/1962483006248235010.json, 视频生成/图生视频/1961798280172781569.json, 视频生成/文生视频/1962914848373968898.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_439

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/1962882725575364609.json、视频生成/图生视频/1972581199266906114.json、视频生成/图生视频/1962483006248235010.json、视频生成/图生视频/1961798280172781569.json、视频生成/文生视频/1962914848373968898.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 5 个 workflow 都包含：
- `INTConstant`
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `JWInteger` —— 4/5 个有
- `ImageResize+` —— 3/5 个有
- `WanVideoApplyNAG` —— 3/5 个有
- `CreateCFGScheduleFloatList` —— 2/5 个有
- `GetImageSizeAndCount` —— 2/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/5 个有
- `LayerUtility: PurgeVRAM` —— 2/5 个有
- `WanVideoTorchCompileSettings` —— 2/5 个有
- `ImageResizeKJv2` —— 1/5 个有
- `LayerUtility: ImageScaleRestore V2` —— 1/5 个有
- `SaveImage` —— 1/5 个有
- `TT_img_enc` —— 1/5 个有
- `Textbox` —— 1/5 个有
- `WanVideoLoraBlockEdit` —— 1/5 个有
- `easy seed` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
