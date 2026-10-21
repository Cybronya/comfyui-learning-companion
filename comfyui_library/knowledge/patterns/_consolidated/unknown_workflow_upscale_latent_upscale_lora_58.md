---
name: unknown_workflow_upscale_latent_upscale_lora_58
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8098
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, ManualSigmas, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SaveVideo, VAEDecodeTiled]
problems: []
missing: []
members: [视频生成/文生视频/LTX 2.3 自动生成播客视频_2035631355412877313.json, 视频生成/文生视频/LTX-2 文生视频官方版_2008956000639918082.json, 视频生成/文生视频/LTX-2 文生视频官方版_2073297832060211201.json, 视频生成/文生视频/LTX-2 文生视频运镜控制_2073298030320775169.json, 视频生成/文生视频/LTX-2 文生视频适配LoRA 1080P_2073300625739313153.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_58

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/文生视频/LTX 2.3 自动生成播客视频_2035631355412877313.json、视频生成/文生视频/LTX-2 文生视频官方版_2008956000639918082.json、视频生成/文生视频/LTX-2 文生视频官方版_2073297832060211201.json、视频生成/文生视频/LTX-2 文生视频运镜控制_2073298030320775169.json、视频生成/文生视频/LTX-2 文生视频适配LoRA 1080P_2073300625739313153.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `CreateVideo`
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
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 4/5 个有
- `GetImageSize` —— 4/5 个有
- `ImageScaleBy` —— 4/5 个有
- `PrimitiveFloat` —— 4/5 个有
- `easy cleanGpuUsed` —— 4/5 个有
- `LTXVScheduler` —— 3/5 个有
- `CR Prompt Text` —— 1/5 个有
- `CR String To Combo` —— 1/5 个有
- `Float to Int` —— 1/5 个有
- `ImpactStringSelector` —— 1/5 个有
- `JWStringReplace` —— 1/5 个有
- `LTXVImgToVideoInplace` —— 1/5 个有
- `LTXVPreprocess` —— 1/5 个有
- `LoadImage` —— 1/5 个有
- `PurgeVRAM_UTK` —— 1/5 个有
- `RH_LLMAPI_NODE` —— 1/5 个有
- `RH_LLMAPI_Pro_Node` —— 1/5 个有
- `ShowAnything|Mie` —— 1/5 个有
- `Switch` —— 1/5 个有
- `TextInput_` —— 1/5 个有
- `easy showAnything` —— 1/5 个有
- `intToFloat _O` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 5 | 100% |
| 高度 | 25 | 25 - 25 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，5 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，5 个样本，取值集中（一致性 100%）
