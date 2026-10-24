---
name: unknown_workflow_sampler_clip_unet_292
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.84325
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/千问Qwen-Image：内容再造引擎，告别重复，高效原创！ 洗图洗稿_8步加速_快速出图_1958917773802024962.json, 图片生成/图生图/千问Qwen-Image：文图互通，创意无限重塑！洗图洗稿重新创作_8步加速、快速出图_1954694622213763074.json, 图片生成/文生图/Qwen-Image文字海报生成（含图像提示词反推）_1953630061981257729.json, 图片生成/文生图/Qwen-Image：文字即图像，原生中文，细节无敌！文生图_中文_文字直出_通义千问_1954550112557121538.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_292

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/千问Qwen-Image：内容再造引擎，告别重复，高效原创！ 洗图洗稿_8步加速_快速出图_1958917773802024962.json、图片生成/图生图/千问Qwen-Image：文图互通，创意无限重塑！洗图洗稿重新创作_8步加速、快速出图_1954694622213763074.json、图片生成/文生图/Qwen-Image文字海报生成（含图像提示词反推）_1953630061981257729.json、图片生成/文生图/Qwen-Image：文字即图像，原生中文，细节无敌！文生图_中文_文字直出_通义千问_1954550112557121538.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: PurgeVRAM` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `RH_Captioner` —— 3/4 个有
- `Seed Everywhere` —— 3/4 个有
- `ImageScaleByAspectRatio_UTK` —— 2/4 个有
- `JWInteger` —— 2/4 个有
- `CR Text` —— 1/4 个有
- `RH_LLMAPI_NODE` —— 1/4 个有
- `RH_Translator` —— 1/4 个有
- `Switch` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 14 | 8 - 20 | 4 | 57% |
| Prompt 约束强度(CFG) | 1.75 | 1 - 4 | 4 | 41% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | beta | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 14，观测区间 8 - 20，4 个样本
- Prompt 约束强度(CFG) 中位数 1.75，观测区间 1 - 4，4 个样本，取值分散，一致性仅 41%
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 beta，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
