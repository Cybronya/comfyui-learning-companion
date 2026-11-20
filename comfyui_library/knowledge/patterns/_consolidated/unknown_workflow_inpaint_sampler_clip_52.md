---
name: unknown_workflow_inpaint_sampler_clip_52
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.854
common_nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, ImageConcanate, ImageCrop+, ImageToMask, InpaintModelConditioning, InpaintStitch, KSampler, LoadImage, MaskToImage, PreviewImage, SaveImage, StyleModelApply, StyleModelLoader, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/换脸换发型工作流V2.0_1928219088726966273.json, 图片生成/图生图/超强万物迁移_1915340896831733762.json, 图片生成/图生图/遮罩局部参考重绘_1989320919707471874.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_52

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/换脸换发型工作流V2.0_1928219088726966273.json、图片生成/图生图/超强万物迁移_1915340896831733762.json、图片生成/图生图/遮罩局部参考重绘_1989320919707471874.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImageConcanate`
- `ImageCrop+`
- `ImageToMask`
- `InpaintModelConditioning`
- `InpaintStitch`
- `KSampler`
- `LoadImage`
- `MaskToImage`
- `PreviewImage`
- `SaveImage`
- `StyleModelApply`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Blank` —— 2/3 个有
- `Image Comparer (rgthree)` —— 2/3 个有
- `ImageResize+` —— 2/3 个有
- `InpaintCrop` —— 2/3 个有
- `LayerMask: SegmentAnythingUltra V2` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `RHHiddenNodes` —— 2/3 个有
- `easy imageSize` —— 2/3 个有
- `DF_Image_scale_to_side` —— 1/3 个有
- `EmptyImage` —— 1/3 个有
- `GetImageSize+` —— 1/3 个有
- `LayerUtility: ColorImage` —— 1/3 个有
- `LayerUtility: ImageBlendAdvance` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `LayerUtility: ImageScaleRestore V2` —— 1/3 个有
- `Mask Fill Holes` —— 1/3 个有
- `MaskPreview+` —— 1/3 个有
- `ReduxAdvanced` —— 1/3 个有
- `SUPIR_Upscale` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有
- `easy imageCropFromMask` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 28 | 3 | 83% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 28，3 个样本，取值集中（一致性 83%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
