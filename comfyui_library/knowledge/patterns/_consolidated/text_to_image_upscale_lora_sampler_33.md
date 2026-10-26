---
name: text_to_image_upscale_lora_sampler_33
type: Text To Image
frequency: 7
level: strong
coverage: 0.869429
common_nodes: [CLIPLoader, CLIPTextEncode, CM_FloatToInt, CR Text, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), ImageScaleToTotalPixels, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, PixaromaLoraLoader, PixaromaTextJoinTwo, PreviewImage, ReferenceLatent, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAEEncode, VAELoader, YC Color Match, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux2局部重绘加放大，遮罩控制区域编辑换装配饰发型图生图方案_2103571954241458177.json, 图片生成/图生图/Flux2洗图加放大控尺寸 图片优化分辨率可调_2105116266620080129.json, 图片生成/图生图/Flux2洗图加放大控尺寸，图生图高清修复分辨率提升工具_2103570471265587202.json, 图片生成/图生图/Flux2洗图加放大控尺寸｜图生图精修一步到位_2100830289231704066.json, 图片生成/图生图/Flux2洗图放大控尺寸｜图生图画质重塑｜输出尺寸自己说了算_2104824382769160194.json, 图片生成/图生图/flux2局部重绘加放大 图片局部修改分辨率提升_2105114830226153474.json, 图片生成/图生图/flux2局部重绘加放大｜图生图二合一｜改完直接出高清_2104822887134875649.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_33

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Flux2局部重绘加放大，遮罩控制区域编辑换装配饰发型图生图方案_2103571954241458177.json、图片生成/图生图/Flux2洗图加放大控尺寸 图片优化分辨率可调_2105116266620080129.json、图片生成/图生图/Flux2洗图加放大控尺寸，图生图高清修复分辨率提升工具_2103570471265587202.json、图片生成/图生图/Flux2洗图加放大控尺寸｜图生图精修一步到位_2100830289231704066.json、图片生成/图生图/Flux2洗图放大控尺寸｜图生图画质重塑｜输出尺寸自己说了算_2104824382769160194.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CM_FloatToInt`
- `CR Text`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PixaromaLoraLoader`
- `PixaromaTextJoinTwo`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `YC Color Match`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `Float` —— 6/7 个有
- `FloatConstant` —— 4/7 个有
- `FluxGuidance` —— 4/7 个有
- `GrowMaskWithBlur` —— 3/7 个有
- `Kontext Inpainting Conditioning` —— 3/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/7 个有
- `Text Multiline` —— 3/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高发问题（14/7 个样本）：Steps较低可能导致细节不足
