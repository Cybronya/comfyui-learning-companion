---
name: unknown_workflow_video_lora_sampler_415
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9708
common_nodes: [CLIPVisionLoader, ImageResizeKJv2, Int, LayerUtility: PurgeVRAM V2, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, RHHiddenNodes, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan Animate_1998231978564575234.json, 视频生成/图生视频/人物角色替换Wan Animate+SeedVR2.5 wan2.2 视频重绘动作迁移参考图片_1997869036803436545.json, 视频生成/图生视频/视频二创人物 背景完美高清替换Wan Animate+SeedVR2.5_1996912831717130242.json, 视频生成/图生视频/视频二创人物角色替换Wan+Animate+OneToAll+SeedVR2.5_2002709997517717506.json, 视频生成/图生视频/视频二创人物角色替换Wan+Animate+OneToAll+SeedVR2.5_2059162619151470594.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_415

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/Wan Animate_1998231978564575234.json、视频生成/图生视频/人物角色替换Wan Animate+SeedVR2.5 wan2.2 视频重绘动作迁移参考图片_1997869036803436545.json、视频生成/图生视频/视频二创人物 背景完美高清替换Wan Animate+SeedVR2.5_1996912831717130242.json、视频生成/图生视频/视频二创人物角色替换Wan+Animate+OneToAll+SeedVR2.5_2002709997517717506.json、视频生成/图生视频/视频二创人物角色替换Wan+Animate+OneToAll+SeedVR2.5_2059162619151470594.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPVisionLoader`
- `ImageResizeKJv2`
- `Int`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `RHHiddenNodes`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 4/5 个有
- `FlashVSRNode` —— 4/5 个有
- `SDPoseOODLoader` —— 3/5 个有
- `SDPoseOODProcessor` —— 3/5 个有
- `PoseDetectionOneToAllAnimation` —— 2/5 个有
- `Text _O` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
