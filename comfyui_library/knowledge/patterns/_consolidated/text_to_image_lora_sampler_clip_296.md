---
name: text_to_image_lora_sampler_clip_296
type: Text To Image
frequency: 3
level: strong
coverage: 0.96
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Boogu vs Z vs Q2152工作流_2069058937420337153.json, 图片生成/文生图/Krea2-Cc测试Lora专用流_2080172818469318657.json, 图片生成/文生图/Z-Image-Turbo文生图标准工作流_2091176473360166914.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_296

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Boogu vs Z vs Q2152工作流_2069058937420337153.json、图片生成/文生图/Krea2-Cc测试Lora专用流_2080172818469318657.json、图片生成/文生图/Z-Image-Turbo文生图标准工作流_2091176473360166914.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 2/3 个有
- `INTConstant` —— 2/3 个有
- `ModelSamplingAuraFlow` —— 2/3 个有
- `ResolutionSelector` —— 2/3 个有
- `AddLabel` —— 1/3 个有
- `EmptySD3LatentImage` —— 1/3 个有
- `StringConstantMultiline` —— 1/3 个有
- `easy imageConcat` —— 1/3 个有
- `easy seed` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1024 | 512 - 1664 | 3 | 56% |
| 高度 | 928 | 512 - 1024 | 3 | 73% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 512 - 1664，3 个样本
- 高度 中位数 928，观测区间 512 - 1024，3 个样本
- 高发问题（10/3 个样本）：Steps较低可能导致细节不足
