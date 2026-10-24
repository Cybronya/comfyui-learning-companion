---
name: unknown_workflow_sampler_clip_unet_179
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.933
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, KSampler, Krea2SizePreset, Krea2StyleReference, Krea2StyleTransfer, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea2 单图风格参考_2074315052915712001.json, 图片生成/图生图/Krea2 单图风格迁移_2074085764102709250.json, 图片生成/图生图/Krea2-真风格迁移（单图）_2081019058392227841.json, 图片生成/图生图/Krea2单图风格参考Style+Reference+seedvr2超清8K放大_2074739996078206977.json, 图片生成/文生图/Krea2单图风格参考Style Reference+seedvr2超清8K放大_2074388519597989889.json, 图片生成/文生图/Krea2单图风格参考seedvr2超清8K放大_2074756140059152385.json, 图片生成/文生图/krea2风格迁移_2074377841915027457.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_179

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Krea2 单图风格参考_2074315052915712001.json、图片生成/图生图/Krea2 单图风格迁移_2074085764102709250.json、图片生成/图生图/Krea2-真风格迁移（单图）_2081019058392227841.json、图片生成/图生图/Krea2单图风格参考Style+Reference+seedvr2超清8K放大_2074739996078206977.json、图片生成/文生图/Krea2单图风格参考Style Reference+seedvr2超清8K放大_2074388519597989889.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `KSampler`
- `Krea2SizePreset`
- `Krea2StyleReference`
- `Krea2StyleTransfer`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 4/7 个有
- `SeedVR2LoadDiTModel` —— 3/7 个有
- `SeedVR2LoadVAEModel` —— 3/7 个有
- `SeedVR2VideoUpscaler` —— 3/7 个有
- `easy int` —— 3/7 个有
- `PreviewImage` —— 2/7 个有
- `RH_Translator` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 7 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 57% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 57%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
