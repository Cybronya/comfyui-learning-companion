---
name: unknown_workflow_sampler_clip_unet_476
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9365
common_nodes: [CLIPTextEncode, DualCLIPLoader, EmptyHunyuanImageLatent, HunyuanRefinerLatent, KSampler, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/hunyuan_image_2.1 image generation_1968720557237837826.json, 图片生成/文生图/腾讯混元2.1(refiner)文生图_1966005684850651138.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_476

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/hunyuan_image_2.1 image generation_1968720557237837826.json、图片生成/文生图/腾讯混元2.1(refiner)文生图_1966005684850651138.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyHunyuanImageLatent`
- `HunyuanRefinerLatent`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR SDXL Aspect Ratio` —— 1/2 个有
- `Label (rgthree)` —— 1/2 个有
- `LayerUtility: PurgeVRAM V2` —— 1/2 个有
- `RH_Translator` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 12 | - | 2 | 33% |
| Prompt 约束强度(CFG) | 2.25 | - | 2 | 44% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 12，样本不足，未给区间，2 个样本，取值分散，一致性仅 33%
- Prompt 约束强度(CFG) 中位数 2.25，样本不足，未给区间，2 个样本，取值分散，一致性仅 44%
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（3/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
