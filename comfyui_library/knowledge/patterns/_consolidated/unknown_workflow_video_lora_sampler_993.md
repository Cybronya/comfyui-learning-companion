---
name: unknown_workflow_video_lora_sampler_993
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.452
common_nodes: [AIO_Preprocessor, ApplyFaceProcessor, FaceProcessorLoader, GetImageSizeAndCount, GetNode, ImageResizeKJv2, ImpactSwitch, Int, LoadImage, LoadWanVideoT5TextEncoder, Manual XY Entry Info, OnnxDetectionModelLoader, PoseDetectionOneToAllAnimation, PreviewImage, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddStandInLatent, WanVideoBlockSwap, WanVideoContextOptions, WanVideoDecode, WanVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoVACEEncode, WanVideoVAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/🈚️动作迁移_姿势迁移_跳舞_深度参考 wan2.1_2.2 low vace stand in_1949622272819646465.json, 视频生成/图生视频/🈚️动作迁移_姿势迁移_跳舞_深度参考-wan 2.2-vace 2.2 fun+stand in_1967303690803666945.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_993

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/🈚️动作迁移_姿势迁移_跳舞_深度参考 wan2.1_2.2 low vace stand in_1949622272819646465.json、视频生成/图生视频/🈚️动作迁移_姿势迁移_跳舞_深度参考-wan 2.2-vace 2.2 fun+stand in_1967303690803666945.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：45%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `ApplyFaceProcessor`
- `FaceProcessorLoader`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageResizeKJv2`
- `ImpactSwitch`
- `Int`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `Manual XY Entry Info`
- `OnnxDetectionModelLoader`
- `PoseDetectionOneToAllAnimation`
- `PreviewImage`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAddStandInLatent`
- `WanVideoBlockSwap`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoVACEEncode`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/2 个有
- `CR Text Concatenate` —— 1/2 个有
- `CreateCFGScheduleFloatList` —— 1/2 个有
- `LayerUtility: PurgeVRAM V2` —— 1/2 个有
- `RH_Captioner` —— 1/2 个有
- `VHS_DuplicateImages` —— 1/2 个有
- `WanVideoTextEncode` —— 1/2 个有
- `WanVideoTextEncodeSingle` —— 1/2 个有
- `WanVideoVACEModelSelect` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
