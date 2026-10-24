---
name: unknown_workflow_upscale_lora_sampler_113
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.872
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, Image Comparer (rgthree), ImageScaleToTotalPixels, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-Seed 超清人像引擎_2093595659097165826.json, 图片生成/文生图/anima2 lora 高清放大Q版卡通画风_2036789720553889793.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_113

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Z-Seed 超清人像引擎_2093595659097165826.json、图片生成/文生图/anima2 lora 高清放大Q版卡通画风_2036789720553889793.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `FloatConstant` —— 1/2 个有
- `ImageSharpenKJ` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `ResolutionSelector` —— 1/2 个有
- `SimpleCalculatorKJ` —— 1/2 个有
- `UnetLoaderGGUF` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 16 | - | 2 | 25% |
| Prompt 约束强度(CFG) | 3 | - | 2 | 33% |
| 采样算法 | euler | - | 2 | 50% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 16，样本不足，未给区间，2 个样本，取值分散，一致性仅 25%
- Prompt 约束强度(CFG) 中位数 3，样本不足，未给区间，2 个样本，取值分散，一致性仅 33%
- 采样算法 最常用 euler，2 个样本，一致性 50%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
