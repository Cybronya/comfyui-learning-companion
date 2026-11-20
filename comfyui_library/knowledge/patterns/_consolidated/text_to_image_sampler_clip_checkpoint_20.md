---
name: text_to_image_sampler_clip_checkpoint_20
type: Text To Image
frequency: 4
level: moderate
coverage: 0.97925
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, SaveImage, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/FLUX文生图基础工作流（极速版）_1947277056507793410.json, 图片生成/文生图/FluxDev文生图工作流_1969281537156018177.json, 图片生成/文生图/K2文生图工作流竖版推荐_2082984803409944578.json, 图片生成/文生图/豹豹喵呜制作：K2白玉AIO测试工作流_2082374968163258369.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_20

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/FLUX文生图基础工作流（极速版）_1947277056507793410.json、图片生成/文生图/FluxDev文生图工作流_1969281537156018177.json、图片生成/文生图/K2文生图工作流竖版推荐_2082984803409944578.json、图片生成/文生图/豹豹喵呜制作：K2白玉AIO测试工作流_2082374968163258369.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `LayerColor: Brightness & Contrast` —— 2/4 个有
- `LayerFilter: AddGrain` —— 2/4 个有
- `PathchSageAttentionKJ` —— 2/4 个有
- `FluxGuidance` —— 1/4 个有
- `LoadImage` —— 1/4 个有
- `孤海注释` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 20 | 4 | 53% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 1056 | 768 - 2160 | 4 | 58% |
| 高度 | 1472 | 1024 - 3840 | 4 | 41% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 20，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 1056，观测区间 768 - 2160，4 个样本
- 高度 中位数 1472，观测区间 1024 - 3840，4 个样本，取值分散，一致性仅 41%
- 高发问题（3/4 个样本）：Steps较低可能导致细节不足
