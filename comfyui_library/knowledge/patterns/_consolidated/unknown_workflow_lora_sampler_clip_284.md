---
name: unknown_workflow_lora_sampler_clip_284
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8735
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, Image Comparer (rgthree), ImageFromBatch, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoraLoaderModelOnly, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, Seed (rgthree), UNETLoader, VAEDecode, VAEEncode, VAELoader, easy batchAnything, easy forLoopEnd, easy forLoopStart, easy imageColorMatch, easy imageCount, easy int, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/Flux2+Z-image+SeedVR2高一致性人像修复细化8K高清放大_2045061406919237633.json, 平台全量/批量高清修复（F2K一致性）_2058063744596533249.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_284

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Flux2+Z-image+SeedVR2高一致性人像修复细化8K高清放大_2045061406919237633.json、平台全量/批量高清修复（F2K一致性）_2058063744596533249.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `Image Comparer (rgthree)`
- `ImageFromBatch`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `Seed (rgthree)`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy batchAnything`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy imageColorMatch`
- `easy imageCount`
- `easy int`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Get Image Size` —— 1/2 个有
- `GetImageSize` —— 1/2 个有
- `ImageListToBatch+` —— 1/2 个有
- `ImageResize+` —— 1/2 个有
- `ImageSmartSharpen+` —— 1/2 个有
- `ImpactMinMax` —— 1/2 个有
- `KOOK_ImageCompression` —— 1/2 个有
- `KSamplerAdvanced` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `ModelSamplingAuraFlow` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `SeedVR2LoadDiTModel` —— 1/2 个有
- `SeedVR2LoadVAEModel` —— 1/2 个有
- `SeedVR2VideoUpscaler` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有
- `TTP_Image_Assy` —— 1/2 个有
- `TTP_Image_Tile_Batch` —— 1/2 个有
- `YuanMultiImage` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 1 | 100% |
| Prompt 约束强度(CFG) | 8 | - | 1 | 100% |
| 采样算法 | 1 | - | 1 | 100% |
| 调度器 | euler | - | 1 | 100% |
| 重绘幅度 | beta57 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
