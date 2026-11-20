---
name: unknown_workflow_controlnet_video
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.861
common_nodes: [CLIPVisionLoader, ConvertOpenPoseKeypointsToDWPose, DWPreprocessor, DownloadAndLoadNLFModel, GetImageSize, ImageResizeKJv2, LoadImage, NLFPredict, OnnxDetectionModelLoader, PoseDetectionVitPoseToDWPose, PrimitiveInt, PrimitiveStringMultiline, RenderNLFPoses, SaveImage, SimpleMathDual+, VHS_LoadVideo, VHS_VideoInfoLoaded, WanVideoContextOptions, WanVideoEncode, WanVideoTextEncode, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, easy blocker, easy compare, easy ifElse, easy int, easy seed, workflow>Scail embeds, workflow>Wan2.1采样器]
problems: []
missing: []
members: ["平台全量/动作迁移再添新王Wan SCAIL, 单_多人支持_2000957796424220673.json", 视频生成/图生视频/WAN_Scail动作迁移_2003449655788748801.json, "视频生成/图生视频/【推荐，多人运镜支持】动作迁移Wan SCAIL,单_多人支持_2009862240601645057.json"]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/动作迁移再添新王Wan SCAIL, 单_多人支持_2000957796424220673.json、视频生成/图生视频/WAN_Scail动作迁移_2003449655788748801.json、视频生成/图生视频/【推荐，多人运镜支持】动作迁移Wan SCAIL,单_多人支持_2009862240601645057.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPVisionLoader`
- `ConvertOpenPoseKeypointsToDWPose`
- `DWPreprocessor`
- `DownloadAndLoadNLFModel`
- `GetImageSize`
- `ImageResizeKJv2`
- `LoadImage`
- `NLFPredict`
- `OnnxDetectionModelLoader`
- `PoseDetectionVitPoseToDWPose`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RenderNLFPoses`
- `SaveImage`
- `SimpleMathDual+`
- `VHS_LoadVideo`
- `VHS_VideoInfoLoaded`
- `WanVideoContextOptions`
- `WanVideoEncode`
- `WanVideoTextEncode`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `easy blocker`
- `easy compare`
- `easy ifElse`
- `easy int`
- `easy seed`
- `workflow>Scail embeds`
- `workflow>Wan2.1采样器`

**可变部分**（部分 workflow 才有）：
- `LoadWanVideoT5TextEncoder` —— 2/3 个有
- `SaveVideoRGBA` —— 2/3 个有
- `VHS_VideoCombine` —— 2/3 个有
- `WanVideoBlockSwap` —— 2/3 个有
- `WanVideoModelLoader` —— 2/3 个有
- `WanVideoSetBlockSwap` —— 2/3 个有
- `WanVideoSetLoRAs` —— 2/3 个有
- `WanVideoVAELoader` —— 2/3 个有
- `easy boolean` —— 2/3 个有
- `easy cleanGpuUsed` —— 2/3 个有
- `ConvertAny2Float` —— 1/3 个有
- `CreateVideo` —— 1/3 个有
- `INTConstant` —— 1/3 个有
- `MathExpression|pysssss` —— 1/3 个有
- `SaveVideo` —— 1/3 个有
- `WanVideoLoraSelect` —— 1/3 个有
- `WanVideoLoraSelectMulti` —— 1/3 个有
- `WanVideoTorchCompileSettings` —— 1/3 个有
- `workflow>Wan2.1模型加载器` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
