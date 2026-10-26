---
name: unknown_workflow_video_lora_sampler_353
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.725857
common_nodes: [CLIPVisionLoader, FantasyPortraitFaceDetector, FantasyPortraitModelLoader, ImageResizeKJv2, LoadImage, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddFantasyPortrait, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/FantasyPortrait音频驱动表情迁移-单人wan2.1_1956179221490094081.json, 视频生成/图生视频/FantasyPortrait音频驱动表情迁移-泛化版wan2.1_1956045555967381505.json, 视频生成/图生视频/FantasyPortrait音频驱动表情迁移-泛化版wan2.1_1956317081069342721.json, 视频生成/图生视频/FantasyPortrait音频驱动表情迁移-泛化版wan2.1_2051923749418610689.json, 视频生成/图生视频/FantasyPortrait音频驱动表情迁移-泛化版wan2.1_2052630555186999297.json, 视频生成/图生视频/wanvideo_2_1_I2V_FantasyPortrait_表情迁移_1957641914193473538.json, 视频生成/图生视频/【FantasyPortrait】复刻钟馗怒目圆睁表情_1958352739837362177.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_353

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/FantasyPortrait音频驱动表情迁移-单人wan2.1_1956179221490094081.json、视频生成/图生视频/FantasyPortrait音频驱动表情迁移-泛化版wan2.1_1956045555967381505.json、视频生成/图生视频/FantasyPortrait音频驱动表情迁移-泛化版wan2.1_1956317081069342721.json、视频生成/图生视频/FantasyPortrait音频驱动表情迁移-泛化版wan2.1_2051923749418610689.json、视频生成/图生视频/FantasyPortrait音频驱动表情迁移-泛化版wan2.1_2052630555186999297.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：73%

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
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoSetBlockSwap` —— 6/7 个有
- `WanVideoSetLoRAs` —— 6/7 个有
- `GetNode` —— 5/7 个有
- `SetNode` —— 5/7 个有
- `ImageConcatMulti` —— 4/7 个有
- `Primitive integer [Crystools]` —— 3/7 个有
- `INTConstant` —— 2/7 个有
- `ImageConcanate` —— 2/7 个有
- `PrimitiveInt` —— 2/7 个有
- `VHS_VideoInfoLoaded` —— 2/7 个有
- `WanVideoContextOptions` —— 2/7 个有
- `Any Switch (rgthree)` —— 1/7 个有
- `GetImageRangeFromBatch` —— 1/7 个有
- `Label (rgthree)` —— 1/7 个有
- `LandmarksToImage` —— 1/7 个有
- `PreviewImage` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
