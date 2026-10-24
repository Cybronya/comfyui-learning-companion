---
name: unknown_workflow_sampler_clip_unet_109
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.9315
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/超强文生图，Z-image_1993890621761011713.json, 图片生成/文生图/1.Z-image 文生图工作流_2056576711298478082.json, 图片生成/文生图/Boogu文生图工作流（Turbo+Base可选）_2069668261842743298.json, 图片生成/文生图/Z-image图片生成_1993961233665769474.json, 图片生成/文生图/ZImage文生图极速版_1994390225893924866.json, 图片生成/文生图/文生图  boogu_2067835171948290050.json, 图片生成/文生图/文生图 强大输出_2039875075289128962.json, 图片生成/文生图/文生图 拼好模 BOOGU!_2067835110157799425.json, 图片生成/文生图/文生图，ZImage，强 DOPSD_1993892831561449474.json, 图片生成/文生图/文生图，ZImage，强 DOPSD，自用封面_2068318813740953602.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_109

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/超强文生图，Z-image_1993890621761011713.json、图片生成/文生图/1.Z-image 文生图工作流_2056576711298478082.json、图片生成/文生图/Boogu文生图工作流（Turbo+Base可选）_2069668261842743298.json、图片生成/文生图/Z-image图片生成_1993961233665769474.json、图片生成/文生图/ZImage文生图极速版_1994390225893924866.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 9/10 个有
- `PreviewImage` —— 8/10 个有
- `QwenImageLatentAspectRatio` —— 6/10 个有
- `MuyeTextEditOutput` —— 5/10 个有
- `CR SDXL Aspect Ratio` —— 4/10 个有
- `LoraLoaderModelOnly` —— 2/10 个有
- `AddLabel` —— 1/10 个有
- `Label (rgthree)` —— 1/10 个有
- `忽略多组孤海` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 4 - 10 | 10 | 68% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 70% |
| 调度器 | simple | - | 10 | 70% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 4 - 10，10 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 70%
- 调度器 最常用 simple，10 个样本，一致性 70%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（8/10 个样本）：Steps较低可能导致细节不足
