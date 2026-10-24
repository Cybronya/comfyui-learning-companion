---
name: unknown_workflow_upscale_latent_upscale_lora_20
type: Unknown Workflow
frequency: 13
level: strong
coverage: 0.807462
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, ImageScaleBy, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, ManualSigmas, RandomNoise, SamplerCustomAdvanced, VAEDecodeTiled]
problems: []
missing: []
members: [视频生成/文生视频/LTX2.0文生视频-48G专用_2008734330729795586.json, 视频生成/文生视频/LTX2.0文生视频1080p_2022249801970098177.json, 视频生成/文生视频/LTX2.0文生视频V1_2008526831959412737.json, 视频生成/文生视频/LTX2.0文生视频_2008480312854056962.json, 视频生成/文生视频/LTX2.0文生视频_2009184025579098114.json, 视频生成/文生视频/LTX2.0文生视频（48g使用）视频与音频同步生成_2008803878514462721.json, 视频生成/文生视频/LTX2.0文生视频（plus）_2009269100320661506.json, 视频生成/文生视频/LTX2.0蒸馏模型1080p文生视频（48G使用）_2008441572072890370.json, 视频生成/文生视频/LTX2.0蒸馏模型1080p文生视频（48G使用）_2042529454865522690.json, 视频生成/文生视频/LTX2.0音视频同步-文生视频_2009172721598472194.json, 视频生成/文生视频/文生视频+语音+音乐 LTX2 优化版_2012877844082331650.json, 视频生成/文生视频/文生视频+语音+音乐+LTX2+优化版_2037769306263527425.json, 视频生成/文生视频/🥗开源视频新秀LTX2.0！【文生视频】工作流🥗_2008810413869244418.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_20

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/文生视频/LTX2.0文生视频-48G专用_2008734330729795586.json、视频生成/文生视频/LTX2.0文生视频1080p_2022249801970098177.json、视频生成/文生视频/LTX2.0文生视频V1_2008526831959412737.json、视频生成/文生视频/LTX2.0文生视频_2008480312854056962.json、视频生成/文生视频/LTX2.0文生视频_2009184025579098114.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 13 个 workflow 都包含：
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
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `PrimitiveFloat` —— 12/13 个有
- `PrimitiveInt` —— 11/13 个有
- `LTXVCropGuides` —— 10/13 个有
- `LTXVScheduler` —— 10/13 个有
- `VAEDecode` —— 9/13 个有
- `SaveVideo` —— 8/13 个有
- `VHS_VideoCombine` —— 8/13 个有
- `CreateVideo` —— 5/13 个有
- `MathExpression|pysssss` —— 5/13 个有
- `RH_LLMAPI_NODE` —— 5/13 个有
- `ImpactSwitch` —— 4/13 个有
- `PrimitiveStringMultiline` —— 4/13 个有
- `easy showAnything` —— 4/13 个有
- `ImpactInt` —— 3/13 个有
- `TextInput_` —— 3/13 个有
- `b7c2d337-c38d-4c04-922b-2d638449d13e` —— 3/13 个有
- `CR Text` —— 2/13 个有
- `Int` —— 2/13 个有
- `floatToInt _O` —— 2/13 个有
- `IntConditions` —— 1/13 个有
- `LayerUtility: PurgeVRAM V2` —— 1/13 个有
- `Note Plus (mtb)` —— 1/13 个有
- `ShowText|pysssss` —— 1/13 个有
- `SimpleMath+` —— 1/13 个有
- `ToFloat` —— 1/13 个有
- `easy ifElse` —— 1/13 个有
- `easy int` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 121 | 13 | 90% |
| 高度 | 25 | 25 - 25 | 13 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 121，13 个样本，取值集中（一致性 90%）
- 高度 中位数 25，观测区间 25 - 25，13 个样本，取值集中（一致性 100%）
