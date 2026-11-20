---
name: unknown_workflow_inpaint_lora_sampler_6
type: Unknown Workflow
frequency: 15
level: strong
coverage: 0.7754
common_nodes: [CLIPTextEncode, CLIPVisionEncode, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, GetImageSize+, ImageCrop+, InpaintModelConditioning, InvertMask, KSampler, LayerMask: LoadFlorence2Model, LayerUtility: Florence2Image2Prompt, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LayerUtility: TextJoin, LoadImage, LoraLoaderModelOnly, MaskPreview+, MathExpression|pysssss, PreviewImage, Replace Text _O, SaveImage, String Literal, StyleModelApply, StyleModelLoader, TTP_Expand_And_Mask, VAEDecode, VAELoader, image_concat_mask(rh)]
problems: []
missing: []
members: [图片生成/图生图/OneReward万物迁移Plus加强版V2（换脸）_1965927486938853377.json, 图片生成/图生图/OneReward万物迁移加强Plus版V2（服装）_1965927391329718273.json, 图片生成/图生图/OneReward万物迁移超强一致性Plus加强版V2（通用）_1965925840011857922.json, 图片生成/图生图/OneReward超强万物迁移_2074106783924318209.json, 图片生成/图生图/OneReward重绘版_2073057791182458881.json, 图片生成/图生图/万物迁移实验版CV512+IcEdit+Ace+Redux512工作流V4_1919594340698488833.json, 图片生成/图生图/换脸万物迁移Plus加强版V2（换脸）_1966128025324654594.json, 图片生成/图生图/新版Redux 512万物迁移超强一致性进阶V3（服装）_1912151378163367938.json, 图片生成/图生图/新版Redux 512万物迁移超强一致性进阶V3（通用）_1912322718623301633.json, 图片生成/文生图/新版Redux 512万物迁移超强一致性进阶V3（换头）_1912119247219425281.json, 平台全量/OneReward高清换脸 加强版高真实度 +皮肤修复+去除AI感  万物迁移_1993871974487228418.json, 平台全量/一键快速换脸，高相似度，高融合度_1923710460460527617.json, 平台全量/万物迁移（OneReward＋ace+pmrf放大）v2_1966427092739108865.json, 平台全量/新版Redux 512万物迁移换装换背景_1912326815527174145.json, 平台全量/蒙版指定换脸_1920755594402136065.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_6

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/图生图/OneReward万物迁移Plus加强版V2（换脸）_1965927486938853377.json、图片生成/图生图/OneReward万物迁移加强Plus版V2（服装）_1965927391329718273.json、图片生成/图生图/OneReward万物迁移超强一致性Plus加强版V2（通用）_1965925840011857922.json、图片生成/图生图/OneReward超强万物迁移_2074106783924318209.json、图片生成/图生图/OneReward重绘版_2073057791182458881.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `GetImageSize+`
- `ImageCrop+`
- `InpaintModelConditioning`
- `InvertMask`
- `KSampler`
- `LayerMask: LoadFlorence2Model`
- `LayerUtility: Florence2Image2Prompt`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: TextJoin`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskPreview+`
- `MathExpression|pysssss`
- `PreviewImage`
- `Replace Text _O`
- `SaveImage`
- `String Literal`
- `StyleModelApply`
- `StyleModelLoader`
- `TTP_Expand_And_Mask`
- `VAEDecode`
- `VAELoader`
- `image_concat_mask(rh)`

**可变部分**（部分 workflow 才有）：
- `AdvancedVisionLoader` —— 14/15 个有
- `ApplyFBCacheOnModel` —— 14/15 个有
- `DisplayText_Zho` —— 14/15 个有
- `ImitationHueNode` —— 14/15 个有
- `LayerMask: BiRefNetUltraV2` —— 14/15 个有
- `LayerMask: LoadBiRefNetModelV2` —— 14/15 个有
- `preview_mask` —— 14/15 个有
- `ImageConcanate` —— 13/15 个有
- `easy showAnything` —— 13/15 个有
- `PMRF` —— 12/15 个有
- `TeaCache` —— 12/15 个有
- `UNETLoader` —— 8/15 个有
- `Note Plus (mtb)` —— 7/15 个有
- `CheckpointLoaderSimple` —— 6/15 个有
- `CropFace` —— 6/15 个有
- `ImpactSwitch` —— 3/15 个有
- `JWInteger` —— 3/15 个有
- `GrowMaskWithBlur` —— 2/15 个有
- `InpaintCrop` —— 2/15 个有
- `InpaintStitch` —— 2/15 个有
- `CLIPVisionLoader` —— 1/15 个有
- `DeepTranslatorTextNode` —— 1/15 个有
- `GetNode` —— 1/15 个有
- `ImageResizeKJ` —— 1/15 个有
- `InpaintResize` —— 1/15 个有
- `JWImageResizeByLongerSide` —— 1/15 个有
- `LayerMask: SegmentAnythingUltra V2` —— 1/15 个有
- `LayerUtility: CropByMask V2` —— 1/15 个有
- `LayerUtility: RestoreCropBox` —— 1/15 个有
- `SetNode` —— 1/15 个有
- `ShowText|pysssss` —— 1/15 个有
- `UnetLoaderGGUF` —— 1/15 个有
- `easy imageSize` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 30 - 30 | 15 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 15 | 100% |
| 采样算法 | euler | - | 15 | 100% |
| 调度器 | normal | - | 15 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 30 - 30，15 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，15 个样本，一致性 100%
- 调度器 最常用 normal，15 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
