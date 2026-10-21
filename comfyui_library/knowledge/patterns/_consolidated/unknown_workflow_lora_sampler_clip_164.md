---
name: unknown_workflow_lora_sampler_clip_164
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8545
common_nodes: [CLIPTextEncode, DualCLIPLoader, FluxGuidance, KSampler, LoraLoader, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [Empty Latent by Size (WLSH), Seed (rgthree)]
members: [图片生成/文生图/1967252910071537666.json, 图片生成/文生图/蒜-FLux1.D加载多个Lora生图工作流_1995009169252134914.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_164

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1967252910071537666.json、图片生成/文生图/蒜-FLux1.D加载多个Lora生图工作流_1995009169252134914.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LoraLoader`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Empty Latent by Size (WLSH)` —— 1/2 个有
- `EmptySD3LatentImage` —— 1/2 个有
- `ModelSamplingFlux` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `Seed (rgthree)` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 14 | - | 2 | 57% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | beta | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |
| LoRA 模型强度 | 0.9 | - | 2 | 89% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 14，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.9，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：Empty Latent by Size (WLSH)、Seed (rgthree)
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
