---
name: unknown_workflow_inpaint_upscale_sampler_5
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.881
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, DetailDaemonSamplerNode, Florence2ModelLoader, Florence2Run, FluxKontextMultiReferenceLatentMethod, Image Comparer (rgthree), ImageScale, InpaintModelConditioning, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewBridge, ReferenceLatent, SamplerCustom, SaveImage, Seed (rgthree), SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/qwen-Image-edit-2511-超低画质图像高清修复-放大200倍_2009492416549625858.json, 图片生成/图生图/qwen-edit-2511-老照片高清修复_2007617526280228865.json, 图片生成/图生图/老照片高清修复-Twinkle_2019283374648598529.json, 图片生成/图生图/超小尺寸放大200倍——Qwen-Image-Edit-2511_2009602940213923842.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_upscale_sampler_5

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/qwen-Image-edit-2511-超低画质图像高清修复-放大200倍_2009492416549625858.json、图片生成/图生图/qwen-edit-2511-老照片高清修复_2007617526280228865.json、图片生成/图生图/老照片高清修复-Twinkle_2019283374648598529.json、图片生成/图生图/超小尺寸放大200倍——Qwen-Image-Edit-2511_2009602940213923842.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `DetailDaemonSamplerNode`
- `Florence2ModelLoader`
- `Florence2Run`
- `FluxKontextMultiReferenceLatentMethod`
- `Image Comparer (rgthree)`
- `ImageScale`
- `InpaintModelConditioning`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewBridge`
- `ReferenceLatent`
- `SamplerCustom`
- `SaveImage`
- `Seed (rgthree)`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 2/4 个有
- `Any Switch (rgthree)` —— 2/4 个有
- `ColorMatch` —— 2/4 个有
- `ControlNetApplyAdvanced` —— 2/4 个有
- `ControlNetLoader` —— 2/4 个有
- `Fast Groups Bypasser (rgthree)` —— 2/4 个有
- `ImpactMakeAnyList` —— 2/4 个有
- `easy imageSizeBySide` —— 2/4 个有
- `Anything Everywhere` —— 1/4 个有
- `Anything Everywhere3` —— 1/4 个有
- `LayerUtility: PurgeVRAM V2` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.9 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.9，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
