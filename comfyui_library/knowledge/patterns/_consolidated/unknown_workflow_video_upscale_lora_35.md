---
name: unknown_workflow_video_upscale_lora_35
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.39
common_nodes: [BlockifyMask, CLIPVisionLoader, DWPreprocessor, DrawMaskOnImage, Fast Groups Bypasser (rgthree), FloatConstant, GetNode, GrowMask, INTConstant, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, RIFE VFI, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader, easy sam3ModelLoader, easy sam3VideoSegmentation]
problems: []
missing: []
members: [视频生成/图生视频/2029486015072706561.json, 视频生成/图生视频/2002281060912230402.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_lora_35

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2029486015072706561.json、视频生成/图生视频/2002281060912230402.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：39%

## 共有节点

全部 2 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DWPreprocessor`
- `DrawMaskOnImage`
- `Fast Groups Bypasser (rgthree)`
- `FloatConstant`
- `GetNode`
- `GrowMask`
- `INTConstant`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `RIFE VFI`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
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
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy sam3ModelLoader`
- `easy sam3VideoSegmentation`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
