---
name: text_to_image_controlnet_ipadapter_upscale
type: Text To Image
frequency: 6
level: weak
coverage: 0.718
common_nodes: [BrushNet, BrushNetLoader, CLIPTextEncode, CLIPTextEncodeFlux, CLIPVisionLoader, CannyEdgePreprocessor, CheckpointLoaderSimple, ConditioningZeroOut, ControlNetApplyAdvanced, ControlNetLoader, DetailTransfer, DetailerForEachDebug, DualCLIPLoader, Efficient Loader, EmptyLatentImage, ICLightConditioning, IPAdapterAdvanced, IPAdapterUnifiedLoader, ImageScale, ImageScaleBy, ImageToMask, ImageUpscaleWithModel, ImpactDilateMask, InvertMask, KSampler, KSampler (Efficient), LayerMask: MaskGrow, LayerMask: SegmentAnythingUltra V2, LayerUtility: ExtendCanvas, LayerUtility: ImageBlend, LoadAndApplyICLightUnet, LoadImage, MaskToImage, MaskToSEGS, SaveImage, TextInput_, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy imageScaleDownToSize, easy imageSize]
problems: [Steps较低可能导致细节不足]
missing: [Efficient Loader, LayerMask: MaskGrow, LayerMask: SegmentAnythingUltra V2, LayerUtility: ExtendCanvas, LayerUtility: ImageBlend, easy cleanGpuUsed, KSampler (Efficient), easy imageScaleDownToSize, easy imageSize]
members: [图片生成/图生图/2030958376661815298.json, 视频生成/图生视频/PRO图生图工具｜文生图图生视频多模态处理_2094305135324389378.json, 视频生成/图生视频/PRO级图生图｜超强风格模拟背景创意光影画质优化_2090828347478728705.json, 视频生成/图生视频/2067057454910885889.json, 视频生成/图生视频/图生图 PRO_2030958376661815298.json, 视频生成/图生视频/超强风格模拟图生图 PRO 光影画质优化创意背景文生图_2094168668145012738.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_ipadapter_upscale

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/2030958376661815298.json、视频生成/图生视频/PRO图生图工具｜文生图图生视频多模态处理_2094305135324389378.json、视频生成/图生视频/PRO级图生图｜超强风格模拟背景创意光影画质优化_2090828347478728705.json、视频生成/图生视频/2067057454910885889.json、视频生成/图生视频/图生图 PRO_2030958376661815298.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：72%

## 共有节点

全部 6 个 workflow 都包含：
- `BrushNet`
- `BrushNetLoader`
- `CLIPTextEncode`
- `CLIPTextEncodeFlux`
- `CLIPVisionLoader`
- `CannyEdgePreprocessor`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DetailTransfer`
- `DetailerForEachDebug`
- `DualCLIPLoader`
- `Efficient Loader`
- `EmptyLatentImage`
- `ICLightConditioning`
- `IPAdapterAdvanced`
- `IPAdapterUnifiedLoader`
- `ImageScale`
- `ImageScaleBy`
- `ImageToMask`
- `ImageUpscaleWithModel`
- `ImpactDilateMask`
- `InvertMask`
- `KSampler`
- `KSampler (Efficient)`
- `LayerMask: MaskGrow`
- `LayerMask: SegmentAnythingUltra V2`
- `LayerUtility: ExtendCanvas`
- `LayerUtility: ImageBlend`
- `LoadAndApplyICLightUnet`
- `LoadImage`
- `MaskToImage`
- `MaskToSEGS`
- `SaveImage`
- `TextInput_`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageScaleDownToSize`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 4/6 个有
- `LoraLoaderModelOnly` —— 4/6 个有
- `JjkText` —— 3/6 个有
- `solarL_SaveImagesToZip` —— 3/6 个有
- `孤海注释` —— 3/6 个有
- `DF_Text_Box` —— 1/6 个有
- `GrowMask` —— 1/6 个有
- `Image Comparer (rgthree)` —— 1/6 个有
- `JWImageResizeByLongerSide` —— 1/6 个有
- `Joy_caption_two` —— 1/6 个有
- `Joy_caption_two_load` —— 1/6 个有
- `LatentUpscaleBy` —— 1/6 个有
- `LoraLoader` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `PreviewMask_` —— 1/6 个有
- `QwenImageIntegratedKSampler` —— 1/6 个有
- `ShowText|pysssss` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 296 | 80 - 512 | 6 | 27% |
| 高度 | 296 | 80 - 512 | 6 | 27% |
| ControlNet 权重 | 0.3 | 0.3 - 0.3 | 6 | 100% |
| 采样步数 | 4 | 4 - 28 | 5 | 14% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 6 | 67% |
| 采样算法 | er_sde | - | 6 | 50% |
| 调度器 | beta | - | 6 | 50% |
| 重绘幅度 | 1 | 1 - 999 | 6 | 0% |
| LoRA 模型强度 | 0.8 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 296，观测区间 80 - 512，6 个样本，取值分散，一致性仅 27%
- 高度 中位数 296，观测区间 80 - 512，6 个样本，取值分散，一致性仅 27%
- ControlNet 权重 中位数 0.3，观测区间 0.3 - 0.3，6 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 28，5 个样本，取值分散，一致性仅 14%
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，6 个样本
- 采样算法 最常用 er_sde，6 个样本，一致性 50%
- 调度器 最常用 beta，6 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 999，6 个样本，取值分散，一致性仅 0%
- 风险：重绘幅度 观测到 999，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
- 高发问题（3/6 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：Efficient Loader、LayerMask: MaskGrow、LayerMask: SegmentAnythingUltra V2、LayerUtility: ExtendCanvas、LayerUtility: ImageBlend
