---
name: unknown_workflow_upscale_lora_clip_7
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.744
common_nodes: [CLIPTextEncode, DualCLIPLoader, Image Comparer (rgthree), LayerColor: ColorAdapter, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, SaveImage, SeedVR2, SeedVR2BlockSwap, TeaCache, UNETLoader, UltimateSDUpscale, UpscaleModelLoader, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/香蕉  移除+seedvr2.5采样高清放大_1992060255425327105.json, 图片生成/图生图/高清放大流 （不改变底图）_1980089374639558657.json, 平台全量/高清放大流 （不改变底图）_1985634682681401345.json, 平台全量/高清放大流_2080219695105536002.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_clip_7

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/香蕉  移除+seedvr2.5采样高清放大_1992060255425327105.json、图片生成/图生图/高清放大流 （不改变底图）_1980089374639558657.json、平台全量/高清放大流 （不改变底图）_1985634682681401345.json、平台全量/高清放大流_2080219695105536002.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：74%

## 共有节点

全部 4 个 workflow 都包含：
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
- `Image Lucy Sharpen` —— 3/4 个有
- `ImageUpscaleWithModel` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `RH_Nano_Banana_Image2Image` —— 1/4 个有
- `SeedVR2LoadDiTModel` —— 1/4 个有
- `SeedVR2LoadVAEModel` —— 1/4 个有
- `SeedVR2VideoUpscaler` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
