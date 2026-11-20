---
name: unknown_workflow_sampler_clip_unet_278
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8256
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, KSampler, ResolutionSelector, SaveImage, SkipLayerGuidanceDiTSimple, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/MOSS-Image｜Base vs SFT 双模型同参对决·画质横评版_2114209796613296130.json, 图片生成/文生图/MOSS-Image｜色彩深度LoRA·光影与色彩控制实验版_2114557159357902850.json, 图片生成/文生图/MOSS_Krea2_文生图_2113205128068161538.json, 图片生成/文生图/MOSS_Krea2_文生图_2113240561628049409.json, 图片生成/文生图/Moos文生图 你想要的一切_2113432558376673281.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_278

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/MOSS-Image｜Base vs SFT 双模型同参对决·画质横评版_2114209796613296130.json、图片生成/文生图/MOSS-Image｜色彩深度LoRA·光影与色彩控制实验版_2114557159357902850.json、图片生成/文生图/MOSS_Krea2_文生图_2113205128068161538.json、图片生成/文生图/MOSS_Krea2_文生图_2113240561628049409.json、图片生成/文生图/Moos文生图 你想要的一切_2113432558376673281.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `KSampler`
- `ResolutionSelector`
- `SaveImage`
- `SkipLayerGuidanceDiTSimple`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 4/5 个有
- `Image Comparer (rgthree)` —— 2/5 个有
- `PrimitiveStringMultiline` —— 2/5 个有
- `Anything Everywhere3` —— 1/5 个有
- `GetNode` —— 1/5 个有
- `Seed (rgthree)` —— 1/5 个有
- `SeedNode` —— 1/5 个有
- `SetNode` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 8 - 50 | 5 | 50% |
| Prompt 约束强度(CFG) | 3 | 1 - 3 | 5 | 69% |
| 采样算法 | er_sde | - | 5 | 60% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 25，观测区间 8 - 50，5 个样本，取值分散，一致性仅 50%
- Prompt 约束强度(CFG) 中位数 3，观测区间 1 - 3，5 个样本
- 采样算法 最常用 er_sde，5 个样本，一致性 60%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
