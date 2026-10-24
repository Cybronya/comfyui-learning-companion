---
name: unknown_workflow_upscale_lora_clip_7
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.771
common_nodes: [CLIPTextEncode, DualCLIPLoader, Image Comparer (rgthree), LayerColor: ColorAdapter, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, SaveImage, SeedVR2, SeedVR2BlockSwap, TeaCache, UNETLoader, UltimateSDUpscale, UpscaleModelLoader, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/香蕉  移除+seedvr2.5采样高清放大_1992060255425327105.json, 图片生成/图生图/高清放大流 （不改变底图）_1980089374639558657.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_clip_7

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/香蕉  移除+seedvr2.5采样高清放大_1992060255425327105.json、图片生成/图生图/高清放大流 （不改变底图）_1980089374639558657.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：77%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `Image Comparer (rgthree)`
- `LayerColor: ColorAdapter`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `TeaCache`
- `UNETLoader`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Lucy Sharpen` —— 1/2 个有
- `ImageUpscaleWithModel` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `RH_Nano_Banana_Image2Image` —— 1/2 个有
- `SeedVR2LoadDiTModel` —— 1/2 个有
- `SeedVR2LoadVAEModel` —— 1/2 个有
- `SeedVR2VideoUpscaler` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
