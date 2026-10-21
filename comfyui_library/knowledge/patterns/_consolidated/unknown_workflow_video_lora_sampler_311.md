---
name: unknown_workflow_video_lora_sampler_311
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.630571
common_nodes: [CLIPVisionLoader, DownloadAndLoadNLFModel, GetImageSizeAndCount, GetNode, LoadImage, NLFPredict, OnnxDetectionModelLoader, PoseDetectionVitPoseToDWPose, RenderNLFPoses, SetNode, SimpleCalculatorKJ, VHS_VideoCombine, WanVideoAddSCAILPoseEmbeds, WanVideoAddSCAILReferenceEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSamplerExtraArgs, WanVideoSamplerv2, WanVideoSchedulerv2, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2038819844543483905.json, 视频生成/图生视频/2004486159680106498.json, 视频生成/图生视频/2015614153280462849.json, 视频生成/图生视频/2001927280328884225.json, 视频生成/图生视频/2003448511268069377.json, 视频生成/图生视频/2073307615077163010.json, 视频生成/图生视频/2013817943620067329.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_311

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/2038819844543483905.json、视频生成/图生视频/2004486159680106498.json、视频生成/图生视频/2015614153280462849.json、视频生成/图生视频/2001927280328884225.json、视频生成/图生视频/2003448511268069377.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：63%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPVisionLoader`
- `DownloadAndLoadNLFModel`
- `GetImageSizeAndCount`
- `GetNode`
- `LoadImage`
- `NLFPredict`
- `OnnxDetectionModelLoader`
- `PoseDetectionVitPoseToDWPose`
- `RenderNLFPoses`
- `SetNode`
- `SimpleCalculatorKJ`
- `VHS_VideoCombine`
- `WanVideoAddSCAILPoseEmbeds`
- `WanVideoAddSCAILReferenceEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSamplerExtraArgs`
- `WanVideoSamplerv2`
- `WanVideoSchedulerv2`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 6/7 个有
- `ImageResizeKJv2` —— 6/7 个有
- `VHS_LoadVideo` —— 6/7 个有
- `WanVideoEncode` —— 6/7 个有
- `WanVideoUni3C_ControlnetLoader` —— 6/7 个有
- `WanVideoUni3C_embeds` —— 6/7 个有
- `ConvertOpenPoseKeypointsToDWPose` —— 4/7 个有
- `DWPreprocessor` —— 4/7 个有
- `ImageConcatMulti` —— 4/7 个有
- `Int` —— 4/7 个有
- `RHHiddenNodes` —— 4/7 个有
- `WanVideoTorchCompileSettings` —— 3/7 个有
- `intToFloat _O` —— 3/7 个有
- `Fast Groups Bypasser (rgthree)` —— 2/7 个有
- `FloatConstant` —— 2/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/7 个有
- `AddLabel` —— 1/7 个有
- `CR Prompt Text` —— 1/7 个有
- `GroundingDinoModelLoader_SDPose` —— 1/7 个有
- `ImpactSwitch` —— 1/7 个有
- `JjkText` —— 1/7 个有
- `Label (rgthree)` —— 1/7 个有
- `PixelPerfectResolution` —— 1/7 个有
- `RIFE VFI` —— 1/7 个有
- `SDPoseOODLoader` —— 1/7 个有
- `SDPoseOODProcessor` —— 1/7 个有
- `TwoWaySwitch` —— 1/7 个有
- `VHS_LoadVideoFFmpeg` —— 1/7 个有
- `VHS_VideoInfo` —— 1/7 个有
- `YOLOModelLoader` —— 1/7 个有
- `easy imageSize` —— 1/7 个有
- `easy int` —— 1/7 个有
- `easy showAnything` —— 1/7 个有
- `ttN text` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
