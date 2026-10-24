---
name: unknown_workflow_sampler_clip_unet_47
type: Unknown Workflow
frequency: 17
level: strong
coverage: 0.817824
common_nodes: [CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLTXVLatentVideo, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, ManualSigmas, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecodeTiled, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/LTX-2.5文生视频（提示词指南）_2087564051504263169.json, 视频生成/文生视频/LTX2.5-文生视频_2087399947888062465.json, 视频生成/文生视频/LTX2.5-文生视频_2087529409245958145.json, 视频生成/文生视频/LTX2.5-文生视频超快工作流_2087433108160344066.json, 视频生成/文生视频/LTX2.5-经典文生视频_2087564635775004674.json, 视频生成/文生视频/LTX2.5文生视频-自动扩写提示词-高质量直出1K_2087739530110660610.json, 视频生成/文生视频/LTX2.5文生视频-高质量直出1K_2087559289287303170.json, 视频生成/文生视频/LTX2.5文生视频2608_2095392989672722433.json, 视频生成/文生视频/LTX2.5文生视频_2087332158187859970.json, 视频生成/文生视频/LTX2.5文生视频_2087393833666568193.json, 视频生成/文生视频/LTX2.5文生视频_2087526329527922689.json, 视频生成/文生视频/LTX2.5文生视频_2087539582974906369.json, 视频生成/文生视频/LTX2.5文生视频减油版v1_2087405116231081985.json, 视频生成/文生视频/LTX2.5文生视频极速版_2087431365884207105.json, 视频生成/文生视频/LTX2.5文生视频极速版_2087443856160804866.json, 视频生成/文生视频/LTX2.5文生视频（原生支持4K高清）_2087436136628187138.json, 视频生成/文生视频/LTX2.5文生视频（速度快、像素高）_2087530677137928194.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_47

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（视频生成/文生视频/LTX-2.5文生视频（提示词指南）_2087564051504263169.json、视频生成/文生视频/LTX2.5-文生视频_2087399947888062465.json、视频生成/文生视频/LTX2.5-文生视频_2087529409245958145.json、视频生成/文生视频/LTX2.5-文生视频超快工作流_2087433108160344066.json、视频生成/文生视频/LTX2.5-经典文生视频_2087564635775004674.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 17 个 workflow 都包含：
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
- `LTXVDualCFGGuider` —— 16/17 个有
- `LTXVLatentUpsampler` —— 16/17 个有
- `LatentUpscaleModelLoader` —— 16/17 个有
- `PrimitiveStringMultiline` —— 16/17 个有
- `ResolutionSelector` —— 16/17 个有
- `CreateVideo` —— 14/17 个有
- `SaveVideo` —— 14/17 个有
- `TextGenerateLTX2Prompt` —— 13/17 个有
- `ComfySwitchNode` —— 12/17 个有
- `PreviewAny` —— 11/17 个有
- `PrimitiveBoolean` —— 10/17 个有
- `VHS_VideoCombine` —— 4/17 个有
- `easy showAnything` —— 4/17 个有
- `LoraLoaderModelOnly` —— 3/17 个有
- `RH_LLMAPI_Pro_Node` —— 2/17 个有
- `CFGGuider` —— 1/17 个有
- `CR Prompt Text` —— 1/17 个有
- `CR Text` —— 1/17 个有
- `FlashVSRNode` —— 1/17 个有
- `Int` —— 1/17 个有
- `LTXFloatToInt` —— 1/17 个有
- `PrimitiveFloat` —— 1/17 个有
- `ShellAgentPluginOutputText` —— 1/17 个有
- `孤海注释` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 121 | 17 | 94% |
| 高度 | 25 | 25 - 25 | 17 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 121，17 个样本，取值集中（一致性 94%）
- 高度 中位数 25，观测区间 25 - 25，17 个样本，取值集中（一致性 100%）
