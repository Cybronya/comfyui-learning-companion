---
name: unknown_workflow_video_lora_sampler_738
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 1
common_nodes: [ImageFromBatch+, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/wan2.2图生视频kj版_1950852674944180226.json, 视频生成/图生视频/wan2.2图生视频kj版_1978672767467982850.json, 视频生成/图生视频/【KJ加速版】Wan2.2 图生视频_1953401583553925122.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_738

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/wan2.2图生视频kj版_1950852674944180226.json、视频生成/图生视频/wan2.2图生视频kj版_1978672767467982850.json、视频生成/图生视频/【KJ加速版】Wan2.2 图生视频_1953401583553925122.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 3 个 workflow 都包含：
- `ImageFromBatch+`
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
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `Text` —— 2/3 个有
- `CLIPVisionLoader` —— 1/3 个有
- `CR Text` —— 1/3 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/3 个有
- `GIMMVFI_interpolate` —— 1/3 个有
- `GetImageSizeAndCount` —— 1/3 个有
- `WanVideoClipVisionEncode` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
