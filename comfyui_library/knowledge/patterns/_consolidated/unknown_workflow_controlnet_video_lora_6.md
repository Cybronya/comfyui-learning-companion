---
name: unknown_workflow_controlnet_video_lora_6
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.726364
common_nodes: [CLIPVisionLoader, DownloadAndLoadNLFModel, GetImageSizeAndCount, GetNode, INTConstant, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, NLFPredict, OnnxDetectionModelLoader, PoseDetectionVitPoseToDWPose, RenderNLFPoses, SetNode, SimpleMath+, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddSCAILPoseEmbeds, WanVideoAddSCAILReferenceEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSamplerExtraArgs, WanVideoSamplerv2, WanVideoSchedulerv2, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2026286261522141186.json, 视频生成/图生视频/2002263013321261058.json, 视频生成/图生视频/2002262953242030082.json, 视频生成/图生视频/2000571970808934401.json, 视频生成/图生视频/2019605218685624321.json, 视频生成/图生视频/2019643173101903873.json, 视频生成/图生视频/2036758720331386881.json, 视频生成/图生视频/SCAIL大模型：一键图生AI跳舞视频，单人 动物跳舞 竖屏模式_2048613644405055490.json, 视频生成/图生视频/SCAIL大模型：一键生成单人 动物跳舞 动作迁移 视频竖屏模式版_2082798681614544897.json, 视频生成/图生视频/2068653827720572930.json, 视频生成/图生视频/2016000836404514818.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_6

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/2026286261522141186.json、视频生成/图生视频/2002263013321261058.json、视频生成/图生视频/2002262953242030082.json、视频生成/图生视频/2000571970808934401.json、视频生成/图生视频/2019605218685624321.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：73%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPVisionLoader`
- `DownloadAndLoadNLFModel`
- `GetImageSizeAndCount`
- `GetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `NLFPredict`
- `OnnxDetectionModelLoader`
- `PoseDetectionVitPoseToDWPose`
- `RenderNLFPoses`
- `SetNode`
- `SimpleMath+`
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
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSamplerExtraArgs`
- `WanVideoSamplerv2`
- `WanVideoSchedulerv2`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Float to Int` —— 9/11 个有
- `PrimitiveFloat` —— 9/11 个有
- `PrimitiveInt` —— 9/11 个有
- `easy cleanGpuUsed` —— 9/11 个有
- `JjkText` —— 4/11 个有
- `FloatConstant` —— 2/11 个有
- `ImageConcatMulti` —— 2/11 个有
- `PreviewImage` —— 2/11 个有
- `WanVideoTorchCompileSettings` —— 2/11 个有
- `AudioToPath` —— 1/11 个有
- `ConvertOpenPoseKeypointsToDWPose` —— 1/11 个有
- `DWPreprocessor` —— 1/11 个有
- `GetImageSizeRatio` —— 1/11 个有
- `INPAINT_InpaintWithModel` —— 1/11 个有
- `INPAINT_LoadInpaintModel` —— 1/11 个有
- `ImageFromBatch+` —— 1/11 个有
- `ImagePadForOutpaint` —— 1/11 个有
- `ImageResize+` —— 1/11 个有
- `ImageToMask` —— 1/11 个有
- `Int` —— 1/11 个有
- `Mask Invert` —— 1/11 个有
- `MaskToImage` —— 1/11 个有
- `OverlayVideos` —— 1/11 个有
- `PrimitiveBoolean` —— 1/11 个有
- `SaveVideo` —— 1/11 个有
- `SolidMask` —— 1/11 个有
- `Text` —— 1/11 个有
- `TextInput_` —— 1/11 个有
- `VideoToPath` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
