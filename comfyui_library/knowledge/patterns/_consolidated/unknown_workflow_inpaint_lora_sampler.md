---
name: unknown_workflow_inpaint_lora_sampler
type: Unknown Workflow
frequency: 18
level: strong
coverage: 0.899389
common_nodes: [AddMask, BlendInpaint, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CM_IntBinaryOperation, CM_NumberToInt, CachePreviewBridge, ColorMatch, ConditioningZeroOut, CutForInpaint, DifferentialDiffusion, DownloadAndLoadFlorence2Model, Florence2Run, FluxGuidance, Get Image Size, GrowMaskWithBlur, ImageAndMaskPreview, ImageConcanate, ImageCrop+, ImageMaskSwitch, ImageToMask, InpaintModelConditioning, Int Literal, IsMaskEmpty, KSampler, LayerMask: PersonMaskUltra V2, LayerUtility: ColorImage V2, LayerUtility: CropByMask V2, LayerUtility: ImageBlend, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleRestore V2, LoadImage, LoraLoaderModelOnly, Mask Fill Holes, MaskToImage, PreviewImage, RHHiddenNodes, RepeatLatentBatch, SaveImage, StyleModelApply, StyleModelLoader, SubtractMask, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed, easy mathInt, workflow>123, workflow>zz]
problems: []
missing: []
members: [图片生成/图生图/AI换脸丨FLUX Fill＋Redux丨妆容眼镜迁移_2099780352662401025.json, 图片生成/图生图/Face and Head Swap 换脸换头+表情复刻+妆容迁移_2097132475427414017.json, 图片生成/图生图/Face_and_Head_Swap_换脸换头+表情复刻+妆容迁移_2098904543428960258.json, 图片生成/图生图/Face_and_Head_Swap_换脸换头+表情复刻+妆容迁移_2098970368957575170.json, 图片生成/图生图/【CQ808】换脸-V2_2037468637665169409.json, 图片生成/图生图/一键换脸-支持眼镜、妆容-后期搭配动作迁移、人物替换无敌！_2034916228472512514.json, 图片生成/图生图/人物换脸【支持眼镜、妆容】_1988437528309096450.json, 图片生成/图生图/换脸-支持眼镜、妆容Face Swap—Supports Glasses and Makeup_2094977915917266946.json, 图片生成/图生图/换脸-支持眼镜、妆容Face Swap—Supports Glasses and Makeup_2095757267034525698.json, 图片生成/图生图/换脸-支持眼镜、妆容Face Swap—Supports Glasses and Makeup_2096845139057664001.json, 图片生成/图生图/换脸-支持眼镜、妆容Face_Swap—Supports_Glasses_and_Makeup_2098978249643749378.json, 图片生成/图生图/换脸-支持眼镜、妆容Face_Swap—Supports_Glasses_and_Makeup_2099135250055131138.json, 图片生成/图生图/换脸-支持眼镜、妆容Face_Swap—Supports_Glasses_and_Makeup_2100074137111846913.json, 图片生成/图生图/换脸-支持眼镜、妆容Face_Swap—Supports_Glasses_and_Makeup_2101491472297189378.json, 图片生成/图生图/换脸-支持眼镜、妆容Face_Swap—Supports_Glasses_and_Makeup_2102305436341985281.json, 图片生成/图生图/换脸_1986649960412282882.json, 图片生成/图生图/最新无痕换脸换头+表情复刻+妆容迁移+眼镜_2080111188746264578.json, 图片生成/图生图/最新无痕换脸换头+表情复刻+妆容迁移+眼镜图生图_2078064288127868929.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（图片生成/图生图/AI换脸丨FLUX Fill＋Redux丨妆容眼镜迁移_2099780352662401025.json、图片生成/图生图/Face and Head Swap 换脸换头+表情复刻+妆容迁移_2097132475427414017.json、图片生成/图生图/Face_and_Head_Swap_换脸换头+表情复刻+妆容迁移_2098904543428960258.json、图片生成/图生图/Face_and_Head_Swap_换脸换头+表情复刻+妆容迁移_2098970368957575170.json、图片生成/图生图/【CQ808】换脸-V2_2037468637665169409.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 18 个 workflow 都包含：
- `AddMask`
- `BlendInpaint`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CM_IntBinaryOperation`
- `CM_NumberToInt`
- `CachePreviewBridge`
- `ColorMatch`
- `ConditioningZeroOut`
- `CutForInpaint`
- `DifferentialDiffusion`
- `DownloadAndLoadFlorence2Model`
- `Florence2Run`
- `FluxGuidance`
- `Get Image Size`
- `GrowMaskWithBlur`
- `ImageAndMaskPreview`
- `ImageConcanate`
- `ImageCrop+`
- `ImageMaskSwitch`
- `ImageToMask`
- `InpaintModelConditioning`
- `Int Literal`
- `IsMaskEmpty`
- `KSampler`
- `LayerMask: PersonMaskUltra V2`
- `LayerUtility: ColorImage V2`
- `LayerUtility: CropByMask V2`
- `LayerUtility: ImageBlend`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleRestore V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `Mask Fill Holes`
- `MaskToImage`
- `PreviewImage`
- `RHHiddenNodes`
- `RepeatLatentBatch`
- `SaveImage`
- `StyleModelApply`
- `StyleModelLoader`
- `SubtractMask`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy mathInt`
- `workflow>123`
- `workflow>zz`

**可变部分**（部分 workflow 才有）：
- `ImpactInt` —— 17/18 个有
- `ImageScale` —— 16/18 个有
- `easy imageSize` —— 16/18 个有
- `EmptyImage` —— 5/18 个有
- `ImageResizeKJ` —— 2/18 个有
- `GetNode` —— 1/18 个有
- `SetNode` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 25 | 18 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 18 | 100% |
| 采样算法 | euler | - | 18 | 100% |
| 调度器 | beta | - | 18 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 18 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 25，18 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，18 个样本，一致性 100%
- 调度器 最常用 beta，18 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
