---
name: unknown_workflow_lora_sampler_clip_88
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.7405
common_nodes: [Audio Duration (mtb), AudioEncoderEncode, AudioEncoderLoader, BasicScheduler, CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, ImageBatch, ImageFromBatch, KSamplerSelect, LoadAudio, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, ModelPatchLoader, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, WanInfiniteTalkToVideo, easy forLoopEnd, easy forLoopStart]
problems: []
missing: []
members: [数字人/数字人/infinite_talk_双人官流-长视频-循环-自动版_2018616978436526082.json, 数字人/数字人/infinite数字人-官流长视频循环自动版_2018616944190038017.json, 数字人/数字人/官方循环-infinitetalk_2018923804638056449.json, 视频生成/图生视频/官方循环-infinitetalk_2019285651199369217.json, 视频生成/文生视频/单人InfiniteTalk无限时长原生循环_2018256491320451073.json, 视频生成/文生视频/双人InfiniteTalk无限时长原生循环_2018267797146570753.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_88

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（数字人/数字人/infinite_talk_双人官流-长视频-循环-自动版_2018616978436526082.json、数字人/数字人/infinite数字人-官流长视频循环自动版_2018616944190038017.json、数字人/数字人/官方循环-infinitetalk_2018923804638056449.json、视频生成/图生视频/官方循环-infinitetalk_2019285651199369217.json、视频生成/文生视频/单人InfiniteTalk无限时长原生循环_2018256491320451073.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：74%

## 共有节点

全部 6 个 workflow 都包含：
- `Audio Duration (mtb)`
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `BasicScheduler`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `ImageBatch`
- `ImageFromBatch`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `ModelPatchLoader`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `WanInfiniteTalkToVideo`
- `easy forLoopEnd`
- `easy forLoopStart`

**可变部分**（部分 workflow 才有）：
- `AudioConcat` —— 5/6 个有
- `SimpleMath+` —— 5/6 个有
- `MelBandRoFormerModelLoader` —— 4/6 个有
- `MelBandRoFormerSampler` —— 4/6 个有
- `easy showAnything` —— 4/6 个有
- `AudioCrop` —— 3/6 个有
- `CreateVideo` —— 3/6 个有
- `PreviewAudio` —— 3/6 个有
- `SaveVideo` —— 3/6 个有
- `VHS_VideoCombine` —— 3/6 个有
- `GetNode` —— 2/6 个有
- `LayerUtility: BooleanOperatorV2` —— 2/6 个有
- `LayerUtility: If ` —— 2/6 个有
- `SetNode` —— 2/6 个有
- `SimpleCalculatorKJ` —— 2/6 个有
- `TrimAudioDuration` —— 2/6 个有
- `ImageResizeKJv2` —— 1/6 个有
- `MaskPreview+` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `PrimitiveString` —— 1/6 个有
- `easy sam3ImageSegmentation` —— 1/6 个有
- `easy sam3ModelLoader` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
