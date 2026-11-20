---
name: text_to_image_lora_sampler_clip_35
type: Text To Image
frequency: 21
level: weak
coverage: 0.887667
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, EmptyLatentImage, GetImageSize, KSampler, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux2 Klein图像编辑API｜图生图精准局部修改_2098712100834205698.json, 图片生成/图生图/KleinFace换头换脸Flux2 Klein 9B模型高清人物AI智能面部替换，图生图_2106910609794232322.json, 图片生成/图生图/KleinFace换头换脸Flux2_Klein_9B模型高清人物AI智能面部替换，图生图_2108373965847744513.json, 图片生成/图生图/KleinFace换头换脸Flux2_Klein_9B模型高清人物AI智能面部替换，图生图_2112837974730829825.json, 图片生成/图生图/KleinFace换头换脸Flux2_Klein_9B模型高清人物AI智能面部替换，图生图_2114992075082129410.json, 图片生成/图生图/KleinFace高清换头换脸｜Flux2-Klein-9B面部替换_2106642679978356738.json, 图片生成/图生图/Klein搭配QwenImage2.1洗图，去AI感出真实皮肤细节_2110806135577079809.json, 图片生成/图生图/Qwen 2.1+Klein去AI感洗图真实皮肤Removing the “AI-like” Nat_2111978227160932353.json, 图片生成/图生图/QwenImage2.1+Klein去AI感洗图真实皮肤_2110266747344482305.json, 图片生成/图生图/QwenImage2.1+Klein去AI感洗图真实皮肤_2110290173765443586.json, 图片生成/图生图/QwenImage2.1+Klein去AI感洗图真实皮肤_2110294391612076033.json, 图片生成/图生图/QwenImage2.1+Klein洗图｜去AI感真实皮肤质感还原_2110756724784324610.json, 图片生成/图生图/QwenImage2.1+Klein真实皮肤洗图｜高清去AI感实战_2110765479462793218.json, 图片生成/图生图/QwenImage2.1加Klein去AI感洗图，真实皮肤质感还原_2110804601464250369.json, 图片生成/图生图/QwenImage2.1去AI感洗图方案，Klein加持真实皮肤出片_2110809057987743746.json, 图片生成/图生图/QwenImage2.1携手Klein洗图｜真实皮肤去AI感必收_2110759590169239553.json, 数字人/数字人/QwenImage2.1+Klein去AI感洗图真实皮肤_2108431762991964161.json, 数字人/数字人/QwenImage2.1+Klein去AI感洗图真实皮肤_2108886341202300929.json, 数字人/数字人/QwenImage2.1+Klein去AI感洗图真实皮肤_2108891627866640386.json, 数字人/数字人/QwenImage2.1加Klein去AI感洗图真实皮肤 照片级质感优化_2109018096492175361.json, 数字人/数字人/QwenImage2.1加Klein去AI感洗图真实皮肤 照片级质感优化_2109414860994994177.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_35

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（图片生成/图生图/Flux2 Klein图像编辑API｜图生图精准局部修改_2098712100834205698.json、图片生成/图生图/KleinFace换头换脸Flux2 Klein 9B模型高清人物AI智能面部替换，图生图_2106910609794232322.json、图片生成/图生图/KleinFace换头换脸Flux2_Klein_9B模型高清人物AI智能面部替换，图生图_2108373965847744513.json、图片生成/图生图/KleinFace换头换脸Flux2_Klein_9B模型高清人物AI智能面部替换，图生图_2112837974730829825.json、图片生成/图生图/KleinFace换头换脸Flux2_Klein_9B模型高清人物AI智能面部替换，图生图_2114992075082129410.json…）

- **类型**：Text To Image
- **样本数**：21
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 21 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `EmptyLatentImage`
- `GetImageSize`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGGuider` —— 20/21 个有
- `Flux2Scheduler` —— 20/21 个有
- `Image Comparer (rgthree)` —— 20/21 个有
- `KSamplerSelect` —— 20/21 个有
- `RandomNoise` —— 20/21 个有
- `SamplerCustomAdvanced` —— 20/21 个有
- `PreviewImage` —— 17/21 个有
- `ColorMatch` —— 15/21 个有
- `ImageScaleToTotalPixels` —— 15/21 个有
- `ImageSharpen` —— 15/21 个有
- `PreviewAny` —— 15/21 个有
- `QwenImagePromptOptimizer` —— 15/21 个有
- `ResolutionSelector` —— 15/21 个有
- `JjkText` —— 14/21 个有
- `QwenImagePromptStyler` —— 14/21 个有
- `solarL_SaveImagesToZip` —— 14/21 个有
- `孤海注释` —— 11/21 个有
- `FluxKontextImageScale` —— 5/21 个有
- `YC Color Match` —— 5/21 个有
- `EmptyImage` —— 2/21 个有
- `Anything Everywhere` —— 1/21 个有
- `CR Value` —— 1/21 个有
- `图像缩放V2_孤海` —— 1/21 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 30 | 21 | 3% |
| Prompt 约束强度(CFG) | 4.5 | 2 - 4.5 | 21 | 68% |
| 采样算法 | er_sde | - | 21 | 67% |
| 调度器 | beta | - | 21 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 21 | 100% |
| 宽度 | 80 | 80 - 2048 | 21 | 0% |
| 高度 | 80 | 80 - 2048 | 21 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/21 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 30，21 个样本，取值分散，一致性仅 3%
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 2 - 4.5，21 个样本
- 采样算法 最常用 er_sde，21 个样本，一致性 67%
- 调度器 最常用 beta，21 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，21 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 2048，21 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 2048，21 个样本，取值分散，一致性仅 0%
- 高发问题（15/21 个样本）：Steps较低可能导致细节不足
