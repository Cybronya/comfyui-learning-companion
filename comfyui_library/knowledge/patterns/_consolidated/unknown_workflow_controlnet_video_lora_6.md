---
name: unknown_workflow_controlnet_video_lora_6
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.780333
common_nodes: [CLIPVisionLoader, DownloadAndLoadNLFModel, GetImageSizeAndCount, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, NLFPredict, OnnxDetectionModelLoader, PoseDetectionVitPoseToDWPose, RenderNLFPoses, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddSCAILPoseEmbeds, WanVideoAddSCAILReferenceEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSamplerExtraArgs, WanVideoSamplerv2, WanVideoSchedulerv2, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/(（自用）-脸部识别版)Scail双人动作迁移(720P高质量版)V3_2000985576838922241.json, 视频生成/图生视频/AI图片跳舞!美女跳舞=SCAIL动作模仿=艾橘溪_2000571970808934401.json, 视频生成/图生视频/AI图片跳舞!美女跳舞=动作模仿_2019605218685624321.json, 视频生成/图生视频/AI图片跳舞！SCAIL姿势转移动作模仿_2019643173101903873.json, 视频生成/图生视频/Ai动物跳舞：Scail图片跳舞工作流_2036758720331386881.json, 视频生成/图生视频/SCAIL 多人物动作参考（表情、运镜、动作多重参考）_2001210850083995649.json, 视频生成/图生视频/SCAIL大模型：一键图生AI跳舞视频，单人 动物跳舞 竖屏模式_2048613644405055490.json, 视频生成/图生视频/SCAIL大模型：一键生成单人 动物跳舞 动作迁移 视频竖屏模式版_2082798681614544897.json, 视频生成/图生视频/SCAIL大模型：一键生成单人 动物跳舞视频竖屏模式版_2068653827720572930.json, 视频生成/图生视频/SCAIL：重新定义 AI 姿势迁移_2008532893487861762.json, 视频生成/图生视频/ScaiL单_双人动作迁移-舞蹈、口播、带货-数字人_2003735062367641602.json, 视频生成/图生视频/ScaiL单_双人动作迁移-舞蹈、口播、带货-数字人_2004016053883682817.json, 视频生成/图生视频/Scail动作迁移_2001603322555559938.json, 视频生成/图生视频/（脸部识别）Scail双人动作迁移(720P高质量版)V4_2000648605100802049.json, 视频生成/图生视频/（自用）Scail单人动作迁移(720P高质量版)V2_2000980028173283329.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_6

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/图生视频/(（自用）-脸部识别版)Scail双人动作迁移(720P高质量版)V3_2000985576838922241.json、视频生成/图生视频/AI图片跳舞!美女跳舞=SCAIL动作模仿=艾橘溪_2000571970808934401.json、视频生成/图生视频/AI图片跳舞!美女跳舞=动作模仿_2019605218685624321.json、视频生成/图生视频/AI图片跳舞！SCAIL姿势转移动作模仿_2019643173101903873.json、视频生成/图生视频/Ai动物跳舞：Scail图片跳舞工作流_2036758720331386881.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPVisionLoader`
- `DownloadAndLoadNLFModel`
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `NLFPredict`
- `OnnxDetectionModelLoader`
- `PoseDetectionVitPoseToDWPose`
- `RenderNLFPoses`
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
- `SetNode` —— 11/15 个有
- `SimpleMath+` —— 11/15 个有
- `GetNode` —— 10/15 个有
- `INTConstant` —— 9/15 个有
- `easy cleanGpuUsed` —— 8/15 个有
- `Float to Int` —— 7/15 个有
- `PrimitiveFloat` —— 7/15 个有
- `PrimitiveInt` —— 7/15 个有
- `CR Prompt Text` —— 6/15 个有
- `JWInteger` —— 6/15 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/15 个有
- `MathExpression|pysssss` —— 6/15 个有
- `RunningHub Deepcleaner` —— 6/15 个有
- `ConvertOpenPoseKeypointsToDWPose` —— 5/15 个有
- `DWPreprocessor` —— 5/15 个有
- `ImageConcatMulti` —— 5/15 个有
- `JjkText` —— 4/15 个有
- `PDIMAGE_LongerSize` —— 3/15 个有
- `SaveImage` —— 3/15 个有
- `DuckHideNode` —— 2/15 个有
- `FloatConstant` —— 2/15 个有
- `TT_img_enc` —— 2/15 个有
- `TT_img_enc_v2` —— 2/15 个有
- `WanVideoTorchCompileSettings` —— 2/15 个有
- `DF_Int_to_Float` —— 1/15 个有
- `ImpactSwitch` —— 1/15 个有
- `Int` —— 1/15 个有
- `Inversed Switch` —— 1/15 个有
- `TextBox` —— 1/15 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
