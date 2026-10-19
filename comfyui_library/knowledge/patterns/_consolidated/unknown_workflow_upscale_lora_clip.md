---
name: unknown_workflow_upscale_lora_clip
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.792
common_nodes: [CLIPTextEncode, DualCLIPLoader, Get Image Size, Image Comparer (rgthree), ImageResize+, ImageScaleToTotalPixels, LayerColor: ColorAdapter, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, SeedVR2, SeedVR2BlockSwap, TeaCache, UNETLoader, UltimateSDUpscale, UpscaleModelLoader, VAELoader, easy compare, easy ifElse]
problems: []
missing: []
members: [图片生成/文生图/高清放大流-好用（干净版）_2104395854693093377.json, 图片生成/文生图/高清放大流最新版（干净版）_2104394861406408705.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_clip

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/高清放大流-好用（干净版）_2104395854693093377.json、图片生成/文生图/高清放大流最新版（干净版）_2104394861406408705.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：79%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `Get Image Size`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImageScaleToTotalPixels`
- `LayerColor: ColorAdapter`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `TeaCache`
- `UNETLoader`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAELoader`
- `easy compare`
- `easy ifElse`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
