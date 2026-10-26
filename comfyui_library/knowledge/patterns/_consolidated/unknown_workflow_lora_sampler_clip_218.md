---
name: unknown_workflow_lora_sampler_clip_218
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.960667
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, EmptySD3LatentImage, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UnetLoaderGGUF, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen-ImageQ8+LLM自动扩词_极速地域名人节假日等艺术字_2068271943459102722.json, 图片生成/文生图/文字生成艺术字_2056612699504734210.json, 图片生成/文生图/（贞贞版）Qwen Image 2512 Kook写实人像文生图V1_2007898049535807489.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_218

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Qwen-ImageQ8+LLM自动扩词_极速地域名人节假日等艺术字_2068271943459102722.json、图片生成/文生图/文字生成艺术字_2056612699504734210.json、图片生成/文生图/（贞贞版）Qwen Image 2512 Kook写实人像文生图V1_2007898049535807489.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `EmptySD3LatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: PurgeVRAM V2` —— 2/3 个有
- `RHHiddenNodes` —— 2/3 个有
- `SeedVR2GGUF` —— 2/3 个有
- `ShowText|pysssss` —— 2/3 个有
- `UNETLoader` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 3 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（6/3 个样本）：Steps较低可能导致细节不足
