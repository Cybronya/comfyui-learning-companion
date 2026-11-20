---
name: unknown_workflow_upscale_latent_upscale_sampler_4
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.825333
common_nodes: [CLIPLoader, CLIPTextEncode, ComfyMathExpression, ComfySwitchNode, EmptyLTXVLatentVideo, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVDualCFGGuider, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, ManualSigmas, PrimitiveBoolean, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecodeTiled, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/LTX 2.5 文生视频版_2094317793788383233.json, 视频生成/文生视频/LTX-2.5 文生视频_2089155568840830977.json, 视频生成/文生视频/LTX-2.5_文生视频T2V·_音画同步生成_2102690657440718849.json, 视频生成/文生视频/LTX-2.5_文生视频T2V·_音画同步生成_2104492526324510722.json, 视频生成/文生视频/LTX2.5  图生视频 二采高清_2100577700896399362.json, 视频生成/文生视频/LTX2.5 二采高清（图生+文生视频）_2087733249475956738.json, 视频生成/文生视频/LTX2.5 图生视频 视频生成  二次采样_2092076309282381825.json, 视频生成/文生视频/LTX2.5 图生视频 视频生成  二次采样_2092080533667926017.json, 视频生成/文生视频/LTX2.5 图生视频_2087377269655425025.json, 视频生成/文生视频/LTX2.5 文生视频_2087431075462213634.json, 视频生成/文生视频/LTX2.5 视频生成 I 提示词强化_2087468290628214785.json, 视频生成/文生视频/Ltx2.5 图_文生视频-双采高清-蒸馏加速_2087683911039143937.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_sampler_4

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/文生视频/LTX 2.5 文生视频版_2094317793788383233.json、视频生成/文生视频/LTX-2.5 文生视频_2089155568840830977.json、视频生成/文生视频/LTX-2.5_文生视频T2V·_音画同步生成_2102690657440718849.json、视频生成/文生视频/LTX-2.5_文生视频T2V·_音画同步生成_2104492526324510722.json、视频生成/文生视频/LTX2.5  图生视频 二采高清_2100577700896399362.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVDualCFGGuider`
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `ManualSigmas`
- `PrimitiveBoolean`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 11/12 个有
- `PrimitiveInt` —— 11/12 个有
- `SaveVideo` —— 11/12 个有
- `PreviewAny` —— 10/12 个有
- `ResolutionSelector` —— 10/12 个有
- `TextGenerateLTX2Prompt` —— 10/12 个有
- `LTXVImgToVideoInplace` —— 8/12 个有
- `LTXVPreprocess` —— 8/12 个有
- `LoadImage` —— 8/12 个有
- `ResizeImageMaskNode` —— 8/12 个有
- `PurgeVRAM_UTK` —— 5/12 个有
- `VHS_VideoCombine` —— 4/12 个有
- `ImageFromBatch` —— 3/12 个有
- `SaveAudio` —— 3/12 个有
- `SaveImage` —— 3/12 个有
- `DisTorchPurgeVRAMV2` —— 2/12 个有
- `llama_cpp_instruct_adv` —— 2/12 个有
- `llama_cpp_model_loader` —— 2/12 个有
- `llama_cpp_parameters` —— 2/12 个有
- `孤海注释` —— 2/12 个有
- `GetImageSize` —— 1/12 个有
- `Int` —— 1/12 个有
- `Note Plus (mtb)` —— 1/12 个有

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
