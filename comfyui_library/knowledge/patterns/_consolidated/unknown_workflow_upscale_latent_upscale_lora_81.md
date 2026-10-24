---
name: unknown_workflow_upscale_latent_upscale_lora_81
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.853
common_nodes: [Any Switch (rgthree), CFGGuider, CLIPTextEncode, CreateVideo, DualCLIPLoader, EmptyLTXVLatentVideo, ImageListToImageBatch, JsonExtractString, KSamplerSelect, LTXAddVideoICLoRAGuide, LTXTiledSampler, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVMakeRefVideo, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, ManualSigmas, ModelPreviewOverrideKJ, PathchSageAttentionKJ, PreviewAny, PromptRelaySmartEncode, RHLLMChatNode, RandomNoise, RegexMatch, SamplerCustomAdvanced, SaveImage, SaveVideo, SetLatentNoiseMask, SimpleMath+, SimpleMathDual+, SolidMask, TextGenerate, UNETLoader, VAEDecodeTiled, VAELoader, easy audioMerge, easy blocker, easy compare, easy ifElse, easy int, easy lengthAnything, easy multiTrackAddSubtitleToVIdeo, easy multiTrackEditor, easy multiTrackInfoOutput, easy multiTrackTaskOutput, easy promptReplace, easy seed, easy splitImages, easy string]
problems: []
missing: []
members: [视频生成/图生视频/多轨导演台 LTX2.3 MSR V2  多参简易单段_2078136645257351169.json, 视频生成/图生视频/多轨导演台+LTX2.3+MSR+V2++多参简易单段 (1)_2083009294554980353.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_81

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/多轨导演台 LTX2.3 MSR V2  多参简易单段_2078136645257351169.json、视频生成/图生视频/多轨导演台+LTX2.3+MSR+V2++多参简易单段 (1)_2083009294554980353.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CFGGuider`
- `CLIPTextEncode`
- `CreateVideo`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `ImageListToImageBatch`
- `JsonExtractString`
- `KSamplerSelect`
- `LTXAddVideoICLoRAGuide`
- `LTXTiledSampler`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVMakeRefVideo`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `ModelPreviewOverrideKJ`
- `PathchSageAttentionKJ`
- `PreviewAny`
- `PromptRelaySmartEncode`
- `RHLLMChatNode`
- `RandomNoise`
- `RegexMatch`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SaveVideo`
- `SetLatentNoiseMask`
- `SimpleMath+`
- `SimpleMathDual+`
- `SolidMask`
- `TextGenerate`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`
- `easy audioMerge`
- `easy blocker`
- `easy compare`
- `easy ifElse`
- `easy int`
- `easy lengthAnything`
- `easy multiTrackAddSubtitleToVIdeo`
- `easy multiTrackEditor`
- `easy multiTrackInfoOutput`
- `easy multiTrackTaskOutput`
- `easy promptReplace`
- `easy seed`
- `easy splitImages`
- `easy string`

**可变部分**（部分 workflow 才有）：
- `LTXVLatentUpsampler` —— 1/2 个有
- `LTXVLatentUpsamplerTiled` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | - | 2 | 100% |
| 高度 | 24 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 24，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
