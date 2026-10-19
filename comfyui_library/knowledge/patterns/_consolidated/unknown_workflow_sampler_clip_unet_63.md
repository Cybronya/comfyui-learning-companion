---
name: unknown_workflow_sampler_clip_unet_63
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.908
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, FluxGuidance, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [LayerUtility: PurgeVRAM]
members: [图片生成/文生图/1926661482686353410.json, 图片生成/文生图/1933332658841628674.json, 图片生成/文生图/1986239618842578945.json, "视频生成/文生视频/谁与争锋 Flux2 Z-image,  多图编辑 挑战 Qwen Edit_1994227326332370945.json"]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_63

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/1926661482686353410.json、图片生成/文生图/1933332658841628674.json、图片生成/文生图/1986239618842578945.json、视频生成/文生视频/谁与争锋 Flux2 Z-image,  多图编辑 挑战 Qwen Edit_1994227326332370945.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `FluxGuidance`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ReferenceLatent` —— 3/4 个有
- `ImageScaleToTotalPixels` —— 2/4 个有
- `LoadImage` —— 2/4 个有
- `VAEEncode` —— 2/4 个有
- `ImageConcanate` —— 1/4 个有
- `Int` —— 1/4 个有
- `LayerUtility: PurgeVRAM` —— 1/4 个有
- `PrimitiveInt` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: PurgeVRAM
