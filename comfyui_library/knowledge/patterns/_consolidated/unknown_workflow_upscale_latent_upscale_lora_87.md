---
name: unknown_workflow_upscale_latent_upscale_lora_87
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9095
common_nodes: [CFGGuider, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLTXVLatentVideo, GetImageSizeAndCount, GetVideoComponents, KSamplerSelect, LTXAddVideoICLoRAGuide, LTXFloatToInt, LTXICLoRALoaderModelOnly, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVSeparateAVLatent, LTXVSetAudioRefTokens, LTXVTiledVAEDecode, LatentUpscaleModelLoader, LoadVideo, LoraLoaderModelOnly, ManualSigmas, RandomNoise, ResizeImageMaskNode, SamplerCustomAdvanced, SaveVideo]
problems: []
missing: []
members: [平台全量/LTX2.3一键去视频字幕_模糊_水印_高清放大_2067962196621086721.json, 音频生成/音频生成/LTX-2.3_ICLoRA_Lipdub V2V 口型同步工作流_2054609608710344705.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_87

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/LTX2.3一键去视频字幕_模糊_水印_高清放大_2067962196621086721.json、音频生成/音频生成/LTX-2.3_ICLoRA_Lipdub V2V 口型同步工作流_2054609608710344705.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `GetImageSizeAndCount`
- `GetVideoComponents`
- `KSamplerSelect`
- `LTXAddVideoICLoRAGuide`
- `LTXFloatToInt`
- `LTXICLoRALoaderModelOnly`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LTXVSetAudioRefTokens`
- `LTXVTiledVAEDecode`
- `LatentUpscaleModelLoader`
- `LoadVideo`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `RandomNoise`
- `ResizeImageMaskNode`
- `SamplerCustomAdvanced`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 1/2 个有
- `DualCLIPLoaderGGUF` —— 1/2 个有
- `Fast Groups Muter (rgthree)` —— 1/2 个有
- `GemmaAPITextEncode` —— 1/2 个有
- `GetImageSize` —— 1/2 个有
- `ImageResizeKJv2` —— 1/2 个有
- `ImageStitch` —— 1/2 个有
- `LTXAVTextEncoderLoader` —— 1/2 个有
- `LTXVAudioVAELoader` —— 1/2 个有
- `PrimitiveString` —— 1/2 个有
- `UNETLoader` —— 1/2 个有
- `VAELoaderKJ` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | - | 2 | 100% |
| 高度 | 25 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
