---
name: unknown_workflow_sampler_clip_unet_133
type: Unknown Workflow
frequency: 9
level: weak
coverage: 0.945778
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen通义千问文生图（中文海报直出）_1953446698997743618.json, 图片生成/文生图/Z-IMAGE文生图--标准版--必收藏_2048436971835498497.json, 图片生成/文生图/Z-IMAGE文生图_2017069432048193538.json, 图片生成/文生图/Z-IMAGE文生图_2033075658359836674.json, 图片生成/文生图/Z-IMAGE文生图_2052276305177133058.json, 图片生成/文生图/Z-Image-Base文生图亮亮丝袜美女_2018164986979295233.json, 图片生成/文生图/Z-Image-Fun- Lora-Distill-4步、8步对比工作流-20倍提速_2025134419132026881.json, 图片生成/文生图/Z-Image-Fun- Lora-Distill-4步工作流-20倍提速-高清放大_2025147553636950017.json, 图片生成/文生图/Z-Image-Fun- Lora-Distill-8步工作流-速度极快-高清放大_2025157935407570946.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_133

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/Qwen通义千问文生图（中文海报直出）_1953446698997743618.json、图片生成/文生图/Z-IMAGE文生图--标准版--必收藏_2048436971835498497.json、图片生成/文生图/Z-IMAGE文生图_2017069432048193538.json、图片生成/文生图/Z-IMAGE文生图_2033075658359836674.json、图片生成/文生图/Z-IMAGE文生图_2052276305177133058.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 5/9 个有
- `Int` —— 4/9 个有
- `ConditioningZeroOut` —— 3/9 个有
- `CustomAddLabel` —— 3/9 个有
- `JjkText` —— 3/9 个有
- `LayerUtility: PurgeVRAM V2` —— 2/9 个有
- `SeedVR2` —— 2/9 个有
- `CR Latent Input Switch` —— 1/9 个有
- `CompressImages` —— 1/9 个有
- `FluxResolutionNode` —— 1/9 个有
- `ImageConcatMulti` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 25 | 9 | 34% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 9 | 29% |
| 采样算法 | euler | - | 9 | 44% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 25，9 个样本，取值分散，一致性仅 34%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，9 个样本，取值分散，一致性仅 29%
- 采样算法 最常用 euler，9 个样本，一致性 44%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（8/9 个样本）：Steps较低可能导致细节不足
