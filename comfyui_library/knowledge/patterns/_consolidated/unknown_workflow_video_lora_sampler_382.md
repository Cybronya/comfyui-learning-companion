---
name: unknown_workflow_video_lora_sampler_382
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.5396
common_nodes: [CLIPVisionLoader, GetNode, ImageConcatMulti, ImageResizeKJv2, Int, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/Wan2.2-Animate_去AI感新版动作迁移，美女跳舞（体型自适应 脸部更一致）_1971077076524638209.json, 视频生成/图生视频/24号特工：快速版舞蹈视频人物替换+节约RH币+节约时间+性价比拉满_2030543201047678977.json, 视频生成/图生视频/4V商用版本 支持 运镜，切镜头，武术，跳舞，侧面迁移，_2093353108847030274.json, 视频生成/图生视频/Wan-Animate 完美复刻官方效果-调参升级版_1969938728464621569.json, 视频生成/图生视频/主体替换调参版本_转身_1980181283542306818.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_382

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Wan2.2-Animate_去AI感新版动作迁移，美女跳舞（体型自适应 脸部更一致）_1971077076524638209.json、视频生成/图生视频/24号特工：快速版舞蹈视频人物替换+节约RH币+节约时间+性价比拉满_2030543201047678977.json、视频生成/图生视频/4V商用版本 支持 运镜，切镜头，武术，跳舞，侧面迁移，_2093353108847030274.json、视频生成/图生视频/Wan-Animate 完美复刻官方效果-调参升级版_1969938728464621569.json、视频生成/图生视频/主体替换调参版本_转身_1980181283542306818.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：54%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPVisionLoader`
- `GetNode`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `Int`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
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
- `BlockifyMask` —— 4/5 个有
- `DownloadAndLoadSAM2Model` —— 4/5 个有
- `DrawMaskOnImage` —— 4/5 个有
- `GrowMask` —— 4/5 个有
- `ImageFromBatch` —— 4/5 个有
- `ImpactInt` —— 4/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `Sam2Segmentation` —— 4/5 个有
- `WanVideoTorchCompileSettings` —— 4/5 个有
- `DrawViTPose` —— 3/5 个有
- `MathExpression|pysssss` —— 3/5 个有
- `Textbox` —— 3/5 个有
- `easy showAnything` —— 3/5 个有
- `BBoxesToSAM2` —— 2/5 个有
- `CR String To Number` —— 2/5 个有
- `DWPreprocessor` —— 2/5 个有
- `DownloadAndLoadQwenModel` —— 2/5 个有
- `FaceMaskFromPoseKeypoints` —— 2/5 个有
- `GetImagesFromBatchIndexed` —— 2/5 个有
- `ImageCropByMaskAndResize` —— 2/5 个有
- `ImpactSwitch` —— 2/5 个有
- `LayerMask: SAM2VideoUltra` —— 2/5 个有
- `LayerUtility: PurgeVRAM V2` —— 2/5 个有
- `QwenVLDetection` —— 2/5 个有
- `TextBoxNode_UTK` —— 2/5 个有
- `VHS_VideoInfo` —— 2/5 个有
- `WanVideoLoraSelect` —— 2/5 个有
- `Anything Everywhere` —— 1/5 个有
- `GemmaAPITextEncode` —— 1/5 个有
- `GetImageSizeAndCount` —— 1/5 个有
- `Image Stitch` —— 1/5 个有
- `PoseRetargetPromptHelper` —— 1/5 个有
- `PrimitiveStringMultiline` —— 1/5 个有
- `RHHiddenNodes` —— 1/5 个有
- `ShellAgentPluginSaveAudios` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
