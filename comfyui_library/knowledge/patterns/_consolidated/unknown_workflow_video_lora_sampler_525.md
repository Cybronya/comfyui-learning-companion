---
name: unknown_workflow_video_lora_sampler_525
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.94125
common_nodes: [CR Text, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/1950372019490701313.json, 视频生成/图生视频/1949993851035541506.json, 视频生成/图生视频/1950068834109710337.json, 视频生成/图生视频/1957349808384176130.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_525

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/1950372019490701313.json、视频生成/图生视频/1949993851035541506.json、视频生成/图生视频/1950068834109710337.json、视频生成/图生视频/1957349808384176130.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 4 个 workflow 都包含：
- `CR Text`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 3/4 个有
- `PrimitiveInt` —— 3/4 个有
- `WanVideoApplyNAG` —— 3/4 个有
- `WanVideoSetBlockSwap` —— 3/4 个有
- `WanVideoSetLoRAs` —— 3/4 个有
- `WanVideoTextEncodeSingle` —— 3/4 个有
- `CR SDXL Aspect Ratio` —— 2/4 个有
- `DownloadAndLoadGIMMVFIModel` —— 2/4 个有
- `GIMMVFI_interpolate` —— 2/4 个有
- `GetImageSizeAndCount` —— 2/4 个有
- `SimpleMath+` —— 2/4 个有
- `ADE_CameraPoseBasic` —— 1/4 个有
- `NumberClamp` —— 1/4 个有
- `Primitive integer [Crystools]` —— 1/4 个有
- `SeedVR2` —— 1/4 个有
- `SeedVR2BlockSwap` —— 1/4 个有
- `WanVideoFunCameraEmbeds` —— 1/4 个有
- `WanVideoLoraSelectMulti` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
