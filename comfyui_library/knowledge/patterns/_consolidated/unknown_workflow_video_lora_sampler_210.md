---
name: unknown_workflow_video_lora_sampler_210
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.5395
common_nodes: [BlockifyMask, CLIPVisionLoader, DownloadAndLoadSAM2Model, DrawMaskOnImage, GetImageSizeAndCount, GetNode, ImageConcatMulti, ImageResizeKJv2, LoadImage, Sam2Segmentation, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/wanvideo_WanAnimate_V2_1974837982966493186.json, 数字人/数字人/wanvideo_WanAnimate_角色替换工作流_1969720507606200322.json, 数字人/数字人/视频人物替换-Wan Animate_V2版_1976639386127343617.json, 数字人/数字人/长视频 人物替换动作迁移wan2.2-Animate_1976989855852961793.json, 视频生成/图生视频/1280P Wan2.2 Animate人物替换【无限时长，跟随运镜】_1981708744444780545.json, 视频生成/图生视频/1280P高清Wan2.2 Animate人物替换加速版（无限时长）_1981690387544842241.json, 视频生成/图生视频/Wan Animate2.2人物融合(Mix)V2增强版_2073214426706173954.json, 视频生成/图生视频/Wan Animate2.2动作迁移V2(Move)增强版_2073218471797805057.json, 视频生成/图生视频/Wan2.2 Animate人物替换加速版（无限时长）_1969270955216412673.json, 视频生成/图生视频/WanAnimate -超级版视频换人换背景_1971495725483933698.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_210

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（数字人/数字人/wanvideo_WanAnimate_V2_1974837982966493186.json、数字人/数字人/wanvideo_WanAnimate_角色替换工作流_1969720507606200322.json、数字人/数字人/视频人物替换-Wan Animate_V2版_1976639386127343617.json、数字人/数字人/长视频 人物替换动作迁移wan2.2-Animate_1976989855852961793.json、视频生成/图生视频/1280P Wan2.2 Animate人物替换【无限时长，跟随运镜】_1981708744444780545.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：54%

## 共有节点

全部 10 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DownloadAndLoadSAM2Model`
- `DrawMaskOnImage`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `LoadImage`
- `Sam2Segmentation`
- `SetNode`
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
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GrowMask` —— 7/10 个有
- `PointsEditor` —— 7/10 个有
- `PoseAndFaceDetection` —— 6/10 个有
- `DWPreprocessor` —— 5/10 个有
- `DrawViTPose` —— 5/10 个有
- `INTConstant` —— 5/10 个有
- `JWInteger` —— 5/10 个有
- `LayerUtility: PurgeVRAM V2` —— 5/10 个有
- `OnnxDetectionModelLoader` —— 5/10 个有
- `FaceMaskFromPoseKeypoints` —— 4/10 个有
- `ImageCropByMaskAndResize` —— 4/10 个有
- `PixelPerfectResolution` —— 4/10 个有
- `easy cleanGpuUsed` —— 4/10 个有
- `easy int` —— 4/10 个有
- `GrowMaskWithBlur` —— 3/10 个有
- `PrimitiveStringMultiline` —— 3/10 个有
- `ACE_ImageFaceCrop` —— 2/10 个有
- `CR Prompt Text` —— 2/10 个有
- `ConvertAny2Int` —— 2/10 个有
- `LayerUtility: PurgeVRAM` —— 2/10 个有
- `RHHiddenNodes` —— 2/10 个有
- `Text` —— 2/10 个有
- `easy float` —— 2/10 个有
- `WanVideoContextOptions` —— 1/10 个有
- `WanVideoTorchCompileSettings` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
