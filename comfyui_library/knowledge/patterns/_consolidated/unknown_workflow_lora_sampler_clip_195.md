---
name: unknown_workflow_lora_sampler_clip_195
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.835333
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, Seed Everywhere, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/千问Qwen-Image：内容再造引擎，告别重复，高效原创！ 洗图洗稿_8步加速_快速出图_1958917773802024962.json, 图片生成/图生图/千问Qwen-Image：文图互通，创意无限重塑！洗图洗稿重新创作_8步加速、快速出图_1954694622213763074.json, 图片生成/文生图/Qwen-Image：文字即图像，原生中文，细节无敌！文生图_中文_文字直出_通义千问_1954550112557121538.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_195

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/千问Qwen-Image：内容再造引擎，告别重复，高效原创！ 洗图洗稿_8步加速_快速出图_1958917773802024962.json、图片生成/图生图/千问Qwen-Image：文图互通，创意无限重塑！洗图洗稿重新创作_8步加速、快速出图_1954694622213763074.json、图片生成/文生图/Qwen-Image：文字即图像，原生中文，细节无敌！文生图_中文_文字直出_通义千问_1954550112557121538.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `Seed Everywhere`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ImageScaleByAspectRatio_UTK` —— 2/3 个有
- `JWInteger` —— 2/3 个有
- `RH_Captioner` —— 2/3 个有
- `CR Text` —— 1/3 个有
- `RH_LLMAPI_NODE` —— 1/3 个有
- `Switch` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 20 | 3 | 53% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 3 | 29% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 20，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，3 个样本，取值分散，一致性仅 29%
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（4/3 个样本）：Steps较低可能导致细节不足
