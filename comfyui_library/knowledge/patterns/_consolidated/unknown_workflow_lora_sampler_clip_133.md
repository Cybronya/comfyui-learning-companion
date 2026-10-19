---
name: unknown_workflow_lora_sampler_clip_133
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.908
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, ComfyMathExpression, CreateVideo, EmptyLTXVLatentVideo, GemmaAPITextEncode, GetVideoComponents, KSamplerSelect, LTXAVTextEncoderLoader, LTXAddVideoICLoRAGuide, LTXFloatToInt, LTXICLoRALoaderModelOnly, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LTXVTiledVAEDecode, LoadVideo, LoraLoaderModelOnly, ManualSigmas, PrimitiveString, RandomNoise, SamplerCustomAdvanced, SaveVideo]
problems: []
missing: []
members: [视频生成/图生视频/LTX2.3人物动作迁移（视频）_2083198650917941249.json, 音频生成/音频生成/LTX-2.3_ICLoRA_Lipdub V2V 口型同步工作流_2054609608710344705.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_133

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/LTX2.3人物动作迁移（视频）_2083198650917941249.json、音频生成/音频生成/LTX-2.3_ICLoRA_Lipdub V2V 口型同步工作流_2054609608710344705.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `GemmaAPITextEncode`
- `GetVideoComponents`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXAddVideoICLoRAGuide`
- `LTXFloatToInt`
- `LTXICLoRALoaderModelOnly`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVSeparateAVLatent`
- `LTXVTiledVAEDecode`
- `LoadVideo`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveString`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `CannyEdgePreprocessor` —— 1/2 个有
- `DWPreprocessor` —— 1/2 个有
- `GetImageSize` —— 1/2 个有
- `GetImageSizeAndCount` —— 1/2 个有
- `ImageScale` —— 1/2 个有
- `ImageToMask` —— 1/2 个有
- `LTXVAudioVAEEncode` —— 1/2 个有
- `LTXVDilateVideoMask` —— 1/2 个有
- `LTXVImgToVideoConditionOnly` —— 1/2 个有
- `LTXVLaplacianPyramidBlend` —— 1/2 个有
- `LTXVLatentUpsampler` —— 1/2 个有
- `LTXVSetAudioRefTokens` —— 1/2 个有
- `LatentUpscaleModelLoader` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `MaskToImage` —— 1/2 个有
- `PrimitiveBoolean` —— 1/2 个有
- `ResizeImageMaskNode` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有

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
