---
name: unknown_workflow_lora_sampler_clip_224
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.877333
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, DF_Integer, EmptySD3LatentImage, Fast Groups Bypasser (rgthree), Get Image Size, ImageCASharpening+, ImageResize+, ImpactMinMax, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, SeedVR2, ShowText|pysssss, SimpleMath+, TTP_Image_Assy, TTP_Image_Tile_Batch, Text, Text Concatenate, Text Multiline, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed, easy imageScaleDownToSize, easy joyCaption2API]
problems: []
missing: []
members: [图片生成/图生图/z_都市场景_2000191599701356545.json, 图片生成/图生图/z_都市男_2000203054748233730.json, 平台全量/z_都市女_2000205424139829250.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_224

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/z_都市场景_2000191599701356545.json、图片生成/图生图/z_都市男_2000203054748233730.json、平台全量/z_都市女_2000205424139829250.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DF_Integer`
- `EmptySD3LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Get Image Size`
- `ImageCASharpening+`
- `ImageResize+`
- `ImpactMinMax`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `SeedVR2`
- `ShowText|pysssss`
- `SimpleMath+`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `Text`
- `Text Concatenate`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageScaleDownToSize`
- `easy joyCaption2API`

**可变部分**（部分 workflow 才有）：
- `easy imageChooser` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 15 | 15 - 15 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | res_multistep | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 15，观测区间 15 - 15，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_multistep，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
