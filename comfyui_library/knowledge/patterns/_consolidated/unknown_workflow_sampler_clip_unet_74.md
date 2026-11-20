---
name: unknown_workflow_sampler_clip_unet_74
type: Unknown Workflow
frequency: 14
level: strong
coverage: 0.801143
common_nodes: [CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVDualCFGGuider, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, ManualSigmas, PreviewAny, PrimitiveInt, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecodeTiled, VAELoader]
problems: []
missing: []
members: [平台全量/LTX2.5极速图生视频_2120446059276230658.json, 平台全量/Ltx2.5视频自动反推生视频_2089709955942273025.json, 平台全量/ltx2.5-disttilled 文生视频_2117862405958098946.json, 视频生成/图生视频/A-9 LTX-2.5 图生视频（I2V）· 首帧图直接出片 · 音画同步_2087380641817124866.json, 视频生成/图生视频/LTX 2.5 图生视频_2093915637625212929.json, 视频生成/图生视频/LTX-2.5 T2V_I2V单采样_2087377086850883585.json, 视频生成/图生视频/LTX-2.5 T2V_I2V双采样_2087409169308676098.json, 视频生成/图生视频/LTX2.5图生视频_2088701698968743938.json, 视频生成/图生视频/LTX2.5图生视频_2089721005475459074.json, 视频生成/图生视频/LTX2.5图生视频_2090891877334736897.json, 视频生成/图生视频/LTX2.5图生视频（速度快、像素高）_2087522388522127361.json, 视频生成/图生视频/LTX2.5超精简图生视频480P只要2分钟【推荐新手试用】_2087528931011424257.json, 视频生成/图生视频/LTX2.5音画精准匹配+图生视频+尾帧提取+无限时长_2089012468189323266.json, 视频生成/文生视频/LTX2.5音画精准匹配+图生视频+尾帧提取+无限时长_2092080500621004801.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_74

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（平台全量/LTX2.5极速图生视频_2120446059276230658.json、平台全量/Ltx2.5视频自动反推生视频_2089709955942273025.json、平台全量/ltx2.5-disttilled 文生视频_2117862405958098946.json、视频生成/图生视频/A-9 LTX-2.5 图生视频（I2V）· 首帧图直接出片 · 音画同步_2087380641817124866.json、视频生成/图生视频/LTX 2.5 图生视频_2093915637625212929.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVDualCFGGuider`
- `LTXVEmptyLatentAudio`
- `LTXVSeparateAVLatent`
- `ManualSigmas`
- `PreviewAny`
- `PrimitiveInt`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 13/14 个有
- `PrimitiveBoolean` —— 13/14 个有
- `PrimitiveStringMultiline` —— 13/14 个有
- `TextGenerateLTX2Prompt` —— 13/14 个有
- `LTXVImgToVideoInplace` —— 12/14 个有
- `LTXVLatentUpsampler` —— 12/14 个有
- `LTXVPreprocess` —— 12/14 个有
- `LatentUpscaleModelLoader` —— 12/14 个有
- `LoadImage` —— 12/14 个有
- `ResizeImageMaskNode` —— 11/14 个有
- `PreviewImage` —— 3/14 个有
- `VHS_VideoCombine` —— 3/14 个有
- `llama_cpp_instruct_adv` —— 3/14 个有
- `llama_cpp_model_loader` —— 3/14 个有
- `llama_cpp_parameters` —— 3/14 个有
- `CFGGuider` —— 2/14 个有
- `CLIPVisionEncode` —— 2/14 个有
- `CLIPVisionLoader` —— 2/14 个有
- `ComfyNotNode` —— 2/14 个有
- `DualCLIPLoader` —— 2/14 个有
- `Fast Groups Muter (rgthree)` —— 2/14 个有
- `GetVideoComponents` —— 2/14 个有
- `ImageFromBatch+` —— 2/14 个有
- `ImageSizeAndBatchSize` —— 2/14 个有
- `LTXFloatToInt` —— 2/14 个有
- `LoadVideo` —— 2/14 个有
- `PrimitiveFloat` —— 2/14 个有
- `RIFE VFI` —— 2/14 个有
- `GemmaAPITextEncode` —— 1/14 个有
- `ImageFromBatch` —— 1/14 个有
- `SaveAudio` —— 1/14 个有
- `SaveImage` —— 1/14 个有
- `SeedGenerator` —— 1/14 个有
- `StringContains` —— 1/14 个有
- `VHS_LoadVideo` —— 1/14 个有
- `孤海注释` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 121 | 14 | 92% |
| 高度 | 25 | 24 - 25 | 14 | 99% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 121，14 个样本，取值集中（一致性 92%）
- 高度 中位数 25，观测区间 24 - 25，14 个样本，取值集中（一致性 99%）
