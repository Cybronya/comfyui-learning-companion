---
name: unknown_workflow_inpaint_lora_sampler_7
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.7856
common_nodes: [AdvancedVisionLoader, ApplyFBCacheOnModel, CLIPTextEncode, CLIPVisionEncode, DifferentialDiffusion, DisplayText_Zho, DualCLIPLoader, FluxGuidance, GetImageSize+, ImageCrop+, ImitationHueNode, InpaintModelConditioning, InvertMask, KSampler, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModelV2, LayerMask: LoadFlorence2Model, LayerUtility: Florence2Image2Prompt, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LayerUtility: TextJoin, LoadImage, LoraLoaderModelOnly, MaskPreview+, MathExpression|pysssss, PreviewImage, Replace Text _O, SaveImage, String Literal, StyleModelApply, StyleModelLoader, TTP_Expand_And_Mask, VAEDecode, VAELoader, image_concat_mask(rh), preview_mask]
problems: []
missing: []
members: [图片生成/图生图/OneReward万物迁移Plus加强版V2（换脸）_1965927486938853377.json, 图片生成/图生图/OneReward万物迁移加强Plus版V2（服装）_1965927391329718273.json, 图片生成/图生图/OneReward万物迁移超强一致性Plus加强版V2（通用）_1965925840011857922.json, 图片生成/图生图/OneReward超强万物迁移_2074106783924318209.json, 图片生成/图生图/OneReward重绘版_2073057791182458881.json, 图片生成/图生图/万物迁移实验版CV512+IcEdit+Ace+Redux512工作流V4_1919594340698488833.json, 图片生成/图生图/换脸万物迁移Plus加强版V2（换脸）_1966128025324654594.json, 图片生成/图生图/新版Redux 512万物迁移超强一致性进阶V3（服装）_1912151378163367938.json, 图片生成/图生图/新版Redux 512万物迁移超强一致性进阶V3（通用）_1912322718623301633.json, 图片生成/文生图/新版Redux 512万物迁移超强一致性进阶V3（换头）_1912119247219425281.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_7

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/OneReward万物迁移Plus加强版V2（换脸）_1965927486938853377.json、图片生成/图生图/OneReward万物迁移加强Plus版V2（服装）_1965927391329718273.json、图片生成/图生图/OneReward万物迁移超强一致性Plus加强版V2（通用）_1965925840011857922.json、图片生成/图生图/OneReward超强万物迁移_2074106783924318209.json、图片生成/图生图/OneReward重绘版_2073057791182458881.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 10 个 workflow 都包含：
- `AdvancedVisionLoader`
- `ApplyFBCacheOnModel`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `DifferentialDiffusion`
- `DisplayText_Zho`
- `DualCLIPLoader`
- `FluxGuidance`
- `GetImageSize+`
- `ImageCrop+`
- `ImitationHueNode`
- `InpaintModelConditioning`
- `InvertMask`
- `KSampler`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: LoadBiRefNetModelV2`
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
- `preview_mask`

**可变部分**（部分 workflow 才有）：
- `ImageConcanate` —— 8/10 个有
- `PMRF` —— 8/10 个有
- `TeaCache` —— 8/10 个有
- `easy showAnything` —— 8/10 个有
- `Note Plus (mtb)` —— 7/10 个有
- `UNETLoader` —— 6/10 个有
- `CheckpointLoaderSimple` —— 4/10 个有
- `CropFace` —— 3/10 个有
- `ImpactSwitch` —— 3/10 个有
- `JWInteger` —— 3/10 个有
- `InpaintCrop` —— 1/10 个有
- `InpaintStitch` —— 1/10 个有
- `JWImageResizeByLongerSide` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 30 - 30 | 10 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | normal | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 30 - 30，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 normal，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
