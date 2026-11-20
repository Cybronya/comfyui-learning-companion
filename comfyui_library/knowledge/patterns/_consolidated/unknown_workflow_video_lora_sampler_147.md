---
name: unknown_workflow_video_lora_sampler_147
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.606769
common_nodes: [CLIPVisionLoader, DownloadAndLoadNLFModel, GetImageSizeAndCount, GetNode, LoadImage, NLFPredict, OnnxDetectionModelLoader, PoseDetectionVitPoseToDWPose, RenderNLFPoses, SetNode, SimpleCalculatorKJ, VHS_VideoCombine, WanVideoAddSCAILPoseEmbeds, WanVideoAddSCAILReferenceEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSamplerExtraArgs, WanVideoSamplerv2, WanVideoSchedulerv2, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/SCAIL 动作迁移_2038819844543483905.json, 视频生成/图生视频/SCAIL 动作迁移（高清版）_2004486159680106498.json, 视频生成/图生视频/SCAIL 动作迁移（高清版）_2015614153280462849.json, 视频生成/图生视频/SCAIL_3D姿态驱动+自动对齐骨骼+镜头控制+人物360旋转_2001927280328884225.json, 视频生成/图生视频/SCAIL_pose_control：丝滑动作迁移-适配各种风格也适合多人_2003448511268069377.json, 视频生成/图生视频/SCAIL动作迁移 单人_多人统一版_2073307615077163010.json, 视频生成/图生视频/SCAIL大模型：一键图生AI跳舞视频，支持多人同时跳舞！_2011341601720766466.json, 视频生成/图生视频/SCAIL大模型：一键图生AI跳舞视频，支持多人同时跳舞！_2041436850325295106.json, 视频生成/图生视频/SCAIL大模型：一键图生AI跳舞视频，支持多人同时跳舞！_2042104629911101442.json, 视频生成/图生视频/SCAIL大模型：一键图生AI跳舞视频，支持多人同时跳舞！_2054250246871494658.json, 视频生成/图生视频/SCAIL大模型：一键图生AI跳舞视频，支持多人多动物同时跳舞_2048599310039785473.json, 视频生成/图生视频/SCAIL大模型：一键生成动物小猫小狗人物跳舞视频多人多动物同时跳舞多人舞蹈模仿scail动作舞蹈_2049441031812288514.json, 视频生成/图生视频/萌宠跳舞（高清版）需要48gPlus运行_2013817943620067329.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_147

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/SCAIL 动作迁移_2038819844543483905.json、视频生成/图生视频/SCAIL 动作迁移（高清版）_2004486159680106498.json、视频生成/图生视频/SCAIL 动作迁移（高清版）_2015614153280462849.json、视频生成/图生视频/SCAIL_3D姿态驱动+自动对齐骨骼+镜头控制+人物360旋转_2001927280328884225.json、视频生成/图生视频/SCAIL_pose_control：丝滑动作迁移-适配各种风格也适合多人_2003448511268069377.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：61%

## 共有节点

全部 13 个 workflow 都包含：
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
- `INTConstant` —— 12/13 个有
- `ImageResizeKJv2` —— 12/13 个有
- `VHS_LoadVideo` —— 12/13 个有
- `WanVideoEncode` —— 12/13 个有
- `WanVideoUni3C_ControlnetLoader` —— 12/13 个有
- `WanVideoUni3C_embeds` —— 12/13 个有
- `ConvertOpenPoseKeypointsToDWPose` —— 10/13 个有
- `DWPreprocessor` —— 10/13 个有
- `ImageConcatMulti` —— 10/13 个有
- `WanVideoTorchCompileSettings` —— 9/13 个有
- `FloatConstant` —— 8/13 个有
- `JjkText` —— 7/13 个有
- `Int` —— 4/13 个有
- `RHHiddenNodes` —— 4/13 个有
- `intToFloat _O` —— 3/13 个有
- `Fast Groups Bypasser (rgthree)` —— 2/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/13 个有
- `AddLabel` —— 1/13 个有
- `CR Prompt Text` —— 1/13 个有
- `GroundingDinoModelLoader_SDPose` —— 1/13 个有
- `ImpactSwitch` —— 1/13 个有
- `Label (rgthree)` —— 1/13 个有
- `PixelPerfectResolution` —— 1/13 个有
- `RIFE VFI` —— 1/13 个有
- `SDPoseOODLoader` —— 1/13 个有
- `SDPoseOODProcessor` —— 1/13 个有
- `TwoWaySwitch` —— 1/13 个有
- `VHS_LoadVideoFFmpeg` —— 1/13 个有
- `VHS_VideoInfo` —— 1/13 个有
- `YOLOModelLoader` —— 1/13 个有
- `easy imageSize` —— 1/13 个有
- `easy int` —— 1/13 个有
- `easy showAnything` —— 1/13 个有
- `ttN text` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
