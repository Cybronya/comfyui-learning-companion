---
name: text_to_image_lora_sampler_clip_24
type: Text To Image
frequency: 23
level: weak
coverage: 0.881261
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, EmptyLatentImage, Flux2Scheduler, Image Comparer (rgthree), KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Klein搭配QwenImage2.1洗图，去AI感出真实皮肤细节_2110806135577079809.json, 图片生成/图生图/PS级扩图无需参数，角色一致性图生图扩图方案_2110823025108148226.json, 图片生成/图生图/Qwen 2.1+Klein去AI感洗图真实皮肤Removing the “AI-like” Nat_2111978227160932353.json, 图片生成/图生图/QwenImage2.1+Klein去AI感洗图真实皮肤_2110266747344482305.json, 图片生成/图生图/QwenImage2.1+Klein去AI感洗图真实皮肤_2110290173765443586.json, 图片生成/图生图/QwenImage2.1+Klein去AI感洗图真实皮肤_2110294391612076033.json, 图片生成/图生图/QwenImage2.1+Klein洗图｜去AI感真实皮肤质感还原_2110756724784324610.json, 图片生成/图生图/QwenImage2.1+Klein真实皮肤洗图｜高清去AI感实战_2110765479462793218.json, 图片生成/图生图/QwenImage2.1加Klein去AI感洗图，真实皮肤质感还原_2110804601464250369.json, 图片生成/图生图/QwenImage2.1去AI感洗图方案，Klein加持真实皮肤出片_2110809057987743746.json, 图片生成/图生图/QwenImage2.1携手Klein洗图｜真实皮肤去AI感必收_2110759590169239553.json, 图片生成/图生图/real-Flux2+Klein换脸｜局部重绘图生图工作流_2090574124233084930.json, 图片生成/图生图/real-Flux2+Klein换脸｜局部重绘图生图工作流_2090887818322206722.json, 图片生成/图生图/real-Flux2与Klein换脸｜局部重绘图生图工作流_2092078678518882305.json, 图片生成/图生图/real-Flux2与Klein换脸｜局部重绘图生图工作流_2092617560872284161.json, 图片生成/图生图/图片风格迁移转化灵感造像师像素级保留与灵魂级风格注入生成器，图生图方案_2107600836317761538.json, 图片生成/图生图/灵感造像师图片风格迁移｜像素级保留画面灵魂级注入风格，图生图_2107316373348241410.json, 图片生成/图生图/灵感造像师风格迁移｜像素级保留加灵魂级风格注入二合一_2112857706112577537.json, 数字人/数字人/QwenImage2.1+Klein去AI感洗图真实皮肤_2108431762991964161.json, 数字人/数字人/QwenImage2.1+Klein去AI感洗图真实皮肤_2108886341202300929.json, 数字人/数字人/QwenImage2.1+Klein去AI感洗图真实皮肤_2108891627866640386.json, 数字人/数字人/QwenImage2.1加Klein去AI感洗图真实皮肤 照片级质感优化_2109018096492175361.json, 数字人/数字人/QwenImage2.1加Klein去AI感洗图真实皮肤 照片级质感优化_2109414860994994177.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_24

> 由 `engine/knowledge_consolidation` 从 23 个 workflow 归纳得出（图片生成/图生图/Klein搭配QwenImage2.1洗图，去AI感出真实皮肤细节_2110806135577079809.json、图片生成/图生图/PS级扩图无需参数，角色一致性图生图扩图方案_2110823025108148226.json、图片生成/图生图/Qwen 2.1+Klein去AI感洗图真实皮肤Removing the “AI-like” Nat_2111978227160932353.json、图片生成/图生图/QwenImage2.1+Klein去AI感洗图真实皮肤_2110266747344482305.json、图片生成/图生图/QwenImage2.1+Klein去AI感洗图真实皮肤_2110290173765443586.json…）

- **类型**：Text To Image
- **样本数**：23
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 23 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `EmptyLatentImage`
- `Flux2Scheduler`
- `Image Comparer (rgthree)`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 20/23 个有
- `PreviewAny` —— 18/23 个有
- `PreviewImage` —— 18/23 个有
- `JjkText` —— 16/23 个有
- `solarL_SaveImagesToZip` —— 16/23 个有
- `ColorMatch` —— 15/23 个有
- `ImageScaleToTotalPixels` —— 15/23 个有
- `ImageSharpen` —— 15/23 个有
- `QwenImagePromptOptimizer` —— 15/23 个有
- `ResolutionSelector` —— 15/23 个有
- `孤海注释` —— 15/23 个有
- `QwenImagePromptStyler` —— 14/23 个有
- `LayerUtility: ImageReel` —— 7/23 个有
- `LayerUtility: ImageReelComposit` —— 7/23 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/23 个有
- `SegmentV2` —— 4/23 个有
- `easy imageColorMatch` —— 4/23 个有
- `CR Text Concatenate` —— 3/23 个有
- `ImageColorMatch+` —— 3/23 个有
- `PlaySound|pysssss` —— 3/23 个有
- `Qwen3VL_Chat` —— 3/23 个有
- `easy imageConcat` —— 3/23 个有
- `ImageResize+` —— 1/23 个有
- `InspyrenetRembg` —— 1/23 个有
- `RHHiddenNodes` —— 1/23 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 2048 | 23 | 0% |
| 高度 | 80 | 80 - 2048 | 23 | 0% |
| 采样步数 | 4 | 4 - 30 | 23 | 0% |
| Prompt 约束强度(CFG) | 4.5 | 2 - 4.5 | 23 | 69% |
| 采样算法 | er_sde | - | 23 | 70% |
| 调度器 | beta | - | 23 | 70% |
| 重绘幅度 | 1 | 1 - 1 | 23 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/23 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 2048，23 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 2048，23 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 4，观测区间 4 - 30，23 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 2 - 4.5，23 个样本
- 采样算法 最常用 er_sde，23 个样本，一致性 70%
- 调度器 最常用 beta，23 个样本，一致性 70%
- 重绘幅度 中位数 1，观测区间 1 - 1，23 个样本，取值集中（一致性 100%）
- 高发问题（16/23 个样本）：Steps较低可能导致细节不足
