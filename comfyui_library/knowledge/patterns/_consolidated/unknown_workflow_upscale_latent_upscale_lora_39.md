---
name: unknown_workflow_upscale_latent_upscale_lora_39
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.490286
common_nodes: [CFGGuider, CLIPTextEncode, ComfySwitchNode, EmptyLTXVLatentVideo, GetImageSize, GetNode, INTConstant, ImageResizeKJv2, KSamplerSelect, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, MelBandRoFormerModelLoader, MelBandRoFormerSampler, PrimitiveFloat, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, SetLatentNoiseMask, SetNode, SimpleCalculatorKJ, SolidMask, VAEDecodeTiled, VAELoader]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [视频生成/图生视频/2019398568087392257.json, 视频生成/图生视频/2057324612706455554.json, 视频生成/图生视频/LTX-2 一键高效生成数字人制作实时口型同步视频对嘴型对口型音频图片生成数字人视频_2015670036052058114.json, 视频生成/图生视频/2055521986851418114.json, 视频生成/图生视频/2039169355828695041.json, 视频生成/图生视频/2020783511728295938.json, 视频生成/图生视频/2017813232496418818.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_39

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/2019398568087392257.json、视频生成/图生视频/2057324612706455554.json、视频生成/图生视频/LTX-2 一键高效生成数字人制作实时口型同步视频对嘴型对口型音频图片生成数字人视频_2015670036052058114.json、视频生成/图生视频/2055521986851418114.json、视频生成/图生视频/2039169355828695041.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：49%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `ComfySwitchNode`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `GetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `PrimitiveFloat`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SetNode`
- `SimpleCalculatorKJ`
- `SolidMask`
- `VAEDecodeTiled`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DualCLIPLoaderGGUF` —— 6/7 个有
- `SimpleMath+` —— 6/7 个有
- `TrimAudioDuration` —— 6/7 个有
- `VAELoaderKJ` —— 6/7 个有
- `LTXVChunkFeedForward` —— 5/7 个有
- `LoadAudio` —— 5/7 个有
- `PathchSageAttentionKJ` —— 5/7 个有
- `VHS_VideoCombine` —— 5/7 个有
- `ImageScaleBy` —— 4/7 个有
- `UnetLoaderGGUF` —— 4/7 个有
- `AudioCrop` —— 3/7 个有
- `CheckpointLoaderSimple` —— 3/7 个有
- `LTX2_NAG` —— 3/7 个有
- `PrimitiveBoolean` —— 3/7 个有
- `ResizeImageMaskNode` —— 3/7 个有
- `UNETLoader` —— 3/7 个有
- `easy showAnything` —— 3/7 个有
- `1hew_AudioDuration` —— 2/7 个有
- `CR Text` —— 2/7 个有
- `ComfyMathExpression` —— 2/7 个有
- `ConditioningZeroOut` —— 2/7 个有
- `CreateVideo` —— 2/7 个有
- `EmptyAceStep1.5LatentAudio` —— 2/7 个有
- `KSampler` —— 2/7 个有
- `ModelSamplingAuraFlow` —— 2/7 个有
- `PreviewAudio` —— 2/7 个有
- `SaveAudioMP3` —— 2/7 个有
- `SaveVideo` —— 2/7 个有
- `TextEncodeAceStepAudio1.5` —— 2/7 个有
- `VAEDecodeAudio` —— 2/7 个有
- `llama_cpp_instruct_adv` —— 2/7 个有
- `llama_cpp_model_loader` —— 2/7 个有
- `llama_cpp_parameters` —— 2/7 个有
- `Audio Duration (mtb)` —— 1/7 个有
- `CR Prompt Text` —— 1/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有
- `LTX2SamplingPreviewOverride` —— 1/7 个有
- `LTXAVTextEncoderLoader` —— 1/7 个有
- `LTXVAudioVAELoader` —— 1/7 个有
- `LTXVImgToVideoInplaceKJ` —— 1/7 个有
- `Label (rgthree)` —— 1/7 个有
- `LoadDiffusionModelShared //Inspire` —— 1/7 个有
- `ModelPatchTorchSettings` —— 1/7 个有
- `MuyeTextEditOutput` —— 1/7 个有
- `PrimitiveStringMultiline` —— 1/7 个有
- `Text Multiline` —— 1/7 个有
- `easy imageConcat` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 121 | 121 - 121 | 7 | 100% |
| 高度 | 25 | 24 - 25 | 7 | 99% |
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 2/7 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 宽度 中位数 121，观测区间 121 - 121，7 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 24 - 25，7 个样本，取值集中（一致性 99%）
- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
