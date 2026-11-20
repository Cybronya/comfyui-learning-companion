---
name: unknown_workflow_inpaint_lora_sampler_9
type: Unknown Workflow
frequency: 13
level: strong
coverage: 0.905462
common_nodes: [CLIPTextEncode, CLIPVisionLoader, ConditioningZeroOut, DualCLIPLoader, FaceAnalysisModels, FaceBoundingBox, FluxGuidance, GrowMaskWithBlur, ImageConcanate, ImageCrop, ImageResize+, ImageToMask, InpaintModelConditioning, KSampler, LayerMask: PersonMaskUltra V2, LayerUtility: CropByMask V2, LayerUtility: RestoreCropBox, LoadImage, LoraLoaderModelOnly, MaskToImage, ReduxAdvanced, ResizeMask, SaveImage, StyleModelLoader, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/超强换脸组合FLUX版Redux+ACE+PuLID+表情迁移_1925082430783299586.json, 平台全量/ACE + Redux 换脸_1893311791655501826.json, 平台全量/ACE++redux换脸_1909114596920336386.json, 平台全量/FLUX Redux+ACE++ 换脸工作流_1992572646634352641.json, 平台全量/FLUX Redux+ACE++ 换脸真人专用工作流 一键生成_1998702797640060929.json, 平台全量/FLUX Redux+ACE++ 换脸真人专用工作流 精修_1998721669009133570.json, 平台全量/【首发最强】FLUX_fill+ACE + Redux 换脸1.0_1931952044364464129.json, 平台全量/全自动换脸原度超高【FLUX redux】_1907458513549815810.json, 平台全量/升级版超强换脸组合FLUX版Redux+ACE+PuLID+表情迁移_1911955488177881090.json, 平台全量/超像本人，超像换脸，越看越像，就这个_1998692884826181633.json, 平台全量/超强换脸_1915675455121461250.json, 平台全量/超强换脸组合FLUX版Redux+ACE+PuLID_1905618775213789185.json, 平台全量/龙明Redux+ACE+PuLID换脸_1928675410148757505.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_9

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/超强换脸组合FLUX版Redux+ACE+PuLID+表情迁移_1925082430783299586.json、平台全量/ACE + Redux 换脸_1893311791655501826.json、平台全量/ACE++redux换脸_1909114596920336386.json、平台全量/FLUX Redux+ACE++ 换脸工作流_1992572646634352641.json、平台全量/FLUX Redux+ACE++ 换脸真人专用工作流 一键生成_1998702797640060929.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FaceAnalysisModels`
- `FaceBoundingBox`
- `FluxGuidance`
- `GrowMaskWithBlur`
- `ImageConcanate`
- `ImageCrop`
- `ImageResize+`
- `ImageToMask`
- `InpaintModelConditioning`
- `KSampler`
- `LayerMask: PersonMaskUltra V2`
- `LayerUtility: CropByMask V2`
- `LayerUtility: RestoreCropBox`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskToImage`
- `ReduxAdvanced`
- `ResizeMask`
- `SaveImage`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DetailerForEach` —— 12/13 个有
- `MaskToSEGS` —— 12/13 个有
- `PreviewImage` —— 12/13 个有
- `easy cleanGpuUsed` —— 8/13 个有
- `EmptyImage` —— 7/13 个有
- `ImpactGaussianBlurMask` —— 7/13 个有
- `ApplyPulidFlux` —— 6/13 个有
- `CR Color Panel` —— 6/13 个有
- `DifferentialDiffusion` —— 6/13 个有
- `Image Comparer (rgthree)` —— 6/13 个有
- `PulidFluxEvaClipLoader` —— 6/13 个有
- `PulidFluxInsightFaceLoader` —— 6/13 个有
- `PulidFluxModelLoader` —— 6/13 个有
- `TeaCache` —— 5/13 个有
- `preview_mask` —— 5/13 个有
- `ConstrainImage|pysssss` —— 4/13 个有
- `RepeatLatentBatch` —— 3/13 个有
- `ExpressionEditor` —— 2/13 个有
- `ImageAndMaskPreview` —— 2/13 个有
- `ImitationHueNode` —— 2/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/13 个有
- `FloatConstant` —— 1/13 个有
- `LayerMask: MaskStroke` —— 1/13 个有
- `MaskPreview+` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 15 - 28 | 13 | 75% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 13 | 100% |
| 采样算法 | euler | - | 13 | 100% |
| 调度器 | normal | - | 13 | 92% |
| 重绘幅度 | 1 | 0.6 - 1 | 13 | 89% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 15 - 28，13 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，13 个样本，一致性 100%
- 调度器 最常用 normal，13 个样本，一致性 92%
- 重绘幅度 中位数 1，观测区间 0.6 - 1，13 个样本，取值集中（一致性 89%）
