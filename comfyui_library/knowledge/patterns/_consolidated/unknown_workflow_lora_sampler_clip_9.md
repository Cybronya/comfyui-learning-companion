---
name: unknown_workflow_lora_sampler_clip_9
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.676273
common_nodes: [BasicScheduler, CFGGuider, CLIPTextEncode, ComfyNumberConvert, DualCLIPLoader, EmptyLTXVLatentVideo, ImageResizeKJv2, KSamplerSelect, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, PreviewAny, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SimpleCalculatorKJ, StringConcatenate, TextGenerate, VAELoaderKJ]
problems: []
missing: []
members: [数字人/数字人/LTX2.3 BFI+MSR双参数字人（Dasiwa版）_2083776511118766081.json, 视频生成/图生视频/2080683502672105473.json, 视频生成/图生视频/2081230598076719106.json, 视频生成/图生视频/2080669920962105346.json, 视频生成/图生视频/2080951858130153474.json, 视频生成/图生视频/2081226029741465601.json, 视频生成/图生视频/LTX2.3双参BFI+MSR参考生视频V1(Dasiwa版)_2083772098836787201.json, 视频生成/图生视频/2075950261675323393.json, 视频生成/文生视频/LTX-2.3 Best-Face-ID身份参考 IPT2V_2074723965876133889.json, 视频生成/文生视频/LTX-2.3 BestFaceID一致性双采样_2074729921989144578.json, 视频生成/文生视频/LTX2.3 audio+face ID参考视频R2V_2080868375269564418.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_9

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（数字人/数字人/LTX2.3 BFI+MSR双参数字人（Dasiwa版）_2083776511118766081.json、视频生成/图生视频/2080683502672105473.json、视频生成/图生视频/2081230598076719106.json、视频生成/图生视频/2080669920962105346.json、视频生成/图生视频/2080951858130153474.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：68%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPTextEncode`
- `ComfyNumberConvert`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewAny`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SimpleCalculatorKJ`
- `StringConcatenate`
- `TextGenerate`
- `VAELoaderKJ`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 10/11 个有
- `LTXIdentityOverlapConditioning` —— 10/11 个有
- `LTXVAudioVAEDecode` —— 10/11 个有
- `PrimitiveInt` —— 10/11 个有
- `SaveVideo` —— 10/11 个有
- `UNETLoader` —— 10/11 个有
- `VAEDecode` —— 10/11 个有
- `LTX2_NAG` —— 8/11 个有
- `LTXICLoRALoaderModelOnly` —— 7/11 个有
- `LoadAudio` —— 6/11 个有
- `ComfySwitchNode` —— 5/11 个有
- `GetNode` —— 5/11 个有
- `SetNode` —— 5/11 个有
- `VHS_VideoCombine` —— 5/11 个有
- `LTX2SamplingPreviewOverride` —— 4/11 个有
- `LTXVAudioVAEEncode` —— 4/11 个有
- `LTXVLatentUpsampler` —— 4/11 个有
- `LatentUpscaleModelLoader` —— 4/11 个有
- `ManualSigmas` —— 4/11 个有
- `RecordAudio` —— 4/11 个有
- `SetLatentNoiseMask` —— 4/11 个有
- `SolidMask` —— 4/11 个有
- `TrimAudioDuration` —— 4/11 个有
- `ComfyMathExpression` —— 3/11 个有
- `ImageConcatMulti` —— 3/11 个有
- `MelBandRoFormerModelLoader` —— 3/11 个有
- `MelBandRoFormerSampler` —— 3/11 个有
- `VAEDecodeTiled` —— 3/11 个有
- `VAELoader` —— 3/11 个有
- `AddLabel` —— 2/11 个有
- `CropFace` —— 2/11 个有
- `PreviewImage` —— 2/11 个有
- `PrimitiveBoolean` —— 2/11 个有
- `RMBG` —— 2/11 个有
- `ResizeImageMaskNode` —— 2/11 个有
- `SeedGenerator` —— 2/11 个有
- `CheckpointLoaderSimple` —— 1/11 个有
- `Fast Groups Bypasser (rgthree)` —— 1/11 个有
- `GetImageSize` —— 1/11 个有
- `INTConstant` —— 1/11 个有
- `LTX2AttentionTunerPatch` —— 1/11 个有
- `LTX2LoraLoaderAdvanced` —— 1/11 个有
- `LTX2MemoryEfficientSageAttentionPatch` —— 1/11 个有
- `LTXAddVideoICLoRAGuide` —— 1/11 个有
- `LTXIdentityTransfer` —— 1/11 个有
- `LTXVChunkFeedForward` —— 1/11 个有
- `LTXVImgToVideoInplace` —— 1/11 个有
- `LTXVReferenceAudio` —— 1/11 个有
- `ModelSamplingSD3` —— 1/11 个有
- `OpenposePreprocessor` —— 1/11 个有
- `PathchSageAttentionKJ` —— 1/11 个有
- `Power Lora Loader (rgthree)` —— 1/11 个有
- `VAEDecodeAudio` —— 1/11 个有
- `VHS_LoadVideo` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 11 | 100% |
| 高度 | 25 | 25 - 25 | 11 | 100% |
| LoRA 模型强度 | 1.5 | - | 1 | 100% |
| LoRA 文本强度 | 0 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，11 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，11 个样本，取值集中（一致性 100%）
