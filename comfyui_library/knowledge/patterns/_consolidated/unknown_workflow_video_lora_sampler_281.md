---
name: unknown_workflow_video_lora_sampler_281
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.7702
common_nodes: [CLIPVisionLoader, FantasyPortraitFaceDetector, FantasyPortraitModelLoader, ImageResizeKJv2, LoadImage, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddFantasyPortrait, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/FantasyPortrait音频驱动表情迁移-单人wan2.1_1956020151047127042.json, 视频生成/图生视频/FantasyPortrait音频驱动表情迁移-单人wan2.1_1956179221490094081.json, 视频生成/图生视频/FantasyPortrait音频驱动表情迁移-多人wan2.1_1956036782594904065.json, 视频生成/图生视频/FantasyPortrait音频驱动表情迁移-泛化版wan2.1_1956045555967381505.json, 视频生成/图生视频/FantasyPortrait音频驱动表情迁移-泛化版wan2.1_1956317081069342721.json, 视频生成/图生视频/FantasyPortrait音频驱动表情迁移-泛化版wan2.1_2051923749418610689.json, 视频生成/图生视频/FantasyPortrait音频驱动表情迁移-泛化版wan2.1_2052630555186999297.json, 视频生成/图生视频/Wan2.1+FantasyPortrait表情动作迁移V1_1956269991735775234.json, 视频生成/图生视频/wanvideo_2_1_I2V_FantasyPortrait_表情迁移_1957641914193473538.json, 视频生成/图生视频/最新FantasyPortrait音频驱动表情迁移_1956951532585541633.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_281

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/FantasyPortrait音频驱动表情迁移-单人wan2.1_1956020151047127042.json、视频生成/图生视频/FantasyPortrait音频驱动表情迁移-单人wan2.1_1956179221490094081.json、视频生成/图生视频/FantasyPortrait音频驱动表情迁移-多人wan2.1_1956036782594904065.json、视频生成/图生视频/FantasyPortrait音频驱动表情迁移-泛化版wan2.1_1956045555967381505.json、视频生成/图生视频/FantasyPortrait音频驱动表情迁移-泛化版wan2.1_1956317081069342721.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 10 个 workflow 都包含：
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
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoTorchCompileSettings` —— 9/10 个有
- `ImageConcatMulti` —— 8/10 个有
- `GetNode` —— 6/10 个有
- `Primitive integer [Crystools]` —— 6/10 个有
- `SetNode` —— 6/10 个有
- `INTConstant` —— 3/10 个有
- `ImageConcanate` —— 2/10 个有
- `PrimitiveInt` —— 2/10 个有
- `VHS_VideoInfoLoaded` —— 2/10 个有
- `GetImageRangeFromBatch` —— 1/10 个有
- `JWInteger` —— 1/10 个有
- `LayerUtility: PurgeVRAM V2` —— 1/10 个有
- `PreviewImage` —— 1/10 个有
- `VHS_VideoInfo` —— 1/10 个有
- `WanVideoContextOptions` —— 1/10 个有
- `easy cleanGpuUsed` —— 1/10 个有
- `easy showAnything` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
