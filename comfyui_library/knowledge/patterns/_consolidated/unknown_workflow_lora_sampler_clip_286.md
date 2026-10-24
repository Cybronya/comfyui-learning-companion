---
name: unknown_workflow_lora_sampler_clip_286
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.857
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Get Image Size, ImageCASharpening+, ImageResize+, ImpactMinMax, KSamplerAdvanced, LayerUtility: PurgeVRAM, LoraLoaderModelOnly, PreviewImage, SaveImage, SeedVR2, TTP_Image_Assy, TTP_Image_Tile_Batch, Text Multiline, UNETLoader, VAEDecode, VAELoader, VRAM_Debug]
problems: []
missing: []
members: [图片生成/文生图/Z-Image双采样4K极速放大_2008804942550667266.json, 图片生成/文生图/Z-Image双采样4K极速放大_2010341972136960001.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_286

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Z-Image双采样4K极速放大_2008804942550667266.json、图片生成/文生图/Z-Image双采样4K极速放大_2010341972136960001.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Get Image Size`
- `ImageCASharpening+`
- `ImageResize+`
- `ImpactMinMax`
- `KSamplerAdvanced`
- `LayerUtility: PurgeVRAM`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `SeedVR2`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VRAM_Debug`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 1536 | - | 2 | 100% |
| 采样步数 | randomize | - | 2 | 100% |
| Prompt 约束强度(CFG) | 10 | - | 2 | 100% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler_ancestral | - | 2 | 100% |
| 重绘幅度 | FlowMatchEulerDiscreteScheduler | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1536，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 最常用 randomize，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 10，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，2 个样本，一致性 100%
- 重绘幅度 最常用 FlowMatchEulerDiscreteScheduler，2 个样本，一致性 100%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
