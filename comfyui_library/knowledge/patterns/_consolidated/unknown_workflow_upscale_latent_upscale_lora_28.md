---
name: unknown_workflow_upscale_latent_upscale_lora_28
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.8255
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, ComfyMathExpression, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveBoolean, PrimitiveInt, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, SaveVideo, VAEDecodeTiled]
problems: []
missing: []
members: [视频生成/图生视频/2049507628333670402.json, 视频生成/图生视频/2037239092089458690.json, 视频生成/图生视频/2031942296714878977.json, 视频生成/文生视频/AI真人短剧工作流+文生_图生视频_2035632455331356674.json, 视频生成/文生视频/LTX-2.3+Qwen3.5生成宠物播客视频_2030535698637398018.json, 视频生成/文生视频/LTX-2.3+Qwen3.5生成武打电影视频_2030549062293921794.json, 视频生成/文生视频/LTX-2.3龙虾术：把”白狐酱板鸭_视频生成器装进OpenClaw！_2034812167572164610.json, 视频生成/文生视频/LTX2.3文生_图生视频 AI真人短剧工作流_2053318411618398209.json, 视频生成/文生视频/LTX2.3文生_图生视频 AI真人短剧工作流_2054136644139266049.json, 视频生成/文生视频/LTX2.3文生_图生视频_2055972165740179457.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_28

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/2049507628333670402.json、视频生成/图生视频/2037239092089458690.json、视频生成/图生视频/2031942296714878977.json、视频生成/文生视频/AI真人短剧工作流+文生_图生视频_2035632455331356674.json、视频生成/文生视频/LTX-2.3+Qwen3.5生成宠物播客视频_2030535698637398018.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 10 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ComfyMathExpression`
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
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 7/10 个有
- `ResizeImageMaskNode` —— 7/10 个有
- `PreviewAny` —— 6/10 个有
- `RH_LLMAPI_Pro_Node` —— 5/10 个有
- `DeepTranslatorTextNode` —— 4/10 个有
- `Label (rgthree)` —— 4/10 个有
- `easy showAnything` —— 4/10 个有
- `llama_cpp_instruct_adv` —— 4/10 个有
- `llama_cpp_model_loader` —— 4/10 个有
- `llama_cpp_parameters` —— 4/10 个有
- `GetNode` —— 3/10 个有
- `SetNode` —— 3/10 个有
- `StringReplace` —— 3/10 个有
- `string_util_StrConcat` —— 3/10 个有
- `CR Text` —— 2/10 个有
- `ImageResizeKJv2` —— 2/10 个有
- `LTXVImgToVideoInplaceKJ` —— 1/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/10 个有
- `LoraLoader` —— 1/10 个有
- `PrimitiveFloat` —— 1/10 个有
- `TextGenerateLTX2Prompt` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 10 | 100% |
| 高度 | 25 | 25 - 25 | 10 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，10 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，10 个样本，取值集中（一致性 100%）
