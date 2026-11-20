---
name: unknown_workflow_controlnet_lora_sampler_32
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.76
common_nodes: [AIO_Preprocessor, CFGGuider, CLIPLoader, CLIPLoaderGGUF, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Float, Flux2Scheduler, HAIGC_LoadImagesFromZip, ImageResizeAdvanced, KSampler, KSamplerSelect, LayerUtility: PurgeVRAM V2, LoraLoaderModelOnly, ModelPatchLoader, Qwen3VL_Chat, Qwen3_VQA, RandomNoise, ReferenceLatent, RepeatLatentBatch, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, UNETLoader, VAEDecode, VAEEncode, VAELoader, ZImageFunControlnet, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/杰洛特去水印＋图生图洗图v3生图工作流_2048572047739064322.json, 图片生成/图生图/杰洛特相似度百分之八十替换衣服场景工作流v3_2047567050679259137.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_lora_sampler_32

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/杰洛特去水印＋图生图洗图v3生图工作流_2048572047739064322.json、图片生成/图生图/杰洛特相似度百分之八十替换衣服场景工作流v3_2047567050679259137.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：76%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `CFGGuider`
- `CLIPLoader`
- `CLIPLoaderGGUF`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Float`
- `Flux2Scheduler`
- `HAIGC_LoadImagesFromZip`
- `ImageResizeAdvanced`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: PurgeVRAM V2`
- `LoraLoaderModelOnly`
- `ModelPatchLoader`
- `Qwen3VL_Chat`
- `Qwen3_VQA`
- `RandomNoise`
- `ReferenceLatent`
- `RepeatLatentBatch`
- `SamplerCustomAdvanced`
- `SaveImage`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `ZImageFunControlnet`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 1/2 个有
- `CFGNorm` —— 1/2 个有
- `CR Prompt Text` —— 1/2 个有
- `FluxKontextImageScale` —— 1/2 个有
- `ModelSamplingAuraFlow` —— 1/2 个有
- `TextEncodeQwenImageEditPlus` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | - | 2 | 89% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 50% |
| 调度器 | simple | - | 2 | 50% |
| 重绘幅度 | 0.6 | - | 2 | 33% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 50%
- 调度器 最常用 simple，2 个样本，一致性 50%
- 重绘幅度 中位数 0.6，样本不足，未给区间，2 个样本，取值分散，一致性仅 33%
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
