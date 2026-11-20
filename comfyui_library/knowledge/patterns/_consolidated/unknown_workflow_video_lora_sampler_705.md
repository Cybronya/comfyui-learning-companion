---
name: unknown_workflow_video_lora_sampler_705
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.63825
common_nodes: [DWPreprocessor, GetImageSizeAndCount, GetNode, INTConstant, ImageConcatMulti, ImageResizeKJv2, LoadImage, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddControlEmbeds, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoEncode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoScheduler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/（KJ版）Wan Fun Control视频洗稿工作流V1_1956347988744523778.json, 视频生成/图生视频/(KJ版)Wan2.2 Fun Control姿势控制加速版V1_1956358490119962626.json, 视频生成/图生视频/(KJ版)Wan2.2 Fun Control深度控制加速版V1_1956361346596130818.json, 视频生成/图生视频/Fun-Control动作迁移-KJ最新Wan2.2-Lightning版_1960740371133345793.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_705

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/（KJ版）Wan Fun Control视频洗稿工作流V1_1956347988744523778.json、视频生成/图生视频/(KJ版)Wan2.2 Fun Control姿势控制加速版V1_1956358490119962626.json、视频生成/图生视频/(KJ版)Wan2.2 Fun Control深度控制加速版V1_1956361346596130818.json、视频生成/图生视频/Fun-Control动作迁移-KJ最新Wan2.2-Lightning版_1960740371133345793.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：64%

## 共有节点

全部 4 个 workflow 都包含：
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
- `CR Prompt Text` —— 3/4 个有
- `DepthAnything_V2` —— 3/4 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 3/4 个有
- `JWInteger` —— 3/4 个有
- `CLIPLoader` —— 2/4 个有
- `CLIPTextEncode` —— 2/4 个有
- `ImageConcanate` —— 2/4 个有
- `PDIMAGE_LongerSize` —— 2/4 个有
- `WanVideoTextEmbedBridge` —— 2/4 个有
- `CreateShapeImageOnPath` —— 1/4 个有
- `GetMaskSizeAndCount` —— 1/4 个有
- `ImageBlend` —— 1/4 个有
- `SplineEditor` —— 1/4 个有
- `Zoe-DepthMapPreprocessor` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
