---
name: unknown_workflow_sampler_clip_unet_163
type: Unknown Workflow
frequency: 4
level: strong
coverage: 1
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, KSampler, QwenImageLatentAspectRatio, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/ZImage多种风格文生图极速版_1994667329688641537.json, 图片生成/文生图/ZImage文生图极速版_1994390225893924866.json, 图片生成/文生图/ZImage文生图高清生图工作流_1995538393234857986.json, 图片生成/文生图/ZImage，文生图高清生图工作流_1994233153258799106.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_163

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/ZImage多种风格文生图极速版_1994667329688641537.json、图片生成/文生图/ZImage文生图极速版_1994390225893924866.json、图片生成/文生图/ZImage文生图高清生图工作流_1995538393234857986.json、图片生成/文生图/ZImage，文生图高清生图工作流_1994233153258799106.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `KSampler`
- `QwenImageLatentAspectRatio`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `MuyeTextEditOutput` —— 3/4 个有
- `Florence2ModelLoader` —— 2/4 个有
- `Florence2Run` —— 2/4 个有
- `LatentUpscaleBy` —— 2/4 个有
- `Primitive string multiline [Crystools]` —— 1/4 个有
- `ProcessString` —— 1/4 个有
- `easy promptLine` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 9 - 9 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 0.75 | 0.5 - 1 | 4 | 67% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 9 - 9，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 0.75，观测区间 0.5 - 1，4 个样本
- 高发问题（6/4 个样本）：Steps较低可能导致细节不足
