---
name: text_to_image_lora_sampler_clip_55
type: Text To Image
frequency: 17
level: strong
coverage: 0.886059
common_nodes: [CLIPLoader, CLIPTextEncode, ComfySwitchNode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Minimax H3人像参考图专用生成器｜写真质感一图即出_2112823108011909121.json, 图片生成/图生图/QWEN2.1图像编辑工作流 图片精修局部修改全能处理 图生图必备_2105034860778844162.json, 图片生成/图生图/QWEN2.1图像编辑工作流｜图片精修局部修改全能处理｜图生图必备_2102213493909966850.json, 图片生成/图生图/QWEN2.1图像编辑工作流｜图片精修局部修改全能处理｜图生图必备_2104445483052781569.json, 图片生成/图生图/QWen2.1图像编辑利器｜图生图轻松改图修图一键搞定_2106200271583014914.json, 图片生成/图生图/QWen2.1官方图像编辑工作流，简洁高效的图生图处理方案_2102808314856955905.json, 图片生成/图生图/QWen2.1官方图像编辑工作流，简洁高效的图生图处理方案_2106915667613143041.json, 图片生成/图生图/Qwen 2.1图片编辑测试工作流，图生图处理方案_2103536589963087874.json, 图片生成/图生图/Qwen Image 2.1全能图片编辑加官方提示词强化，图生图处理质量提升_2103266944416833538.json, 图片生成/图生图/Qwen Image 2.1全能图片编辑官方提示词强化处理工具_2102552758141411330.json, 图片生成/图生图/Qwen Image 2.1图片编辑工作流官流版，局部重绘人像写真图生图方案_2106901434481602561.json, 图片生成/图生图/Qwen Image 2.1官方图片编辑｜局部重绘人像写真_2106601449881952257.json, 图片生成/图生图/Qwen Image 2.1漫转真｜二次元图一键转真人写真_2106609135612686338.json, 图片生成/图生图/Qwen_Image_2.1图片编辑工作流官流版，局部重绘人像写真图生图方案_2108733918542389249.json, 图片生成/图生图/千问2.1图片编辑测试工作流｜文生图图生图双修，稳定可用优先_2107371246542475265.json, 图片生成/图生图/角色资产4格详图制作Qwen Image 2.1工作流，图生图其它图片处理工具_2107887078867558401.json, 图片生成/文生图/Qwen Image 2.1全能文生图官方提示词强化处理工具_2102565199348850689.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_55

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/图生图/Minimax H3人像参考图专用生成器｜写真质感一图即出_2112823108011909121.json、图片生成/图生图/QWEN2.1图像编辑工作流 图片精修局部修改全能处理 图生图必备_2105034860778844162.json、图片生成/图生图/QWEN2.1图像编辑工作流｜图片精修局部修改全能处理｜图生图必备_2102213493909966850.json、图片生成/图生图/QWEN2.1图像编辑工作流｜图片精修局部修改全能处理｜图生图必备_2104445483052781569.json、图片生成/图生图/QWen2.1图像编辑利器｜图生图轻松改图修图一键搞定_2106200271583014914.json…）

- **类型**：Text To Image
- **样本数**：17
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 17 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 16/17 个有
- `QwenImage21Cache` —— 16/17 个有
- `孤海注释` —— 14/17 个有
- `PrimitiveBoolean` —— 12/17 个有
- `ImageScaleToTotalPixels` —— 10/17 个有
- `TextGenerate` —— 9/17 个有
- `BatchImagesNode` —— 8/17 个有
- `PreviewImage` —— 8/17 个有
- `JoinStrings` —— 6/17 个有
- `ShowText|pysssss` —— 6/17 个有
- `easy positive` —— 6/17 个有
- `PrimitiveStringMultiline` —— 5/17 个有
- `SeedVR2LoadDiTModel` —— 5/17 个有
- `SeedVR2LoadVAEModel` —— 5/17 个有
- `SeedVR2VideoUpscaler` —— 5/17 个有
- `EmptyImage` —— 4/17 个有
- `Fast Groups Bypasser (rgthree)` —— 4/17 个有
- `Image Comparer (rgthree)` —— 4/17 个有
- `RegexExtract` —— 3/17 个有
- `ShowAnything|Mie` —— 3/17 个有
- `StringFormat` —— 3/17 个有
- `ImageConcatMulti` —— 2/17 个有
- `ModelPreviewOverrideKJ` —— 2/17 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 17 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 17 | 100% |
| 采样算法 | er_sde | - | 17 | 100% |
| 调度器 | beta | - | 17 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 17 | 100% |
| 宽度 | 80 | 80 - 80 | 17 | 100% |
| 高度 | 80 | 80 - 80 | 17 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 19/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，17 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，17 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，17 个样本，一致性 100%
- 调度器 最常用 beta，17 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，17 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，17 个样本，取值集中（一致性 100%）
- 高发问题（19/17 个样本）：Steps较低可能导致细节不足
