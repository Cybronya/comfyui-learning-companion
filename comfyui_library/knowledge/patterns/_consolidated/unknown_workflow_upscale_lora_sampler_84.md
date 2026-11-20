---
name: unknown_workflow_upscale_lora_sampler_84
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.903
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, CR Text Concatenate, DualCLIPLoader, EmptyLatentImage, FluxSampler, ImageScaleBy, ImageUpscaleWithModel, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/反推提示词/沙雕动画场景{写实转动漫}_超清反推出图_1934615857110949889.json, 图片生成/文生图/沙雕动漫提示词都市动漫图片FLUX_1934960733677658114.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_84

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/反推提示词/沙雕动画场景{写实转动漫}_超清反推出图_1934615857110949889.json、图片生成/文生图/沙雕动漫提示词都市动漫图片FLUX_1934960733677658114.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CR Text Concatenate`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxSampler`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `KSamplerSelect`
- `LoadImage`
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
- `CR Upscale Image` —— 1/2 个有
- `CannyEdgePreprocessor` —— 1/2 个有
- `ControlNetApplyAdvanced` —— 1/2 个有
- `ControlNetLoader` —— 1/2 个有
- `Joy_caption_alpha_load` —— 1/2 个有
- `Joy_caption_alpha_run` —— 1/2 个有
- `PrimitiveString` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有
- `RH_LLMAPI_NODE` —— 1/2 个有
- `SDVN Translate` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1184 | - | 2 | 86% |
| 高度 | 768 | - | 2 | 100% |
| ControlNet 权重 | 0.7 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1184，样本不足，未给区间，2 个样本，取值集中（一致性 86%）
- 高度 中位数 768，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
