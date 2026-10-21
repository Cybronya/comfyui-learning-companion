---
name: text_to_image_sampler_clip_unet_25
type: Text To Image
frequency: 12
level: weak
coverage: 0.864167
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt List, CR Text, ConditioningZeroOut, Dapao_LlamaCaption, Dapao_LlamaCaptionOptions, EmptyLatentImage, Fast Groups Bypasser (rgthree), ImpactInt, KSampler, LoadImage, RegexReplace, SaveImage, String Literal, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: [CR Text, String Literal, easy cleanGpuUsed, CR Prompt List]
members: [图片生成/图生图/2044345054734589954.json, 图片生成/文生图/Gemma4+Zimage-turbo反推文生图｜写实高质量出图_2095248453407432706.json, 图片生成/文生图/Krea 2 Turbo一键反推文生图处理工具_2101015778685440001.json, 图片生成/文生图/Krea 2 turbo-时尚模特_2079102838994718721.json, 图片生成/文生图/Krea 2 turbo一键反推生图_2073390634911748097.json, 图片生成/文生图/Krea 2 turbo一键反推生图｜写实图像生成_2095238362029449218.json, 图片生成/文生图/Krea 2 turbo一键反推生图｜写实艺术性图片生成_2100891841871835137.json, 图片生成/文生图/Krea2 Turbo一键反推生图 超高艺术性图片生成_2099945358976704514.json, 图片生成/文生图/Krea2 turbo一键反推提示词生图 高艺术性图片创作_2098283975210000385.json, 图片生成/文生图/一键反推写实生图｜Krea 2 turbo文生图图生图_2095511411060461570.json, 图片生成/文生图/反推文生图写实生成｜Gemma4+Zimage-turbo图生图_2095587120143495169.json, 视频生成/图生视频/Krea2_Turbo一键反推生图_超高艺术性图片生成_2101078290697117697.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_25

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/2044345054734589954.json、图片生成/文生图/Gemma4+Zimage-turbo反推文生图｜写实高质量出图_2095248453407432706.json、图片生成/文生图/Krea 2 Turbo一键反推文生图处理工具_2101015778685440001.json、图片生成/文生图/Krea 2 turbo-时尚模特_2079102838994718721.json、图片生成/文生图/Krea 2 turbo一键反推生图_2073390634911748097.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt List`
- `CR Text`
- `ConditioningZeroOut`
- `Dapao_LlamaCaption`
- `Dapao_LlamaCaptionOptions`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `ImpactInt`
- `KSampler`
- `LoadImage`
- `RegexReplace`
- `SaveImage`
- `String Literal`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 11/12 个有
- `llama_cpp_instruct_adv` —— 11/12 个有
- `llama_cpp_model_loader` —— 11/12 个有
- `llama_cpp_parameters` —— 11/12 个有
- `CR Batch Images From List` —— 9/12 个有
- `ImageConcatMulti` —— 9/12 个有
- `ImageFromBatch` —— 9/12 个有
- `JjkText` —— 9/12 个有
- `solarL_SaveImagesToZip` —— 9/12 个有
- `孤海注释` —— 8/12 个有
- `Image Comparer (rgthree)` —— 3/12 个有
- `PixaromaLoraLoader` —— 3/12 个有
- `SeedVR2LoadDiTModel` —— 3/12 个有
- `SeedVR2LoadVAEModel` —— 3/12 个有
- `SeedVR2VideoUpscaler` —— 3/12 个有
- `easy cleanGpuUsed` —— 3/12 个有
- `EmptyImage` —— 1/12 个有
- `PreviewImage` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 1280 | 12 | 0% |
| 高度 | 80 | 80 - 1280 | 12 | 0% |
| 采样步数 | 4 | 4 - 15 | 12 | 43% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 12 | 59% |
| 采样算法 | er_sde | - | 12 | 83% |
| 调度器 | beta | - | 12 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 1280，12 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1280，12 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 4，观测区间 4 - 15，12 个样本，取值分散，一致性仅 43%
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，12 个样本
- 采样算法 最常用 er_sde，12 个样本，一致性 83%
- 调度器 最常用 beta，12 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 高发问题（18/12 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、String Literal、easy cleanGpuUsed、CR Prompt List
