---
name: unknown_workflow_controlnet_video_lora_3
type: Unknown Workflow
frequency: 21
level: moderate
coverage: 0.678429
common_nodes: [CLIPVisionLoader, GetImageSizeAndCount, GetNode, ImageResizeKJv2, LoadImage, NLFPredict, RenderNLFPoses, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddSCAILPoseEmbeds, WanVideoAddSCAILReferenceEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSamplerExtraArgs, WanVideoSamplerv2, WanVideoSchedulerv2, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/SCAIL单人动作迁移_2008501135774060546.json, 平台全量/SCAIL单人动作迁移_2008514502781837314.json, 平台全量/SCAIL多人动作参考_2001972242156273665.json, 平台全量/SCAIL多人动作迁移-舞蹈动作迁移_2001491151653830658.json, 平台全量/SCAIL多人动作迁移_2001287576491356161.json, 平台全量/SCAIL多人支持 实测8人通过 1217_2001285366705422337.json, 平台全量/SCAIL多人支持达成！！_2027292424720097282.json, 平台全量/SCAIL大模型一键生成小猫小狗人物跳舞视频，支持多人多动物同步舞蹈动作模仿多人跳舞_2041063992495443969.json, 平台全量/SCAIL大模型：一键图生AI跳舞视频，支持多人同时跳舞！_2049380971916562433.json, 平台全量/SCAIL大模型：一键生成AI跳舞视频，支持多人同时跳舞，让你开跳胜利之舞！_2001896148799504385.json, 平台全量/SCAIL大模型：一键生成动物小猫小狗人物跳舞视频多人多动物同时跳舞多人舞蹈模仿scail动作舞蹈模_2028099373153918978.json, 平台全量/SCAIL大模型：一键生成动物小猫小狗人物跳舞视频多人多动物同时跳舞多人舞蹈模仿scail动作舞蹈模_2080212319010902017.json, 平台全量/SCAIL视频姿势参考支持多人_2002800592563105793.json, 平台全量/SCAIL，丝滑转身，支持双人对打，支持单人_2000870298708832257.json, 平台全量/SCAIL，双人动作迁移-（可复刻双人对打）_2000509982518935553.json, 平台全量/动物跳舞，支持多只动物，真人_2016186565311078401.json, 数字人/数字人/SCAIL动作迁移：多人同框互动迁移_2013194857988235266.json, 数字人/数字人/SCAIL多人_单人--动作迁移_2001571883931824129.json, 数字人/数字人/SCAIL视频姿势参考支持多人_2019650977418186753.json, 视频生成/图生视频/SCAIL AI舞蹈生成：一键创造小猫小狗人物多人跳舞视频，支持多人多动物动作跳舞模仿_2015270492097220610.json, 视频生成/图生视频/SCAIL视频姿势参考支持多人_2000497050389184513.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_3

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（平台全量/SCAIL单人动作迁移_2008501135774060546.json、平台全量/SCAIL单人动作迁移_2008514502781837314.json、平台全量/SCAIL多人动作参考_2001972242156273665.json、平台全量/SCAIL多人动作迁移-舞蹈动作迁移_2001491151653830658.json、平台全量/SCAIL多人动作迁移_2001287576491356161.json…）

- **类型**：Unknown Workflow
- **样本数**：21
- **可信度**：中等可信
- **平均知识覆盖**：68%

## 共有节点

全部 21 个 workflow 都包含：
- `CLIPVisionLoader`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageResizeKJv2`
- `LoadImage`
- `NLFPredict`
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
- `WanVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSamplerExtraArgs`
- `WanVideoSamplerv2`
- `WanVideoSchedulerv2`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageConcatMulti` —— 20/21 个有
- `OnnxDetectionModelLoader` —— 20/21 个有
- `PoseDetectionVitPoseToDWPose` —— 20/21 个有
- `DownloadAndLoadNLFModel` —— 19/21 个有
- `WanVideoTorchCompileSettings` —— 18/21 个有
- `SimpleMath+` —— 16/21 个有
- `FloatConstant` —— 15/21 个有
- `INTConstant` —— 14/21 个有
- `ConvertOpenPoseKeypointsToDWPose` —— 13/21 个有
- `DWPreprocessor` —— 13/21 个有
- `LoadWanVideoT5TextEncoder` —— 12/21 个有
- `WanVideoTextEncode` —— 12/21 个有
- `WanVideoTextEncodeCached` —— 9/21 个有
- `Int` —— 6/21 个有
- `SimpleCalculatorKJ` —— 6/21 个有
- `Bookmark (rgthree)` —— 4/21 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/21 个有
- `MemoryCleaner` —— 4/21 个有
- `Text Multiline` —— 4/21 个有
- `Any Switch (rgthree)` —— 3/21 个有
- `Fast Groups Bypasser (rgthree)` —— 3/21 个有
- `ImageFromBatch+` —— 3/21 个有
- `ImpactInt` —— 3/21 个有
- `PreviewImage` —— 3/21 个有
- `LoadNLFModel` —— 2/21 个有
- `Manual XY Entry Info` —— 2/21 个有
- `intToFloat _O` —— 2/21 个有
- `ImpactSwitch` —— 1/21 个有
- `JWInteger` —— 1/21 个有
- `JjkText` —— 1/21 个有
- `Label (rgthree)` —— 1/21 个有
- `easy anythingIndexSwitch` —— 1/21 个有
- `easy int` —— 1/21 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
