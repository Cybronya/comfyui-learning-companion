---
name: unknown_workflow_lora_sampler_clip_249
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8685
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, DF_Integer, EmptySD3LatentImage, Fast Groups Bypasser (rgthree), Get Image Size, ImageCASharpening+, ImageResize+, ImpactMinMax, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, SeedVR2, ShowText|pysssss, SimpleMath+, TTP_Image_Assy, TTP_Image_Tile_Batch, Text, Text Concatenate, Text Multiline, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed, easy imageScaleDownToSize, easy joyCaption2API]
problems: []
missing: []
members: [图片生成/图生图/z_都市场景_2000191599701356545.json, 图片生成/图生图/z_都市男_2000203054748233730.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_249

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/z_都市场景_2000191599701356545.json、图片生成/图生图/z_都市男_2000203054748233730.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 2 个 workflow 都包含：
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
- `easy imageChooser` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 15 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | res_multistep | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 15，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_multistep，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
