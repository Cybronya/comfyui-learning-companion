---
name: unknown_workflow_clip_unet_vae_16
type: Unknown Workflow
frequency: 3
level: weak
coverage: 0.924
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Moss-image-洗图工作流_2112880056493240322.json, 图片生成/文生图/ERNIE vs  Z-image 效果对比_2045040847086952449.json, 图片生成/文生图/ERNIE-Image + Z-Image 双采_2045168408412561410.json]
source: knowledge_consolidation
---

# unknown_workflow_clip_unet_vae_16

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Moss-image-洗图工作流_2112880056493240322.json、图片生成/文生图/ERNIE vs  Z-image 效果对比_2045040847086952449.json、图片生成/文生图/ERNIE-Image + Z-Image 双采_2045168408412561410.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 2/3 个有
- `EmptySD3LatentImage` —— 2/3 个有
- `ImageResize+` —— 2/3 个有
- `KSampler` —— 2/3 个有
- `AddLabel` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `ImageConcatMulti` —— 1/3 个有
- `Int` —— 1/3 个有
- `KSamplerAdvanced` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `VAEEncode` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 29 | - | 2 | 28% |
| Prompt 约束强度(CFG) | 4 | 1 - 10 | 3 | 25% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 29，样本不足，未给区间，2 个样本，取值分散，一致性仅 28%
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 10，3 个样本，取值分散，一致性仅 25%
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
