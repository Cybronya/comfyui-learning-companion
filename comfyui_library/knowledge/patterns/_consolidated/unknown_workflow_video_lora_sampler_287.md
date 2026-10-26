---
name: unknown_workflow_video_lora_sampler_287
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.747
common_nodes: [CLIPVisionLoader, FantasyPortraitFaceDetector, FantasyPortraitModelLoader, ImageResizeKJv2, LoadImage, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddFantasyPortrait, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/wanvideo_2_1_I2V_FantasyPortrait_表情迁移_1957329197184249857.json, 数字人/数字人/直播视频表情模仿_1956705772944986113.json, 数字人/数字人/表情迁移 - Wan2.1_1966784793595850754.json, 视频生成/图生视频/Fantasy Portrait表情迁移-图片输入_1958414298089472002.json, 视频生成/图生视频/FantasyPortrait_表情迁移 WAN2.1工作流_1967251208723423233.json, 视频生成/图生视频/FantasyPortrait音频驱动表情迁移-单人wan2.1_1956020151047127042.json, 视频生成/图生视频/FantasyPortrait音频驱动表情迁移-多人wan2.1_1956036782594904065.json, 视频生成/图生视频/最新FantasyPortrait音频驱动表情迁移_1956951532585541633.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_287

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（数字人/数字人/wanvideo_2_1_I2V_FantasyPortrait_表情迁移_1957329197184249857.json、数字人/数字人/直播视频表情模仿_1956705772944986113.json、数字人/数字人/表情迁移 - Wan2.1_1966784793595850754.json、视频生成/图生视频/Fantasy Portrait表情迁移-图片输入_1958414298089472002.json、视频生成/图生视频/FantasyPortrait_表情迁移 WAN2.1工作流_1967251208723423233.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 8 个 workflow 都包含：
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
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoTextEncodeCached` —— 7/8 个有
- `GetNode` —— 6/8 个有
- `ImageConcatMulti` —— 6/8 个有
- `SetNode` —— 6/8 个有
- `INTConstant` —— 5/8 个有
- `WanVideoContextOptions` —— 4/8 个有
- `Primitive integer [Crystools]` —— 3/8 个有
- `easy cleanGpuUsed` —— 2/8 个有
- `Anything Everywhere` —— 1/8 个有
- `LandmarksToImage` —— 1/8 个有
- `LayerUtility: PurgeVRAM V2` —— 1/8 个有
- `LoadWanVideoT5TextEncoder` —— 1/8 个有
- `PreviewImage` —— 1/8 个有
- `SimpleMath+` —— 1/8 个有
- `TrimVideoLatent` —— 1/8 个有
- `WanVideoTextEncode` —— 1/8 个有
- `easy showAnything` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
