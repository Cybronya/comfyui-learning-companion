---
name: text_to_image_lora_sampler_clip_435
type: Text To Image
frequency: 4
level: strong
coverage: 0.99525
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, EmptyLatentImage, FluxGuidance, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Flux生态对比_1973765930620727297.json, 图片生成/文生图/flux  krea基础文生图工作流_1953071206398365698.json, 图片生成/文生图/krea 批量出图_1955652380474818561.json, 图片生成/文生图/基础Flux八步加速工作流_1950469653418184706.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_435

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Flux生态对比_1973765930620727297.json、图片生成/文生图/flux  krea基础文生图工作流_1953071206398365698.json、图片生成/文生图/krea 批量出图_1955652380474818561.json、图片生成/文生图/基础Flux八步加速工作流_1950469653418184706.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxResolutionNode` —— 2/4 个有
- `RH_Prompter` —— 2/4 个有
- `Anything Everywhere3` —— 1/4 个有
- `CR Seed` —— 1/4 个有
- `ImageConcanate` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 8 - 20 | 4 | 57% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 4 | 100% |
| 高度 | 1024 | 1024 - 1536 | 4 | 81% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 8 - 20，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1536，4 个样本，取值集中（一致性 81%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
