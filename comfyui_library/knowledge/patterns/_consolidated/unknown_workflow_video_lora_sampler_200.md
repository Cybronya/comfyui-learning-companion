---
name: unknown_workflow_video_lora_sampler_200
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.587333
common_nodes: [CLIPVisionLoader, ImageResizeKJv2, LoadImage, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/Wan2.2 Animate角色替换与修改_1932812610956136450.json, 图片生成/图生图/Wan2.2 animate 视频人物替换_1976938900721672193.json, 图片生成/图生图/万物动作迁移One2All_1998760592200585217.json, 视频生成/图生视频/1280P Wan2.2 Animate人物替换【无限时长，跟随运镜】_1981708744444780545.json, 视频生成/图生视频/1280P高清Wan2.2 Animate人物替换加速版（无限时长）_1981690387544842241.json, 视频生成/图生视频/Wan2.2 Animate人物替换加速版（无限时长）_1969270955216412673.json, 视频生成/图生视频/WanAnimate -超级版视频换人换背景_1971495725483933698.json, 视频生成/图生视频/动漫跳舞SDPOSE+Wan Animate_1973029204331728897.json, 视频生成/图生视频/影视动作迁移_2030257978057695233.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_200

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Wan2.2 Animate角色替换与修改_1932812610956136450.json、图片生成/图生图/Wan2.2 animate 视频人物替换_1976938900721672193.json、图片生成/图生图/万物动作迁移One2All_1998760592200585217.json、视频生成/图生视频/1280P Wan2.2 Animate人物替换【无限时长，跟随运镜】_1981708744444780545.json、视频生成/图生视频/1280P高清Wan2.2 Animate人物替换加速版（无限时长）_1981690387544842241.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：59%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPVisionLoader`
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
- `WanVideoSetBlockSwap`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `BlockifyMask` —— 8/9 个有
- `DownloadAndLoadSAM2Model` —— 8/9 个有
- `DrawMaskOnImage` —— 8/9 个有
- `FaceMaskFromPoseKeypoints` —— 8/9 个有
- `GetImageSizeAndCount` —— 8/9 个有
- `GetNode` —— 8/9 个有
- `GrowMask` —— 8/9 个有
- `ImageConcatMulti` —— 8/9 个有
- `ImageCropByMaskAndResize` —— 8/9 个有
- `PointsEditor` —— 8/9 个有
- `Sam2Segmentation` —— 8/9 个有
- `SetNode` —— 8/9 个有
- `WanVideoSetLoRAs` —— 8/9 个有
- `DWPreprocessor` —— 7/9 个有
- `PixelPerfectResolution` —— 6/9 个有
- `WanVideoTorchCompileSettings` —— 6/9 个有
- `easy int` —— 6/9 个有
- `INTConstant` —— 5/9 个有
- `PrimitiveStringMultiline` —— 5/9 个有
- `JWInteger` —— 4/9 个有
- `LayerUtility: PurgeVRAM V2` —— 4/9 个有
- `easy cleanGpuUsed` —— 4/9 个有
- `Fast Groups Bypasser (rgthree)` —— 3/9 个有
- `SDPoseOODLoader` —— 3/9 个有
- `SDPoseOODProcessor` —— 3/9 个有
- `YOLOModelLoader` —— 3/9 个有
- `GroundingDinoModelLoader_SDPose` —— 2/9 个有
- `MathExpression|pysssss` —— 2/9 个有
- `OnnxDetectionModelLoader` —— 2/9 个有
- `PoseAndFaceDetection` —— 2/9 个有
- `RHHiddenNodes` —— 2/9 个有
- `SimpleMath+` —— 2/9 个有
- `DrawViTPose` —— 1/9 个有
- `FancyTimerNode` —— 1/9 个有
- `Fast Groups Muter (rgthree)` —— 1/9 个有
- `FastUnsharpSharpen` —— 1/9 个有
- `Label (rgthree)` —— 1/9 个有
- `OpenposePreprocessor` —— 1/9 个有
- `PoseDetectionOneToAllAnimation` —— 1/9 个有
- `VHS_VideoInfoLoaded` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
