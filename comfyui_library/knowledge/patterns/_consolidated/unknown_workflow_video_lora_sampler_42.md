---
name: unknown_workflow_video_lora_sampler_42
type: Unknown Workflow
frequency: 24
level: moderate
coverage: 0.894917
common_nodes: [CLIPVisionLoader, DownloadAndLoadNLFModel, GetImageSizeAndCount, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, NLFPredict, OnnxDetectionModelLoader, PoseDetectionVitPoseToDWPose, RenderNLFPoses, SimpleMath+, VHS_LoadVideo, WanVideoAddSCAILPoseEmbeds, WanVideoAddSCAILReferenceEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSamplerExtraArgs, WanVideoSamplerv2, WanVideoSchedulerv2, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Scail动作复刻工作流_2008843749622816769.json, 视频生成/图生视频/Scail动物跳舞工作流_1953472755108904961.json, 视频生成/图生视频/Scail多人跳舞，24G版_1954212955724378113.json, 视频生成/图生视频/Scail武术动作，单人动作模仿，可转身，可武术_1995058553109065730.json, 视频生成/图生视频/WAN SCAIL 2 动作参考 高帧率（单人、多人、非人）_2069249951540015105.json, 视频生成/图生视频/WANSCAIL动作参考 高帧率（单人、多人、非人）_2003741598695497730.json, 视频生成/图生视频/[ 完美版 ]SCAIL多人姿态精准迁移_2001286511733637121.json, 视频生成/图生视频/bduck跳舞-升级版_2016000836404514818.json, 视频生成/图生视频/一键“疯狂的鸽子舞”图片跳舞！B站艾橘溪！_2012769463266975745.json, 视频生成/图生视频/一键生成_海豹舞_图片跳舞！_2019406882007425026.json, 视频生成/图生视频/一键生成_海豹舞_图片跳舞！人物模仿海豹跳舞！艾橘溪_2011467663087771649.json, 视频生成/图生视频/二创视频-多人角色迁移、动作迁移_2004185141352296449.json, 视频生成/图生视频/人物模仿海豹跳舞一键生成_图生视频_2022325838447910913.json, 视频生成/图生视频/单人、多人跳舞动作迁移（支持人类和非人类参考，支持运镜参考）_2013066531797737474.json, 视频生成/图生视频/多萌宠跳舞SCAIL+SDPose+Uni3C动作、运镜最强迁移_2027611708860145666.json, 视频生成/图生视频/多萌宠跳舞SCAIL+SDPose+Uni3C动作、运镜最强迁移_2033355110813802497.json, 视频生成/图生视频/老Y运镜最强动作迁移，单人、多人、非人_2044291284843630593.json, 视频生成/图生视频/跳舞SCAIL+SDPose+Uni3C动作、运镜最强迁移_2036792778885173250.json, 视频生成/图生视频/跳舞SCAIL+SDPose+Uni3C动作、运镜最强迁移_2062564633763995649.json, 视频生成/图生视频/跳舞SCAIL+SDPose+Uni3C动作、运镜最强迁移_2065067395315757058.json, 视频生成/图生视频/跳舞SCAIL+SDPose+Uni3C动作、运镜最强迁移_2065103727006142465.json, 视频生成/图生视频/跳舞SCAIL+SDPose+Uni3C动作、运镜最强迁移_2067593207650807809.json, 视频生成/图生视频/跳舞SCAIL+SDPose+Uni3C动作、运镜最强迁移_2067595594784395266.json, 视频生成/图生视频/运镜迁移 多萌宠跳舞_2044671295245262850.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_42

> 由 `engine/knowledge_consolidation` 从 24 个 workflow 归纳得出（视频生成/图生视频/Scail动作复刻工作流_2008843749622816769.json、视频生成/图生视频/Scail动物跳舞工作流_1953472755108904961.json、视频生成/图生视频/Scail多人跳舞，24G版_1954212955724378113.json、视频生成/图生视频/Scail武术动作，单人动作模仿，可转身，可武术_1995058553109065730.json、视频生成/图生视频/WAN SCAIL 2 动作参考 高帧率（单人、多人、非人）_2069249951540015105.json…）

- **类型**：Unknown Workflow
- **样本数**：24
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 24 个 workflow 都包含：
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
- `SimpleMath+`
- `VHS_LoadVideo`
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
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `VHS_VideoCombine` —— 20/24 个有
- `WanVideoTorchCompileSettings` —— 19/24 个有
- `easy cleanGpuUsed` —— 19/24 个有
- `WanVideoEncode` —— 18/24 个有
- `WanVideoUni3C_ControlnetLoader` —— 18/24 个有
- `WanVideoUni3C_embeds` —— 18/24 个有
- `ImageConcatMulti` —— 16/24 个有
- `ConvertOpenPoseKeypointsToDWPose` —— 15/24 个有
- `DWPreprocessor` —— 15/24 个有
- `Any Switch (rgthree)` —— 14/24 个有
- `CR Text` —— 14/24 个有
- `GroundingDinoModelLoader_SDPose` —— 14/24 个有
- `Int` —— 14/24 个有
- `LayerUtility: PurgeVRAM V2` —— 14/24 个有
- `SDPoseOODLoader` —— 14/24 个有
- `SDPoseOODProcessor` —— 14/24 个有
- `YOLOModelLoader` —— 14/24 个有
- `Fast Groups Muter (rgthree)` —— 12/24 个有
- `INTConstant` —— 10/24 个有
- `WanVideoSetBlockSwap` —— 10/24 个有
- `WanVideoSetLoRAs` —— 10/24 个有
- `GetNode` —— 6/24 个有
- `SetNode` —— 6/24 个有
- `AudioToPath` —— 5/24 个有
- `Float to Int` —— 5/24 个有
- `OverlayVideos` —— 5/24 个有
- `PrimitiveFloat` —— 5/24 个有
- `PrimitiveInt` —— 5/24 个有
- `SaveVideo` —— 5/24 个有
- `VideoToPath` —— 5/24 个有
- `PreviewImage` —— 3/24 个有
- `FloatConstant` —— 2/24 个有
- `ImpactSwitch` —— 1/24 个有
- `PrimitiveBoolean` —— 1/24 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 1/24 个有
- `SaveImage` —— 1/24 个有
- `Text` —— 1/24 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
