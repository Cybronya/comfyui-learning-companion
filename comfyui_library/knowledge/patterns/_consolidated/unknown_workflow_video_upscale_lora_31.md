---
name: unknown_workflow_video_upscale_lora_31
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8905
common_nodes: [AILab_ImageStitch, Anything Everywhere3, CLIPVisionLoader, FastUnsharpSharpen, GetImageRangeFromBatch, GetImageSizeAndCount, ImageResize+, ImageUpscaleWithModel, LoadImage, RIFE VFI, UpscaleModelLoader, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddSteadyDancerEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSamplerFromSettings, WanVideoSamplerSettings, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/SteadyDancer-自适应骨骼迁移 版本一 12.8_1997886234179567618.json, 视频生成/图生视频/SteadyDancer-自适应骨骼迁移-版本二 12.11_1998823321796009986.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_lora_31

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/SteadyDancer-自适应骨骼迁移 版本一 12.8_1997886234179567618.json、视频生成/图生视频/SteadyDancer-自适应骨骼迁移-版本二 12.11_1998823321796009986.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 2 个 workflow 都包含：
- `AILab_ImageStitch`
- `Anything Everywhere3`
- `CLIPVisionLoader`
- `FastUnsharpSharpen`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `ImageResize+`
- `ImageUpscaleWithModel`
- `LoadImage`
- `RIFE VFI`
- `UpscaleModelLoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAddSteadyDancerEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSamplerFromSettings`
- `WanVideoSamplerSettings`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerColor: ColorAdapter` —— 1/2 个有
- `OnnxDetectionModelLoader` —— 1/2 个有
- `PoseDetectionOneToAllAnimation` —— 1/2 个有
- `SDPoseOODLoader` —— 1/2 个有
- `SDPoseOODProcessor` —— 1/2 个有
- `SetNode` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
