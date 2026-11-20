---
name: unknown_workflow_sampler_clip_vae_67
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.95375
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen-ImageQ8+LLM自动扩词_极速地域名人节假日等艺术字_2068271943459102722.json, 图片生成/文生图/文字生成艺术字_2056612699504734210.json, 图片生成/文生图/（贞贞版）Qwen Image 2512 Kook写实人像文生图V1_2007898049535807489.json, 平台全量/千问艺术字_1965352551178715138.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_67

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Qwen-ImageQ8+LLM自动扩词_极速地域名人节假日等艺术字_2068271943459102722.json、图片生成/文生图/文字生成艺术字_2056612699504734210.json、图片生成/文生图/（贞贞版）Qwen Image 2512 Kook写实人像文生图V1_2007898049535807489.json、平台全量/千问艺术字_1965352551178715138.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `EmptySD3LatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 3/4 个有
- `RHHiddenNodes` —— 3/4 个有
- `ShowText|pysssss` —— 3/4 个有
- `UnetLoaderGGUF` —— 3/4 个有
- `LayerUtility: PurgeVRAM V2` —— 2/4 个有
- `SeedVR2GGUF` —— 2/4 个有
- `NunchakuQwenImageDiTLoader` —— 1/4 个有
- `UNETLoader` —— 1/4 个有
- `easy seed` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 4 | 75% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（7/4 个样本）：Steps较低可能导致细节不足
