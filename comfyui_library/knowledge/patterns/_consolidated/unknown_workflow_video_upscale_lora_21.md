---
name: unknown_workflow_video_upscale_lora_21
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.406333
common_nodes: [BlockifyMask, CLIPVisionLoader, DWPreprocessor, DrawMaskOnImage, Fast Groups Bypasser (rgthree), FloatConstant, GetNode, GrowMask, INTConstant, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, RIFE VFI, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader, easy sam3ModelLoader, easy sam3VideoSegmentation]
problems: []
missing: []
members: [平台全量/WAN2.2一键人物替换，人物一致性强！_2001257092776423425.json, 视频生成/图生视频/人物替换x凡人二创V2.0_2029486015072706561.json, 视频生成/图生视频/人物替换x凡人二创_2002281060912230402.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_lora_21

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/WAN2.2一键人物替换，人物一致性强！_2001257092776423425.json、视频生成/图生视频/人物替换x凡人二创V2.0_2029486015072706561.json、视频生成/图生视频/人物替换x凡人二创_2002281060912230402.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：41%

## 共有节点

全部 3 个 workflow 都包含：
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

**可变部分**（部分 workflow 才有）：
- `BiRefNetRMBG` —— 1/3 个有
- `LayerUtility: PurgeVRAM` —— 1/3 个有
- `LayerUtility: PurgeVRAM V2` —— 1/3 个有
- `YOLOModelLoader` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
