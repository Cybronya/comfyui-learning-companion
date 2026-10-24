---
name: unknown_workflow_upscale_lora_sampler_57
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.833
common_nodes: [CLIPLoader, CR Text, ConditioningZeroOut, CropWithPadInfo_EditUtils, EditTextEncode_EditUtils, Flux2KleinConfigPreparer_EditUtils, Flux2KleinModelConfig_EditUtils, Flux2KleinOutputExtractor_EditUtils, GetNode, Image Comparer (rgthree), JWImageResizeByLongerSide, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, UNETLoader, VAEDecode, VAELoader, easy imageColorMatch]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/flux2 klein一键无损放大+细节增强_2026965351472304129.json, 图片生成/图生图/flux2_klein一键无损放大+细节增强_2084852240073973762.json, 图片生成/图生图/flux2_klein一键无损放大+细节增强_2084903781879345153.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_57

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/flux2 klein一键无损放大+细节增强_2026965351472304129.json、图片生成/图生图/flux2_klein一键无损放大+细节增强_2084852240073973762.json、图片生成/图生图/flux2_klein一键无损放大+细节增强_2084903781879345153.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CR Text`
- `ConditioningZeroOut`
- `CropWithPadInfo_EditUtils`
- `EditTextEncode_EditUtils`
- `Flux2KleinConfigPreparer_EditUtils`
- `Flux2KleinModelConfig_EditUtils`
- `Flux2KleinOutputExtractor_EditUtils`
- `GetNode`
- `Image Comparer (rgthree)`
- `JWImageResizeByLongerSide`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageColorMatch`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
