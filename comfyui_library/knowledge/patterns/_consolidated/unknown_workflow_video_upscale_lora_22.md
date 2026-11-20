---
name: unknown_workflow_video_upscale_lora_22
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.459333
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionLoader, CheckpointLoaderSimple, Fast Groups Muter (rgthree), Float to Int, FloatConstant, GetImageSizeAndCount, GetNode, ImageConcatMulti, ImageResizeKJv2, LayerUtility: PurgeVRAM V2, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, PrimitiveInt, RTDETR_detect, SDPoseDrawKeypoints, SDPoseKeypointExtractor, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, SimpleMath+, UNETLoader, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSamplerv2, WanVideoSchedulerv2, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEmbedBridge, WanVideoTorchCompileSettings, WanVideoVAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [平台全量/动作模仿_2084175378117120002.json, 平台全量/陈晨2026-一键直出换装视频（手动分镜）V3(1) (1)(1)_2065316537258569729.json, 视频生成/图生视频/ai女装带货视频_wan2.2 animate人物动作迁移v2_2054814579808587777.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_lora_22

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/动作模仿_2084175378117120002.json、平台全量/陈晨2026-一键直出换装视频（手动分镜）V3(1) (1)(1)_2065316537258569729.json、视频生成/图生视频/ai女装带货视频_wan2.2 animate人物动作迁移v2_2054814579808587777.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：46%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `Fast Groups Muter (rgthree)`
- `Float to Int`
- `FloatConstant`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `PrimitiveInt`
- `RTDETR_detect`
- `SDPoseDrawKeypoints`
- `SDPoseKeypointExtractor`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `SimpleMath+`
- `UNETLoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSamplerv2`
- `WanVideoSchedulerv2`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEmbedBridge`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `WanVideoContextOptions` —— 2/3 个有
- `WanVideoSamplerExtraArgs` —— 2/3 个有
- `Any Switch (rgthree)` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `GetImageRangeFromBatch` —— 1/3 个有
- `LoadImagesFromFolderKJ` —— 1/3 个有
- `MemoryCleaner` —— 1/3 个有
- `MemoryManager` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `PrimitiveStringMultiline` —— 1/3 个有
- `Text Load Line From File` —— 1/3 个有
- `easy anythingIndexSwitch` —— 1/3 个有
- `easy batchAnything` —— 1/3 个有
- `easy forLoopEnd` —— 1/3 个有
- `easy forLoopStart` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
