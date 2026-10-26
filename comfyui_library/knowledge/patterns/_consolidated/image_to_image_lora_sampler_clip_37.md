---
name: image_to_image_lora_sampler_clip_37
type: Image To Image
frequency: 7
level: strong
coverage: 0.867714
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, Image Comparer (rgthree), ImpactInt, InspyrenetRembg, KSampler, LayerMask: MaskGrow, LayerUtility: HLFrequencyDetailRestore, LayerUtility: ImageMaskScaleAs, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX Kontext重打光融图_2046426987199209473.json, 图片生成/图生图/KONTX工作流_2056249240434864130.json, 图片生成/图生图/为你的电商产品的广告图注入灵魂和温度的救星！电商产品光影融合_2020751445846396930.json, 图片生成/图生图/电商产品光影融合+真实立体感_1995420196972191745.json, 图片生成/图生图/电商产品光影融合V5_1997582856832618498.json, 图片生成/图生图/电商产品光影融合_1993607823556886530.json, 数字人/数字人/孤松雨露树均沾-电商产品光影融合V5_2004159874609094658.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_37

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/FLUX Kontext重打光融图_2046426987199209473.json、图片生成/图生图/KONTX工作流_2056249240434864130.json、图片生成/图生图/为你的电商产品的广告图注入灵魂和温度的救星！电商产品光影融合_2020751445846396930.json、图片生成/图生图/电商产品光影融合+真实立体感_1995420196972191745.json、图片生成/图生图/电商产品光影融合V5_1997582856832618498.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `ImpactInt`
- `InspyrenetRembg`
- `KSampler`
- `LayerMask: MaskGrow`
- `LayerUtility: HLFrequencyDetailRestore`
- `LayerUtility: ImageMaskScaleAs`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 6/7 个有
- `GetImageSize+` —— 5/7 个有
- `ImageBlend` —— 5/7 个有
- `ImagePosterize+` —— 5/7 个有
- `InversionDemoLazyIndexSwitch` —— 5/7 个有
- `NoiseImage` —— 5/7 个有
- `DetailTransfer` —— 1/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有
- `ImageScaleToTarget` —— 1/7 个有
- `KontextLoraSwitch` —— 1/7 个有
- `Light-Tool: TextConnect` —— 1/7 个有
- `RH_Flux_Kontext_Max` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 7 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，7 个样本，取值集中（一致性 80%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
