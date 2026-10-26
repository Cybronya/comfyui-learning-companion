---
name: unknown_workflow_lora_sampler_clip_249
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9855
common_nodes: [ApplyPulidFlux, BasicGuider, BasicScheduler, CLIPTextEncode, CR Prompt Text, DualCLIPLoader, FluxGuidance, Joy_caption_two, Joy_caption_two_load, KSamplerSelect, LoadImage, LoraLoader, Primitive float [Crystools], Primitive integer [Crystools], PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, PulidFluxModelLoader, RandomNoise, ReroutePrimitive|pysssss, SDXL Empty Latent Image (rgthree), Sampler Selector (Image Saver), SamplerCustomAdvanced, SaveImage, Scheduler Selector (Image Saver), Seed (rgthree), Switch any [Crystools], UNETLoader, UnetLoaderGGUF, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX  PuLID 换脸工作流_1917855752776515585.json, 图片生成/文生图/PuLID for FLUX rl_2027332548585594881.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_249

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/FLUX  PuLID 换脸工作流_1917855752776515585.json、图片生成/文生图/PuLID for FLUX rl_2027332548585594881.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：99%

## 共有节点

全部 2 个 workflow 都包含：
- `ApplyPulidFlux`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CR Prompt Text`
- `DualCLIPLoader`
- `FluxGuidance`
- `Joy_caption_two`
- `Joy_caption_two_load`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoader`
- `Primitive float [Crystools]`
- `Primitive integer [Crystools]`
- `PulidFluxEvaClipLoader`
- `PulidFluxInsightFaceLoader`
- `PulidFluxModelLoader`
- `RandomNoise`
- `ReroutePrimitive|pysssss`
- `SDXL Empty Latent Image (rgthree)`
- `Sampler Selector (Image Saver)`
- `SamplerCustomAdvanced`
- `SaveImage`
- `Scheduler Selector (Image Saver)`
- `Seed (rgthree)`
- `Switch any [Crystools]`
- `UNETLoader`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ShowText|pysssss` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
