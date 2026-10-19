---
name: unknown_workflow_upscale_latent_upscale_sampler
type: Unknown Workflow
frequency: 19
level: strong
coverage: 0.822895
common_nodes: [CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLTXVLatentVideo, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVDualCFGGuider, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, ManualSigmas, PrimitiveInt, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecodeTiled, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/LTX2.5-文生视频_2087529409245958145.json, 视频生成/文生视频/LTX2.5-文生视频超快工作流_2087433108160344066.json, 视频生成/文生视频/LTX2.5-经典文生视频_2087564635775004674.json, 视频生成/文生视频/LTX2.5_I2V_T2V_2087347078044405762.json, 视频生成/文生视频/LTX2.5图生视频（默认工作流）_2088281770851651585.json, 视频生成/文生视频/LTX2.5文生视频-自动扩写提示词-高质量直出1K_2087739530110660610.json, 视频生成/文生视频/LTX2.5文生视频-高质量直出1K_2087559289287303170.json, 视频生成/文生视频/LTX2.5文生视频2608_2095392989672722433.json, 视频生成/文生视频/LTX2.5文生视频_2087332158187859970.json, 视频生成/文生视频/LTX2.5文生视频_2087393833666568193.json, 视频生成/文生视频/LTX2.5文生视频_2087526329527922689.json, 视频生成/文生视频/LTX2.5文生视频_2087539582974906369.json, 视频生成/文生视频/LTX2.5文生视频减油版v1_2087405116231081985.json, 视频生成/文生视频/LTX2.5文生视频极速版_2087431365884207105.json, 视频生成/文生视频/LTX2.5文生视频极速版_2087443856160804866.json, 视频生成/文生视频/LTX2.5文生视频（原生支持4K高清）_2087436136628187138.json, 视频生成/文生视频/LTX2.5文生视频（速度快、像素高）_2087530677137928194.json, 视频生成/文生视频/Ltx2.5 图_文生视频-双采高清-蒸馏加速_2087683911039143937.json, 视频生成/文生视频/阿清的LTX2.5文-图生视频_2090758573637849089.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_sampler

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（视频生成/文生视频/LTX2.5-文生视频_2087529409245958145.json、视频生成/文生视频/LTX2.5-文生视频超快工作流_2087433108160344066.json、视频生成/文生视频/LTX2.5-经典文生视频_2087564635775004674.json、视频生成/文生视频/LTX2.5_I2V_T2V_2087347078044405762.json、视频生成/文生视频/LTX2.5图生视频（默认工作流）_2088281770851651585.json…）

- **类型**：Unknown Workflow
- **样本数**：19
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 19 个 workflow 都包含：
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
- `PrimitiveStringMultiline` —— 17/19 个有
- `CreateVideo` —— 15/19 个有
- `SaveVideo` —— 15/19 个有
- `PrimitiveBoolean` —— 14/19 个有
- `PreviewAny` —— 13/19 个有
- `TextGenerateLTX2Prompt` —— 13/19 个有
- `ComfySwitchNode` —— 12/19 个有
- `VHS_VideoCombine` —— 5/19 个有
- `LTXVImgToVideoInplace` —— 4/19 个有
- `LTXVPreprocess` —— 4/19 个有
- `LoadImage` —— 4/19 个有
- `ResizeImageMaskNode` —— 4/19 个有
- `LoraLoaderModelOnly` —— 3/19 个有
- `RH_LLMAPI_Pro_Node` —— 3/19 个有
- `easy showAnything` —— 3/19 个有
- `CR Text` —— 2/19 个有
- `CR Prompt Text` —— 1/19 个有
- `FlashVSRNode` —— 1/19 个有
- `MuyeTextEditOutput` —— 1/19 个有
- `Note Plus (mtb)` —— 1/19 个有
- `PurgeVRAM_UTK` —— 1/19 个有
- `ShellAgentPluginOutputText` —— 1/19 个有
- `孤海注释` —— 1/19 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 19 | 100% |
| 高度 | 25 | 25 - 25 | 19 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，19 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，19 个样本，取值集中（一致性 100%）
