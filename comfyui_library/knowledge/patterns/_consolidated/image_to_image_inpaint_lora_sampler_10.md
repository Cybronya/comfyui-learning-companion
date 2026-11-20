---
name: image_to_image_inpaint_lora_sampler_10
type: Image To Image
frequency: 3
level: strong
coverage: 0.779667
common_nodes: [Any Switch (rgthree), CFGZeroStarAndInit, CLIPLoader, CLIPTextEncode, CR Text, CR Text Concatenate, Fast Groups Bypasser (rgthree), GrowMask, GrowMaskWithBlur, Image Comparer (rgthree), ImageAndMaskPreview, ImpactInt, ImpactMinMax, ImpactSwitch, InpaintModelConditioning, KSampler, LayerMask: MediapipeFacialSegment, LayerMask: PersonMaskUltra V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoader, MaskComposite, MaskPreview+, PreviewBridge, PreviewImage, RH_Captioner, ResizeMask, SaveImage, SeedVR2, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy ifElse, easy imageSize, easy isMaskEmpty, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/Wan图像去AI味提升皮肤质感工作流_1949745220381491202.json, 图片生成/文生图/Wan图像去AI味提升皮肤质感工作流_2009967741385576450.json, 平台全量/人像去AI味提升皮肤质感_1989145169511460865.json]
source: knowledge_consolidation
---

# image_to_image_inpaint_lora_sampler_10

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Wan图像去AI味提升皮肤质感工作流_1949745220381491202.json、图片生成/文生图/Wan图像去AI味提升皮肤质感工作流_2009967741385576450.json、平台全量/人像去AI味提升皮肤质感_1989145169511460865.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 3 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CFGZeroStarAndInit`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `CR Text Concatenate`
- `Fast Groups Bypasser (rgthree)`
- `GrowMask`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `ImageAndMaskPreview`
- `ImpactInt`
- `ImpactMinMax`
- `ImpactSwitch`
- `InpaintModelConditioning`
- `KSampler`
- `LayerMask: MediapipeFacialSegment`
- `LayerMask: PersonMaskUltra V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoader`
- `MaskComposite`
- `MaskPreview+`
- `PreviewBridge`
- `PreviewImage`
- `RH_Captioner`
- `ResizeMask`
- `SaveImage`
- `SeedVR2`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy ifElse`
- `easy imageSize`
- `easy isMaskEmpty`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageReel` —— 2/3 个有
- `LayerUtility: ImageReelComposit` —— 2/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 10 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | dpmpp_2m | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 0.25 | 0.25 - 0.25 | 3 | 100% |
| LoRA 模型强度 | 0.4 | 0.4 - 0.4 | 3 | 100% |
| LoRA 文本强度 | 0.4 | 0.4 - 0.4 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 10，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 0.25，观测区间 0.25 - 0.25，3 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.4，观测区间 0.4 - 0.4，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 0.4，观测区间 0.4 - 0.4，3 个样本，取值集中（一致性 100%）
