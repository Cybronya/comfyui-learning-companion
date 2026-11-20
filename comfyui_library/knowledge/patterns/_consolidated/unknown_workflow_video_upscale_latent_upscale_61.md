---
name: unknown_workflow_video_upscale_latent_upscale_61
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.477667
common_nodes: [CFGGuider, CLIPTextEncode, ComfySwitchNode, EmptyLTXVLatentVideo, GetImageSize, GetNode, INTConstant, ImageResizeKJv2, KSamplerSelect, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVConditioning, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, ManualSigmas, MelBandRoFormerModelLoader, MelBandRoFormerSampler, PrimitiveFloat, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, SetLatentNoiseMask, SetNode, SimpleCalculatorKJ, SolidMask, VAEDecodeTiled, VAELoader, VHS_VideoCombine]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [视频生成/图生视频/ACE-Step 1.5 + LTX-2：一键制作MV音乐视频！_2019398568087392257.json, 视频生成/图生视频/LTX-2 一键生成数字人制作表情口型同步视频 对口型对嘴型视频 图片生成数字人视频_2057324612706455554.json, 视频生成/图生视频/LTX-2 一键高效生成数字人制作实时口型同步视频对嘴型对口型音频图片生成数字人视频_2015670036052058114.json, 视频生成/图生视频/LTX-2.3-图-文-音频-生视频_2055521986851418114.json, 视频生成/图生视频/LTX2.3 TI2V Audio 图片音频类数字人(超极速版7分钟20秒视频)_2075071109761949697.json, 视频生成/图生视频/一键制作MV音乐视频！(ACE-Step 1.5 + LTX-2)_2020783511728295938.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_61

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/ACE-Step 1.5 + LTX-2：一键制作MV音乐视频！_2019398568087392257.json、视频生成/图生视频/LTX-2 一键生成数字人制作表情口型同步视频 对口型对嘴型视频 图片生成数字人视频_2057324612706455554.json、视频生成/图生视频/LTX-2 一键高效生成数字人制作实时口型同步视频对嘴型对口型音频图片生成数字人视频_2015670036052058114.json、视频生成/图生视频/LTX-2.3-图-文-音频-生视频_2055521986851418114.json、视频生成/图生视频/LTX2.3 TI2V Audio 图片音频类数字人(超极速版7分钟20秒视频)_2075071109761949697.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：48%

## 共有节点

全部 6 个 workflow 都包含：
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
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
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
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LTXVEmptyLatentAudio` —— 5/6 个有
- `LoraLoaderModelOnly` —— 5/6 个有
- `VAELoaderKJ` —— 5/6 个有
- `DualCLIPLoaderGGUF` —— 4/6 个有
- `LoadAudio` —— 4/6 个有
- `PathchSageAttentionKJ` —— 4/6 个有
- `SimpleMath+` —— 4/6 个有
- `TrimAudioDuration` —— 4/6 个有
- `UnetLoaderGGUF` —— 4/6 个有
- `CheckpointLoaderSimple` —— 3/6 个有
- `ImageScaleBy` —— 3/6 个有
- `LTXVChunkFeedForward` —— 3/6 个有
- `PrimitiveBoolean` —— 3/6 个有
- `ResizeImageMaskNode` —— 3/6 个有
- `UNETLoader` —— 3/6 个有
- `AudioCrop` —— 2/6 个有
- `CR Text` —— 2/6 个有
- `ConditioningZeroOut` —— 2/6 个有
- `EmptyAceStep1.5LatentAudio` —— 2/6 个有
- `KSampler` —— 2/6 个有
- `LTX2SamplingPreviewOverride` —— 2/6 个有
- `LTX2_NAG` —— 2/6 个有
- `ModelPatchTorchSettings` —— 2/6 个有
- `ModelSamplingAuraFlow` —— 2/6 个有
- `PreviewAudio` —— 2/6 个有
- `PrimitiveStringMultiline` —— 2/6 个有
- `SaveAudioMP3` —— 2/6 个有
- `TextEncodeAceStepAudio1.5` —— 2/6 个有
- `VAEDecodeAudio` —— 2/6 个有
- `easy showAnything` —— 2/6 个有
- `Audio Duration (mtb)` —— 1/6 个有
- `DualCLIPLoader` —— 1/6 个有
- `Fast Groups Bypasser (rgthree)` —— 1/6 个有
- `LTXAVTextEncoderLoader` —— 1/6 个有
- `LTXVAudioVAELoader` —— 1/6 个有
- `Label (rgthree)` —— 1/6 个有
- `PainterAudioLength` —— 1/6 个有
- `SaveImage` —— 1/6 个有
- `ShowText|pysssss` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有
- `llama_cpp_instruct_adv` —— 1/6 个有
- `llama_cpp_model_loader` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 121 | 121 - 121 | 5 | 100% |
| 高度 | 25 | 24 - 25 | 5 | 98% |
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 2/6 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 宽度 中位数 121，观测区间 121 - 121，5 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 24 - 25，5 个样本，取值集中（一致性 98%）
- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
