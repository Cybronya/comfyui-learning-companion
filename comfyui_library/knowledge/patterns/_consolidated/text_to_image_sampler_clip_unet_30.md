---
name: text_to_image_sampler_clip_unet_30
type: Text To Image
frequency: 15
level: weak
coverage: 0.7876
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, PreviewAny, PrimitiveStringMultiline, SaveImage, TextGenerate, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/文生图_krea2_2071423975636426754.json, 图片生成/图生图/（贞贞版-Raw Lora 11500）Krea2 Turbo文生图V1_2073803035968622594.json, 图片生成/文生图/5.Krea2 文生图_2083469098800996354.json, 图片生成/文生图/KREA2_LORA人像工作流_2078646318087630849.json, 图片生成/文生图/Krea-2_ 文生图_2095794360649601025.json, 图片生成/文生图/Krea-2文生图官方版｜高质量图像生成工作流_2095956990584512513.json, 图片生成/文生图/Krea-2文生图工作流｜写实质感出图效果稳定可靠_2107695970124386305.json, 图片生成/文生图/Krea2 Turbo极速文生图 API写实人像高质量生成_2099221894967947265.json, 图片生成/文生图/MOSS Image SFT图像生成工作流，文生图海报制作字体设计高清直出_2114413747635834882.json, 图片生成/文生图/MOSS Image SFT无损加速工作流，文生图海报字体生成快而不损画质_2114563928046006274.json, 图片生成/文生图/MOSS Image SFT监督微调文生图 海报字体图像生产处理工具_2112983489871175682.json, 图片生成/文生图/MOSS SFT ComfyUI官方文生图工作流 监督微调图像生成工具_2112977270586560513.json, 图片生成/文生图/Moss Image SFT turbo加速文生图 海报字体生成工具_2113736101109264385.json, 图片生成/文生图/Moss Image文生图标准版 标准流程图像生成工具_2114124199613779970.json, 图片生成/文生图/Moss_Image_sft无损加速工作流｜海报制作与字体设计一键搞定_2114168867571462145.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_30

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/图生图/文生图_krea2_2071423975636426754.json、图片生成/图生图/（贞贞版-Raw Lora 11500）Krea2 Turbo文生图V1_2073803035968622594.json、图片生成/文生图/5.Krea2 文生图_2083469098800996354.json、图片生成/文生图/KREA2_LORA人像工作流_2078646318087630849.json、图片生成/文生图/Krea-2_ 文生图_2095794360649601025.json…）

- **类型**：Text To Image
- **样本数**：15
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：79%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `PreviewAny`
- `PrimitiveStringMultiline`
- `SaveImage`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 14/15 个有
- `LoraLoaderModelOnly` —— 14/15 个有
- `ResolutionSelector` —— 13/15 个有
- `PrimitiveBoolean` —— 12/15 个有
- `JjkText` —— 10/15 个有
- `solarL_SaveImagesToZip` —— 10/15 个有
- `孤海注释` —— 10/15 个有
- `ConditioningZeroOut` —— 8/15 个有
- `StringConcatenate` —— 8/15 个有
- `EmptyFlux2LatentImage` —— 7/15 个有
- `SkipLayerGuidanceDiTSimple` —— 7/15 个有
- `Int` —— 2/15 个有
- `LazyCache` —— 2/15 个有
- `CR Prompt Text` —— 1/15 个有
- `PlaySound|pysssss` —— 1/15 个有
- `Power Lora Loader (rgthree)` —— 1/15 个有
- `TextConcat` —— 1/15 个有
- `easy positive` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 10 | 15 | 61% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 15 | 51% |
| 采样算法 | er_sde | - | 15 | 67% |
| 调度器 | beta | - | 15 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |
| 宽度 | 80 | 80 - 1024 | 15 | 0% |
| 高度 | 80 | 80 - 1024 | 15 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 10，15 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，15 个样本
- 采样算法 最常用 er_sde，15 个样本，一致性 67%
- 调度器 最常用 beta，15 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 1024，15 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1024，15 个样本，取值分散，一致性仅 0%
- 高发问题（18/15 个样本）：Steps较低可能导致细节不足
