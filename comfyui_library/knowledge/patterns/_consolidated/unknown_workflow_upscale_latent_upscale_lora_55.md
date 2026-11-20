---
name: unknown_workflow_upscale_latent_upscale_lora_55
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.798857
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, ManualSigmas, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SaveVideo, VAEDecodeTiled]
problems: []
missing: []
members: [视频生成/文生视频/LTX 2.3 自动生成播客视频_2035631355412877313.json, 视频生成/文生视频/LTX-2 文生视频官方版_2008956000639918082.json, 视频生成/文生视频/LTX-2 文生视频官方版_2073297832060211201.json, 视频生成/文生视频/LTX-2 文生视频运镜控制_2073298030320775169.json, 视频生成/文生视频/LTX-2 文生视频适配LoRA 1080P_2073300625739313153.json, 视频生成/文生视频/LTX-2文生视频ComfyUI官方流快速ltx2模型fp8加速模型带音效_2012003240623218689.json, 视频生成/文生视频/LTX2 文生视频原版自动提示词_2008719056999813121.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_55

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/文生视频/LTX 2.3 自动生成播客视频_2035631355412877313.json、视频生成/文生视频/LTX-2 文生视频官方版_2008956000639918082.json、视频生成/文生视频/LTX-2 文生视频官方版_2073297832060211201.json、视频生成/文生视频/LTX-2 文生视频运镜控制_2073298030320775169.json、视频生成/文生视频/LTX-2 文生视频适配LoRA 1080P_2073300625739313153.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 7 个 workflow 都包含：
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
- `EmptyImage` —— 6/7 个有
- `GetImageSize` —— 6/7 个有
- `ImageScaleBy` —— 6/7 个有
- `PrimitiveFloat` —— 6/7 个有
- `easy cleanGpuUsed` —— 6/7 个有
- `LTXVScheduler` —— 5/7 个有
- `RH_LLMAPI_NODE` —— 2/7 个有
- `CR Prompt Text` —— 1/7 个有
- `CR String To Combo` —— 1/7 个有
- `Float to Int` —— 1/7 个有
- `ImpactStringSelector` —— 1/7 个有
- `JWStringReplace` —— 1/7 个有
- `LTXVImgToVideoInplace` —— 1/7 个有
- `LTXVPreprocess` —— 1/7 个有
- `LoadImage` —— 1/7 个有
- `PreviewAny` —— 1/7 个有
- `PrimitiveStringMultiline` —— 1/7 个有
- `PurgeVRAM_UTK` —— 1/7 个有
- `RH_LLMAPI_Pro_Node` —— 1/7 个有
- `ShowAnything|Mie` —— 1/7 个有
- `Switch` —— 1/7 个有
- `TextInput_` —— 1/7 个有
- `Wan_video_prompt_generator` —— 1/7 个有
- `easy showAnything` —— 1/7 个有
- `intToFloat _O` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 7 | 100% |
| 高度 | 25 | 25 - 25 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，7 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，7 个样本，取值集中（一致性 100%）
