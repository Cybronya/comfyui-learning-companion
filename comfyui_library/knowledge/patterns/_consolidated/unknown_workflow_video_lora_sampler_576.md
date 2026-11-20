---
name: unknown_workflow_video_lora_sampler_576
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.835
common_nodes: [CLIPVisionLoader, DrawViTPose, INTConstant, ImageFromBatch, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, OnnxDetectionModelLoader, PoseAndFaceDetection, PreviewImage, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeSingle, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/Sam3+Wan2.2 Animate 动作迁移 顶级效果 20s+长视频 48G显存运行_2012394707908829186.json, 平台全量/本地可跳_2053524764362326017.json, 数字人/数字人/视频制作222_2013521126407806978.json, 视频生成/图生视频/SAM3 + Wan2.2_Animate 视频制作最新版_2003695576329953281.json, 视频生成/图生视频/传视频，指导图像人物按照视频动作跳舞（SAM3 + Wan2.2_Animate）动作迁移_2038176631273037826.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_576

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/Sam3+Wan2.2 Animate 动作迁移 顶级效果 20s+长视频 48G显存运行_2012394707908829186.json、平台全量/本地可跳_2053524764362326017.json、数字人/数字人/视频制作222_2013521126407806978.json、视频生成/图生视频/SAM3 + Wan2.2_Animate 视频制作最新版_2003695576329953281.json、视频生成/图生视频/传视频，指导图像人物按照视频动作跳舞（SAM3 + Wan2.2_Animate）动作迁移_2038176631273037826.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 5 个 workflow 都包含：
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
- `ColorToMask` —— 3/5 个有
- `LayerUtility: ImageBlend V2` —— 3/5 个有
- `SDPoseOODLoader` —— 3/5 个有
- `SDPoseOODProcessor` —— 3/5 个有
- `Int` —— 2/5 个有
- `PrimitiveFloat` —— 2/5 个有
- `SimpleMath+` —— 2/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
