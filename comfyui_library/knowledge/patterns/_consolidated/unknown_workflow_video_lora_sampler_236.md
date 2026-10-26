---
name: unknown_workflow_video_lora_sampler_236
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.833333
common_nodes: [CreateCFGScheduleFloatList, HuMoEmbeds, LoadAudio, MelBandRoFormerModelLoader, MelBandRoFormerSampler, NormalizeAudioLoudness, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoTextEncodeCached, WanVideoVAELoader, WhisperModelLoader]
problems: []
missing: []
members: [数字人/数字人/HuMo单音频数字人工作流_1971596152221200385.json, 数字人/数字人/HuMo数字人工作流_1971185989165162498.json, 数字人/数字人/WanVideo21_HuMo数字人_1968481829999267842.json, 数字人/数字人/双图+语音数字人-字节HuMo多模态数字人(提示+图+音频驱动)_1967086191713587201.json, 数字人/数字人/🤖AI数字人新玩法！HuMo模型+IndexTTS2生成自定义口播视频｜ComfyUI全流程教程_1968012276299104257.json, 视频生成/图生视频/IndexTTS2音频生成+Humo数字人_1957726679996399618.json, 视频生成/图生视频/单图+语音-字节HuMo数字人(提示+图+音频驱动)含双图流_1968378350089719809.json, 视频生成/图生视频/单图-数字人-HuMo多模态+TTS数字人(提示+图+音频驱动)_1968155104769617921.json, 音频生成/音频生成/单图+语音数字人-字节HuMo多模态数字人(提示+图+音频驱动)_1967050326144638978.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_236

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（数字人/数字人/HuMo单音频数字人工作流_1971596152221200385.json、数字人/数字人/HuMo数字人工作流_1971185989165162498.json、数字人/数字人/WanVideo21_HuMo数字人_1968481829999267842.json、数字人/数字人/双图+语音数字人-字节HuMo多模态数字人(提示+图+音频驱动)_1967086191713587201.json、数字人/数字人/🤖AI数字人新玩法！HuMo模型+IndexTTS2生成自定义口播视频｜ComfyUI全流程教程_1968012276299104257.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 9 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `HuMoEmbeds`
- `LoadAudio`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `NormalizeAudioLoudness`
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
- `ImageResizeKJv2` —— 8/9 个有
- `LoadImage` —— 8/9 个有
- `WanVideoSetLoRAs` —— 8/9 个有
- `ImageBatchMulti` —— 7/9 个有
- `PreviewImage` —— 7/9 个有
- `WanVideoTorchCompileSettings` —— 7/9 个有
- `GetNode` —— 6/9 个有
- `INTConstant` —— 6/9 个有
- `IndexTTS2Run` —— 6/9 个有
- `PreviewAudio` —— 6/9 个有
- `SetNode` —— 6/9 个有
- `ImageConcatMulti` —— 5/9 个有
- `PrimitiveInt` —— 4/9 个有
- `Text Multiline` —— 3/9 个有
- `Audio Duration (mtb)` —— 2/9 个有
- `Label (rgthree)` —— 2/9 个有
- `MathExpression|pysssss` —— 2/9 个有
- `PrimitiveString` —— 2/9 个有
- `SaveAudio` —— 2/9 个有
- `easy cleanGpuUsed` —— 2/9 个有
- `easy imageRemBg` —— 2/9 个有
- `easy int` —— 2/9 个有
- `ttN text` —— 2/9 个有
- `AudioToFPS` —— 1/9 个有
- `EmptyImage` —— 1/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/9 个有
- `LayerUtility: PurgeVRAM V2` —— 1/9 个有
- `PrimitiveStringMultiline` —— 1/9 个有
- `SimpleMath+` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
