---
name: unknown_workflow_sampler_clip_unet_105
type: Unknown Workflow
frequency: 11
level: weak
coverage: 0.842273
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z image 直出高清基础流 v1_2002028004870111233.json, 图片生成/文生图/Z image 直出高清基础流 v2_2003053873344462850.json, 图片生成/文生图/Z-image  zimage  文生图  工作流_2042926754704134145.json, 图片生成/文生图/Z-image_zimage_文生图_超真实感_2042921269569527810.json, 图片生成/文生图/ZIT基础文生图_2088289408716992513.json, 图片生成/文生图/Z_Image_Turbo-文生图_2063504172338737154.json, 图片生成/文生图/Zimage base fp8一键出模特大片_2016314793744932866.json, 图片生成/文生图/【老金驿站】Qwen提速20%生成工作流_1953252280764141569.json, 图片生成/文生图/最强最新Qwen image2512文生图工作流0707_2074521092005388289.json, 图片生成/文生图/最新qwen image2512文生图基础工作流_2013152895679602689.json, 图片生成/文生图/最新qwen+image2512文生图基础工作流_2094968730156621826.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_105

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/Z image 直出高清基础流 v1_2002028004870111233.json、图片生成/文生图/Z image 直出高清基础流 v2_2003053873344462850.json、图片生成/文生图/Z-image  zimage  文生图  工作流_2042926754704134145.json、图片生成/文生图/Z-image_zimage_文生图_超真实感_2042921269569527810.json、图片生成/文生图/ZIT基础文生图_2088289408716992513.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 8/11 个有
- `PreviewImage` —— 7/11 个有
- `ConditioningZeroOut` —— 6/11 个有
- `Text Multiline` —— 6/11 个有
- `CFGNorm` —— 5/11 个有
- `LoraLoaderModelOnly` —— 3/11 个有
- `QwenImageLatentAspectRatio` —— 3/11 个有
- `Display Any (rgthree)` —— 2/11 个有
- `PathchSageAttentionKJ` —— 2/11 个有
- `QwenImageEngineer` —— 2/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 15 | 8 - 50 | 11 | 26% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 11 | 42% |
| 采样算法 | euler | - | 11 | 73% |
| 调度器 | simple | - | 11 | 82% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 15，观测区间 8 - 50，11 个样本，取值分散，一致性仅 26%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，11 个样本，取值分散，一致性仅 42%
- 采样算法 最常用 euler，11 个样本，一致性 73%
- 调度器 最常用 simple，11 个样本，一致性 82%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
