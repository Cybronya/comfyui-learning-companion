---
name: unknown_workflow_video_lora_sampler_977
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.4855
common_nodes: [AILab_QwenVL_Advanced, BlockifyMask, CLIPVisionLoader, DrawGaussianNoiseOnImage, DrawMaskOnImage, DrawViTPose, GetImageSizeAndCount, GetNode, ImageFromBatch+, ImageRemoveBackground+, ImageResizeKJv2, InvertMask, LayerUtility: PurgeVRAM, LoadWanVideoT5TextEncoder, OnnxDetectionModelLoader, PoseAndFaceDetection, PrimitiveInt, SetNode, ShowText|pysssss, TransparentBGSession+, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEncode, WanVideoLoraSelect, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoUniLumosEmbeds, WanVideoVAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [平台全量/UniLumos_relight + Wan2.2 Animate 全新角色重新打光_1989175582221012994.json, 视频生成/文生视频/Wan Video UniLumos_Wan 2.2 Animate 课程对应工作流_1989279980154744834.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_977

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/UniLumos_relight + Wan2.2 Animate 全新角色重新打光_1989175582221012994.json、视频生成/文生视频/Wan Video UniLumos_Wan 2.2 Animate 课程对应工作流_1989279980154744834.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：49%

## 共有节点

全部 2 个 workflow 都包含：
- `AILab_QwenVL_Advanced`
- `BlockifyMask`
- `CLIPVisionLoader`
- `DrawGaussianNoiseOnImage`
- `DrawMaskOnImage`
- `DrawViTPose`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageFromBatch+`
- `ImageRemoveBackground+`
- `ImageResizeKJv2`
- `InvertMask`
- `LayerUtility: PurgeVRAM`
- `LoadWanVideoT5TextEncoder`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `PrimitiveInt`
- `SetNode`
- `ShowText|pysssss`
- `TransparentBGSession+`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoUniLumosEmbeds`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `Float to Int` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
