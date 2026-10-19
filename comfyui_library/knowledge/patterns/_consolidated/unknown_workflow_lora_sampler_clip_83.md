---
name: unknown_workflow_lora_sampler_clip_83
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.869
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, CR Text, ConditioningZeroOut, EmptyFlux2LatentImage, EmptyLatentImage, Flux2Scheduler, GetImageSize, ImageScaleToTotalPixels, KSamplerAdvanced, KSamplerSelect, LoraLoaderModelOnly, ModelSamplingAuraFlow, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/文生场景 Krea2_2100205414267834369.json, 视频生成/文生视频/Krea2 巨构场景_2087351374735560705.json, 视频生成/文生视频/zimage+klein三阶采样极致真实优化版文生图_2061987789113217025.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_83

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/文生场景 Krea2_2100205414267834369.json、视频生成/文生视频/Krea2 巨构场景_2087351374735560705.json、视频生成/文生视频/zimage+klein三阶采样极致真实优化版文生图_2061987789113217025.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `EmptyLatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `ImageScaleToTotalPixels`
- `KSamplerAdvanced`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ColorMatchV2` —— 2/3 个有
- `Image Comparer (rgthree)` —— 2/3 个有
- `ImageSharpen` —— 2/3 个有
- `LayerUtility: PurgeVRAM V2` —— 2/3 个有
- `RH_LLMAPI_NODE` —— 2/3 个有
- `Seed (rgthree)` —— 2/3 个有
- `GetNode` —— 1/3 个有
- `ImageColorMatch+` —— 1/3 个有
- `LayerUtility: PurgeVRAM` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `PrimitiveInt` —— 1/3 个有
- `RHLLMChatNode` —— 1/3 个有
- `SetNode` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 3 | 67% |
| Prompt 约束强度(CFG) | 12 | 8 - 12 | 3 | 82% |
| 采样算法 | 1 | 1 - 2 | 3 | 65% |
| 调度器 | euler_ancestral | - | 3 | 100% |
| 重绘幅度 | simple | - | 3 | 67% |
| 宽度 | 1536 | 1280 - 1536 | 3 | 92% |
| 高度 | 832 | 720 - 864 | 3 | 92% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，3 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 12，观测区间 8 - 12，3 个样本，取值集中（一致性 82%）
- 采样算法 中位数 1，观测区间 1 - 2，3 个样本
- 调度器 最常用 euler_ancestral，3 个样本，一致性 100%
- 重绘幅度 最常用 simple，3 个样本，一致性 67%
- 宽度 中位数 1536，观测区间 1280 - 1536，3 个样本，取值集中（一致性 92%）
- 高度 中位数 832，观测区间 720 - 864，3 个样本，取值集中（一致性 92%）
