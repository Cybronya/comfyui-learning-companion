---
name: unknown_workflow_sampler_clip_unet_55
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.9147
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-image单一模型多场景对比测试_2064696364189184002.json, 图片生成/文生图/Z_image文生图极速版_2064941900221734914.json, 图片生成/文生图/chris_export_image_z_image_turbo_02_2004521005383118850.json, 图片生成/文生图/chris_export_image_z_image_turbo_2002908032482852866.json, 图片生成/文生图/danotebook-z-image-turbo_2062428549738487809.json, 图片生成/文生图/image_z_image_turbo_2058123503169269762.json, 图片生成/文生图/z-image-turbo文生图_2081602813930594305.json, 图片生成/文生图/z-image-turbo文生图工作流_1997643407344513025.json, 图片生成/文生图/z_image_turbo文生图_2067946808487276545.json, 图片生成/文生图/z_image_turbo文生图透明_2067952553903611905.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_55

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/Z-image单一模型多场景对比测试_2064696364189184002.json、图片生成/文生图/Z_image文生图极速版_2064941900221734914.json、图片生成/文生图/chris_export_image_z_image_turbo_02_2004521005383118850.json、图片生成/文生图/chris_export_image_z_image_turbo_2002908032482852866.json、图片生成/文生图/danotebook-z-image-turbo_2062428549738487809.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BiRefNetRMBG` —— 1/10 个有
- `DF_Text` —— 1/10 个有
- `GetNode` —— 1/10 个有
- `SetNode` —— 1/10 个有
- `忽略多组孤海` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8.5 | 4 - 9 | 10 | 75% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | res_multistep | - | 10 | 90% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8.5，观测区间 4 - 9，10 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_multistep，10 个样本，一致性 90%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（17/10 个样本）：Steps较低可能导致细节不足
