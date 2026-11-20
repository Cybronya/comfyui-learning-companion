---
name: unknown_workflow_sampler_clip_unet_125
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.807
common_nodes: [CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLTXVLatentVideo, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, ManualSigmas, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecodeTiled, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/LTX-2.5文生视频（提示词指南）_2087564051504263169.json, 视频生成/文生视频/LTX2.5-文生视频_2087399947888062465.json, 视频生成/文生视频/LTX2.5-文生视频_2087529409245958145.json, 视频生成/文生视频/LTX2.5-文生视频超快工作流_2087433108160344066.json, 视频生成/文生视频/LTX2.5-经典文生视频_2087564635775004674.json, 视频生成/文生视频/LTX2.5_I2V_T2V_2087347078044405762.json, 视频生成/文生视频/LTX2.5图生视频（默认工作流）_2088281770851651585.json, 视频生成/文生视频/Ltx2.5 图_文生视频-双采高清-蒸馏加速_2087683911039143937.json, 视频生成/文生视频/ltx2.5 - 文_图生视频 (2)_2087437692429750274.json, 视频生成/文生视频/ltx2.5双采文生+图生_2087504450205339650.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_125

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/文生视频/LTX-2.5文生视频（提示词指南）_2087564051504263169.json、视频生成/文生视频/LTX2.5-文生视频_2087399947888062465.json、视频生成/文生视频/LTX2.5-文生视频_2087529409245958145.json、视频生成/文生视频/LTX2.5-文生视频超快工作流_2087433108160344066.json、视频生成/文生视频/LTX2.5-经典文生视频_2087564635775004674.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVSeparateAVLatent`
- `ManualSigmas`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LTXVLatentUpsampler` —— 9/10 个有
- `LatentUpscaleModelLoader` —— 9/10 个有
- `PrimitiveStringMultiline` —— 9/10 个有
- `CreateVideo` —— 8/10 个有
- `ResolutionSelector` —— 8/10 个有
- `SaveVideo` —— 8/10 个有
- `LTXVDualCFGGuider` —— 7/10 个有
- `PrimitiveBoolean` —— 6/10 个有
- `LTXVImgToVideoInplace` —— 5/10 个有
- `LTXVPreprocess` —— 5/10 个有
- `LoadImage` —— 5/10 个有
- `ResizeImageMaskNode` —— 5/10 个有
- `TextGenerateLTX2Prompt` —— 5/10 个有
- `ComfySwitchNode` —— 4/10 个有
- `CFGGuider` —— 3/10 个有
- `LTXFloatToInt` —— 3/10 个有
- `PreviewAny` —— 3/10 个有
- `PrimitiveFloat` —— 3/10 个有
- `easy showAnything` —— 3/10 个有
- `CR Text` —— 2/10 个有
- `ComfyNotNode` —— 2/10 个有
- `RH_LLMAPI_Pro_Node` —— 2/10 个有
- `VHS_VideoCombine` —— 2/10 个有
- `Fast Groups Bypasser (rgthree)` —— 1/10 个有
- `Int` —— 1/10 个有
- `LoraLoaderModelOnly` —— 1/10 个有
- `Note Plus (mtb)` —— 1/10 个有
- `PurgeVRAM_UTK` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 121 | 10 | 89% |
| 高度 | 25 | 25 - 25 | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 121，10 个样本，取值集中（一致性 89%）
- 高度 中位数 25，观测区间 25 - 25，10 个样本，取值集中（一致性 100%）
