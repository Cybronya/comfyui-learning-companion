---
name: image_to_image_sampler_clip_unet_111
type: Image To Image
frequency: 4
level: moderate
coverage: 0.92725
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Image Comparer (rgthree), KSampler, LoadImage, ModelPatchTorchSettings, PathchSageAttentionKJ, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/FLUX.Klein线稿转效果图洗图一键工作流_2015710449655881729.json, 图片生成/图生图/千府AI-FLUX.2_Klein线稿转效果图一键工作流_2013076463574061058.json, 图片生成/图生图/建筑-Klein效果图洗图工作流_2037902500799451138.json, 图片生成/图生图/线稿生实景图_2111687791036952577.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_111

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/FLUX.Klein线稿转效果图洗图一键工作流_2015710449655881729.json、图片生成/图生图/千府AI-FLUX.2_Klein线稿转效果图一键工作流_2013076463574061058.json、图片生成/图生图/建筑-Klein效果图洗图工作流_2037902500799451138.json、图片生成/图生图/线稿生实景图_2111687791036952577.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text Concatenate` —— 2/4 个有
- `JsonPromptNode` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `Text` —— 2/4 个有
- `KontextArchPresetMain` —— 1/4 个有
- `PreviewAny` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 15.5 | 6 - 25 | 4 | 39% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 15.5，观测区间 6 - 25，4 个样本，取值分散，一致性仅 39%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（2/4 个样本）：Steps较低可能导致细节不足
