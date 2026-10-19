---
name: unknown_workflow_upscale_latent_upscale_lora_22
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.787545
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, ImageScaleBy, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, ManualSigmas, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, VAEDecodeTiled]
problems: []
missing: []
members: [视频生成/文生视频/LTX2.0文生视频-48G专用_2008734330729795586.json, 视频生成/文生视频/LTX2.0文生视频1080p_2022249801970098177.json, 视频生成/文生视频/LTX2.0文生视频V1_2008526831959412737.json, 视频生成/文生视频/LTX2.0文生视频_2008480312854056962.json, 视频生成/文生视频/LTX2.0文生视频_2009184025579098114.json, 视频生成/文生视频/LTX2.0文生视频（48g使用）视频与音频同步生成_2008803878514462721.json, 视频生成/文生视频/LTX2.0文生视频（plus）_2009269100320661506.json, 视频生成/文生视频/LTX2.0智能提示词动态强化运镜加速低显存版文生视频V1_2009271528722010113.json, 视频生成/文生视频/LTX2.0蒸馏模型1080p文生视频（48G使用）_2008441572072890370.json, 视频生成/文生视频/LTX2.0蒸馏模型1080p文生视频（48G使用）_2042529454865522690.json, 视频生成/文生视频/LTX2.0音视频同步-文生视频_2009172721598472194.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_22

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/文生视频/LTX2.0文生视频-48G专用_2008734330729795586.json、视频生成/文生视频/LTX2.0文生视频1080p_2022249801970098177.json、视频生成/文生视频/LTX2.0文生视频V1_2008526831959412737.json、视频生成/文生视频/LTX2.0文生视频_2008480312854056962.json、视频生成/文生视频/LTX2.0文生视频_2009184025579098114.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 11 个 workflow 都包含：
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
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `PrimitiveFloat` —— 10/11 个有
- `LTXVCropGuides` —— 8/11 个有
- `LTXVScheduler` —— 8/11 个有
- `SaveVideo` —— 8/11 个有
- `VAEDecode` —— 7/11 个有
- `VHS_VideoCombine` —— 6/11 个有
- `CreateVideo` —— 5/11 个有
- `PrimitiveStringMultiline` —— 4/11 个有
- `MathExpression|pysssss` —— 3/11 个有
- `b7c2d337-c38d-4c04-922b-2d638449d13e` —— 3/11 个有
- `ImpactSwitch` —— 2/11 个有
- `Int` —— 2/11 个有
- `RH_LLMAPI_NODE` —— 2/11 个有
- `CR Prompt Text` —— 1/11 个有
- `CR Text` —— 1/11 个有
- `ImpactInt` —— 1/11 个有
- `IntConditions` —— 1/11 个有
- `JWInteger` —— 1/11 个有
- `LayerUtility: PurgeVRAM V2` —— 1/11 个有
- `RH_LLMAPI_Pro_Node` —— 1/11 个有
- `ShowText|pysssss` —— 1/11 个有
- `TextInput_` —— 1/11 个有
- `ToFloat` —— 1/11 个有
- `VRAMReserver` —— 1/11 个有
- `easy anythingIndexSwitch` —— 1/11 个有
- `easy ifElse` —— 1/11 个有
- `easy showAnything` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 121 | 11 | 90% |
| 高度 | 25 | 25 - 25 | 11 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 121，11 个样本，取值集中（一致性 90%）
- 高度 中位数 25，观测区间 25 - 25，11 个样本，取值集中（一致性 100%）
