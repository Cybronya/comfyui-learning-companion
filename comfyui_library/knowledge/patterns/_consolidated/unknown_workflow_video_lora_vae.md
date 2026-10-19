---
name: unknown_workflow_video_lora_vae
type: Unknown Workflow
frequency: 19
level: moderate
coverage: 0.773684
common_nodes: [CLIPVisionLoader, DownloadAndLoadNLFModel, GetImageSizeAndCount, ImageResizeKJv2, LoadImage, NLFPredict, RenderNLFPoses, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddSCAILPoseEmbeds, WanVideoAddSCAILReferenceEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoLoraSelect, WanVideoModelLoader, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2000600692651945986.json, 视频生成/图生视频/2001174211215454210.json, 视频生成/图生视频/2006276580754071554.json, 视频生成/图生视频/2004474067589754881.json, 视频生成/图生视频/2008813540995502081.json, 视频生成/图生视频/2008843749622816769.json, 视频生成/图生视频/1953472755108904961.json, 视频生成/图生视频/1954212955724378113.json, 视频生成/图生视频/1995058553109065730.json, 视频生成/图生视频/2000383741266624513.json, 视频生成/图生视频/2000390740419244034.json, 视频生成/图生视频/2001862842288599042.json, 视频生成/图生视频/2001286511733637121.json, 视频生成/图生视频/2015612655679053825.json, 视频生成/图生视频/2031033766637998081.json, 视频生成/图生视频/2002334338010234881.json, 视频生成/图生视频/2013510010877251586.json, 视频生成/图生视频/2001528036937854977.json, 视频生成/图生视频/2014606161722482689.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_vae

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（视频生成/图生视频/2000600692651945986.json、视频生成/图生视频/2001174211215454210.json、视频生成/图生视频/2006276580754071554.json、视频生成/图生视频/2004474067589754881.json、视频生成/图生视频/2008813540995502081.json…）

- **类型**：Unknown Workflow
- **样本数**：19
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 19 个 workflow 都包含：
- `CLIPVisionLoader`
- `DownloadAndLoadNLFModel`
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `LoadImage`
- `NLFPredict`
- `RenderNLFPoses`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAddSCAILPoseEmbeds`
- `WanVideoAddSCAILReferenceEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageConcatMulti` —— 18/19 个有
- `LoadWanVideoT5TextEncoder` —— 18/19 个有
- `OnnxDetectionModelLoader` —— 18/19 个有
- `PoseDetectionVitPoseToDWPose` —— 18/19 个有
- `SimpleMath+` —— 18/19 个有
- `WanVideoTextEncode` —— 18/19 个有
- `WanVideoContextOptions` —— 17/19 个有
- `WanVideoSamplerExtraArgs` —— 17/19 个有
- `WanVideoSamplerv2` —— 17/19 个有
- `WanVideoSchedulerv2` —— 17/19 个有
- `WanVideoSetBlockSwap` —— 17/19 个有
- `WanVideoSetLoRAs` —— 17/19 个有
- `WanVideoTorchCompileSettings` —— 16/19 个有
- `INTConstant` —— 13/19 个有
- `FloatConstant` —— 11/19 个有
- `GetNode` —— 11/19 个有
- `SetNode` —— 11/19 个有
- `WanVideoEncode` —— 10/19 个有
- `WanVideoUni3C_ControlnetLoader` —— 10/19 个有
- `WanVideoUni3C_embeds` —— 10/19 个有
- `ConvertOpenPoseKeypointsToDWPose` —— 8/19 个有
- `DWPreprocessor` —— 8/19 个有
- `PreviewImage` —— 6/19 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/19 个有
- `Int` —— 4/19 个有
- `CR Prompt Text` —— 3/19 个有
- `easy showAnything` —— 3/19 个有
- `ConvertAny2Float` —— 2/19 个有
- `Display Any (rgthree)` —— 2/19 个有
- `GetImageRangeFromBatch` —— 2/19 个有
- `ImpactSwitch` —— 2/19 个有
- `Switch any [Crystools]` —— 2/19 个有
- `Text` —— 2/19 个有
- `WanVideoSampler` —— 2/19 个有
- `WanVideoScheduler` —— 2/19 个有
- `Fast Groups Bypasser (rgthree)` —— 1/19 个有
- `PrimitiveInt` —— 1/19 个有
- `PrimitiveStringMultiline` —— 1/19 个有
- `SDPoseOODLoader` —— 1/19 个有
- `SimpleCalculatorKJ` —— 1/19 个有
- `TextInput_` —— 1/19 个有
- `WanVideoTextEncodeCached` —— 1/19 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
