---
name: unknown_workflow_video_lora_sampler_586
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.648667
common_nodes: [DWPreprocessor, GetImageSizeAndCount, GetNode, INTConstant, ImageConcatMulti, ImageResizeKJv2, LoadImage, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddControlEmbeds, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoEncode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoScheduler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/(KJ版)Wan2.2 Fun Control姿势控制加速版V1_1956358490119962626.json, 视频生成/图生视频/(KJ版)Wan2.2 Fun Control深度控制加速版V1_1956361346596130818.json, 视频生成/图生视频/Fun-Control动作迁移-KJ最新Wan2.2-Lightning版_1960740371133345793.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_586

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/(KJ版)Wan2.2 Fun Control姿势控制加速版V1_1956358490119962626.json、视频生成/图生视频/(KJ版)Wan2.2 Fun Control深度控制加速版V1_1956361346596130818.json、视频生成/图生视频/Fun-Control动作迁移-KJ最新Wan2.2-Lightning版_1960740371133345793.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：65%

## 共有节点

全部 3 个 workflow 都包含：
- `DWPreprocessor`
- `GetImageSizeAndCount`
- `GetNode`
- `INTConstant`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `LoadImage`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAddControlEmbeds`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoScheduler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 2/3 个有
- `CLIPTextEncode` —— 2/3 个有
- `CR Prompt Text` —— 2/3 个有
- `DepthAnything_V2` —— 2/3 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 2/3 个有
- `ImageConcanate` —— 2/3 个有
- `JWInteger` —— 2/3 个有
- `PDIMAGE_LongerSize` —— 2/3 个有
- `WanVideoTextEmbedBridge` —— 2/3 个有
- `CreateShapeImageOnPath` —— 1/3 个有
- `GetMaskSizeAndCount` —— 1/3 个有
- `ImageBlend` —— 1/3 个有
- `SplineEditor` —— 1/3 个有
- `Zoe-DepthMapPreprocessor` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
