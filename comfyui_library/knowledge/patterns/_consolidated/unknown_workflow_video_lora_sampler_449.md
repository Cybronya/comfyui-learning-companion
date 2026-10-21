---
name: unknown_workflow_video_lora_sampler_449
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.7094
common_nodes: [CreateCFGScheduleFloatList, GetNode, HuMoEmbeds, ImageResizeKJv2, LoadAudio, LoadImage, MelBandRoFormerModelLoader, MelBandRoFormerSampler, NormalizeAudioLoudness, PreviewImage, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoTextEncodeCached, WanVideoVAELoader, WhisperModelLoader]
problems: []
missing: []
members: [视频生成/图生视频/1967466923598417921.json, 视频生成/图生视频/1967487607431159809.json, 视频生成/图生视频/1968378350089719809.json, 视频生成/图生视频/1968155104769617921.json, 音频生成/音频生成/单图+语音数字人-字节HuMo多模态数字人(提示+图+音频驱动)_1967050326144638978.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_449

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/1967466923598417921.json、视频生成/图生视频/1967487607431159809.json、视频生成/图生视频/1968378350089719809.json、视频生成/图生视频/1968155104769617921.json、音频生成/音频生成/单图+语音数字人-字节HuMo多模态数字人(提示+图+音频驱动)_1967050326144638978.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：71%

## 共有节点

全部 5 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `GetNode`
- `HuMoEmbeds`
- `ImageResizeKJv2`
- `LoadAudio`
- `LoadImage`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `NormalizeAudioLoudness`
- `PreviewImage`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `WhisperModelLoader`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 4/5 个有
- `ImageBatchMulti` —— 4/5 个有
- `WanVideoSetLoRAs` —— 4/5 个有
- `Audio Duration (mtb)` —— 3/5 个有
- `ImageConcatMulti` —— 3/5 个有
- `IndexTTS2Run` —— 3/5 个有
- `MathExpression|pysssss` —— 3/5 个有
- `PreviewAudio` —— 3/5 个有
- `PrimitiveInt` —— 3/5 个有
- `WanVideoTorchCompileSettings` —— 3/5 个有
- `Label (rgthree)` —— 2/5 个有
- `Text Multiline` —— 2/5 个有
- `easy cleanGpuUsed` —— 2/5 个有
- `EmptyImage` —— 1/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/5 个有
- `PrimitiveStringMultiline` —— 1/5 个有
- `RMBG` —— 1/5 个有
- `WanVideoContextOptions` —— 1/5 个有
- `easy imageRemBg` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
