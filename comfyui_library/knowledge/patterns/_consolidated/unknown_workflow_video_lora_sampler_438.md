---
name: unknown_workflow_video_lora_sampler_438
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.743714
common_nodes: [CLIPVisionLoader, FantasyPortraitFaceDetector, FantasyPortraitModelLoader, ImageResizeKJv2, LoadImage, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddFantasyPortrait, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/wanvideo_2_1_I2V_FantasyPortrait_表情迁移_1957329197184249857.json, 数字人/数字人/直播视频表情模仿_1956705772944986113.json, 数字人/数字人/表情迁移 - Wan2.1_1966784793595850754.json, 视频生成/图生视频/AniWan+FantasyPortrait高动态表情追踪动作迁移V1_1956272186195673089.json, 视频生成/图生视频/Fantasy Portrait+Wan2.2非常规表情动作迁移工作流V2_1956253904029798402.json, 视频生成/图生视频/Fantasy Portrait表情迁移-图片输入_1958414298089472002.json, 视频生成/图生视频/FantasyPortrait_表情迁移 WAN2.1工作流_1967251208723423233.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_438

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（数字人/数字人/wanvideo_2_1_I2V_FantasyPortrait_表情迁移_1957329197184249857.json、数字人/数字人/直播视频表情模仿_1956705772944986113.json、数字人/数字人/表情迁移 - Wan2.1_1966784793595850754.json、视频生成/图生视频/AniWan+FantasyPortrait高动态表情追踪动作迁移V1_1956272186195673089.json、视频生成/图生视频/Fantasy Portrait+Wan2.2非常规表情动作迁移工作流V2_1956253904029798402.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：74%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPVisionLoader`
- `FantasyPortraitFaceDetector`
- `FantasyPortraitModelLoader`
- `ImageResizeKJv2`
- `LoadImage`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAddFantasyPortrait`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 6/7 个有
- `INTConstant` —— 6/7 个有
- `SetNode` —— 6/7 个有
- `WanVideoTextEncodeCached` —— 6/7 个有
- `WanVideoTorchCompileSettings` —— 6/7 个有
- `ImageConcatMulti` —— 5/7 个有
- `WanVideoContextOptions` —— 4/7 个有
- `JWInteger` —— 2/7 个有
- `Anything Everywhere` —— 1/7 个有
- `CR Prompt Text` —— 1/7 个有
- `FloatToSigmas` —— 1/7 个有
- `ImageFromBatch+` —— 1/7 个有
- `LandmarksToImage` —— 1/7 个有
- `LoadWanVideoT5TextEncoder` —— 1/7 个有
- `PreviewImage` —— 1/7 个有
- `SimpleMath+` —— 1/7 个有
- `StringToFloatList` —— 1/7 个有
- `TrimVideoLatent` —— 1/7 个有
- `VHS_VideoInfo` —— 1/7 个有
- `WanVideoTextEncode` —— 1/7 个有
- `easy cleanGpuUsed` —— 1/7 个有
- `easy showAnything` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
