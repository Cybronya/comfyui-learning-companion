---
name: unknown_workflow_video_lora_sampler_665
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.852333
common_nodes: [CLIPVisionLoader, DrawViTPose, INTConstant, ImageFromBatch, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, OnnxDetectionModelLoader, PoseAndFaceDetection, PreviewImage, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeSingle, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/视频制作222_2013521126407806978.json, 视频生成/图生视频/SAM3 + Wan2.2_Animate 视频制作最新版_2003695576329953281.json, 视频生成/图生视频/传视频，指导图像人物按照视频动作跳舞（SAM3 + Wan2.2_Animate）动作迁移_2038176631273037826.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_665

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（数字人/数字人/视频制作222_2013521126407806978.json、视频生成/图生视频/SAM3 + Wan2.2_Animate 视频制作最新版_2003695576329953281.json、视频生成/图生视频/传视频，指导图像人物按照视频动作跳舞（SAM3 + Wan2.2_Animate）动作迁移_2038176631273037826.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPVisionLoader`
- `DrawViTPose`
- `INTConstant`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `PreviewImage`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeSingle`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ColorToMask` —— 2/3 个有
- `LayerUtility: ImageBlend V2` —— 2/3 个有
- `SDPoseOODLoader` —— 2/3 个有
- `SDPoseOODProcessor` —— 2/3 个有
- `Int` —— 1/3 个有
- `PrimitiveFloat` —— 1/3 个有
- `SimpleMath+` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
