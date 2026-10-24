---
name: image_to_image_sampler_unet_vae_8
type: Image To Image
frequency: 14
level: strong
coverage: 0.869286
common_nodes: [ConditioningZeroOut, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/千问QwenEdit 2511一致性图像编辑_2003754623812968450.json, 图片生成/图生图/千问QwenEdit plus一致性图像编辑_1970379059131785217.json, 图片生成/图生图/千问图像编辑，一致性编辑，无像素漂移，感谢Jason_1965208291238400002.json, 图片生成/图生图/去水印_1995428633756020737.json, 图片生成/图生图/去水印_水印去除-kontext_1963971515945504769.json, 图片生成/图生图/图像高精度去水印与无损修复_2057742605227741185.json, 图片生成/图生图/图片去除水印｜Flux Kontext_1965644146411192321.json, 图片生成/图生图/空白工作流_2077308039287361538.json, 图片生成/图生图/精修(全能)-kontext_1946789807444881409.json, 图片生成/图生图/精修(全能)-kontext_1978771739381485569.json, 图片生成/图生图/精修图像人物_商品_2054200148770729986.json, 图片生成/图生图/角色三视图_1946904422775709697.json, 图片生成/图生图/角色三视图_2034158201708486657.json, 图片生成/图生图/角色三视图_2049287384948281346.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_8

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/千问QwenEdit 2511一致性图像编辑_2003754623812968450.json、图片生成/图生图/千问QwenEdit plus一致性图像编辑_1970379059131785217.json、图片生成/图生图/千问图像编辑，一致性编辑，无像素漂移，感谢Jason_1965208291238400002.json、图片生成/图生图/去水印_1995428633756020737.json、图片生成/图生图/去水印_水印去除-kontext_1963971515945504769.json…）

- **类型**：Image To Image
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 14 个 workflow 都包含：
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 13/14 个有
- `CLIPTextEncode` —— 12/14 个有
- `FluxKontextImageScale` —— 12/14 个有
- `ReferenceLatent` —— 12/14 个有
- `DualCLIPLoader` —— 11/14 个有
- `FluxGuidance` —— 11/14 个有
- `LoraLoaderModelOnly` —— 11/14 个有
- `PreviewImage` —— 10/14 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 9/14 个有
- `CLIPLoader` —— 3/14 个有
- `Text` —— 3/14 个有
- `CR Prompt Text` —— 2/14 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 2/14 个有
- `LayerUtility: ImageRemoveAlpha` —— 1/14 个有
- `RHHiddenNodes` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 14 | 67% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 14 | 100% |
| 采样算法 | euler | - | 14 | 100% |
| 调度器 | simple | - | 14 | 79% |
| 重绘幅度 | 1 | 0.8 - 1 | 14 | 95% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，14 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，14 个样本，一致性 100%
- 调度器 最常用 simple，14 个样本，一致性 79%
- 重绘幅度 中位数 1，观测区间 0.8 - 1，14 个样本，取值集中（一致性 95%）
