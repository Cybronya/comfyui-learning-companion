---
name: text_to_image_sampler_clip_unet_175
type: Text To Image
frequency: 4
level: strong
coverage: 0.96875
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/z-image随机Prompt.一键生成一组写真_2004923441016958978.json, 图片生成/文生图/文生图-角色生成_2058015180101083138.json, 图片生成/文生图/阿墨AIGC-Z-image-文生图基础工作流_2025764477991391233.json, 图片生成/文生图/麦穗AI-Z-image-文生图基础工作流_2066558941785579521.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_175

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/z-image随机Prompt.一键生成一组写真_2004923441016958978.json、图片生成/文生图/文生图-角色生成_2058015180101083138.json、图片生成/文生图/阿墨AIGC-Z-image-文生图基础工作流_2025764477991391233.json、图片生成/文生图/麦穗AI-Z-image-文生图基础工作流_2066558941785579521.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DPRandomGenerator` —— 1/4 个有
- `easy batchAnything` —— 1/4 个有
- `easy forLoopEnd` —— 1/4 个有
- `easy forLoopStart` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1500 | 1024 - 1920 | 4 | 71% |
| 高度 | 1308 | 1080 - 1920 | 4 | 75% |
| 采样步数 | 9 | 9 - 9 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1500，观测区间 1024 - 1920，4 个样本
- 高度 中位数 1308，观测区间 1080 - 1920，4 个样本
- 采样步数 中位数 9，观测区间 9 - 9，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
