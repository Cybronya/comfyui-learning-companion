---
name: unknown_workflow_upscale_latent_upscale_lora_89
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [CFGGuider, CLIPTextEncode, EmptyLTXVLatentVideo, INTConstant, ImageResizeKJv2, KSamplerSelect, LTXAVTextEncoderLoader, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LiconMSR, LoadImage, LoraLoaderModelOnly, LowVRAMCheckpointLoader, ManualSigmas, RandomNoise, SamplerCustomAdvanced, VAEDecodeTiled]
problems: []
missing: []
members: [视频生成/文生视频/LTX-2.3 MSR 多图参考视频生成｜三阶渲染增强版_2065743626793209857.json, 视频生成/文生视频/LTX2.3 3.5套件｜多图锁死·MSR多图参考三阶增强_2068718418597081089.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_89

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/LTX-2.3 MSR 多图参考视频生成｜三阶渲染增强版_2065743626793209857.json、视频生成/文生视频/LTX2.3 3.5套件｜多图锁死·MSR多图参考三阶增强_2068718418597081089.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `EmptyLTXVLatentVideo`
- `INTConstant`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXAddVideoICLoRAGuide`
- `LTXICLoRALoaderModelOnly`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LiconMSR`
- `LoadImage`
- `LoraLoaderModelOnly`
- `LowVRAMCheckpointLoader`
- `ManualSigmas`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 1/2 个有
- `GetImageSize` —— 1/2 个有
- `ImageFromBatch` —— 1/2 个有
- `SaveVideo` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有
- `Text` —— 1/2 个有
- `VHS_VideoCombine` —— 1/2 个有
- `image_scale_pixel_v2` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 751 | - | 2 | 100% |
| 高度 | 24 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 751，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 24，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
