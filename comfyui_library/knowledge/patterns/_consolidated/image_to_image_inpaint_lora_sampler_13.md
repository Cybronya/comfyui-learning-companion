---
name: image_to_image_inpaint_lora_sampler_13
type: Image To Image
frequency: 2
level: weak
coverage: 0.966
common_nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ConditioningZeroOut, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, ImageConcanate, ImageCrop+, ImageResize+, ImageScale, ImageToMask, InpaintModelConditioning, Int, KSampler, LayerUtility: ColorImage V2, LayerUtility: CropByMask V2, LayerUtility: RestoreCropBox, LoadImage, LoraLoaderModelOnly, MaskToImage, ResizeMask, SaveImage, StyleModelApply, StyleModelLoader, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageSize]
problems: []
missing: []
members: [图片生成/图生图/Flux模特迁移（替换模特_完美还原）_1917024768196022274.json, 图片生成/图生图/手机壳丨一致性多角度出图_1926543944396738561.json]
source: knowledge_consolidation
---

# image_to_image_inpaint_lora_sampler_13

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Flux模特迁移（替换模特_完美还原）_1917024768196022274.json、图片生成/图生图/手机壳丨一致性多角度出图_1926543944396738561.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：97%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImageConcanate`
- `ImageCrop+`
- `ImageResize+`
- `ImageScale`
- `ImageToMask`
- `InpaintModelConditioning`
- `Int`
- `KSampler`
- `LayerUtility: ColorImage V2`
- `LayerUtility: CropByMask V2`
- `LayerUtility: RestoreCropBox`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskToImage`
- `ResizeMask`
- `SaveImage`
- `StyleModelApply`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncodeFlux` —— 1/2 个有
- `CR Latent Batch Size` —— 1/2 个有
- `ConstrainImage|pysssss` —— 1/2 个有
- `ImpactImageBatchToImageList` —— 1/2 个有
- `LayerMask: LoadFlorence2Model` —— 1/2 个有
- `LayerMask: MaskStroke` —— 1/2 个有
- `LayerMask: SegmentAnythingUltra V2` —— 1/2 个有
- `LayerUtility: Florence2Image2Prompt` —— 1/2 个有
- `LayerUtility: ImageRemoveAlpha` —— 1/2 个有
- `LayerUtility: PurgeVRAM` —— 1/2 个有
- `LayerUtility: TextJoin` —— 1/2 个有
- `Mask Fill Holes` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `RH_Captioner` —— 1/2 个有
- `ReduxAdvanced` —— 1/2 个有
- `Replace Text _O` —— 1/2 个有
- `String Literal` —— 1/2 个有
- `easy makeImageForICLora` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | - | 2 | 80% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 50% |
| 重绘幅度 | 0.625 | - | 2 | 40% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 50%
- 重绘幅度 中位数 0.625，样本不足，未给区间，2 个样本，取值分散，一致性仅 40%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
