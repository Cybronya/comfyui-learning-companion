---
name: unknown_workflow_video_lora_sampler_477
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.93425
common_nodes: [CLIPVisionLoader, CreateVideo, GetVideoComponents, ImageResizeKJv2, LoadImage, PrimitiveFloat, SaveVideo, VHS_GetImageCount, VHS_LoadVideo, Video Slice, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageResizeToClosest, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/AI动作迁移-高精细10秒版｜单次10秒不糊_2106582395486035969.json, 视频生成/图生视频/AI动作迁移-高精细版｜5秒清晰不糊_2106570630329098242.json, 视频生成/图生视频/Animate动作迁移-自动尺寸工作流_2094980950672371713.json, 视频生成/图生视频/SCAIL2动作迁移-免骨架工作流_2095006151107760130.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_477

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/AI动作迁移-高精细10秒版｜单次10秒不糊_2106582395486035969.json、视频生成/图生视频/AI动作迁移-高精细版｜5秒清晰不糊_2106570630329098242.json、视频生成/图生视频/Animate动作迁移-自动尺寸工作流_2094980950672371713.json、视频生成/图生视频/SCAIL2动作迁移-免骨架工作流_2095006151107760130.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPVisionLoader`
- `CreateVideo`
- `GetVideoComponents`
- `ImageResizeKJv2`
- `LoadImage`
- `PrimitiveFloat`
- `SaveVideo`
- `VHS_GetImageCount`
- `VHS_LoadVideo`
- `Video Slice`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageResizeToClosest`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `BBOXToBoundingBoxKJ` —— 3/4 个有
- `CheckpointLoaderSimple` —— 3/4 个有
- `DrawViTPose` —— 3/4 个有
- `OnnxDetectionModelLoader` —— 3/4 个有
- `PoseAndFaceDetection` —— 3/4 个有
- `SDPoseDrawKeypoints` —— 3/4 个有
- `SDPoseKeypointExtractor` —— 3/4 个有
- `WanVideoAnimateEmbeds` —— 3/4 个有
- `WanVideoContextOptions` —— 3/4 个有
- `WanVideoAddSCAILPoseEmbeds` —— 1/4 个有
- `WanVideoAddSCAILReferenceEmbeds` —— 1/4 个有
- `WanVideoEmptyEmbeds` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
