---
name: unknown_workflow_video_lora_sampler_382
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.723667
common_nodes: [CreateCFGScheduleFloatList, GetNode, HuMoEmbeds, ImageResizeKJv2, LoadAudio, LoadImage, MelBandRoFormerModelLoader, MelBandRoFormerSampler, NormalizeAudioLoudness, PreviewImage, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoTextEncodeCached, WanVideoVAELoader, WhisperModelLoader]
problems: []
missing: []
members: [视频生成/图生视频/1967466923598417921.json, 视频生成/图生视频/1967487607431159809.json, 视频生成/图生视频/1968378350089719809.json, 视频生成/图生视频/1968155104769617921.json, 音频生成/音频生成/单图+语音数字人-字节HuMo多模态数字人(提示+图+音频驱动)_1967050326144638978.json, 音频生成/音频生成/数字人HuMo单人参考数字人V1_1967105592944943105.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_382

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/1967466923598417921.json、视频生成/图生视频/1967487607431159809.json、视频生成/图生视频/1968378350089719809.json、视频生成/图生视频/1968155104769617921.json、音频生成/音频生成/单图+语音数字人-字节HuMo多模态数字人(提示+图+音频驱动)_1967050326144638978.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：72%

## 共有节点

全部 6 个 workflow 都包含：
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
- `INTConstant` —— 5/6 个有
- `ImageBatchMulti` —— 5/6 个有
- `WanVideoSetLoRAs` —— 5/6 个有
- `ImageConcatMulti` —— 4/6 个有
- `MathExpression|pysssss` —— 4/6 个有
- `WanVideoTorchCompileSettings` —— 4/6 个有
- `Audio Duration (mtb)` —— 3/6 个有
- `IndexTTS2Run` —— 3/6 个有
- `PreviewAudio` —— 3/6 个有
- `PrimitiveInt` —— 3/6 个有
- `Label (rgthree)` —— 2/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/6 个有
- `RMBG` —— 2/6 个有
- `Text Multiline` —— 2/6 个有
- `easy cleanGpuUsed` —— 2/6 个有
- `CR Prompt Text` —— 1/6 个有
- `DF_Int_to_Float` —— 1/6 个有
- `EmptyImage` —— 1/6 个有
- `Int` —— 1/6 个有
- `PathchSageAttentionKJ` —— 1/6 个有
- `PrimitiveStringMultiline` —— 1/6 个有
- `WanVideoContextOptions` —— 1/6 个有
- `easy imageRemBg` —— 1/6 个有
- `easy showAnything` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
