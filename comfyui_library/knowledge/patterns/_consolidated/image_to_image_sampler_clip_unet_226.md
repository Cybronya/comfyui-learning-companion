---
name: image_to_image_sampler_clip_unet_226
type: Image To Image
frequency: 2
level: weak
coverage: 0.8165
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DownloadAndLoadFlorence2Model, DownloadAndLoadSAM2Model, DualCLIPLoader, Florence2Run, FluxGuidance, ImageScaleDownToSize, KSampler, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModelV2, LoadImage, PreviewImage, RHHiddenNodes, RH_LLMAPI_NODE, RH_Nano_Banana_Image2Image, ReferenceLatent, Sam2Segmentation, SaveImage, ShowText|pysssss, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy forLoopEnd, easy forLoopStart, easy imageCropFromMask, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/高清白模四视图_2008533011859509249.json, 平台全量/香蕉模型全自动一键生成三视图+自动分割+自动裁剪（for循环批量）_1963053340596875266.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_226

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/高清白模四视图_2008533011859509249.json、平台全量/香蕉模型全自动一键生成三视图+自动分割+自动裁剪（for循环批量）_1963053340596875266.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DownloadAndLoadFlorence2Model`
- `DownloadAndLoadSAM2Model`
- `DualCLIPLoader`
- `Florence2Run`
- `FluxGuidance`
- `ImageScaleDownToSize`
- `KSampler`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: LoadBiRefNetModelV2`
- `LoadImage`
- `PreviewImage`
- `RHHiddenNodes`
- `RH_LLMAPI_NODE`
- `RH_Nano_Banana_Image2Image`
- `ReferenceLatent`
- `Sam2Segmentation`
- `SaveImage`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy imageCropFromMask`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `DF_Get_image_size` —— 1/2 个有
- `FluxKontextImageScale` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `ImagePadForOutpaint` —— 1/2 个有
- `ImagePadForOutpaintTargetSize` —— 1/2 个有
- `ImageScaleToTotalPixels` —— 1/2 个有
- `ImageUpscaleWithModel` —— 1/2 个有
- `JWImageResizeByLongerSide` —— 1/2 个有
- `LayerUtility: ImageRemoveAlpha` —— 1/2 个有
- `LoraLoader` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有
- `RH_Nano_Banana2_Image2Image` —— 1/2 个有
- `SeedVR2` —— 1/2 个有
- `SeedVR2BlockSwap` —— 1/2 个有
- `SeedVR2ExtraArgs` —— 1/2 个有
- `UpscaleModelLoader` —— 1/2 个有
- `easy imageConcat` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 22.5 | - | 2 | 89% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |
| LoRA 模型强度 | 0.8 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 22.5，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
