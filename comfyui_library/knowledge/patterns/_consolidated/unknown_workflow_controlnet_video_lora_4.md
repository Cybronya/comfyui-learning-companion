---
name: unknown_workflow_controlnet_video_lora_4
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.707583
common_nodes: [CLIPVisionLoader, DownloadAndLoadNLFModel, GetImageSizeAndCount, GetNode, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, NLFPredict, OnnxDetectionModelLoader, PoseDetectionVitPoseToDWPose, RenderNLFPoses, SetNode, SimpleMath+, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddSCAILPoseEmbeds, WanVideoAddSCAILReferenceEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSamplerExtraArgs, WanVideoSamplerv2, WanVideoSchedulerv2, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/02.16gSCAIL多人_2002262972904947714.json, 视频生成/图生视频/044-SCAIL动作迁移3.0-适配各种风格-单双人均可25-12-16_2000835179973406721.json, 视频生成/图生视频/12号特工：保留原图场景+SCAIL动作迁移_2026286261522141186.json, 视频生成/图生视频/251220001.01.16gSCAIL单人_2002263013321261058.json, 视频生成/图生视频/251220001.03.SCAIL双角色超动态动作迁移_2002262953242030082.json, 视频生成/图生视频/AI图片跳舞!美女跳舞=SCAIL动作模仿=艾橘溪_2000571970808934401.json, 视频生成/图生视频/AI图片跳舞!美女跳舞=动作模仿_2019605218685624321.json, 视频生成/图生视频/AI图片跳舞！SCAIL姿势转移动作模仿_2019643173101903873.json, 视频生成/图生视频/Ai动物跳舞：Scail图片跳舞工作流_2036758720331386881.json, 视频生成/图生视频/SCAIL大模型：一键图生AI跳舞视频，单人 动物跳舞 竖屏模式_2048613644405055490.json, 视频生成/图生视频/SCAIL大模型：一键生成单人 动物跳舞 动作迁移 视频竖屏模式版_2082798681614544897.json, 视频生成/图生视频/SCAIL大模型：一键生成单人 动物跳舞视频竖屏模式版_2068653827720572930.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_4

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/02.16gSCAIL多人_2002262972904947714.json、视频生成/图生视频/044-SCAIL动作迁移3.0-适配各种风格-单双人均可25-12-16_2000835179973406721.json、视频生成/图生视频/12号特工：保留原图场景+SCAIL动作迁移_2026286261522141186.json、视频生成/图生视频/251220001.01.16gSCAIL单人_2002263013321261058.json、视频生成/图生视频/251220001.03.SCAIL双角色超动态动作迁移_2002262953242030082.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：71%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPVisionLoader`
- `DownloadAndLoadNLFModel`
- `GetImageSizeAndCount`
- `GetNode`
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
- `INTConstant` —— 11/12 个有
- `Float to Int` —— 8/12 个有
- `PrimitiveFloat` —— 8/12 个有
- `PrimitiveInt` —— 8/12 个有
- `easy cleanGpuUsed` —— 8/12 个有
- `FloatConstant` —— 4/12 个有
- `ImageConcatMulti` —— 4/12 个有
- `JjkText` —— 4/12 个有
- `WanVideoTorchCompileSettings` —— 3/12 个有
- `ConvertOpenPoseKeypointsToDWPose` —— 2/12 个有
- `DWPreprocessor` —— 2/12 个有
- `CR Text` —— 1/12 个有
- `Fast Bypasser (rgthree)` —— 1/12 个有
- `GetImageSizeRatio` —— 1/12 个有
- `INPAINT_InpaintWithModel` —— 1/12 个有
- `INPAINT_LoadInpaintModel` —— 1/12 个有
- `ImageFromBatch+` —— 1/12 个有
- `ImagePadForOutpaint` —— 1/12 个有
- `ImageResize+` —— 1/12 个有
- `ImageToMask` —— 1/12 个有
- `Int` —— 1/12 个有
- `Mask Invert` —— 1/12 个有
- `MaskToImage` —— 1/12 个有
- `Mute / Bypass Repeater (rgthree)` —— 1/12 个有
- `PreviewImage` —— 1/12 个有
- `SolidMask` —— 1/12 个有
- `TextInput_` —— 1/12 个有
- `easy int` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
