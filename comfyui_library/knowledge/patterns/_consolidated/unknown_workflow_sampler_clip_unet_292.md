---
name: unknown_workflow_sampler_clip_unet_292
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.91
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, ImageScaleToTotalPixels, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX2多图溶图_2016400551017193474.json, 图片生成/图生图/FLUX2支持多图溶图-透视修正_2045081810996043777.json, 图片生成/图生图/Flux 2 klein 单图编辑角色卡（多角度图-图生图）工作流_2054450460597202945.json, 图片生成/图生图/Flux2溶图_2014992165562228737.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_292

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/FLUX2多图溶图_2016400551017193474.json、图片生成/图生图/FLUX2支持多图溶图-透视修正_2045081810996043777.json、图片生成/图生图/Flux 2 klein 单图编辑角色卡（多角度图-图生图）工作流_2054450460597202945.json、图片生成/图生图/Flux2溶图_2014992165562228737.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
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
- `RHHiddenNodes` —— 3/4 个有
- `Text Concatenate` —— 3/4 个有
- `FastCanvas` —— 2/4 个有
- `FastCanvasTool` —— 2/4 个有
- `InspyrenetRembg` —— 2/4 个有
- `LayerUtility: CropByMask V2` —— 2/4 个有
- `LayerUtility: ImageRemoveAlpha` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `RH_LLMAPI_Pro_Node` —— 2/4 个有
- `ShowText|pysssss` —— 2/4 个有
- `ttN text` —— 2/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
