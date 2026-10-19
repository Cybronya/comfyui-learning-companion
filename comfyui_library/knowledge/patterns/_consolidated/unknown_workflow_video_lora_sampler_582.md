---
name: unknown_workflow_video_lora_sampler_582
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.712
common_nodes: [ApplyFaceProcessor, FaceOnlyModeSwitch, FaceProcessorLoader, GetNode, HfImageToRGB, INTConstant, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, SetNode, VHS_LoadVideo, VHS_VideoCombine, VideoFramePreprocessor, VideoInputPreprocessor, WanVideoAddStandInLatent, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1966014870305017857.json, 视频生成/图生视频/1963979940653842434.json, 视频生成/图生视频/1961411519911280642.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_582

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/1966014870305017857.json、视频生成/图生视频/1963979940653842434.json、视频生成/图生视频/1961411519911280642.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：71%

## 共有节点

全部 3 个 workflow 都包含：
- `ApplyFaceProcessor`
- `FaceOnlyModeSwitch`
- `FaceProcessorLoader`
- `GetNode`
- `HfImageToRGB`
- `INTConstant`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VideoFramePreprocessor`
- `VideoInputPreprocessor`
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
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `DWPreprocessor` —— 2/3 个有
- `GetImageRangeFromBatch` —— 2/3 个有
- `ImageCombine` —— 2/3 个有
- `Label (rgthree)` —— 2/3 个有
- `MathExpression|pysssss` —— 2/3 个有
- `RepeatImageBatch` —— 2/3 个有
- `WanVideoVACEEncode` —— 2/3 个有
- `WanVideoVACEModelSelect` —— 2/3 个有
- `AudioSeparation` —— 1/3 个有
- `CreateVideo` —— 1/3 个有
- `DownloadAndLoadWav2VecModel` —— 1/3 个有
- `MultiTalkModelLoader` —— 1/3 个有
- `MultiTalkWav2VecEmbeds` —— 1/3 个有
- `PreViewVideo` —— 1/3 个有
- `PreviewAudio` —— 1/3 个有
- `WanVideoEmptyEmbeds` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
