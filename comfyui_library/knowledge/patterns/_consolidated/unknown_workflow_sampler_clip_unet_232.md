---
name: unknown_workflow_sampler_clip_unet_232
type: Unknown Workflow
frequency: 7
level: weak
coverage: 0.845714
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z image 直出高清基础流 v1_2002028004870111233.json, 图片生成/文生图/Z image 直出高清基础流 v2_2003053873344462850.json, 图片生成/文生图/Z-image_zimage_文生图_超真实感_2042921269569527810.json, 图片生成/文生图/ZIT基础文生图_2088289408716992513.json, 图片生成/文生图/Z_Image_Turbo-文生图_2063504172338737154.json, 图片生成/文生图/Zimage base fp8一键出模特大片_2016314793744932866.json, 图片生成/文生图/【老金驿站】Qwen提速20%生成工作流_1953252280764141569.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_232

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/Z image 直出高清基础流 v1_2002028004870111233.json、图片生成/文生图/Z image 直出高清基础流 v2_2003053873344462850.json、图片生成/文生图/Z-image_zimage_文生图_超真实感_2042921269569527810.json、图片生成/文生图/ZIT基础文生图_2088289408716992513.json、图片生成/文生图/Z_Image_Turbo-文生图_2063504172338737154.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 6/7 个有
- `ConditioningZeroOut` —— 3/7 个有
- `Text Multiline` —— 3/7 个有
- `CFGNorm` —— 2/7 个有
- `Display Any (rgthree)` —— 2/7 个有
- `PathchSageAttentionKJ` —— 2/7 个有
- `QwenImageEngineer` —— 2/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 50 | 7 | 21% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 7 | 41% |
| 采样算法 | euler | - | 7 | 71% |
| 调度器 | simple | - | 7 | 71% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 50，7 个样本，取值分散，一致性仅 21%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，7 个样本，取值分散，一致性仅 41%
- 采样算法 最常用 euler，7 个样本，一致性 71%
- 调度器 最常用 simple，7 个样本，一致性 71%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（4/7 个样本）：Steps较低可能导致细节不足
