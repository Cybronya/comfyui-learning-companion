---
name: unknown_workflow_sampler_clip_unet_165
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.808556
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, KSampler, PrimitiveStringMultiline, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/MOSS｜真实感暴击 · 人像肌感_2115381303557316610.json, 图片生成/文生图/MOSS｜真实感暴击_·_人像肌感_2115961100352180226.json, 图片生成/文生图/MOSS｜真实感暴击_·_人像肌感_2115972097389457409.json, 图片生成/文生图/Moss Base 更好的光影质感_2115636685873700865.json, 图片生成/文生图/Moss base+sft模型共存_2114927677521088513.json, 图片生成/文生图/Moss 动漫风格 8步文生图_2115995274912034817.json, 图片生成/文生图/Moss 双模8步高质量文生图_2115711030461558785.json, 图片生成/文生图/提示词优化Moss-image Base文生图高质量加速版20261022_2112951536082051073.json, 平台全量/MOSS｜真实感暴击 · 人像肌感_2119603126348115969.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_165

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/MOSS｜真实感暴击 · 人像肌感_2115381303557316610.json、图片生成/文生图/MOSS｜真实感暴击_·_人像肌感_2115961100352180226.json、图片生成/文生图/MOSS｜真实感暴击_·_人像肌感_2115972097389457409.json、图片生成/文生图/Moss Base 更好的光影质感_2115636685873700865.json、图片生成/文生图/Moss base+sft模型共存_2114927677521088513.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `KSampler`
- `PrimitiveStringMultiline`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 7/9 个有
- `MOSSMergePreset` —— 7/9 个有
- `SkipLayerGuidanceDiTSimple` —— 7/9 个有
- `ResolutionSelector` —— 5/9 个有
- `孤海注释` —— 5/9 个有
- `GoohaiRatioAndResolution` —— 4/9 个有
- `Note Plus (mtb)` —— 3/9 个有
- `PreviewAny` —— 2/9 个有
- `MOSSImageBlockCacheT8` —— 1/9 个有
- `MOSSImagePromptEnhancerT8` —— 1/9 个有
- `MOSSPromptEnhancerLocal` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 8 - 50 | 9 | 46% |
| Prompt 约束强度(CFG) | 3.5 | 1 - 3.5 | 9 | 56% |
| 采样算法 | er_sde | - | 9 | 56% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 25，观测区间 8 - 50，9 个样本，取值分散，一致性仅 46%
- Prompt 约束强度(CFG) 中位数 3.5，观测区间 1 - 3.5，9 个样本
- 采样算法 最常用 er_sde，9 个样本，一致性 56%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
