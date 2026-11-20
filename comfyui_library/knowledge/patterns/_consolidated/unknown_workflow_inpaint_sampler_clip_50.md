---
name: unknown_workflow_inpaint_sampler_clip_50
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8658
common_nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, ImageConcanate, ImageCrop+, ImageToMask, InpaintModelConditioning, InpaintStitch, KSampler, LoadImage, MaskToImage, PreviewImage, SaveImage, StyleModelApply, StyleModelLoader, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/换脸换发型工作流V2.0_1928219088726966273.json, 图片生成/图生图/超强万物迁移_1915340896831733762.json, 图片生成/图生图/遮罩局部参考重绘_1989320919707471874.json, 平台全量/Flux ReduxV1.0手动遮罩换装_1939995743774216194.json, 平台全量/redux超强局部重绘+迁移+换装_1937804687158460418.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_50

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/换脸换发型工作流V2.0_1928219088726966273.json、图片生成/图生图/超强万物迁移_1915340896831733762.json、图片生成/图生图/遮罩局部参考重绘_1989320919707471874.json、平台全量/Flux ReduxV1.0手动遮罩换装_1939995743774216194.json、平台全量/redux超强局部重绘+迁移+换装_1937804687158460418.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 5 个 workflow 都包含：
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
- `Image Comparer (rgthree)` —— 4/5 个有
- `ImageResize+` —— 4/5 个有
- `InpaintCrop` —— 4/5 个有
- `LayerMask: SegmentAnythingUltra V2` —— 4/5 个有
- `easy imageSize` —— 4/5 个有
- `LayerUtility: ColorImage` —— 3/5 个有
- `Image Blank` —— 2/5 个有
- `LoraLoaderModelOnly` —— 2/5 个有
- `RHHiddenNodes` —— 2/5 个有
- `DF_Image_scale_to_side` —— 1/5 个有
- `EmptyImage` —— 1/5 个有
- `GetImageSize+` —— 1/5 个有
- `LayerUtility: ImageBlendAdvance` —— 1/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/5 个有
- `LayerUtility: ImageScaleRestore V2` —— 1/5 个有
- `Mask Fill Holes` —— 1/5 个有
- `MaskPreview+` —— 1/5 个有
- `ReduxAdvanced` —— 1/5 个有
- `SUPIR_Upscale` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有
- `easy imageCropFromMask` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 28 | 5 | 85% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 28，5 个样本，取值集中（一致性 85%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
