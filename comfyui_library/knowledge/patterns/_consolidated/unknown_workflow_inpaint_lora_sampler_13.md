---
name: unknown_workflow_inpaint_lora_sampler_13
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.910286
common_nodes: [AdvancedVisionLoader, CLIPTextEncode, CLIPVisionEncode, DualCLIPLoader, FluxGuidance, InpaintModelConditioning, KSampler, LayerMask: MaskGrow, LayerUtility: CropByMask V2, LayerUtility: ICMask, LayerUtility: ICMaskCropBack, LayerUtility: RestoreCropBox, LoadImage, LoraLoaderModelOnly, SaveImage, StyleModelApply, StyleModelLoader, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/万物迁移-Redux-512+Pulid-人物-强劲参考_1913094549655486465.json, 图片生成/图生图/万物迁移-Redux-512-强劲参考_1913041299597946882.json, 图片生成/图生图/万物迁移V2-ICE+Redux512强强联合_1925163632135761922.json, 图片生成/图生图/平台用-汽车轮毂商标局部修复_2059452336480808962.json, 图片生成/图生图/汽车轮毂商标局部修复_1984676237534707714.json, 图片生成/图生图/车身替换-Fill&Redux_2062346798567608321.json, 图片生成/图生图/🦖产品强力迁移-超强参考_1925804870501093378.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_13

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/万物迁移-Redux-512+Pulid-人物-强劲参考_1913094549655486465.json、图片生成/图生图/万物迁移-Redux-512-强劲参考_1913041299597946882.json、图片生成/图生图/万物迁移V2-ICE+Redux512强强联合_1925163632135761922.json、图片生成/图生图/平台用-汽车轮毂商标局部修复_2059452336480808962.json、图片生成/图生图/汽车轮毂商标局部修复_1984676237534707714.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 7 个 workflow 都包含：
- `AdvancedVisionLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `InpaintModelConditioning`
- `KSampler`
- `LayerMask: MaskGrow`
- `LayerUtility: CropByMask V2`
- `LayerUtility: ICMask`
- `LayerUtility: ICMaskCropBack`
- `LayerUtility: RestoreCropBox`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `StyleModelApply`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 6/7 个有
- `PreviewImage` —— 6/7 个有
- `Image Comparer (rgthree)` —— 3/7 个有
- `Mask Fill Holes` —— 2/7 个有
- `Mask_image2mask` —— 2/7 个有
- `ApplyPulidFlux` —— 1/7 个有
- `CR Text` —— 1/7 个有
- `LayerUtility: ImageMaskScaleAs` —— 1/7 个有
- `PulidFluxEvaClipLoader` —— 1/7 个有
- `PulidFluxInsightFaceLoader` —— 1/7 个有
- `PulidFluxModelLoader` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 30 | 7 | 91% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | beta | - | 7 | 86% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 30，7 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
