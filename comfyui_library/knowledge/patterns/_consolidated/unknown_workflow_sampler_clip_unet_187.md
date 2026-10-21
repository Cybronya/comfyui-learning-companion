---
name: unknown_workflow_sampler_clip_unet_187
type: Unknown Workflow
frequency: 3
level: weak
coverage: 0.962
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Boogu文生图工作流（Turbo+Base可选）_2069668261842743298.json, 图片生成/文生图/Qwen-千问多字体直出-字体设计 中文字体设计_1993312885105426433.json, 图片生成/文生图/Z-Image-Turbo文生图（OpenClaw远程控制版本）_2020379259021303809.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_187

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Boogu文生图工作流（Turbo+Base可选）_2069668261842743298.json、图片生成/文生图/Qwen-千问多字体直出-字体设计 中文字体设计_1993312885105426433.json、图片生成/文生图/Z-Image-Turbo文生图（OpenClaw远程控制版本）_2020379259021303809.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：96%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR SDXL Aspect Ratio` —— 2/3 个有
- `Label (rgthree)` —— 2/3 个有
- `ModelSamplingAuraFlow` —— 2/3 个有
- `AddLabel` —— 1/3 个有
- `EmptySD3LatentImage` —— 1/3 个有
- `Lora Loader Stack (rgthree)` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `忽略多组孤海` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 20 | 3 | 19% |
| Prompt 约束强度(CFG) | 1 | 1 - 3 | 3 | 43% |
| 采样算法 | lcm | - | 3 | 33% |
| 调度器 | sgm_uniform | - | 3 | 33% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 20，3 个样本，取值分散，一致性仅 19%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3，3 个样本，取值分散，一致性仅 43%
- 采样算法 最常用 lcm，3 个样本，一致性 33%
- 调度器 最常用 sgm_uniform，3 个样本，一致性 33%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
