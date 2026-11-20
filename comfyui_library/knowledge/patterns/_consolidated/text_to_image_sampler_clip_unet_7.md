---
name: text_to_image_sampler_clip_unet_7
type: Text To Image
frequency: 30
level: weak
coverage: 0.8686
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt List, CR Text, ConditioningZeroOut, EmptyLatentImage, ImpactInt, KSampler, LoadImage, SaveImage, String Literal, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/图片反推生图｜Qwen本地模型版_2098721934610624513.json, 图片生成/图生图/Gemma4+Zimage-turbo反推文生图_2044345054734589954.json, 图片生成/图生图/Gemma4+Zimage-turbo反推文生图_2100871042855165954.json, 图片生成/图生图/Gemma4+Zimage-turbo反推文生图_2101137925164593154.json, 图片生成/图生图/Gemma4+Zimage-turbo反推文生图_2105192952220966913.json, 图片生成/图生图/Krea 2 turbo一键反推生图_2096860809161957377.json, 图片生成/图生图/Krea 2 turbo一键反推生图_2096866546353266690.json, 图片生成/图生图/Krea 2 turbo一键反推生图_2096883382834778113.json, 图片生成/图生图/Krea 2 turbo一键反推生图_2096886273872064514.json, 图片生成/图生图/Krea_2_turbo一键反推生图_2099778012253347842.json, 图片生成/图生图/Krea_2_turbo一键反推生图_2100037977606025217.json, 图片生成/图生图/Various Angles and Poses 人物多角度不同姿势qwen3.5+Z-image_2104737920220483586.json, 图片生成/图生图/doubao-seed-2+zimage-turbo模特文生图_2072582582184796162.json, 图片生成/图生图/qwen3.5+Z-image反推生图_2038868462088495105.json, 图片生成/图生图/人物写真 高度一致性 Krea+2+turbo  Character Portraits_ High_2101844900349308929.json, 图片生成/图生图/图片裂变特写qwen3.5+Z-image批量洗图+反推提示词+图生图_2066850786193264642.json, 图片生成/图生图/洗图 指定模特姿势 动作迁移 去油腻修复皮肤质感+高Gemma4+Zimage-turbo反推文生图_2090233124142800897.json, 图片生成/图生图/电商服装模特展示图生成｜Gemma4+Zimage-turbo反推_2095926642286878721.json, 图片生成/图生图/电商模特反推文生图Gemma4+Zimage-turbo_2096236577545609217.json, 图片生成/图生图/高度一致性人物写真 +Krea+2+turbo++Character+Portraits_+High_2107627484991803394.json, 图片生成/文生图/Gemma4+Zimage-turbo反推文生图｜写实高质量出图_2095248453407432706.json, 图片生成/文生图/Krea 2 Turbo一键反推文生图处理工具_2101015778685440001.json, 图片生成/文生图/Krea 2 turbo一键反推生图_2073390634911748097.json, 图片生成/文生图/Krea 2 turbo一键反推生图｜写实图像生成_2095238362029449218.json, 图片生成/文生图/Krea 2 turbo一键反推生图｜写实艺术性图片生成_2100891841871835137.json, 图片生成/文生图/Krea2 Turbo一键反推生图 超高艺术性图片生成_2099945358976704514.json, 图片生成/文生图/Krea2 turbo一键反推提示词生图 高艺术性图片创作_2098283975210000385.json, 图片生成/文生图/一键反推写实生图｜Krea 2 turbo文生图图生图_2095511411060461570.json, 图片生成/文生图/反推文生图写实生成｜Gemma4+Zimage-turbo图生图_2095587120143495169.json, 视频生成/图生视频/Krea2_Turbo一键反推生图_超高艺术性图片生成_2101078290697117697.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_7

> 由 `engine/knowledge_consolidation` 从 30 个 workflow 归纳得出（图片生成/反推提示词/图片反推生图｜Qwen本地模型版_2098721934610624513.json、图片生成/图生图/Gemma4+Zimage-turbo反推文生图_2044345054734589954.json、图片生成/图生图/Gemma4+Zimage-turbo反推文生图_2100871042855165954.json、图片生成/图生图/Gemma4+Zimage-turbo反推文生图_2101137925164593154.json、图片生成/图生图/Gemma4+Zimage-turbo反推文生图_2105192952220966913.json…）

- **类型**：Text To Image
- **样本数**：30
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 30 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt List`
- `CR Text`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `ImpactInt`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `String Literal`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 29/30 个有
- `RegexReplace` —— 29/30 个有
- `easy showAnything` —— 29/30 个有
- `llama_cpp_instruct_adv` —— 29/30 个有
- `llama_cpp_model_loader` —— 29/30 个有
- `llama_cpp_parameters` —— 29/30 个有
- `LoraLoaderModelOnly` —— 27/30 个有
- `Dapao_LlamaCaption` —— 25/30 个有
- `Dapao_LlamaCaptionOptions` —— 25/30 个有
- `CR Batch Images From List` —— 17/30 个有
- `ImageConcatMulti` —— 17/30 个有
- `ImageFromBatch` —— 17/30 个有
- `easy cleanGpuUsed` —— 13/30 个有
- `Image Comparer (rgthree)` —— 11/30 个有
- `SeedVR2LoadDiTModel` —— 11/30 个有
- `SeedVR2LoadVAEModel` —— 11/30 个有
- `SeedVR2VideoUpscaler` —— 11/30 个有
- `JjkText` —— 10/30 个有
- `solarL_SaveImagesToZip` —— 10/30 个有
- `孤海注释` —— 9/30 个有
- `PixaromaLoraLoader` —— 5/30 个有
- `ExecutionBlocker` —— 3/30 个有
- `Int` —— 2/30 个有
- `PreviewImage` —— 2/30 个有
- `EmptyImage` —— 1/30 个有
- `RH_LLMAPI_Pro_Node` —— 1/30 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 720 | 80 - 1280 | 30 | 29% |
| 高度 | 720 | 80 - 1280 | 30 | 30% |
| 采样步数 | 8 | 4 - 15 | 30 | 50% |
| Prompt 约束强度(CFG) | 1.1 | 1 - 4.5 | 30 | 26% |
| 采样算法 | er_sde | - | 30 | 63% |
| 调度器 | beta | - | 30 | 33% |
| 重绘幅度 | 1 | 1 - 1 | 30 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 26/30 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 720，观测区间 80 - 1280，30 个样本，取值分散，一致性仅 29%
- 高度 中位数 720，观测区间 80 - 1280，30 个样本，取值分散，一致性仅 30%
- 采样步数 中位数 8，观测区间 4 - 15，30 个样本，取值分散，一致性仅 50%
- Prompt 约束强度(CFG) 中位数 1.1，观测区间 1 - 4.5，30 个样本，取值分散，一致性仅 26%
- 采样算法 最常用 er_sde，30 个样本，一致性 63%
- 调度器 最常用 beta，30 个样本，一致性 33%
- 重绘幅度 中位数 1，观测区间 1 - 1，30 个样本，取值集中（一致性 100%）
- 高发问题（26/30 个样本）：Steps较低可能导致细节不足
