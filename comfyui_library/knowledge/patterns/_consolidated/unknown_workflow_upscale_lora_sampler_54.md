---
name: unknown_workflow_upscale_lora_sampler_54
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.917
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptySD3LatentImage, Float, GetImageSize+, ImageResize+, ImageScaleBy, KSampler, LoraLoaderModelOnly, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, VAEDecode, easy cleanGpuUsed, easy imageScaleDownBy]
problems: []
missing: []
members: [图片生成/文生图/一键生成二次元动漫_2072607003708579841.json, 视频生成/文生视频/二次元动漫v1_2072142075700801537.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_54

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/一键生成二次元动漫_2072607003708579841.json、视频生成/文生视频/二次元动漫v1_2072142075700801537.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptySD3LatentImage`
- `Float`
- `GetImageSize+`
- `ImageResize+`
- `ImageScaleBy`
- `KSampler`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `VAEDecode`
- `easy cleanGpuUsed`
- `easy imageScaleDownBy`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 4 | - | 2 | 100% |
| 采样算法 | res_multistep | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_multistep，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
