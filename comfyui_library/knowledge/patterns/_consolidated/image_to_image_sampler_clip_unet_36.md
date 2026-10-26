---
name: image_to_image_sampler_clip_unet_36
type: Image To Image
frequency: 9
level: moderate
coverage: 0.806889
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, GetNode, ImageScaleDownToSize, Int, KSampler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PainterFluxImageEdit, Qwen3_VQA, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SetNode, ShowText|pysssss, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/Flux2-Klein 图生图+洗图+线稿  文生图_图生图反推提示词 写实光影_2028305897730084865.json, 图片生成/反推提示词/图生图+洗图+线稿 Flux2-Klein  文生图_图生图反推提示词 写实光影_2028280625148465153.json, 图片生成/图生图/Klein图生图+洗图+线稿+线稿上色_2031931837576122370.json, 图片生成/图生图/Klein图生图+洗图+线稿+线稿上色_2044302454275186690.json, 图片生成/图生图/Klein图生图+洗图+线稿=B站艾橘溪_2028089884472254465.json, 图片生成/图生图/指定人脸+Flux2 klein图生图工作流_2038164410010705921.json, 图片生成/图生图/指定人脸+Klein图生图=B站艾橘溪_2012373696018653186.json, 图片生成/图生图/最新指定人脸换脸高清补光影+Klein图生图＋高清写实 2_2099689034640617474.json, 图片生成/图生图/模特仿图 flux2_2030183259241451521.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_36

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/反推提示词/Flux2-Klein 图生图+洗图+线稿  文生图_图生图反推提示词 写实光影_2028305897730084865.json、图片生成/反推提示词/图生图+洗图+线稿 Flux2-Klein  文生图_图生图反推提示词 写实光影_2028280625148465153.json、图片生成/图生图/Klein图生图+洗图+线稿+线稿上色_2031931837576122370.json、图片生成/图生图/Klein图生图+洗图+线稿+线稿上色_2044302454275186690.json、图片生成/图生图/Klein图生图+洗图+线稿=B站艾橘溪_2028089884472254465.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 9 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetNode`
- `ImageScaleDownToSize`
- `Int`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PainterFluxImageEdit`
- `Qwen3_VQA`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 3/9 个有
- `LayerMask: PersonMaskUltra V2` —— 3/9 个有
- `LayerUtility: CropBoxResolve` —— 3/9 个有
- `LayerUtility: CropByMask V2` —— 3/9 个有
- `RH_Captioner` —— 3/9 个有
- `SolidMask` —— 3/9 个有
- `easy mathInt` —— 3/9 个有
- `ttN concat` —— 3/9 个有
- `Image Comparer (rgthree)` —— 1/9 个有
- `ImageScale` —— 1/9 个有
- `LoraLoader` —— 1/9 个有
- `LoraLoaderModelOnly` —— 1/9 个有
- `PhotoShakeNode` —— 1/9 个有
- `RHHiddenNodes` —— 1/9 个有
- `easy imageConcat` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 5 | 5 - 8 | 9 | 82% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 0.2 - 1 | 9 | 62% |
| LoRA 模型强度 | 0.5 | - | 1 | 100% |
| LoRA 文本强度 | 0.6 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 5，观测区间 5 - 8，9 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.2 - 1，9 个样本
- 高发问题（12/9 个样本）：Steps较低可能导致细节不足
