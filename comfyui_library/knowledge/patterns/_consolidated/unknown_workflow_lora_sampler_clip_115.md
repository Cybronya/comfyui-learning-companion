---
name: unknown_workflow_lora_sampler_clip_115
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8414
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, CR Text, ConditioningZeroOut, EmptyFlux2LatentImage, EmptyLatentImage, Flux2Scheduler, GetImageSize, ImageScaleToTotalPixels, KSamplerAdvanced, KSamplerSelect, LoraLoaderModelOnly, ModelSamplingAuraFlow, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/zimage+klein三阶采样极致真实优化版文生图_2060023035092094977.json, 图片生成/文生图/zimage+klein三阶采样极致真实优化版文生图_2068280017888563201.json, 图片生成/文生图/文生场景 Krea2_2100205414267834369.json, 视频生成/文生视频/Krea2 巨构场景_2087351374735560705.json, 视频生成/文生视频/zimage+klein三阶采样极致真实优化版文生图_2061987789113217025.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_115

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/zimage+klein三阶采样极致真实优化版文生图_2060023035092094977.json、图片生成/文生图/zimage+klein三阶采样极致真实优化版文生图_2068280017888563201.json、图片生成/文生图/文生场景 Krea2_2100205414267834369.json、视频生成/文生视频/Krea2 巨构场景_2087351374735560705.json、视频生成/文生视频/zimage+klein三阶采样极致真实优化版文生图_2061987789113217025.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 5 个 workflow 都包含：
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
- `GetNode` —— 3/5 个有
- `ImageColorMatch+` —— 3/5 个有
- `LayerUtility: PurgeVRAM` —— 3/5 个有
- `PreviewImage` —— 3/5 个有
- `PrimitiveInt` —— 3/5 个有
- `RHLLMChatNode` —— 3/5 个有
- `SetNode` —— 3/5 个有
- `ColorMatchV2` —— 2/5 个有
- `Image Comparer (rgthree)` —— 2/5 个有
- `ImageSharpen` —— 2/5 个有
- `LayerUtility: PurgeVRAM V2` —— 2/5 个有
- `RH_LLMAPI_NODE` —— 2/5 个有
- `Seed (rgthree)` —— 2/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1536 | 1280 - 1536 | 5 | 93% |
| 高度 | 864 | 720 - 864 | 5 | 93% |
| 采样步数 | fixed | - | 5 | 60% |
| Prompt 约束强度(CFG) | 8 | 8 - 12 | 5 | 80% |
| 采样算法 | 1 | 1 - 2 | 5 | 67% |
| 调度器 | euler_ancestral | - | 5 | 100% |
| 重绘幅度 | beta | - | 5 | 60% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1536，观测区间 1280 - 1536，5 个样本，取值集中（一致性 93%）
- 高度 中位数 864，观测区间 720 - 864，5 个样本，取值集中（一致性 93%）
- 采样步数 最常用 fixed，5 个样本，一致性 60%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 12，5 个样本
- 采样算法 中位数 1，观测区间 1 - 2，5 个样本
- 调度器 最常用 euler_ancestral，5 个样本，一致性 100%
- 重绘幅度 最常用 beta，5 个样本，一致性 60%
