---
name: unknown_workflow_upscale_latent_upscale_sampler_3
type: Unknown Workflow
frequency: 18
level: strong
coverage: 0.820278
common_nodes: [CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLTXVLatentVideo, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVDualCFGGuider, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, ManualSigmas, PrimitiveInt, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecodeTiled, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/LTX2.5文生视频-高质量直出1K_2087559289287303170.json, 视频生成/文生视频/LTX2.5文生视频2608_2095392989672722433.json, 视频生成/文生视频/LTX2.5文生视频_2087332158187859970.json, 视频生成/文生视频/LTX2.5文生视频_2087393833666568193.json, 视频生成/文生视频/LTX2.5文生视频_2087526329527922689.json, 视频生成/文生视频/LTX2.5文生视频_2087539582974906369.json, 视频生成/文生视频/LTX2.5文生视频减油版v1_2087405116231081985.json, 视频生成/文生视频/LTX2.5文生视频极速版_2087431365884207105.json, 视频生成/文生视频/LTX2.5文生视频极速版_2087443856160804866.json, 视频生成/文生视频/LTX2.5文生视频（原生支持4K高清）_2087436136628187138.json, 视频生成/文生视频/LTX2.5文生视频（速度快、像素高）_2087530677137928194.json, 视频生成/文生视频/LTX2.5超精简文生视频480P只要1分钟【推荐新手试用】​_2087423274367143937.json, 视频生成/文生视频/Y-video_ltx2_5_t2v_2087478473655939074.json, 视频生成/文生视频/ltx2.5_t2v文生视频_2091808540783636482.json, 视频生成/文生视频/video_ltx2_5_t2v_2087405148887928833.json, 视频生成/文生视频/【开源】LTX2.5 文生视频_2087436423283695618.json, 视频生成/文生视频/极速 文生视频 LTX2.5 音画同出_2087530875780157441.json, 视频生成/文生视频/阿清的LTX2.5文-图生视频_2090758573637849089.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_sampler_3

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（视频生成/文生视频/LTX2.5文生视频-高质量直出1K_2087559289287303170.json、视频生成/文生视频/LTX2.5文生视频2608_2095392989672722433.json、视频生成/文生视频/LTX2.5文生视频_2087332158187859970.json、视频生成/文生视频/LTX2.5文生视频_2087393833666568193.json、视频生成/文生视频/LTX2.5文生视频_2087526329527922689.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 18 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
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
- `PrimitiveInt`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 17/18 个有
- `ComfySwitchNode` —— 14/18 个有
- `CreateVideo` —— 14/18 个有
- `PreviewAny` —— 14/18 个有
- `PrimitiveBoolean` —— 14/18 个有
- `SaveVideo` —— 14/18 个有
- `TextGenerateLTX2Prompt` —— 14/18 个有
- `VHS_VideoCombine` —— 5/18 个有
- `LoadImage` —— 2/18 个有
- `LoraLoaderModelOnly` —— 2/18 个有
- `CR Text` —— 1/18 个有
- `FlashVSRNode` —— 1/18 个有
- `LTXVImgToVideoInplace` —— 1/18 个有
- `LTXVPreprocess` —— 1/18 个有
- `MuyeTextEditOutput` —— 1/18 个有
- `RH_LLMAPI_Pro_Node` —— 1/18 个有
- `ResizeImageMaskNode` —— 1/18 个有
- `Text` —— 1/18 个有
- `easy showAnything` —— 1/18 个有
- `孤海注释` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 18 | 100% |
| 高度 | 25 | 25 - 25 | 18 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，18 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，18 个样本，取值集中（一致性 100%）
