---
name: unknown_workflow_video_lora_sampler_475
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.6574
common_nodes: [ApplyFaceProcessor, FaceProcessorLoader, GetNode, INTConstant, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddStandInLatent, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/AI变身术：把主角换成你：Stand-In+VACE组合_1966014870305017857.json, 视频生成/图生视频/AI替身术：把视频的主角换成另外一个人-视频 换人方案：Stand-In + VACE组合_1963979940653842434.json, 视频生成/图生视频/Stand-In+vace高度人物一致性_1956763019890057217.json, 视频生成/图生视频/wan2.1+stand-in视频人像换脸_1957279872316010498.json, 视频生成/图生视频/【gen全能视频Si】🔥ai易容术stand-in一键换人_1961411519911280642.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_475

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/AI变身术：把主角换成你：Stand-In+VACE组合_1966014870305017857.json、视频生成/图生视频/AI替身术：把视频的主角换成另外一个人-视频 换人方案：Stand-In + VACE组合_1963979940653842434.json、视频生成/图生视频/Stand-In+vace高度人物一致性_1956763019890057217.json、视频生成/图生视频/wan2.1+stand-in视频人像换脸_1957279872316010498.json、视频生成/图生视频/【gen全能视频Si】🔥ai易容术stand-in一键换人_1961411519911280642.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：66%

## 共有节点

全部 5 个 workflow 都包含：
- `ApplyFaceProcessor`
- `FaceProcessorLoader`
- `GetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `SetNode`
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
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoVACEEncode` —— 4/5 个有
- `WanVideoVACEModelSelect` —— 4/5 个有
- `FaceOnlyModeSwitch` —— 3/5 个有
- `HfImageToRGB` —— 3/5 个有
- `VideoFramePreprocessor` —— 3/5 个有
- `VideoInputPreprocessor` —— 3/5 个有
- `AIO_Preprocessor` —— 2/5 个有
- `DWPreprocessor` —— 2/5 个有
- `GetImageRangeFromBatch` —— 2/5 个有
- `ImageCombine` —— 2/5 个有
- `Label (rgthree)` —— 2/5 个有
- `MathExpression|pysssss` —— 2/5 个有
- `RepeatImageBatch` —— 2/5 个有
- `AudioSeparation` —— 1/5 个有
- `CreateVideo` —— 1/5 个有
- `DownloadAndLoadWav2VecModel` —— 1/5 个有
- `MultiTalkModelLoader` —— 1/5 个有
- `MultiTalkWav2VecEmbeds` —— 1/5 个有
- `PreViewVideo` —— 1/5 个有
- `PreviewAudio` —— 1/5 个有
- `WanVideoEmptyEmbeds` —— 1/5 个有
- `WanVideoVACEStartToEndFrame` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
