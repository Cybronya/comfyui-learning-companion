---
name: unknown_workflow_upscale_lora_sampler_125
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9365
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, GetImageSize+, ImageResize+, ImageScaleBy, KSamplerAdvanced, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/写实人像摄影-Zimage+Flow-DPO-真实光影色彩_2030184168344260609.json, 数字人/数字人/VividMuse真实人像摄影V2.1_2022302845051080706.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_125

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/写实人像摄影-Zimage+Flow-DPO-真实光影色彩_2030184168344260609.json、数字人/数字人/VividMuse真实人像摄影V2.1_2022302845051080706.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `GetImageSize+`
- `ImageResize+`
- `ImageScaleBy`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/2 个有
- `DF_Text_Box` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `ImpactSwitch` —— 1/2 个有
- `Int` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `RH_Captioner` —— 1/2 个有
- `Seed_` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有
- `easy promptList` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 2 | 100% |
| Prompt 约束强度(CFG) | 8 | - | 2 | 100% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | res_multistep | - | 2 | 50% |
| 重绘幅度 | simple | - | 2 | 50% |
| 宽度 | 1536 | - | 2 | 100% |
| 高度 | 2048 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 res_multistep，2 个样本，一致性 50%
- 重绘幅度 最常用 simple，2 个样本，一致性 50%
- 宽度 中位数 1536，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 2048，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
