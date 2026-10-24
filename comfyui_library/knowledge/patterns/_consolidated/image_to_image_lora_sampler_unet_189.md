---
name: image_to_image_lora_sampler_unet_189
type: Image To Image
frequency: 3
level: strong
coverage: 0.804667
common_nodes: [AlphaChanelRemove, AutoCropFaces, CFGNorm, CLIPLoader, ConditioningZeroOut, FluxKontextImageScale, Image Comparer (rgthree), ImageRemoveAlpha_UTK, ImageResizeKJv2, ImitationHueNode, KSampler, LBM_Relighting, LayerMask: PersonMaskUltra V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, SeedVR2, SeedVR2BlockSwap, SeedVR2ExtraArgs, Text, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/比换脸更过瘾-神奇的换头术V3-【by神都猫】_1982452159784591362.json, 图片生成/图生图/神都猫多人换头术v3_1974368355002003458.json, 图片生成/图生图/神都猫神奇的换脸V3 FOR 千问2509_1982452463880028162.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_189

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/比换脸更过瘾-神奇的换头术V3-【by神都猫】_1982452159784591362.json、图片生成/图生图/神都猫多人换头术v3_1974368355002003458.json、图片生成/图生图/神都猫神奇的换脸V3 FOR 千问2509_1982452463880028162.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 3 个 workflow 都包含：
- `AlphaChanelRemove`
- `AutoCropFaces`
- `CFGNorm`
- `CLIPLoader`
- `ConditioningZeroOut`
- `FluxKontextImageScale`
- `Image Comparer (rgthree)`
- `ImageRemoveAlpha_UTK`
- `ImageResizeKJv2`
- `ImitationHueNode`
- `KSampler`
- `LBM_Relighting`
- `LayerMask: PersonMaskUltra V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `Text`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GrowMask` —— 2/3 个有
- `InpaintModelConditioning` —— 2/3 个有
- `PIP_图像联结` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 10 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 10，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
