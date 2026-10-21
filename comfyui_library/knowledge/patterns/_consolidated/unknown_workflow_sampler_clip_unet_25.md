---
name: unknown_workflow_sampler_clip_unet_25
type: Unknown Workflow
frequency: 14
level: weak
coverage: 0.879071
common_nodes: [AddLabel, CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, EmptySD3LatentImage, Flux2Scheduler, ImageConcatMulti, KSampler, KSamplerSelect, ModelSamplingAuraFlow, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Flux Klein 多版本 与 Z-image 对比_2012076351213281282.json, 图片生成/文生图/Flux2.Klein文生图基础款_2012069451797106689.json, 图片生成/文生图/Flux2.Klein文生图基础款_2012489427985108993.json, 图片生成/文生图/Z-image-base、klein与Turbo图像对比_2016490330656346114.json, 图片生成/文生图/flux klein多版本与zimage对比工作流_2012061598302605314.json, 图片生成/文生图/flux2+klein与zimage对比工作流_2012151072038592514.json, 图片生成/文生图/文生图Qwen+Flux2 Klein多版本+Zimage_2012141133685592065.json, 图片生成/文生图/文生图Qwen+Flux2 Klein多版本+Zimage_2084894059092598786.json, 图片生成/文生图/文生图Qwen+Flux2 Klein多版本+Zimage_2084901212222218242.json, 图片生成/文生图/文生图Qwen+Flux2 Klein多版本+Zimage_2084905221939089410.json, 图片生成/文生图/文生图Qwen+Flux2 Klein多版本+Zimage_2089609097233657858.json, 图片生成/文生图/文生图Qwen+Flux2 Klein多版本+Zimage_2108479912758833153.json, 图片生成/文生图/文生图大全，Flux2多版本 VS Zimage_2012128533153320961.json, 图片生成/文生图/文生图（大漠孤烟直，长河落日圆）_2061330236628885505.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_25

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/文生图/Flux Klein 多版本 与 Z-image 对比_2012076351213281282.json、图片生成/文生图/Flux2.Klein文生图基础款_2012069451797106689.json、图片生成/文生图/Flux2.Klein文生图基础款_2012489427985108993.json、图片生成/文生图/Z-image-base、klein与Turbo图像对比_2016490330656346114.json、图片生成/文生图/flux klein多版本与zimage对比工作流_2012061598302605314.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 14 个 workflow 都包含：
- `AddLabel`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `EmptySD3LatentImage`
- `Flux2Scheduler`
- `ImageConcatMulti`
- `KSampler`
- `KSamplerSelect`
- `ModelSamplingAuraFlow`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 12/14 个有
- `LayerUtility: PurgeVRAM` —— 10/14 个有
- `DF_Get_latent_size` —— 8/14 个有
- `Fast Groups Bypasser (rgthree)` —— 8/14 个有
- `LoraLoaderModelOnly` —— 8/14 个有
- `PreviewImage` —— 8/14 个有
- `QwenImageLatentAspectRatio` —— 8/14 个有
- `ShowAnything|Mie` —— 8/14 个有
- `easy cleanGpuUsed` —— 8/14 个有
- `CFGNorm` —— 4/14 个有
- `PrimitiveInt` —— 4/14 个有
- `AILab_QwenVL` —— 2/14 个有
- `JDCN_StringToList` —— 2/14 个有
- `ShowText|pysssss` —— 2/14 个有
- `easy int` —— 2/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 30 | 14 | 0% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 14 | 65% |
| 采样算法 | res_multistep | - | 14 | 93% |
| 调度器 | simple | - | 14 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 30，14 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，14 个样本
- 采样算法 最常用 res_multistep，14 个样本，一致性 93%
- 调度器 最常用 simple，14 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 高发问题（16/14 个样本）：Steps较低可能导致细节不足
