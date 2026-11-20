---
name: unknown_workflow_sampler_unet_vae_352
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9165
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, LoadImage, SaveImage, StringToInt, Text, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen image 2.1深度图-线稿-转图片_2112646802997596161.json, 图片生成/图生图/Qwen2.1图像编辑_2101937813171302401.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_352

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Qwen image 2.1深度图-线稿-转图片_2112646802997596161.json、图片生成/图生图/Qwen2.1图像编辑_2101937813171302401.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `StringToInt`
- `Text`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveString` —— 1/2 个有
- `QwenImage21UnionApply` —— 1/2 个有
- `QwenImage21UnionLoader` —— 1/2 个有
- `ResolutionSelector` —— 1/2 个有
- `Seed (rgthree)` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 19 | - | 2 | 42% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 520 | - | 2 | 3% |
| 高度 | 1024 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 19，样本不足，未给区间，2 个样本，取值分散，一致性仅 42%
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 520，样本不足，未给区间，2 个样本，取值分散，一致性仅 3%
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
