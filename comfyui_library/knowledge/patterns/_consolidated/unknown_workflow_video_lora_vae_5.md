---
name: unknown_workflow_video_lora_vae_5
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.391667
common_nodes: [CLIPVisionLoader, GetNode, INTConstant, ImageResizeKJv2, LoadImage, OnnxDetectionModelLoader, PlaySound|pysssss, PoseAndFaceDetection, PreviewImage, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/qy-简化_2035638502787911682.json, 视频生成/图生视频/【Work-Fisher】影视二创单人版_1997152784027947009.json, 视频生成/图生视频/啊癫【丝滑变装】&【动作迁移】&【人物替换】Wan2.2 Animate 分段队列_2062892652022030338.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_vae_5

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/qy-简化_2035638502787911682.json、视频生成/图生视频/【Work-Fisher】影视二创单人版_1997152784027947009.json、视频生成/图生视频/啊癫【丝滑变装】&【动作迁移】&【人物替换】Wan2.2 Animate 分段队列_2062892652022030338.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：39%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPVisionLoader`
- `GetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PlaySound|pysssss`
- `PoseAndFaceDetection`
- `PreviewImage`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `SDPoseOODLoader` —— 2/3 个有
- `SDPoseOODProcessor` —— 2/3 个有
- `Seed (rgthree)` —— 2/3 个有
- `VHS_VideoInfoLoaded` —— 2/3 个有
- `WanVideoLoraSelectMulti` —— 2/3 个有
- `WanVideoSamplerFromSettings` —— 2/3 个有
- `WanVideoSamplerSettings` —— 2/3 个有
- `Any Switch (rgthree)` —— 1/3 个有
- `BBoxYOLO` —— 1/3 个有
- `BodyRatioMapperSDPoseRender` —— 1/3 个有
- `CheckpointLoaderSimple` —— 1/3 个有
- `DrawViTPose` —— 1/3 个有
- `FastUnsharpSharpen` —— 1/3 个有
- `PrimitiveFloat` —— 1/3 个有
- `RHHiddenNodes` —— 1/3 个有
- `RIFE VFI` —— 1/3 个有
- `RTXVideoSuperResolution` —— 1/3 个有
- `SDPoseKeypointExtractor` —— 1/3 个有
- `SegmentQueueRunner` —— 1/3 个有
- `WanVideoContextOptions` —— 1/3 个有
- `WanVideoSampler` —— 1/3 个有
- `YOLOModelLoader` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
