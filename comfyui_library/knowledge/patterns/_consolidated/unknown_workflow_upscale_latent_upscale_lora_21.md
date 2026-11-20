---
name: unknown_workflow_upscale_latent_upscale_lora_21
type: Unknown Workflow
frequency: 13
level: strong
coverage: 0.932923
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyLTXVLatentVideo, GetImageSizeAndCount, KSamplerSelect, LTX2SamplingPreviewOverride, LTXAVTextEncoderLoader, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVSeparateAVLatent, LTXVSetAudioRefTokens, LTXVTiledVAEDecode, LatentUpscaleModelLoader, LoadVideoUI, LoraLoaderModelOnly, ManualSigmas, RandomNoise, SamplerCustomAdvanced]
problems: []
missing: []
members: [平台全量/LTX2.3多国语言翻译+视频对口型_2054034912080080898.json, 平台全量/LTX2.3电商带货+语言翻译+重新对口型_2054017156664315906.json, 平台全量/LTX2.3翻译+重新对口型_2053890304427732993.json, 平台全量/LTX2.3翻译+重新对口型_2054451736919724033.json, 平台全量/LTX2.3翻译+重新对口型_2061823158650490881.json, 平台全量/LTX2.3翻译+重新对口型_2083843813629583362.json, 平台全量/余温-文本参考对口型工作流_2114356200736382978.json, 数字人/数字人/人物对口型 LTX2.3_2054520449886900225.json, 数字人/数字人/真人对口型 Ltx2.3 lipdub_2054752281408614401.json, 视频生成/图生视频/LTX2.3翻译+重新对口型_2111401362473963522.json, 视频生成/文生视频/LTX2.3 3.5套件｜换声不换人·RetalkPro视频重说话_2068718437811179522.json, 视频生成/文生视频/视频重说话3.0｜OmniNFT+Relay+蒸馏1.1｜换词对口型_2057730271897800705.json, 音频生成/音频生成/LTX2.3--视频对口型_2054004846319161346.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_21

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（平台全量/LTX2.3多国语言翻译+视频对口型_2054034912080080898.json、平台全量/LTX2.3电商带货+语言翻译+重新对口型_2054017156664315906.json、平台全量/LTX2.3翻译+重新对口型_2053890304427732993.json、平台全量/LTX2.3翻译+重新对口型_2054451736919724033.json、平台全量/LTX2.3翻译+重新对口型_2061823158650490881.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 13 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLTXVLatentVideo`
- `GetImageSizeAndCount`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTXAVTextEncoderLoader`
- `LTXAddVideoICLoRAGuide`
- `LTXICLoRALoaderModelOnly`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAEEncode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LTXVSetAudioRefTokens`
- `LTXVTiledVAEDecode`
- `LatentUpscaleModelLoader`
- `LoadVideoUI`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `RandomNoise`
- `SamplerCustomAdvanced`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 11/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 11/13 个有
- `ResizeImageMaskNode` —— 11/13 个有
- `Text Multiline` —— 11/13 个有
- `easy showAnything` —— 11/13 个有
- `CreateVideo` —— 10/13 个有
- `SaveVideo` —— 10/13 个有
- `Apply Whisper` —— 9/13 个有
- `DeepTranslatorTextNode` —— 9/13 个有
- `easy promptConcat` —— 9/13 个有
- `VHS_VideoCombine` —— 4/13 个有
- `CM_FloatToInt` —— 2/13 个有
- `Float` —— 2/13 个有
- `Image_Resize_longsize` —— 2/13 个有
- `Int` —— 2/13 个有
- `JWImageSequenceExtractFromBatch` —— 2/13 个有
- `LTX2_NAG` —— 2/13 个有
- `PromptRelaySmartEncode` —— 2/13 个有
- `VAELoader` —— 2/13 个有
- `VHS_LoadVideo` —— 2/13 个有
- `image_scale_pixel_v2` —— 2/13 个有
- `VHS_VideoInfo` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 13 | 100% |
| 高度 | 24 | 24 - 24 | 13 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，13 个样本，取值集中（一致性 100%）
- 高度 中位数 24，观测区间 24 - 24，13 个样本，取值集中（一致性 100%）
