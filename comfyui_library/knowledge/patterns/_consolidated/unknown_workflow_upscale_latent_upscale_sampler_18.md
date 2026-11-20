---
name: unknown_workflow_upscale_latent_upscale_sampler_18
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.804429
common_nodes: [CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLTXVLatentVideo, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, ManualSigmas, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecodeTiled, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/LTX2.5超精简文生视频480P只要1分钟【推荐新手试用】​_2087423274367143937.json, 视频生成/文生视频/Y-video_ltx2_5_t2v_2087478473655939074.json, 视频生成/文生视频/ltx2.5_t2v文生视频_2091808540783636482.json, 视频生成/文生视频/ltx2.5双采文生+图生_2087504450205339650.json, 视频生成/文生视频/video_ltx2_5_t2v_2087405148887928833.json, 视频生成/文生视频/极速 文生视频 LTX2.5 音画同出_2087530875780157441.json, 视频生成/文生视频/阿清的LTX2.5文-图生视频_2090758573637849089.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_sampler_18

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/文生视频/LTX2.5超精简文生视频480P只要1分钟【推荐新手试用】​_2087423274367143937.json、视频生成/文生视频/Y-video_ltx2_5_t2v_2087478473655939074.json、视频生成/文生视频/ltx2.5_t2v文生视频_2091808540783636482.json、视频生成/文生视频/ltx2.5双采文生+图生_2087504450205339650.json、视频生成/文生视频/video_ltx2_5_t2v_2087405148887928833.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `ManualSigmas`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LTXVDualCFGGuider` —— 6/7 个有
- `PrimitiveBoolean` —— 6/7 个有
- `ResolutionSelector` —— 6/7 个有
- `ComfySwitchNode` —— 5/7 个有
- `CreateVideo` —— 5/7 个有
- `SaveVideo` —— 5/7 个有
- `TextGenerateLTX2Prompt` —— 5/7 个有
- `PreviewAny` —— 4/7 个有
- `LoadImage` —— 3/7 个有
- `LTXVImgToVideoInplace` —— 2/7 个有
- `LTXVPreprocess` —— 2/7 个有
- `ResizeImageMaskNode` —— 2/7 个有
- `VHS_VideoCombine` —— 2/7 个有
- `CFGGuider` —— 1/7 个有
- `ComfyNotNode` —— 1/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有
- `LTXFloatToInt` —— 1/7 个有
- `MuyeTextEditOutput` —— 1/7 个有
- `PrimitiveFloat` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 121 | 7 | 92% |
| 高度 | 25 | 25 - 25 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 121，7 个样本，取值集中（一致性 92%）
- 高度 中位数 25，观测区间 25 - 25，7 个样本，取值集中（一致性 100%）
