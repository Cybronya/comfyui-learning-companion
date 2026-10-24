---
name: unknown_workflow_video_lora_sampler_786
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.859
common_nodes: [ApplyFaceProcessor, AudioSeparation, CR Text, DownloadAndLoadWav2VecModel, FaceProcessorLoader, ImageResizeKJv2, JWInteger, LayerUtility: PurgeVRAM, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PreviewImage, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoAddStandInLatent, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVACEStartToEndFrame, WanVideoVAELoader, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/Stand In+Vace+MultiTalk脸部参考姿势控制语音数字人V1_1956761919991287809.json, 视频生成/图生视频/吴京梗 _ 单人讲话 _ 配音口型同步 _ 动作&表情迁移 _ 采访类视频 V3_1985579275598417922.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_786

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/Stand In+Vace+MultiTalk脸部参考姿势控制语音数字人V1_1956761919991287809.json、视频生成/图生视频/吴京梗 _ 单人讲话 _ 配音口型同步 _ 动作&表情迁移 _ 采访类视频 V3_1985579275598417922.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `ApplyFaceProcessor`
- `AudioSeparation`
- `CR Text`
- `DownloadAndLoadWav2VecModel`
- `FaceProcessorLoader`
- `ImageResizeKJv2`
- `JWInteger`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PreviewImage`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
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
- `WanVideoVACEStartToEndFrame`
- `WanVideoVAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `AudioToFPS` —— 1/2 个有
- `CM_FloatToInt` —— 1/2 个有
- `DWPreprocessor` —— 1/2 个有
- `DrawViTPose` —— 1/2 个有
- `ImageConcatMulti` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `LoadAudio` —— 1/2 个有
- `OnnxDetectionModelLoader` —— 1/2 个有
- `PoseAndFaceDetection` —— 1/2 个有
- `PreviewAudio` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
