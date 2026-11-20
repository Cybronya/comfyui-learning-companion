---
name: unknown_workflow_sampler_clip_unet_275
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.8895
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptySD3LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-image单一模型多场景对比测试_2064696364189184002.json, 图片生成/文生图/Z-image文生图_2098605302726873090.json, 图片生成/文生图/Z_image_turbo_int8_2079199590628282369.json, 图片生成/文生图/亚秒级生成！Zimage超快图片生成器官方工作流_2035604076301393921.json, 图片生成/文生图/文生图_2109550123767386113.json, 图片生成/文生图/更快 更强 支持中文 Z turbo_1993984068826103810.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_275

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/Z-image单一模型多场景对比测试_2064696364189184002.json、图片生成/文生图/Z-image文生图_2098605302726873090.json、图片生成/文生图/Z_image_turbo_int8_2079199590628282369.json、图片生成/文生图/亚秒级生成！Zimage超快图片生成器官方工作流_2035604076301393921.json、图片生成/文生图/文生图_2109550123767386113.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 4/6 个有
- `DF_Text` —— 1/6 个有
- `GetNode` —— 1/6 个有
- `SDXLAspectRatio` —— 1/6 个有
- `SetNode` —— 1/6 个有
- `忽略多组孤海` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8.5 | 8 - 10 | 6 | 91% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | res_multistep | - | 6 | 67% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8.5，观测区间 8 - 10，6 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_multistep，6 个样本，一致性 67%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（12/6 个样本）：Steps较低可能导致细节不足
