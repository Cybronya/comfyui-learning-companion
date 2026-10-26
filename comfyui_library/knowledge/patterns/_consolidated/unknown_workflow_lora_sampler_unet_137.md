---
name: unknown_workflow_lora_sampler_unet_137
type: Unknown Workflow
frequency: 5
level: weak
coverage: 0.9322
common_nodes: [CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, PainterFluxImageEdit, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux2-Klein换脸_换头_高级换脸多种参数色调可调_2063593099074560001.json, 图片生成/图生图/Flux2-Klein换脸_换头_高级换脸多种参数色调可调_2063946262113767426.json, 图片生成/图生图/flux klein MC皮肤生成_2048078695188926466.json, 图片生成/图生图/换脸_换头_Flux2-Klein_2070314503065137153.json, 图片生成/图生图/换脸_换头_Flux2-Klein不但换脸直接给你换头发型也换了高级换脸多种参数色调可调_2037844279611101186.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_137

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Flux2-Klein换脸_换头_高级换脸多种参数色调可调_2063593099074560001.json、图片生成/图生图/Flux2-Klein换脸_换头_高级换脸多种参数色调可调_2063946262113767426.json、图片生成/图生图/flux klein MC皮肤生成_2048078695188926466.json、图片生成/图生图/换脸_换头_Flux2-Klein_2070314503065137153.json、图片生成/图生图/换脸_换头_Flux2-Klein不但换脸直接给你换头发型也换了高级换脸多种参数色调可调_2037844279611101186.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PainterFluxImageEdit`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 4/5 个有
- `GetImageSize` —— 4/5 个有
- `ImageSharpen` —— 4/5 个有
- `ModelSamplingAuraFlow` —— 4/5 个有
- `easy cleanGpuUsed` —— 4/5 个有
- `RepeatLatentBatch` —— 3/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 20 | 5 | 54% |
| Prompt 约束强度(CFG) | 1 | 1 - 5 | 5 | 11% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 20，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 5，5 个样本，取值分散，一致性仅 11%
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（4/5 个样本）：Steps较低可能导致细节不足
