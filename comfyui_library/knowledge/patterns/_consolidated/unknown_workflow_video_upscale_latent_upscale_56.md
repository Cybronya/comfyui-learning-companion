---
name: unknown_workflow_video_upscale_latent_upscale_56
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.858429
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, ManualSigmas, RandomNoise, SamplerCustomAdvanced, VAEDecodeTiled, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/LTX2文生视频（for creator）_2019245488033239041.json, 视频生成/文生视频/LTXV2.0 T2V文生视频直出1080P带声音_2008772792640081922.json, 视频生成/文生视频/LTXV2.0文生视频-点PLUS运行_2009517391662813186.json, 视频生成/文生视频/LTXV2.0文生视频_2009085511117316097.json, 视频生成/文生视频/LTXV2.0文生视频（48g使用）_2008455790264328193.json, 视频生成/文生视频/LTXV2.0文生视频（48g使用）_2028658389923930113.json, 视频生成/文生视频/Ltx2.3反推提示词 文生音视频_2044962799889162242.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_56

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/文生视频/LTX2文生视频（for creator）_2019245488033239041.json、视频生成/文生视频/LTXV2.0 T2V文生视频直出1080P带声音_2008772792640081922.json、视频生成/文生视频/LTXV2.0文生视频-点PLUS运行_2009517391662813186.json、视频生成/文生视频/LTXV2.0文生视频_2009085511117316097.json、视频生成/文生视频/LTXV2.0文生视频（48g使用）_2008455790264328193.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 6/7 个有
- `GetImageSize` —— 6/7 个有
- `ImageScaleBy` —— 6/7 个有
- `PrimitiveFloat` —— 6/7 个有
- `PrimitiveInt` —— 6/7 个有
- `VAEDecode` —— 4/7 个有
- `CR Text` —— 3/7 个有
- `RH_Translator` —— 3/7 个有
- `CR SDXL Aspect Ratio` —— 1/7 个有
- `DF_Int_to_Float` —— 1/7 个有
- `DualCLIPLoader` —— 1/7 个有
- `ImpactSwitch` —— 1/7 个有
- `JWInteger` —— 1/7 个有
- `LoadImage` —— 1/7 个有
- `MathExpression|pysssss` —— 1/7 个有
- `PreviewAny` —— 1/7 个有
- `RH_LLMAPI_NODE` —— 1/7 个有
- `TextGenerateLTX2Prompt` —— 1/7 个有
- `VRAMReserver` —— 1/7 个有
- `easy showAnything` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 7 | 100% |
| 高度 | 25 | 25 - 25 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，7 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，7 个样本，取值集中（一致性 100%）
