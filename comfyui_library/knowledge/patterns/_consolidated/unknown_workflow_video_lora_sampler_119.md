---
name: unknown_workflow_video_lora_sampler_119
type: Unknown Workflow
frequency: 16
level: moderate
coverage: 0.62525
common_nodes: [CLIPVisionLoader, DWPreprocessor, ImageResizeKJv2, LoadImage, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/wan2.2 Animate 姿势控制（动作迁移）_1969400959162085378.json, 平台全量/wan2.2 animate 人物替换_1969350690336350209.json, 平台全量/wan2.2-Animate-工作流_1970417631662665730.json, 平台全量/wan2.2Animate美女跳舞工作流（内附教学版）_2026683701299515394.json, 平台全量/wan_animate 人物替换和动作迁移_1969640550402039810.json, 平台全量/影视二创-人物替换对口型 动作迁移 30秒以上长视频 视频换脸_2050414425278038018.json, 平台全量/影视二创-人物替换对口型_2012812258056871937.json, 数字人/数字人/WanAnimate 人物替换 表情迁移_1969056420173934594.json, 数字人/数字人/WanAnimate 场景二 动作+表情迁移_1970111704807993345.json, 数字人/数字人/WanAnimate-动作迁移01_1969358029953134594.json, 视频生成/图生视频/1280P Wan2.2 Animate人物替换【无限时长，跟随运镜】_1981708744444780545.json, 视频生成/图生视频/1280P高清Wan2.2 Animate人物替换加速版（无限时长）_1981690387544842241.json, 视频生成/图生视频/Wan Animate2.2主体混合mix加速版V1_1969219198985662465.json, 视频生成/图生视频/Wan2.2 Animate人物替换加速版（无限时长）_1969270955216412673.json, 视频生成/图生视频/Wan2.2-Animate 视频换脸+动作迁移_1981706242731196418.json, 视频生成/图生视频/WanAnimate -超级版视频换人换背景_1971495725483933698.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_119

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（平台全量/wan2.2 Animate 姿势控制（动作迁移）_1969400959162085378.json、平台全量/wan2.2 animate 人物替换_1969350690336350209.json、平台全量/wan2.2-Animate-工作流_1970417631662665730.json、平台全量/wan2.2Animate美女跳舞工作流（内附教学版）_2026683701299515394.json、平台全量/wan_animate 人物替换和动作迁移_1969640550402039810.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：63%

## 共有节点

全部 16 个 workflow 都包含：
- `CLIPVisionLoader`
- `DWPreprocessor`
- `ImageResizeKJv2`
- `LoadImage`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `FaceMaskFromPoseKeypoints` —— 15/16 个有
- `ImageCropByMaskAndResize` —— 15/16 个有
- `PixelPerfectResolution` —— 15/16 个有
- `WanVideoSetBlockSwap` —— 15/16 个有
- `WanVideoSetLoRAs` —— 15/16 个有
- `BlockifyMask` —— 14/16 个有
- `DownloadAndLoadSAM2Model` —— 14/16 个有
- `DrawMaskOnImage` —— 14/16 个有
- `GrowMask` —— 14/16 个有
- `ImageConcatMulti` —— 14/16 个有
- `Sam2Segmentation` —— 14/16 个有
- `SetNode` —— 14/16 个有
- `GetImageSizeAndCount` —— 13/16 个有
- `GetNode` —— 13/16 个有
- `PointsEditor` —— 13/16 个有
- `JWInteger` —— 8/16 个有
- `WanVideoTorchCompileSettings` —— 8/16 个有
- `INTConstant` —— 7/16 个有
- `easy cleanGpuUsed` —— 7/16 个有
- `WanVideoContextOptions` —— 6/16 个有
- `PrimitiveStringMultiline` —— 5/16 个有
- `easy int` —— 5/16 个有
- `LayerUtility: PurgeVRAM V2` —— 4/16 个有
- `Florence2Run` —— 3/16 个有
- `Florence2toCoordinates` —— 3/16 个有
- `PreviewImage` —— 3/16 个有
- `CR Text` —— 2/16 个有
- `Florence2ModelLoader` —— 2/16 个有
- `PrimitiveString` —— 2/16 个有
- `RHHiddenNodes` —— 2/16 个有
- `SimpleMath+` —— 2/16 个有
- `Display Int (rgthree)` —— 1/16 个有
- `DownloadAndLoadFlorence2Model` —— 1/16 个有
- `EmptyImage` —— 1/16 个有
- `PoseAndFaceDetection` —— 1/16 个有
- `Switch any [Crystools]` —— 1/16 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
