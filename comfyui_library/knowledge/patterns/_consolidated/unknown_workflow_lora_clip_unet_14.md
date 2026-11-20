---
name: unknown_workflow_lora_clip_unet_14
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.853
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, LoraLoaderModelOnly, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/工作流系列00-klein的文生图工作流-基础向讲解此工作流_2012049130310340610.json, 图片生成/文生图/组件系列10-FLUX.2-Klein文生图_2058761708835008514.json, 平台全量/CG神幻漫剧角色设计（CG Fantasy Character Design）_2030574519403945985.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_clip_unet_14

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/工作流系列00-klein的文生图工作流-基础向讲解此工作流_2012049130310340610.json、图片生成/文生图/组件系列10-FLUX.2-Klein文生图_2058761708835008514.json、平台全量/CG神幻漫剧角色设计（CG Fantasy Character Design）_2030574519403945985.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGGuider` —— 2/3 个有
- `ConditioningZeroOut` —— 2/3 个有
- `Flux2Scheduler` —— 2/3 个有
- `KSampler` —— 2/3 个有
- `KSamplerSelect` —— 2/3 个有
- `RandomNoise` —— 2/3 个有
- `SamplerCustomAdvanced` —— 2/3 个有
- `Seed (rgthree)` —— 2/3 个有
- `Text` —— 2/3 个有
- `CR SDXL Aspect Ratio` —— 1/3 个有
- `CR Text` —— 1/3 个有
- `GetNode` —— 1/3 个有
- `PrimitiveInt` —— 1/3 个有
- `SetNode` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 5.5 | - | 2 | 91% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 5.5，样本不足，未给区间，2 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
