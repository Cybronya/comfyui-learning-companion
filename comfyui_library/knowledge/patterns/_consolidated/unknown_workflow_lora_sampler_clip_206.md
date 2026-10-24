---
name: unknown_workflow_lora_sampler_clip_206
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.865333
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, KSampler, LoraLoader, SaveImage, UNETLoader, VAEDecode, VAELoader, easy int]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/wan2.2文生图+高清放大（高质量极简流）_2029319670993522690.json, 图片生成/文生图/wan2.2文生图--高质量极简流_1968282023137824769.json, 图片生成/文生图/通义万相最强文生图写实快速工作流_1950169292044197890.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_206

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/wan2.2文生图+高清放大（高质量极简流）_2029319670993522690.json、图片生成/文生图/wan2.2文生图--高质量极简流_1968282023137824769.json、图片生成/文生图/通义万相最强文生图写实快速工作流_1950169292044197890.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `KSampler`
- `LoraLoader`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 2/3 个有
- `PathchSageAttentionKJ` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `CFGZeroStarAndInit` —— 1/3 个有
- `SeedVR2LoadDiTModel` —— 1/3 个有
- `SeedVR2LoadVAEModel` —— 1/3 个有
- `SeedVR2VideoUpscaler` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |
| 采样步数 | 5 | 5 - 8 | 3 | 76% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | res_2s | - | 3 | 100% |
| 调度器 | bong_tangent | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 5，观测区间 5 - 8，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，3 个样本，一致性 100%
- 调度器 最常用 bong_tangent，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
