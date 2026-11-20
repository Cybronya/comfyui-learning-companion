---
name: unknown_workflow_video_lora_sampler_808
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.836333
common_nodes: [ApplyFaceProcessor, AudioSeparation, DownloadAndLoadWav2VecModel, FaceProcessorLoader, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PreviewImage, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddStandInLatent, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader, easy showAnything]
problems: []
missing: []
members: [平台全量/VACE&InfiniteTalk&StandIn控制+参考+配音+对口型_1959210184050683905.json, 视频生成/图生视频/Stand In+Vace+MultiTalk脸部参考姿势控制语音数字人V1_1956761919991287809.json, 视频生成/图生视频/吴京梗 _ 单人讲话 _ 配音口型同步 _ 动作&表情迁移 _ 采访类视频 V3_1985579275598417922.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_808

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/VACE&InfiniteTalk&StandIn控制+参考+配音+对口型_1959210184050683905.json、视频生成/图生视频/Stand In+Vace+MultiTalk脸部参考姿势控制语音数字人V1_1956761919991287809.json、视频生成/图生视频/吴京梗 _ 单人讲话 _ 配音口型同步 _ 动作&表情迁移 _ 采访类视频 V3_1985579275598417922.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 3 个 workflow 都包含：
- `ApplyFaceProcessor`
- `AudioSeparation`
- `DownloadAndLoadWav2VecModel`
- `FaceProcessorLoader`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PreviewImage`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAddStandInLatent`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 2/3 个有
- `DWPreprocessor` —— 2/3 个有
- `ImageConcatMulti` —— 2/3 个有
- `JWInteger` —— 2/3 个有
- `LayerUtility: PurgeVRAM` —— 2/3 个有
- `LoadAudio` —— 2/3 个有
- `VHS_VideoInfo` —— 2/3 个有
- `WanVideoVACEStartToEndFrame` —— 2/3 个有
- `AudioCrop` —— 1/3 个有
- `AudioToFPS` —— 1/3 个有
- `CM_FloatToInt` —— 1/3 个有
- `DrawViTPose` —— 1/3 个有
- `GetImageSize+` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `OnnxDetectionModelLoader` —— 1/3 个有
- `PoseAndFaceDetection` —— 1/3 个有
- `PreviewAudio` —— 1/3 个有
- `WanVideoTorchCompileSettings` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
