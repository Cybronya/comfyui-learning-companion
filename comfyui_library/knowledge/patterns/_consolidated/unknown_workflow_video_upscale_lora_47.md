---
name: unknown_workflow_video_upscale_lora_47
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6965
common_nodes: [Anything Everywhere3, GetNode, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, Primitive integer [Crystools], RH_Captioner, RIFE VFI, SetNode, SimpleMath+, TextCombinerTwo, VHS_VideoCombine, Video_Upscale_With_Model, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoMagCache, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/图像组合编辑-FusionX_VACE_1929787256947773441.json, 视频生成/图生视频/图生视频-FusionX_VACE_自动补帧放大_1935165726103937025.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_lora_47

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/图像组合编辑-FusionX_VACE_1929787256947773441.json、视频生成/图生视频/图生视频-FusionX_VACE_自动补帧放大_1935165726103937025.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：70%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere3`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `Primitive integer [Crystools]`
- `RH_Captioner`
- `RIFE VFI`
- `SetNode`
- `SimpleMath+`
- `TextCombinerTwo`
- `VHS_VideoCombine`
- `Video_Upscale_With_Model`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoMagCache`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/2 个有
- `GetImageSizeAndCount` —— 1/2 个有
- `ImageResizeKJv2` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `RH_Prompter` —— 1/2 个有
- `WanVideoEncode` —— 1/2 个有
- `WanVideoPhantomEmbeds` —— 1/2 个有
- `WanVideoVACEEncode` —— 1/2 个有
- `WanVideoVACEStartToEndFrame` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
