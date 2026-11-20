---
name: unknown_workflow_sampler_clip_unet_133
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.8504
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, KSampler, Krea2SizePreset, Krea2StyleReference, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea2 单图风格参考_2074315052915712001.json, 图片生成/图生图/Krea2 单图风格迁移_2074085764102709250.json, 图片生成/图生图/Krea2-真风格迁移（单图）_2081019058392227841.json, 图片生成/图生图/Krea2风格参考_2073729211445108737.json, 图片生成/图生图/Krea2风格参考产品设计_2082828018342522882.json, 图片生成/图生图/[Krea_2_·_08.2]_双图风格迁移_两张参考图，如何控制各自影响？_2098214446819799041.json, 图片生成/文生图/Krea2 风格参考_2073576483880259585.json, 图片生成/文生图/Krea2-风格参考_2073836086790541314.json, 平台全量/Krea2风格转换的设计_2080703174951915522.json, 平台全量/[Krea 2 · 08.1] 风格迁移：不用 LoRA，一张参考图直接迁移视觉风格_2095752635822460930.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_133

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/Krea2 单图风格参考_2074315052915712001.json、图片生成/图生图/Krea2 单图风格迁移_2074085764102709250.json、图片生成/图生图/Krea2-真风格迁移（单图）_2081019058392227841.json、图片生成/图生图/Krea2风格参考_2073729211445108737.json、图片生成/图生图/Krea2风格参考产品设计_2082828018342522882.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `KSampler`
- `Krea2SizePreset`
- `Krea2StyleReference`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Krea2StyleTransfer` —— 9/10 个有
- `PreviewImage` —— 7/10 个有
- `Krea2TwoStyleReferences` —— 4/10 个有
- `Krea2TwoStyleTransfer` —— 4/10 个有
- `Anything Everywhere` —— 2/10 个有
- `Fast Groups Bypasser (rgthree)` —— 2/10 个有
- `GetNode` —— 2/10 个有
- `ImageConcatMulti` —— 2/10 个有
- `PathchSageAttentionKJ` —— 2/10 个有
- `SetNode` —— 2/10 个有
- `ImageStitch` —— 1/10 个有
- `LoraLoaderModelOnly` —— 1/10 个有
- `RH_Translator` —— 1/10 个有
- `Seed (rgthree)` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 10 | 10 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler_ancestral | - | 10 | 100% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 10，10 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足
