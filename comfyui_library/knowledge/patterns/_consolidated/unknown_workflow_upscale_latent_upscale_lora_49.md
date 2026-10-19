---
name: unknown_workflow_upscale_latent_upscale_lora_49
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.9538
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyLTXVLatentVideo, GetImageSizeAndCount, KSamplerSelect, LTX2SamplingPreviewOverride, LTXAVTextEncoderLoader, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVSeparateAVLatent, LTXVSetAudioRefTokens, LTXVTiledVAEDecode, LatentUpscaleModelLoader, LoadVideoUI, LoraLoaderModelOnly, ManualSigmas, RandomNoise, SamplerCustomAdvanced]
problems: []
missing: []
members: [数字人/数字人/真人对口型 Ltx2.3 lipdub_2054752281408614401.json, 视频生成/图生视频/LTX2.3翻译+重新对口型_2111401362473963522.json, 视频生成/文生视频/LTX2.3 3.5套件｜换声不换人·RetalkPro视频重说话_2068718437811179522.json, 视频生成/文生视频/视频重说话3.0｜OmniNFT+Relay+蒸馏1.1｜换词对口型_2057730271897800705.json, 音频生成/音频生成/LTX2.3--视频对口型_2054004846319161346.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_49

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（数字人/数字人/真人对口型 Ltx2.3 lipdub_2054752281408614401.json、视频生成/图生视频/LTX2.3翻译+重新对口型_2111401362473963522.json、视频生成/文生视频/LTX2.3 3.5套件｜换声不换人·RetalkPro视频重说话_2068718437811179522.json、视频生成/文生视频/视频重说话3.0｜OmniNFT+Relay+蒸馏1.1｜换词对口型_2057730271897800705.json、音频生成/音频生成/LTX2.3--视频对口型_2054004846319161346.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 5 个 workflow 都包含：
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
- `ComfyMathExpression` —— 4/5 个有
- `easy showAnything` —— 4/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/5 个有
- `ResizeImageMaskNode` —— 3/5 个有
- `Text Multiline` —— 3/5 个有
- `VHS_VideoCombine` —— 3/5 个有
- `Apply Whisper` —— 2/5 个有
- `CreateVideo` —— 2/5 个有
- `DeepTranslatorTextNode` —— 2/5 个有
- `Image_Resize_longsize` —— 2/5 个有
- `JWImageSequenceExtractFromBatch` —— 2/5 个有
- `LTX2_NAG` —— 2/5 个有
- `PromptRelaySmartEncode` —— 2/5 个有
- `SaveVideo` —— 2/5 个有
- `VAELoader` —— 2/5 个有
- `easy promptConcat` —— 2/5 个有
- `image_scale_pixel_v2` —— 2/5 个有
- `CM_FloatToInt` —— 1/5 个有
- `Float` —— 1/5 个有
- `Int` —— 1/5 个有
- `VHS_LoadVideo` —— 1/5 个有
- `VHS_VideoInfo` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 5 | 100% |
| 高度 | 24 | 24 - 24 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，5 个样本，取值集中（一致性 100%）
- 高度 中位数 24，观测区间 24 - 24，5 个样本，取值集中（一致性 100%）
