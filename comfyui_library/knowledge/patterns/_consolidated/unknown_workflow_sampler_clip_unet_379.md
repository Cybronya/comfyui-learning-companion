---
name: unknown_workflow_sampler_clip_unet_379
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.767667
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, PIP_StringConcatenation, PrimitiveInt, RH_Captioner, RH_RhartImageG2TextToImage, SaveImage, SeedVR2, SeedVR2BlockSwap, SeedVR2ExtraArgs, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy positive]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/A-1 文生图像 真实人像 4k输出 全能图片全能图片G-image2_2083836421638541315.json, 图片生成/文生图/A-1_文生图像_真实人像_4k输出_全能图片全能图片G-image2_2100199502044028930.json, 图片生成/文生图/A-1_文生图像_真实人像_4k输出_全能图片全能图片G-image2_2101871474138243074.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_379

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/A-1 文生图像 真实人像 4k输出 全能图片全能图片G-image2_2083836421638541315.json、图片生成/文生图/A-1_文生图像_真实人像_4k输出_全能图片全能图片G-image2_2100199502044028930.json、图片生成/文生图/A-1_文生图像_真实人像_4k输出_全能图片全能图片G-image2_2101871474138243074.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `PIP_StringConcatenation`
- `PrimitiveInt`
- `RH_Captioner`
- `RH_RhartImageG2TextToImage`
- `SaveImage`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy positive`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 2/3 个有
- `PreviewImage` —— 2/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 6 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 0.15 | 0.15 - 0.15 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 6，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 0.15，观测区间 0.15 - 0.15，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
