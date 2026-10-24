---
name: unknown_workflow_lora_sampler_clip_147
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.90375
common_nodes: [BasicScheduler, CFGGuider, CLIPLoader, CLIPTextEncode, CR Text, ConditioningZeroOut, DetailDaemonSamplerNode, EmptyLatentImage, KSamplerSelect, LayerUtility: PurgeVRAM, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/BEYOND REALITY Z-image加噪对比_2003074750492680194.json, 图片生成/文生图/Z-IMAGE高清摄影写真流_2007098283063255042.json, 图片生成/文生图/最强人像摄影模型 Beyond+Reality+Z-image文生图_2003818575100035073.json, 图片生成/文生图/（噪波控制版）Beyond Reality Z-image文生图V1_2003170287237701633.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_147

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/BEYOND REALITY Z-image加噪对比_2003074750492680194.json、图片生成/文生图/Z-IMAGE高清摄影写真流_2007098283063255042.json、图片生成/文生图/最强人像摄影模型 Beyond+Reality+Z-image文生图_2003818575100035073.json、图片生成/文生图/（噪波控制版）Beyond Reality Z-image文生图V1_2003170287237701633.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `DetailDaemonSamplerNode`
- `EmptyLatentImage`
- `KSamplerSelect`
- `LayerUtility: PurgeVRAM`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Float` —— 3/4 个有
- `AddLabel` —— 1/4 个有
- `Image Comparer (rgthree)` —— 1/4 个有
- `ImageConcatMulti` —— 1/4 个有
- `ImageScaleBy` —— 1/4 个有
- `SeedVR2GGUF` —— 1/4 个有
- `SeedVR2LoadDiTModel` —— 1/4 个有
- `SeedVR2LoadVAEModel` —— 1/4 个有
- `SeedVR2VideoUpscaler` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 1080 - 1080 | 4 | 100% |
| 高度 | 1920 | 1560 - 1920 | 4 | 91% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1080，观测区间 1080 - 1080，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1920，观测区间 1560 - 1920，4 个样本，取值集中（一致性 91%）
