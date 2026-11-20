---
name: unknown_workflow_video_lora_sampler_983
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.895
common_nodes: [CLIPVisionLoader, DrawViTPose, ImageFromBatch, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, PrimitiveInt, RTXVideoSuperResolution, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/WanAnimate-1动作迁移专用（自动长视频高清版）_2117479198167228417.json, 平台全量/WanAnimate1-指定人物替换_2117845042026082305.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_983

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/WanAnimate-1动作迁移专用（自动长视频高清版）_2117479198167228417.json、平台全量/WanAnimate1-指定人物替换_2117845042026082305.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPVisionLoader`
- `DrawViTPose`
- `ImageFromBatch`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `PrimitiveInt`
- `RTXVideoSuperResolution`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `BlockifyMask` —— 1/2 个有
- `CLIPTextEncode` —— 1/2 个有
- `CheckpointLoaderSimple` —— 1/2 个有
- `DrawMaskOnImage` —— 1/2 个有
- `Float` —— 1/2 个有
- `GrowMaskWithBlur` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `LayerUtility: PurgeVRAM V2` —— 1/2 个有
- `MaskToImage` —— 1/2 个有
- `RTXVideoFrameGeneration` —— 1/2 个有
- `SAM3_Detect` —— 1/2 个有
- `easy framesEditor` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
