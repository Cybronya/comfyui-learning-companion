---
name: unknown_workflow_sampler_clip_unet_268
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8332
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, ImageScaleToTotalPixels, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/danotebook-flux2-klein-9b_2062427994236481537.json, 图片生成/文生图/flux2-ftp8 workflow_1993525727769411585.json, 图片生成/文生图/flux2_文生图+图片参考_1993696007951237121.json, 图片生成/文生图/flux2基础_文生图_图生图_迁移_1993562025060139010.json, "视频生成/文生视频/谁与争锋 Flux2 Z-image,  多图编辑 挑战 Qwen Edit_1994227326332370945.json"]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_268

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/danotebook-flux2-klein-9b_2062427994236481537.json、图片生成/文生图/flux2-ftp8 workflow_1993525727769411585.json、图片生成/文生图/flux2_文生图+图片参考_1993696007951237121.json、图片生成/文生图/flux2基础_文生图_图生图_迁移_1993562025060139010.json、视频生成/文生视频/谁与争锋 Flux2 Z-image,  多图编辑 挑战 Qwen Edit_1994227326332370945.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `ImageScaleToTotalPixels`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 4/5 个有
- `FluxGuidance` —— 4/5 个有
- `CFGGuider` —— 1/5 个有
- `ComfySwitchNode` —— 1/5 个有
- `ConditioningZeroOut` —— 1/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `ImageConcanate` —— 1/5 个有
- `LayerUtility: PurgeVRAM` —— 1/5 个有
- `PrimitiveInt` —— 1/5 个有
- `PrimitiveString` —— 1/5 个有
- `StringCompare` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
