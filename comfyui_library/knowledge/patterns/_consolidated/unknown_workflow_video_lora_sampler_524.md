---
name: unknown_workflow_video_lora_sampler_524
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.51725
common_nodes: [CLIPVisionLoader, DF_Int_to_Float, GetNode, ImageFromBatch, ImageResizeKJv2, LoadImage, MemoryCleaner, OnnxDetectionModelLoader, PoseAndFaceDetection, SetNode, SimpleMath+, Text, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader, easy boolean, easy float, easy int]
problems: []
missing: []
members: [图片生成/图生图/YJ-APP-animate-v2-动作迁移_2039956611556450306.json, 图片生成/图生图/YJ-APP-animate-v4-视频替换元素_2053682581748629505.json, 视频生成/图生视频/YJ-APP-WanAnimate-v2-动作迁移_2044639396833529858.json, 视频生成/图生视频/YJ-APP-animate-v3-视频替换元素_2044639687251337217.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_524

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/YJ-APP-animate-v2-动作迁移_2039956611556450306.json、图片生成/图生图/YJ-APP-animate-v4-视频替换元素_2053682581748629505.json、视频生成/图生视频/YJ-APP-WanAnimate-v2-动作迁移_2044639396833529858.json、视频生成/图生视频/YJ-APP-animate-v3-视频替换元素_2044639687251337217.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：52%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPVisionLoader`
- `DF_Int_to_Float`
- `GetNode`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `LoadImage`
- `MemoryCleaner`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `SetNode`
- `SimpleMath+`
- `Text`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `easy boolean`
- `easy float`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `BBoxYOLO` —— 3/4 个有
- `BlockifyMask` —— 3/4 个有
- `CheckpointLoaderSimple` —— 3/4 个有
- `DrawMaskOnImage` —— 3/4 个有
- `LayerMask: MaskGrow` —— 3/4 个有
- `SDPoseDrawKeypoints` —— 3/4 个有
- `SDPoseKeypointExtractor` —— 3/4 个有
- `YOLOModelLoader` —— 3/4 个有
- `easy sam3ModelLoader` —— 3/4 个有
- `easy sam3VideoSegmentation` —— 3/4 个有
- `VHS_VideoInfoLoaded` —— 2/4 个有
- `easy cleanGpuUsed` —— 2/4 个有
- `DrawViTPose` —— 1/4 个有
- `If ANY execute A else B` —— 1/4 个有
- `Int` —— 1/4 个有
- `Masks Combine Regions` —— 1/4 个有
- `RunningHub Deepcleaner` —— 1/4 个有
- `easy compare` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
