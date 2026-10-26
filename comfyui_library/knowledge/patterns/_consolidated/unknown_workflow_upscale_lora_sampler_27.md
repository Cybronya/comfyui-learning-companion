---
name: unknown_workflow_upscale_lora_sampler_27
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.892286
common_nodes: [CFGNorm, CLIPLoader, ConditioningZeroOut, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image Edit 2511动漫转真实_2061721856541020161.json, 图片生成/图生图/Qwen Image Edit 2511单图编辑_2061688951336947713.json, 图片生成/图生图/Qwen Image Edit 2511双图编辑_2061697796184567810.json, 图片生成/图生图/Qwen Image Edit 2511多图编辑_2061708762708275202.json, 图片生成/图生图/Qwen-Edit 2511生活照一键改职业形象照_2061036720539398146.json, 图片生成/图生图/Qwen-Edit 2511生活照职业形象照企业形象照_2057466750949740546.json, 图片生成/图生图/Qwen-Edit 2511生活照职业形象照企业形象照_2062388891402989569.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_27

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Qwen Image Edit 2511动漫转真实_2061721856541020161.json、图片生成/图生图/Qwen Image Edit 2511单图编辑_2061688951336947713.json、图片生成/图生图/Qwen Image Edit 2511双图编辑_2061697796184567810.json、图片生成/图生图/Qwen Image Edit 2511多图编辑_2061708762708275202.json、图片生成/图生图/Qwen-Edit 2511生活照一键改职业形象照_2061036720539398146.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ConditioningZeroOut`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
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
- `Anything Everywhere3` —— 4/7 个有
- `CR Prompt Text` —— 4/7 个有
- `FluxKontextMultiReferenceLatentMethod` —— 4/7 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 4/7 个有
- `Image Comparer (rgthree)` —— 3/7 个有
- `Int` —— 3/7 个有
- `RHHiddenNodes` —— 3/7 个有
- `TextEncodeQwenImageEditPlus_lrzjason` —— 3/7 个有
- `easy positive` —— 3/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 7 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
