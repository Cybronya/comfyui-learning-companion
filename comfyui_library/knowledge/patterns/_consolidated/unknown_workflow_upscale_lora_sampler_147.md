---
name: unknown_workflow_upscale_lora_sampler_147
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.84
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, FluxGuidance, ImageUpscaleWithModel, KSamplerSelect, LoraLoaderModelOnly, ModelSamplingFlux, PreviewImage, RH_LLMAPI_NODE, RandomNoise, SamplerCustomAdvanced, SaveImage, UpscaleModelLoader, VAEDecode, easy showAnything]
problems: []
missing: []
members: [图片生成/文生图/可爱四格漫画-一键生成_1933214827978338306.json, 平台全量/四格漫画生成_1993610178333442050.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_147

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/可爱四格漫画-一键生成_1933214827978338306.json、平台全量/四格漫画生成_1993610178333442050.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `FluxGuidance`
- `ImageUpscaleWithModel`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `ModelSamplingFlux`
- `PreviewImage`
- `RH_LLMAPI_NODE`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UpscaleModelLoader`
- `VAEDecode`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR SDXL Aspect Ratio` —— 1/2 个有
- `CR Text` —— 1/2 个有
- `FluxResolutionNode` —— 1/2 个有
- `Int` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有
- `TextBox` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 704 | - | 2 | 100% |
| 高度 | 2048 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 704，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 2048，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
