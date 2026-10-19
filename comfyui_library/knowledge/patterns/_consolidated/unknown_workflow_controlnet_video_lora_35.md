---
name: unknown_workflow_controlnet_video_lora_35
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6165
common_nodes: [Bjornulf_ShowInt, CLIPVisionLoader, GetImageSizeAndCount, GetNode, INTConstant, ImageConcatMulti, ImageResizeKJv2, NLFPredict, OnnxDetectionModelLoader, PoseDetectionVitPoseToDWPose, PreviewImage, Primitive string [Crystools], RHBatchImages:, RHExtractImage, RHUploadZip, RenderNLFPoses, SaveImage, SetNode, SimpleCalculatorKJ, TT_img_enc, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddSCAILPoseEmbeds, WanVideoAddSCAILReferenceEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEncode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSamplerExtraArgs, WanVideoSamplerv2, WanVideoSchedulerv2, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader, easy cleanGpuUsed, easy forLoopEnd, easy forLoopStart, easy imageCount, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/2011633491498246146.json, 视频生成/图生视频/2027971895844413441.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_35

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2011633491498246146.json、视频生成/图生视频/2027971895844413441.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：62%

## 共有节点

全部 2 个 workflow 都包含：
- `Bjornulf_ShowInt`
- `CLIPVisionLoader`
- `GetImageSizeAndCount`
- `GetNode`
- `INTConstant`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `NLFPredict`
- `OnnxDetectionModelLoader`
- `PoseDetectionVitPoseToDWPose`
- `PreviewImage`
- `Primitive string [Crystools]`
- `RHBatchImages:`
- `RHExtractImage`
- `RHUploadZip`
- `RenderNLFPoses`
- `SaveImage`
- `SetNode`
- `SimpleCalculatorKJ`
- `TT_img_enc`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAddSCAILPoseEmbeds`
- `WanVideoAddSCAILReferenceEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoEncode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSamplerExtraArgs`
- `WanVideoSamplerv2`
- `WanVideoSchedulerv2`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy imageCount`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `DownloadAndLoadNLFModel` —— 1/2 个有
- `LoadNLFModel` —— 1/2 个有
- `Text` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
