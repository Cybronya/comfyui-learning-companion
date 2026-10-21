---
name: unknown_workflow_lora_sampler_clip_78
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.793
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, KSampler, LoraLoader, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [CR Text, easy int]
members: [图片生成/文生图/1950169292044197890.json, 图片生成/文生图/1954733353410949121.json, 图片生成/文生图/1968282023137824769.json, 图片生成/文生图/wan2.2文生图+高清放大（高质量极简流）_2029319670993522690.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_78

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/1950169292044197890.json、图片生成/文生图/1954733353410949121.json、图片生成/文生图/1968282023137824769.json、图片生成/文生图/wan2.2文生图+高清放大（高质量极简流）_2029319670993522690.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `KSampler`
- `LoraLoader`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `easy int` —— 3/4 个有
- `CFGZeroStarAndInit` —— 2/4 个有
- `CR Text` —— 2/4 个有
- `PathchSageAttentionKJ` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `ModelSamplingSD3` —— 1/4 个有
- `PrimitiveInt` —— 1/4 个有
- `SeedVR2LoadDiTModel` —— 1/4 个有
- `SeedVR2LoadVAEModel` —— 1/4 个有
- `SeedVR2VideoUpscaler` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 0.8 - 1 | 4 | 91% |
| LoRA 文本强度 | 1 | 0.8 - 1 | 4 | 91% |
| 采样步数 | 6.5 | 5 - 8 | 4 | 77% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 4 | 33% |
| 采样算法 | res_2s | - | 4 | 75% |
| 调度器 | bong_tangent | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 0.8 - 1，4 个样本，取值集中（一致性 91%）
- LoRA 文本强度 中位数 1，观测区间 0.8 - 1，4 个样本，取值集中（一致性 91%）
- 采样步数 中位数 6.5，观测区间 5 - 8，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，4 个样本，取值分散，一致性仅 33%
- 采样算法 最常用 res_2s，4 个样本，一致性 75%
- 调度器 最常用 bong_tangent，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、easy int
