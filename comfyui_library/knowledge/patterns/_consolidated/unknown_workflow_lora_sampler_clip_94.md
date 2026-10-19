---
name: unknown_workflow_lora_sampler_clip_94
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.516667
common_nodes: [BasicScheduler, CFGGuider, CLIPTextEncode, ComfyNumberConvert, DualCLIPLoader, EmptyLTXVLatentVideo, KSamplerSelect, LTXIdentityOverlapConditioning, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, PreviewAny, PrimitiveFloat, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SimpleCalculatorKJ, StringConcatenate, TextGenerate, UNETLoader, VAEDecode, VAELoaderKJ]
problems: []
missing: []
members: [视频生成/文生视频/LTX2.3-R2V人物参考图-图生视频_2081338352216924161.json, 视频生成/文生视频/LTX2.3_Best-FaceID_文生视频_人物脸部参考_2081784355512471553.json, 视频生成/文生视频/ltx2.3-BFI_2079731636958224385.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_94

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/LTX2.3-R2V人物参考图-图生视频_2081338352216924161.json、视频生成/文生视频/LTX2.3_Best-FaceID_文生视频_人物脸部参考_2081784355512471553.json、视频生成/文生视频/ltx2.3-BFI_2079731636958224385.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：52%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPTextEncode`
- `ComfyNumberConvert`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXIdentityOverlapConditioning`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewAny`
- `PrimitiveFloat`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SimpleCalculatorKJ`
- `StringConcatenate`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoaderKJ`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 2/3 个有
- `GetNode` —— 2/3 个有
- `ImageResizeKJv2` —— 2/3 个有
- `LTX2SamplingPreviewOverride` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `SaveVideo` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `VAELoader` —— 2/3 个有
- `VHS_VideoCombine` —— 2/3 个有
- `AddLabel` —— 1/3 个有
- `ImageConcatMulti` —— 1/3 个有
- `LatentUpscaleModelLoader` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `LoadAudio` —— 1/3 个有
- `ManualSigmas` —— 1/3 个有
- `RecordAudio` —— 1/3 个有
- `SetReserveVRAM` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 3 | 100% |
| 高度 | 25 | 25 - 25 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，3 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，3 个样本，取值集中（一致性 100%）
