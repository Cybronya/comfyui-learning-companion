---
name: unknown_workflow_upscale_lora_sampler_21
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8105
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, FluxSampler, ImageScaleBy, ImageUpscaleWithModel, KSamplerSelect, LoraLoaderModelOnly, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: [CR Text Concatenate, SDVN Translate, CR Upscale Image, CR Text, ttN concat]
members: [图片生成/文生图/1934960733677658114.json, 图片生成/文生图/1934978430360592385.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_21

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1934960733677658114.json、图片生成/文生图/1934978430360592385.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：81%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxSampler`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Bjornulf_ShowStringText` —— 1/2 个有
- `CR Text` —— 1/2 个有
- `CR Text Concatenate` —— 1/2 个有
- `CR Upscale Image` —— 1/2 个有
- `DeepTranslatorTextNode` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有
- `RH_LLMAPI_NODE` —— 1/2 个有
- `SDVN Translate` —— 1/2 个有
- `TextInputBasic` —— 1/2 个有
- `ttN concat` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1184 | - | 2 | 86% |
| 高度 | 768 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1184，样本不足，未给区间，2 个样本，取值集中（一致性 86%）
- 高度 中位数 768，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text Concatenate、SDVN Translate、CR Upscale Image、CR Text、ttN concat
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
