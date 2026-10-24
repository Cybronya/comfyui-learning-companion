---
name: unknown_workflow_upscale_lora_sampler_71
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.752667
common_nodes: [CFGNorm, CLIPLoader, CLIPTextEncode, CR Prompt Text, EmptySD3LatentImage, Image Comparer (rgthree), ImageScaleToTotalPixels, KSampler, LayerUtility: PurgeVRAM, LoraLoaderModelOnly, MemoryCleaner, ModelSamplingAuraFlow, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen Image 2512唯美厚涂插画风文生图+SeedVR2放大（可选）_2020165818063003650.json, 图片生成/文生图/Qwen Image 2512手动提示词文生图+SeedVR2放大V1_2006555012117303298.json, 图片生成/文生图/Qwen Image 2512清晰插画风文生图+SeedVR2放大V1_2019737526575046657.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_71

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Qwen Image 2512唯美厚涂插画风文生图+SeedVR2放大（可选）_2020165818063003650.json、图片生成/文生图/Qwen Image 2512手动提示词文生图+SeedVR2放大V1_2006555012117303298.json、图片生成/文生图/Qwen Image 2512清晰插画风文生图+SeedVR2放大V1_2019737526575046657.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `EmptySD3LatentImage`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LayerUtility: PurgeVRAM`
- `LoraLoaderModelOnly`
- `MemoryCleaner`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Int` —— 2/3 个有
- `LoraLoader` —— 2/3 个有
- `easy promptConcat` —— 2/3 个有
- `CR Text` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | res_2s | - | 3 | 100% |
| 调度器 | beta57 | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，3 个样本，一致性 100%
- 调度器 最常用 beta57，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
