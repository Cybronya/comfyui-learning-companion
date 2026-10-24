---
name: unknown_workflow_video_lora_sampler_133
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.73775
common_nodes: [CLIPVisionLoader, FantasyPortraitFaceDetector, FantasyPortraitModelLoader, ImageResizeKJv2, LoadImage, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddFantasyPortrait, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Fantasy Portrait表情迁移-图片输入_1958414298089472002.json, 视频生成/图生视频/FantasyPortrait_表情迁移 WAN2.1工作流_1967251208723423233.json, 视频生成/图生视频/FantasyPortrait音频驱动表情迁移-单人wan2.1_1956020151047127042.json, 视频生成/图生视频/FantasyPortrait音频驱动表情迁移-单人wan2.1_1956179221490094081.json, 视频生成/图生视频/FantasyPortrait音频驱动表情迁移-多人wan2.1_1956036782594904065.json, 视频生成/图生视频/FantasyPortrait音频驱动表情迁移-泛化版wan2.1_1956045555967381505.json, 视频生成/图生视频/FantasyPortrait音频驱动表情迁移-泛化版wan2.1_1956317081069342721.json, 视频生成/图生视频/FantasyPortrait音频驱动表情迁移-泛化版wan2.1_2051923749418610689.json, 视频生成/图生视频/FantasyPortrait音频驱动表情迁移-泛化版wan2.1_2052630555186999297.json, 视频生成/图生视频/wanvideo_2_1_I2V_FantasyPortrait_表情迁移_1957641914193473538.json, 视频生成/图生视频/【FantasyPortrait】复刻钟馗怒目圆睁表情_1958352739837362177.json, 视频生成/图生视频/最新FantasyPortrait音频驱动表情迁移_1956951532585541633.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_133

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/Fantasy Portrait表情迁移-图片输入_1958414298089472002.json、视频生成/图生视频/FantasyPortrait_表情迁移 WAN2.1工作流_1967251208723423233.json、视频生成/图生视频/FantasyPortrait音频驱动表情迁移-单人wan2.1_1956020151047127042.json、视频生成/图生视频/FantasyPortrait音频驱动表情迁移-单人wan2.1_1956179221490094081.json、视频生成/图生视频/FantasyPortrait音频驱动表情迁移-多人wan2.1_1956036782594904065.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：74%

## 共有节点

全部 12 个 workflow 都包含：
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
- `WanVideoSetBlockSwap` —— 11/12 个有
- `WanVideoSetLoRAs` —— 11/12 个有
- `GetNode` —— 9/12 个有
- `ImageConcatMulti` —— 9/12 个有
- `SetNode` —— 9/12 个有
- `Primitive integer [Crystools]` —— 6/12 个有
- `INTConstant` —— 5/12 个有
- `WanVideoContextOptions` —— 4/12 个有
- `ImageConcanate` —— 2/12 个有
- `LandmarksToImage` —— 2/12 个有
- `PrimitiveInt` —— 2/12 个有
- `VHS_VideoInfoLoaded` —— 2/12 个有
- `Any Switch (rgthree)` —— 1/12 个有
- `GetImageRangeFromBatch` —— 1/12 个有
- `Label (rgthree)` —— 1/12 个有
- `LayerUtility: PurgeVRAM V2` —— 1/12 个有
- `PreviewImage` —— 1/12 个有
- `easy cleanGpuUsed` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
