---
name: unknown_workflow_sampler_clip_unet_100
type: Unknown Workflow
frequency: 10
level: weak
coverage: 0.8949
common_nodes: [AddLabel, CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, ImageConcatMulti, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux2 Klein 文生图测试_2013468861047246850.json, 图片生成/文生图/Flux Klein 多版本 与 Z-image 对比_2012076351213281282.json, 图片生成/文生图/Flux2.Klein文生图基础款_2012069451797106689.json, 图片生成/文生图/Flux2.Klein文生图基础款_2012489427985108993.json, 图片生成/文生图/Flux2.Klein末世女战士_2043619331346538497.json, 图片生成/文生图/Z-image-base、klein与Turbo图像对比_2016490330656346114.json, 图片生成/文生图/flux klein4B和9B 对比工作流 浮云1.17_2012475320712040449.json, 图片生成/文生图/flux klein多版本与zimage对比工作流_2012061598302605314.json, 图片生成/文生图/flux2+klein与zimage对比工作流_2012151072038592514.json, 图片生成/文生图/生图效果大比拼：LongCat vs Z‑image vs Klein_2028831826680221697.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_100

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/Flux2 Klein 文生图测试_2013468861047246850.json、图片生成/文生图/Flux Klein 多版本 与 Z-image 对比_2012076351213281282.json、图片生成/文生图/Flux2.Klein文生图基础款_2012069451797106689.json、图片生成/文生图/Flux2.Klein文生图基础款_2012489427985108993.json、图片生成/文生图/Flux2.Klein末世女战士_2043619331346538497.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 10 个 workflow 都包含：
- `AddLabel`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `ImageConcatMulti`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 9/10 个有
- `KSampler` —— 9/10 个有
- `ModelSamplingAuraFlow` —— 8/10 个有
- `PrimitiveInt` —— 7/10 个有
- `PrimitiveStringMultiline` —— 7/10 个有
- `CFGNorm` —— 6/10 个有
- `JDCN_StringToList` —— 3/10 个有
- `LayerUtility: PurgeVRAM` —— 3/10 个有
- `ShowText|pysssss` —— 3/10 个有
- `easy int` —— 3/10 个有
- `AILab_QwenVL` —— 2/10 个有
- `LoadImage` —— 2/10 个有
- `ApplySageAttention` —— 1/10 个有
- `LoraLoaderModelOnly` —— 1/10 个有
- `PreviewImage` —— 1/10 个有
- `QwenVisionNode` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 30 | 9 | 0% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 9 | 60% |
| 采样算法 | res_multistep | - | 9 | 78% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 30，9 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，9 个样本
- 采样算法 最常用 res_multistep，9 个样本，一致性 78%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足
