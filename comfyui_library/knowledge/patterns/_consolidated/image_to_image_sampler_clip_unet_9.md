---
name: image_to_image_sampler_clip_unet_9
type: Image To Image
frequency: 19
level: strong
coverage: 0.897789
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, ReferenceLatent, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/kontext人像草图处理v2_2058796047136288769.json, 图片生成/图生图/kontext商业级印花提取工作流V1版本_1945098408367673345.json, 图片生成/图生图/kontext图生图(双图)故事绘本_2010263590753800193.json, 图片生成/图生图/kontext官方工作流[教学]_1999020387990130690.json, 图片生成/图生图/kontext皮肤纹理真实化_1942120587915587585.json, 图片生成/图生图/【非API】 Kontext Dev 模型｜光影修改_1938479250225692674.json, 图片生成/图生图/【非API】 Kontext Dev 模型｜图像文字增加_1938450260434051074.json, 图片生成/图生图/【非API】 Kontext Dev 模型｜图像风格重绘_1938443160634720257.json, 图片生成/图生图/万物毛毡_Kontext-DEV-LORA_1940660615935586306.json, 图片生成/图生图/人物转身首尾帧_Kontext-LORA_1940624522338873345.json, 图片生成/图生图/修复老照片（新版）_1988514615141253122.json, 图片生成/图生图/像素风转绘_Kontext-DEV-LORA_1940668432364843010.json, 图片生成/图生图/去除马赛克LORA_Kontext-dev_1943348611730337794.json, 图片生成/图生图/取衣去人_Kontext-DEV-LORA_1940461645275754497.json, 图片生成/图生图/已知最强老照片修复 高清上色修复 精准还原_2011432965464662017.json, 图片生成/图生图/木刻版画转绘_Kontext-LORA_1941099293753372673.json, 图片生成/图生图/电影颗粒质感风格_Kontext-dev_1943855045148545025.json, 图片生成/图生图/美漫手绘故事_Kontext-LORA_1955150925189058561.json, 图片生成/图生图/马克笔风格风格转绘_1943325807521505281.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_9

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（图片生成/图生图/kontext人像草图处理v2_2058796047136288769.json、图片生成/图生图/kontext商业级印花提取工作流V1版本_1945098408367673345.json、图片生成/图生图/kontext图生图(双图)故事绘本_2010263590753800193.json、图片生成/图生图/kontext官方工作流[教学]_1999020387990130690.json、图片生成/图生图/kontext皮肤纹理真实化_1942120587915587585.json…）

- **类型**：Image To Image
- **样本数**：19
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 19 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 18/19 个有
- `ImageStitch` —— 17/19 个有
- `LoraLoaderModelOnly` —— 14/19 个有
- `PreviewImage` —— 13/19 个有
- `EmptySD3LatentImage` —— 12/19 个有
- `ShowText|pysssss` —— 12/19 个有
- `Text Multiline` —— 12/19 个有
- `ImageConcatMulti` —— 10/19 个有
- `GetImageSizeAndCount` —— 6/19 个有
- `LoadImageOutput` —— 3/19 个有
- `CompressImages` —— 1/19 个有
- `ETN_Translate` —— 1/19 个有
- `GetImageSize+` —— 1/19 个有
- `ImageScaleDownToSize` —— 1/19 个有
- `ImageUpscaleWithModelBatched` —— 1/19 个有
- `RH_Translator` —— 1/19 个有
- `Seed` —— 1/19 个有
- `UpscaleModelLoader` —— 1/19 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 19 | 86% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 19 | 100% |
| 采样算法 | euler | - | 19 | 100% |
| 调度器 | simple | - | 19 | 95% |
| 重绘幅度 | 1 | 1 - 1 | 19 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/19 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，19 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，19 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，19 个样本，一致性 100%
- 调度器 最常用 simple，19 个样本，一致性 95%
- 重绘幅度 中位数 1，观测区间 1 - 1，19 个样本，取值集中（一致性 100%）
