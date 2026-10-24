---
name: unknown_workflow_sampler_clip_vae_16
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8694
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, NunchakuQwenImageDiTLoader, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/nucnhaku-qwen-image_1966414867236368386.json, 图片生成/文生图/nunchaku qwen加速文生图_1964600749260947457.json, 图片生成/文生图/nunchaku-qwen-image with lora_2073405156171018242.json, 图片生成/文生图/nunchaku-qwen-image_1959414093880963073.json, 图片生成/文生图/nunchaku-qwen-image_2073056140971298817.json, 图片生成/文生图/nunchaku_Qwen_image_1959965300433301506.json, 图片生成/文生图/nunkucha-qwen-image_1960520624663949314.json, 图片生成/文生图/qwen image nunchaku加速_1963054435381522434.json, 图片生成/文生图/qwen-Image -nunchaku+lora_1963114884189884418.json, 图片生成/文生图/qwen文生图片（加速）_2003133550327209985.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_16

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/nucnhaku-qwen-image_1966414867236368386.json、图片生成/文生图/nunchaku qwen加速文生图_1964600749260947457.json、图片生成/文生图/nunchaku-qwen-image with lora_2073405156171018242.json、图片生成/文生图/nunchaku-qwen-image_1959414093880963073.json、图片生成/文生图/nunchaku-qwen-image_2073056140971298817.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `NunchakuQwenImageDiTLoader`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 1/10 个有
- `EmptyImage` —— 1/10 个有
- `NunchakuQwenImageLoraLoader1` —— 1/10 个有
- `PrimitiveStringMultiline` —— 1/10 个有
- `ResizeAndPadImage` —— 1/10 个有
- `easy clearCacheAll` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 15 | 8 - 20 | 10 | 59% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 3.5 | 10 | 57% |
| 采样算法 | euler | - | 10 | 80% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 15，观测区间 8 - 20，10 个样本
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 3.5，10 个样本
- 采样算法 最常用 euler，10 个样本，一致性 80%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
