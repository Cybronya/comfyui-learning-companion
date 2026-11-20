---
name: unknown_workflow_video_upscale_latent_upscale_13
type: Unknown Workflow
frequency: 17
level: strong
coverage: 0.914706
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, ImageScaleBy, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, RandomNoise, SamplerCustomAdvanced, VAEDecode, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/LTX2.0 + VQA 图生视频（48G）_2011995842403635201.json, 视频生成/图生视频/LTX2.0 I2V图生视频直出720P带声音_2008774790064119810.json, 视频生成/图生视频/LTX2.0 丝滑图生视频工作流_2017462120622854146.json, 视频生成/图生视频/LTX2.0 图生视频_2056545383723130882.json, 视频生成/图生视频/LTX2.0 图生视频工作流-48G专用_2008746733387390978.json, 视频生成/图生视频/LTX2.0 图生视频工作流_2014327108255883265.json, 视频生成/图生视频/LTX2.0 图生视频工作流_2014336630131269634.json, 视频生成/图生视频/LTX2.0 图生视频工作流_2014596837386231809.json, 视频生成/图生视频/LTX2.0 图生视频工作流_音画同步（plus48G）_2009533582175375361.json, 视频生成/图生视频/LTX2.0 图生视频工作流（48G）_2008536262742904834.json, 视频生成/图生视频/LTX2.0 图生视频工作流（48G）_2013860991863365633.json, 视频生成/图生视频/LTX2.0 图生视频工作流（48G）中文对白友好_2008824264467685377.json, 视频生成/图生视频/LTX2.0 图生视频工作流（抖音1024_1536_9_16）_2026499302796828674.json, 视频生成/图生视频/LTX2.0 图生视频工作流（自动配音）_2013889078332231681.json, 视频生成/图生视频/LTX2.0 图生音画同步视频+提示词自动润色_2009276516399583233.json, 视频生成/图生视频/LTX2.0图生视频工作流（48G）视频与音频同步生成_2008794813583331330.json, 视频生成/图生视频/LTX2.0图生视频工作流（48G）视频与音频同步生成_2021544395123724290.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_13

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（视频生成/图生视频/LTX2.0 + VQA 图生视频（48G）_2011995842403635201.json、视频生成/图生视频/LTX2.0 I2V图生视频直出720P带声音_2008774790064119810.json、视频生成/图生视频/LTX2.0 丝滑图生视频工作流_2017462120622854146.json、视频生成/图生视频/LTX2.0 图生视频_2056545383723130882.json、视频生成/图生视频/LTX2.0 图生视频工作流-48G专用_2008746733387390978.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 17 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyImage`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `ImageScaleBy`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
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
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecode`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `PrimitiveInt` —— 16/17 个有
- `ResizeImagesByLongerEdge` —— 16/17 个有
- `ImageResizeKJv2` —— 15/17 个有
- `Int` —— 5/17 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/17 个有
- `MathExpression|pysssss` —— 4/17 个有
- `CR Text` —— 3/17 个有
- `DF_Int_to_Float` —— 3/17 个有
- `easy showAnything` —— 3/17 个有
- `GetNode` —— 2/17 个有
- `RH_LLMAPI_NODE` —— 2/17 个有
- `SetNode` —— 2/17 个有
- `AILab_QwenVL` —— 1/17 个有
- `CM_IntToFloat` —— 1/17 个有
- `CR SDXL Aspect Ratio` —— 1/17 个有
- `DF_Text_Box` —— 1/17 个有
- `IntToText` —— 1/17 个有
- `JWInteger` —— 1/17 个有
- `RHHiddenNodes` —— 1/17 个有
- `SaveImage` —— 1/17 个有
- `SimpleMath+` —— 1/17 个有
- `TTP_text_mix` —— 1/17 个有
- `Text` —— 1/17 个有
- `Text Multiline` —— 1/17 个有
- `TextCombinerTwo` —— 1/17 个有
- `VRAMReserver` —— 1/17 个有
- `easy boolean` —— 1/17 个有
- `easy ifElse` —— 1/17 个有
- `easy int` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 17 | 100% |
| 高度 | 25 | 24 - 25 | 17 | 99% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，17 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 24 - 25，17 个样本，取值集中（一致性 99%）
