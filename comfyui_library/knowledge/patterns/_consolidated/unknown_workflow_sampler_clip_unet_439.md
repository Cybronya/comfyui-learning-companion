---
name: unknown_workflow_sampler_clip_unet_439
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.845333
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2双图-风格参考-融合-迁移Style Reference_2074414607590060034.json, 图片生成/文生图/image_z_image_turbo文生图_2085969344235917313.json, 平台全量/[Krea 2 · 08.2] 双图风格迁移：两张参考图，如何控制各自影响？_2097941829827260417.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_439

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Krea2双图-风格参考-融合-迁移Style Reference_2074414607590060034.json、图片生成/文生图/image_z_image_turbo文生图_2085969344235917313.json、平台全量/[Krea 2 · 08.2] 双图风格迁移：两张参考图，如何控制各自影响？_2097941829827260417.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Krea2SizePreset` —— 2/3 个有
- `Krea2StyleReference` —— 2/3 个有
- `Krea2TwoStyleReferences` —— 2/3 个有
- `Krea2TwoStyleTransfer` —— 2/3 个有
- `Anything Everywhere` —— 1/3 个有
- `GetNode` —— 1/3 个有
- `ModelSamplingAuraFlow` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `SDXLEmptyLatentSizePicker+` —— 1/3 个有
- `SetNode` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 20 | 3 | 53% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler_ancestral | - | 3 | 67% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1024x1024 (1.0) | - | 1 | 100% |
| 高度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 20，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
