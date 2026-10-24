---
name: unknown_workflow_sampler_clip_unet_366
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.884333
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, ImpactInt, KSamplerAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/文生图/2030807710291202049.json, 图片生成/文生图/Z-image文生图 -多批次人物一致性_2002833348940709889.json, 图片生成/文生图/🤖Z-image小钢炮来袭！[随机性增强]_1999663045167153154.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_366

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/2030807710291202049.json、图片生成/文生图/Z-image文生图 -多批次人物一致性_2002833348940709889.json、图片生成/文生图/🤖Z-image小钢炮来袭！[随机性增强]_1999663045167153154.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `ImpactInt`
- `KSamplerAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 2/3 个有
- `CR Text` —— 2/3 个有
- `Mute / Bypass Repeater (rgthree)` —— 2/3 个有
- `Note Plus (mtb)` —— 2/3 个有
- `RH_LLMAPI_NODE` —— 2/3 个有
- `CR Prompt List` —— 1/3 个有
- `Fast Bypasser (rgthree)` —— 1/3 个有
- `String Literal` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 720 | 720 - 720 | 3 | 100% |
| 高度 | 1280 | 1280 - 1280 | 3 | 100% |
| 采样步数 | randomize | - | 3 | 100% |
| Prompt 约束强度(CFG) | 10 | 10 - 10 | 3 | 100% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | dpmpp_3m_sde_gpu | - | 3 | 67% |
| 重绘幅度 | ddim_uniform | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 720，观测区间 720 - 720，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1280，观测区间 1280 - 1280，3 个样本，取值集中（一致性 100%）
- 采样步数 最常用 randomize，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 10，观测区间 10 - 10，3 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 dpmpp_3m_sde_gpu，3 个样本，一致性 67%
- 重绘幅度 最常用 ddim_uniform，3 个样本，一致性 100%
