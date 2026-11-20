---
name: image_to_image_upscale_sampler_clip_5
type: Image To Image
frequency: 19
level: moderate
coverage: 0.668105
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, ImageScaleBy, JoinStrings, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, ShowText|pysssss, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen+ZI二次元转真人，真实感洗图_2003166729146703873.json, 图片生成/图生图/Qwen+ZI动漫转真人写实感洗图_2040971599993638913.json, 图片生成/图生图/Qwen+ZI动漫转真人写实感洗图_2070031093717360642.json, 图片生成/图生图/Qwen+ZI动漫转真人写实感洗图_2070344105913307138.json, 图片生成/图生图/Qwen+ZI动漫转真人写实感洗图_2092868889398046722.json, 图片生成/图生图/Qwen+ZI手绘转真人！很好用！_2067503115376619521.json, 图片生成/图生图/Qwen+ZI手绘转真人！很好用！_2072197751311519745.json, 图片生成/图生图/Qwen+ZI风格迁移-二次元转真人_2026921283136528386.json, 图片生成/图生图/Qwen+ZI风格迁移，动漫转真人_2046480250682478593.json, 图片生成/图生图/Qwen+Zimage动漫转真人+逼真4k高清优化_2024774674177073153.json, 图片生成/图生图/Qwen-Image二次元转真人真实感洗图_2031691578514874369.json, 图片生成/图生图/QwenPro3二次元转真人，真实感洗图_2007995640994865154.json, 图片生成/图生图/QwenPro3动漫转真人，超真实洗图_2008811157867466753.json, 图片生成/图生图/Qwen_edit  Z_image  线稿转真人  线稿上色 去AI感 超真实_2036767019097399298.json, 图片生成/图生图/Qwen二次元转真人_2109446422545387522.json, 图片生成/图生图/Z-image-turbo-图片反推去AI感+SeedVR2二次放大-V2版_1997584846346194945.json, 图片生成/图生图/【楚心钟陌】Qwen+ZI二次元转真人，真实感洗图(本地API调用)_2001670288888721409.json, 图片生成/图生图/一键效果图  渲染图  线稿转实景   手稿转效果图_2059922894699982849.json, 图片生成/图生图/二次元转真人（可洗图）_2018912672795856898.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_clip_5

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（图片生成/图生图/Qwen+ZI二次元转真人，真实感洗图_2003166729146703873.json、图片生成/图生图/Qwen+ZI动漫转真人写实感洗图_2040971599993638913.json、图片生成/图生图/Qwen+ZI动漫转真人写实感洗图_2070031093717360642.json、图片生成/图生图/Qwen+ZI动漫转真人写实感洗图_2070344105913307138.json、图片生成/图生图/Qwen+ZI动漫转真人写实感洗图_2092868889398046722.json…）

- **类型**：Image To Image
- **样本数**：19
- **可信度**：中等可信
- **平均知识覆盖**：67%

## 共有节点

全部 19 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `ImageScaleBy`
- `JoinStrings`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: PurgeVRAM V2` —— 18/19 个有
- `Qwen3_VQA` —— 18/19 个有
- `easy clearCacheAll` —— 18/19 个有
- `ImageScaleToTotalPixels` —— 17/19 个有
- `LoraLoaderModelOnly` —— 17/19 个有
- `TextEncodeQwenImageEdit` —— 17/19 个有
- `TextEncodeQwenImageEditPlus` —— 17/19 个有
- `WD14Tagger|pysssss` —— 16/19 个有
- `GetNode` —— 15/19 个有
- `SetNode` —— 15/19 个有
- `Fast Groups Bypasser (rgthree)` —— 13/19 个有
- `PreviewImage` —— 5/19 个有
- `TextInput_` —— 3/19 个有
- `Image Comparer (rgthree)` —— 2/19 个有
- `ImpactInt` —— 1/19 个有
- `Label (rgthree)` —— 1/19 个有
- `LayerUtility: ImageReel` —— 1/19 个有
- `LayerUtility: ImageReelComposit` —— 1/19 个有
- `PlaySound|pysssss` —— 1/19 个有
- `RH_Captioner` —— 1/19 个有
- `RH_ExecuteNode` —— 1/19 个有
- `RH_ImageUploaderNode` —— 1/19 个有
- `RH_NodeInfoListNode` —— 1/19 个有
- `RH_SettingsNode` —— 1/19 个有
- `SaveLatent` —— 1/19 个有
- `TT_img_enc` —— 1/19 个有
- `easy imageConcat` —— 1/19 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 5 - 10 | 19 | 79% |
| Prompt 约束强度(CFG) | 1 | 1 - 1.6 | 19 | 76% |
| 采样算法 | euler | - | 19 | 47% |
| 调度器 | simple | - | 19 | 47% |
| 重绘幅度 | 0.6 | 0.35 - 1 | 19 | 55% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 35/19 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 5 - 10，19 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1.6，19 个样本
- 采样算法 最常用 euler，19 个样本，一致性 47%
- 调度器 最常用 simple，19 个样本，一致性 47%
- 重绘幅度 中位数 0.6，观测区间 0.35 - 1，19 个样本
- 高发问题（35/19 个样本）：Steps较低可能导致细节不足
