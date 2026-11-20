---
name: unknown_workflow_lora_sampler_clip_252
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.897333
common_nodes: [CLIPTextEncode, CR SDXL Aspect Ratio, CR Text Concatenate, ConditioningZeroOut, ImpactInt, KSampler, Lora Loader Stack (rgthree), ModelSamplingAuraFlow, PreviewImage, SaveImage, Text, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/z-image_超级写实效果。_2047565472735956993.json, 平台全量/Z-Image+seedvr2.5.1放大 极致写实文生图 直生4K_2121124605560713217.json, 平台全量/Z-Image+seedvr2.5.1放大 极致写实文生图 直生4K_2121133480846389250.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_252

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/z-image_超级写实效果。_2047565472735956993.json、平台全量/Z-Image+seedvr2.5.1放大 极致写实文生图 直生4K_2121124605560713217.json、平台全量/Z-Image+seedvr2.5.1放大 极致写实文生图 直生4K_2121133480846389250.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CR SDXL Aspect Ratio`
- `CR Text Concatenate`
- `ConditioningZeroOut`
- `ImpactInt`
- `KSampler`
- `Lora Loader Stack (rgthree)`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 2/3 个有
- `LayerUtility: PurgeVRAM V2` —— 2/3 个有
- `SeedVR2LoadDiTModel` —— 2/3 个有
- `SeedVR2LoadVAEModel` —— 2/3 个有
- `SeedVR2VideoUpscaler` —— 2/3 个有
- `CLIPLoaderGGUF` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 9 - 9 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | res_multistep | - | 3 | 100% |
| 调度器 | sgm_uniform | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 9 - 9，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_multistep，3 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
