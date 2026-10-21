---
name: unknown_workflow_video_lora_sampler_110
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.659071
common_nodes: [CLIPVisionLoader, GetNode, INTConstant, ImageResizeKJv2, LoadImage, NLFPredict, OnnxDetectionModelLoader, PoseDetectionVitPoseToDWPose, RenderNLFPoses, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddSCAILPoseEmbeds, WanVideoAddSCAILReferenceEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoModelLoader, WanVideoSamplerExtraArgs, WanVideoSamplerv2, WanVideoSchedulerv2, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2006028757395578881.json, 视频生成/图生视频/2006202937944576001.json, 视频生成/图生视频/2050494894682189826.json, 视频生成/图生视频/2006433739613675522.json, 视频生成/图生视频/2000760906177015810.json, 视频生成/图生视频/2000851201182793729.json, 视频生成/图生视频/2018306523847467009.json, 视频生成/图生视频/2023998769439711234.json, 视频生成/图生视频/2002405950176804865.json, 视频生成/图生视频/2002182497679077377.json, 视频生成/图生视频/1996588683803369474.json, 视频生成/图生视频/2058885569916264450.json, 视频生成/图生视频/2018335059614375937.json, 视频生成/图生视频/2066354482107207682.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_110

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/图生视频/2006028757395578881.json、视频生成/图生视频/2006202937944576001.json、视频生成/图生视频/2050494894682189826.json、视频生成/图生视频/2006433739613675522.json、视频生成/图生视频/2000760906177015810.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：66%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPVisionLoader`
- `GetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `LoadImage`
- `NLFPredict`
- `OnnxDetectionModelLoader`
- `PoseDetectionVitPoseToDWPose`
- `RenderNLFPoses`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAddSCAILPoseEmbeds`
- `WanVideoAddSCAILReferenceEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoModelLoader`
- `WanVideoSamplerExtraArgs`
- `WanVideoSamplerv2`
- `WanVideoSchedulerv2`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 12/14 个有
- `ImageConcatMulti` —— 12/14 个有
- `WanVideoLoraSelect` —— 12/14 个有
- `WanVideoEncode` —— 11/14 个有
- `WanVideoUni3C_ControlnetLoader` —— 11/14 个有
- `WanVideoUni3C_embeds` —— 11/14 个有
- `ConvertOpenPoseKeypointsToDWPose` —— 8/14 个有
- `DWPreprocessor` —— 8/14 个有
- `LoadWanVideoT5TextEncoder` —— 8/14 个有
- `SimpleMath+` —— 8/14 个有
- `WanVideoTextEncode` —— 8/14 个有
- `WanVideoTorchCompileSettings` —— 8/14 个有
- `DownloadAndLoadNLFModel` —— 7/14 个有
- `FloatConstant` —— 7/14 个有
- `LoadNLFModel` —— 7/14 个有
- `SimpleCalculatorKJ` —— 6/14 个有
- `WanVideoTextEncodeCached` —— 6/14 个有
- `Label (rgthree)` —— 5/14 个有
- `easy cleanGpuUsed` —— 4/14 个有
- `CustomAddLabel` —— 3/14 个有
- `Int` —— 3/14 个有
- `JjkText` —— 3/14 个有
- `TwoWaySwitch` —— 3/14 个有
- `intToFloat _O` —— 3/14 个有
- `DownloadAndLoadGIMMVFIModel` —— 2/14 个有
- `GIMMVFI_interpolate` —— 2/14 个有
- `LayerUtility: PurgeVRAM V2` —— 2/14 个有
- `PreviewImage` —— 2/14 个有
- `Text Multiline` —— 2/14 个有
- `WanVideoLoraSelectMulti` —— 2/14 个有
- `TTResolutionSelector` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
