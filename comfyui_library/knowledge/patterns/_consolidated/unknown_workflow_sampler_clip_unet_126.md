---
name: unknown_workflow_sampler_clip_unet_126
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8914
common_nodes: [BasicScheduler, CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, DetailDaemonSamplerNode, EmptyLatentImage, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [Label (rgthree)]
members: [图片生成/文生图/1982805138127630338.json, 图片生成/文生图/BEYOND REALITY Z-image加噪对比_2003074750492680194.json, 图片生成/文生图/Z-IMAGE高清摄影写真流_2007098283063255042.json, 图片生成/文生图/最强人像摄影模型 Beyond+Reality+Z-image文生图_2003818575100035073.json, 图片生成/文生图/（噪波控制版）Beyond Reality Z-image文生图V1_2003170287237701633.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_126

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/1982805138127630338.json、图片生成/文生图/BEYOND REALITY Z-image加噪对比_2003074750492680194.json、图片生成/文生图/Z-IMAGE高清摄影写真流_2007098283063255042.json、图片生成/文生图/最强人像摄影模型 Beyond+Reality+Z-image文生图_2003818575100035073.json、图片生成/文生图/（噪波控制版）Beyond Reality Z-image文生图V1_2003170287237701633.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DetailDaemonSamplerNode`
- `EmptyLatentImage`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 4/5 个有
- `LayerUtility: PurgeVRAM` —— 4/5 个有
- `LoraLoaderModelOnly` —— 4/5 个有
- `Float` —— 3/5 个有
- `Image Comparer (rgthree)` —— 2/5 个有
- `AddLabel` —— 1/5 个有
- `FastFilmGrain` —— 1/5 个有
- `FastLaplacianSharpen` —— 1/5 个有
- `ImageConcatMulti` —— 1/5 个有
- `ImageScaleBy` —— 1/5 个有
- `Label (rgthree)` —— 1/5 个有
- `SeedVR2GGUF` —— 1/5 个有
- `SeedVR2LoadDiTModel` —— 1/5 个有
- `SeedVR2LoadVAEModel` —— 1/5 个有
- `SeedVR2VideoUpscaler` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 1080 - 1080 | 5 | 100% |
| 高度 | 1920 | 1560 - 1920 | 5 | 92% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1080，观测区间 1080 - 1080，5 个样本，取值集中（一致性 100%）
- 高度 中位数 1920，观测区间 1560 - 1920，5 个样本，取值集中（一致性 92%）
- 这些节点还没有知识卡，系统对它们的理解有限：Label (rgthree)
