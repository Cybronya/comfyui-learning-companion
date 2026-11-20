---
name: unknown_workflow_upscale_latent_upscale_lora_40
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.514222
common_nodes: [CFGGuider, CLIPTextEncode, EmptyLTXVLatentVideo, GetImageSize, GetNode, INTConstant, ImageResizeKJv2, ImageScaleBy, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveFloat, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, SetNode, SimpleCalculatorKJ, VAEDecodeTiled, VAELoader, VAELoaderKJ]
problems: []
missing: []
members: [数字人/数字人/LTX-2.3-数字人_2063143281101459457.json, 数字人/数字人/LTX-2数字人制作教程：一键生成表情口型同步视频！_2014317548833083393.json, 数字人/数字人/LTX-2数字人制作教程：一键生成表情口型同步视频！_2015460028857196546.json, 数字人/数字人/LTX-2数字人换2.3模型 表情口型同步_2019717989897084929.json, 数字人/数字人/LTX2-图-音频生视频-参考放大-V_2025406568388366338.json, 数字人/数字人/用Qwen3-TTS模仿良子配音，搭配LTX-2生成AI漫画短剧！_2015453390020550658.json, 数字人/数字人/高质量LTX-2.3图生视频MV制作工作流（无字幕））_2051561852550828033.json, 视频生成/图生视频/LTX-2.3图生视频MV工作流（双图）_2039169355828695041.json, 视频生成/图生视频/高质量LTX-2.3图生视频MV制作工作流（无字幕））_2017813232496418818.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_40

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（数字人/数字人/LTX-2.3-数字人_2063143281101459457.json、数字人/数字人/LTX-2数字人制作教程：一键生成表情口型同步视频！_2014317548833083393.json、数字人/数字人/LTX-2数字人制作教程：一键生成表情口型同步视频！_2015460028857196546.json、数字人/数字人/LTX-2数字人换2.3模型 表情口型同步_2019717989897084929.json、数字人/数字人/LTX2-图-音频生视频-参考放大-V_2025406568388366338.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：51%

## 共有节点

全部 9 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `GetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `ImageScaleBy`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveFloat`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `SetNode`
- `SimpleCalculatorKJ`
- `VAEDecodeTiled`
- `VAELoader`
- `VAELoaderKJ`

**可变部分**（部分 workflow 才有）：
- `LTXVAudioVAEEncode` —— 8/9 个有
- `LTXVChunkFeedForward` —— 8/9 个有
- `LTXVEmptyLatentAudio` —— 8/9 个有
- `LoadAudio` —— 8/9 个有
- `SetLatentNoiseMask` —— 8/9 个有
- `SolidMask` —— 8/9 个有
- `ComfySwitchNode` —— 7/9 个有
- `DualCLIPLoaderGGUF` —— 7/9 个有
- `PathchSageAttentionKJ` —— 7/9 个有
- `SimpleMath+` —— 7/9 个有
- `TrimAudioDuration` —— 7/9 个有
- `MelBandRoFormerModelLoader` —— 6/9 个有
- `MelBandRoFormerSampler` —— 6/9 个有
- `VHS_VideoCombine` —— 6/9 个有
- `easy showAnything` —— 5/9 个有
- `AudioCrop` —— 4/9 个有
- `LTX2_NAG` —— 4/9 个有
- `UNETLoader` —— 4/9 个有
- `UnetLoaderGGUF` —— 4/9 个有
- `1hew_AudioDuration` —— 3/9 个有
- `ComfyMathExpression` —— 3/9 个有
- `CreateVideo` —— 3/9 个有
- `Label (rgthree)` —— 3/9 个有
- `PreviewAudio` —— 3/9 个有
- `SaveVideo` —— 3/9 个有
- `llama_cpp_instruct_adv` —— 3/9 个有
- `llama_cpp_model_loader` —— 3/9 个有
- `llama_cpp_parameters` —— 3/9 个有
- `Audio Duration (mtb)` —— 2/9 个有
- `CR Prompt Text` —— 2/9 个有
- `DualCLIPLoader` —— 2/9 个有
- `LTX2AudioLatentNormalizingSampling` —— 2/9 个有
- `LTXVImgToVideoInplaceKJ` —— 2/9 个有
- `LoadDiffusionModelShared //Inspire` —— 2/9 个有
- `MuyeTextEditOutput` —— 2/9 个有
- `AudioSeparation` —— 1/9 个有
- `CR Text` —— 1/9 个有
- `CheckpointLoaderSimple` —— 1/9 个有
- `EnhancedLoadDiffusionModel` —— 1/9 个有
- `Fast Groups Bypasser (rgthree)` —— 1/9 个有
- `LTX2SamplingPreviewOverride` —— 1/9 个有
- `Qwen3TTSModelLoader` —— 1/9 个有
- `Qwen3TTSVoiceClone` —— 1/9 个有
- `Seed (rgthree)` —— 1/9 个有
- `Text Multiline` —— 1/9 个有
- `VRAM_Debug` —— 1/9 个有
- `easy imageConcat` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 121 | 97 - 121 | 8 | 93% |
| 高度 | 25 | 25 - 25 | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 121，观测区间 97 - 121，8 个样本，取值集中（一致性 93%）
- 高度 中位数 25，观测区间 25 - 25，8 个样本，取值集中（一致性 100%）
