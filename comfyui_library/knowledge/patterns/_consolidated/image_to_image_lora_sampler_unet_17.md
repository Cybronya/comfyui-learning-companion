---
name: image_to_image_lora_sampler_unet_17
type: Image To Image
frequency: 18
level: strong
coverage: 0.973944
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/F.2Klein提取3d立体服装_2053799596253556738.json, 图片生成/图生图/F.2Klein提取3d立体服装_2056216125565874178.json, 图片生成/图生图/F.2Klein提取3d立体服装_2057635695820369921.json, 图片生成/图生图/F.2Klein提取3d立体服装_2058364672834891778.json, 图片生成/图生图/F.2Klein提取3d立体服装_2058380006920904706.json, 图片生成/图生图/FireRed Edit艺术字风格迁移设计_2052228410910486530.json, 图片生成/图生图/FireRed Edit艺术字风格迁移设计_2059096605923565569.json, 图片生成/图生图/FireRed Edit艺术字风格迁移设计_2059435718690304002.json, 图片生成/图生图/FireRed Edit艺术字风格迁移设计_2061660098623262721.json, 图片生成/图生图/FireRed-Image-Edit1.1单图编辑换装_2031741074665902081.json, 图片生成/图生图/FireRed-Image-edit1.1单图_双图_三图编辑_2029806395092115457.json, 图片生成/图生图/FireRed-Image-edit1.1单图_双图_三图编辑_2030064414078017537.json, 图片生成/图生图/FireRed_Edit艺术字风格迁移设计_2069077798647586817.json, 图片生成/图生图/Flux2-Klein9b一键提取3d立体服装_2038251793729200129.json, 图片生成/图生图/Flux2-Klein一键提取3d立体服装_2038862090676473857.json, 图片生成/图生图/KINWING_白底图背景替换_Qwen edit_2046550050255413249.json, 图片生成/图生图/QwenEdit2511多图编辑工作流_2058767665044480001.json, 图片生成/图生图/换装迁移-小红书firered超高一致性_2045202503913967618.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_17

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（图片生成/图生图/F.2Klein提取3d立体服装_2053799596253556738.json、图片生成/图生图/F.2Klein提取3d立体服装_2056216125565874178.json、图片生成/图生图/F.2Klein提取3d立体服装_2057635695820369921.json、图片生成/图生图/F.2Klein提取3d立体服装_2058364672834891778.json、图片生成/图生图/F.2Klein提取3d立体服装_2058380006920904706.json…）

- **类型**：Image To Image
- **样本数**：18
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 18 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 14/18 个有
- `TextEncodeQwenImageEditPlus` —— 11/18 个有
- `ConditioningZeroOut` —— 10/18 个有
- `FluxKontextImageScale` —— 10/18 个有
- `Int` —— 9/18 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 8/18 个有
- `Flux2KleinEditTextEncode_EditUtils` —— 7/18 个有
- `Image Comparer (rgthree)` —— 6/18 个有
- `easy imageConcat` —— 6/18 个有
- `CR Prompt Text` —— 3/18 个有
- `EmptyLatentImage` —— 2/18 个有
- `FluxKontextMultiReferenceLatentMethod` —— 2/18 个有
- `PreviewImage` —— 2/18 个有
- `CLIPTextEncode` —— 1/18 个有
- `DapaoImageAspectRatioResizeNode` —— 1/18 个有
- `Fast Bypasser (rgthree)` —— 1/18 个有
- `ImageScaleToTotalPixels` —— 1/18 个有
- `PDIMAGE_LongerSize` —— 1/18 个有
- `ReferenceLatent` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 20 | 18 | 46% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 18 | 100% |
| 采样算法 | euler | - | 18 | 94% |
| 调度器 | simple | - | 18 | 89% |
| 重绘幅度 | 1 | 1 - 1 | 18 | 100% |
| 宽度 | 1920 | - | 2 | 100% |
| 高度 | 1080 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 22/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 20，18 个样本，取值分散，一致性仅 46%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，18 个样本，一致性 94%
- 调度器 最常用 simple，18 个样本，一致性 89%
- 重绘幅度 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 宽度 中位数 1920，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1080，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（22/18 个样本）：Steps较低可能导致细节不足
