---
name: unknown_workflow_upscale_latent_upscale_lora_25
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.842583
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, ManualSigmas, RandomNoise, SamplerCustomAdvanced, VAEDecodeTiled]
problems: []
missing: []
members: [视频生成/文生视频/LTX2文生视频（for creator）_2019245488033239041.json, 视频生成/文生视频/LTXV2.0 T2V文生视频直出1080P带声音_2008772792640081922.json, 视频生成/文生视频/LTXV2.0文生视频-点PLUS运行_2009517391662813186.json, 视频生成/文生视频/LTXV2.0文生视频_2008464606221574146.json, 视频生成/文生视频/LTXV2.0文生视频_2009085511117316097.json, 视频生成/文生视频/LTXV2.0文生视频（48g使用）_2008455790264328193.json, 视频生成/文生视频/LTXV2.0文生视频（48g使用）_2028658389923930113.json, 视频生成/文生视频/Ltx2.3反推提示词 文生音视频_2044962799889162242.json, 视频生成/文生视频/Ltx2.3文生音视频官方流FP8_2029911647363538945.json, 视频生成/文生视频/video_ltx2_3_t2v文生视频_2032300523310813186.json, 视频生成/文生视频/用LTX-2大模型轻松制作搞笑祝福视频，ComfyUI工作流教程来啦！_2010631084064641025.json, 视频生成/文生视频/🥗开源视频新秀LTX2.0！【文生视频】工作流🥗_2008810413869244418.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_25

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/文生视频/LTX2文生视频（for creator）_2019245488033239041.json、视频生成/文生视频/LTXV2.0 T2V文生视频直出1080P带声音_2008772792640081922.json、视频生成/文生视频/LTXV2.0文生视频-点PLUS运行_2009517391662813186.json、视频生成/文生视频/LTXV2.0文生视频_2008464606221574146.json、视频生成/文生视频/LTXV2.0文生视频_2009085511117316097.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 12 个 workflow 都包含：
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

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 11/12 个有
- `GetImageSize` —— 11/12 个有
- `ImageScaleBy` —— 11/12 个有
- `PrimitiveFloat` —— 11/12 个有
- `PrimitiveInt` —— 11/12 个有
- `VAEDecode` —— 8/12 个有
- `VHS_VideoCombine` —— 8/12 个有
- `CR Text` —— 4/12 个有
- `CreateVideo` —— 4/12 个有
- `SaveVideo` —— 4/12 个有
- `RH_Translator` —— 3/12 个有
- `PreviewAny` —— 2/12 个有
- `RH_LLMAPI_NODE` —— 2/12 个有
- `TextGenerateLTX2Prompt` —— 2/12 个有
- `easy showAnything` —— 2/12 个有
- `CR SDXL Aspect Ratio` —— 1/12 个有
- `DF_Int_to_Float` —— 1/12 个有
- `DualCLIPLoader` —— 1/12 个有
- `ImpactSwitch` —— 1/12 个有
- `JWInteger` —— 1/12 个有
- `Label (rgthree)` —— 1/12 个有
- `LoadImage` —— 1/12 个有
- `MathExpression|pysssss` —— 1/12 个有
- `Note Plus (mtb)` —— 1/12 个有
- `SimpleMath+` —— 1/12 个有
- `VRAMReserver` —— 1/12 个有
- `easy int` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 12 | 100% |
| 高度 | 25 | 25 - 25 | 12 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，12 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，12 个样本，取值集中（一致性 100%）
