---
name: unknown_workflow_upscale_lora_sampler_102
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.936
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ColorMatch, Image Comparer (rgthree), ImageResize+, ImageScaleBy, ImageUpscaleWithModel, KSampler, LoadImage, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, NunchakuTextEncoderLoader, PreviewImage, SUPIR_conditioner, SUPIR_decode, SUPIR_encode, SUPIR_first_stage, SUPIR_model_loader_v2, SUPIR_sample, SaveImage, UpscaleModelLoader, VAEDecodeTiled, VAEEncodeTiled, VAELoader, easy int]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/图生图/高质感人像纹理还原_1990348117071548418.json, 图片生成/文生图/SUPIR+FLUX.krea图片变清晰去ai感_1934859493480013825.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_102

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/高质感人像纹理还原_1990348117071548418.json、图片生成/文生图/SUPIR+FLUX.krea图片变清晰去ai感_1934859493480013825.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ColorMatch`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoadImage`
- `NunchakuFluxDiTLoader`
- `NunchakuFluxLoraLoader`
- `NunchakuTextEncoderLoader`
- `PreviewImage`
- `SUPIR_conditioner`
- `SUPIR_decode`
- `SUPIR_encode`
- `SUPIR_first_stage`
- `SUPIR_model_loader_v2`
- `SUPIR_sample`
- `SaveImage`
- `UpscaleModelLoader`
- `VAEDecodeTiled`
- `VAEEncodeTiled`
- `VAELoader`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `CR Image Input Switch` —— 1/2 个有
- `DF_Integer` —— 1/2 个有
- `ImageCASharpening+` —— 1/2 个有
- `ImpactMinMax` —— 1/2 个有
- `LayerUtility: PurgeVRAM V2` —— 1/2 个有
- `MemoryCleaner` —— 1/2 个有
- `SeedVR2` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有
- `TTP_Image_Assy` —— 1/2 个有
- `TTP_Image_Tile_Batch` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有
- `easy imageSize` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | kl_optimal | - | 2 | 50% |
| 重绘幅度 | 0.475 | - | 2 | 53% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 2/2 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 kl_optimal，2 个样本，一致性 50%
- 重绘幅度 中位数 0.475，样本不足，未给区间，2 个样本
- 高发问题（2/2 个样本）：发现KSampler但没有VAEDecode
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
