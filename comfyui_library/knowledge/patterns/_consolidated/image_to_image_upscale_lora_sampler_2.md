---
name: image_to_image_upscale_lora_sampler_2
type: Image To Image
frequency: 29
level: moderate
coverage: 0.676345
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, ImageScaleToTotalPixels, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TextEncodeQwenImageEdit, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/26313-动漫转真人_2032308024513138690.json, 图片生成/图生图/Qwen   Z_image   zimage  线稿转效果图  线稿上色 图生图_2039882255182602241.json, 图片生成/图生图/Qwen  Z_image  线稿转效果图  手稿转效果图 建筑设计_2039689984633999361.json, 图片生成/图生图/Qwen  zimage 图生图  线稿转效果图 线稿上色_2039891477131698177.json, 图片生成/图生图/Qwen ZI 二次元 转真人 真实感  洗图_2008160677533323265.json, 图片生成/图生图/Qwen edit +Z-lmage Turbo 二次元转真人 动漫转真人 真实感洗图  极致写实图_2041687465215397890.json, 图片生成/图生图/Qwen image+Z-image二次元转真人，真实感洗图!_2011631332140519426.json, 图片生成/图生图/Qwen 二次元转真人  线稿转真人 超真实感 去AI感_2034189810599993345.json, 图片生成/图生图/Qwen 漫画转真人 去AI感 超真实_2034554986268463106.json, 图片生成/图生图/Qwen+Z-image二次元转真人（可洗图）_2029057737249787906.json, 图片生成/图生图/Qwen+Z-image二次元转真人，真实感洗图!一比一还原！_2006640953188163585.json, 图片生成/图生图/Qwen+ZI二次元转真人_2007986059270950914.json, 图片生成/图生图/Qwen+ZI二次元转真人_2011321068090298369.json, 图片生成/图生图/Qwen+ZI二次元转真人_2044682901060591618.json, 图片生成/图生图/Qwen+ZI二次元转真人_2109893692935991297.json, 图片生成/图生图/Qwen+ZI二次元转真人真实感洗图_2031261933726339073.json, 图片生成/图生图/Qwen+ZI二次元转真人！很好用！_2058810045835603970.json, 图片生成/图生图/Qwen+ZI二次元转真人！很好用！_2084159255174795265.json, 图片生成/图生图/Qwen+ZI二次元转真人，真实感洗图_2006971430335946754.json, 图片生成/图生图/Qwen+ZI二次元转真人，真实感洗图_2006977149189758978.json, 图片生成/图生图/Qwen+ZI二次元转真人，真实感洗图_2014573947509018626.json, 图片生成/图生图/Qwen+ZI二次元转真人，真实感洗图_2020054362193661953.json, 图片生成/图生图/Qwen+ZI二次元转真人，真实感洗图_2030278386714677249.json, 图片生成/图生图/Qwen+ZI二次元转真人，真实感洗图_2039543860065472513.json, 图片生成/图生图/Qwen+ZI二次元转真人，真实感洗图【贼拉带劲！无比好用，谁用谁知道！】_2029072350313975809.json, 图片生成/图生图/Qwen+ZI二次元转真人，真实感洗图【贼拉带劲！无比好用，谁用谁知道！】_2041681908236554241.json, 图片生成/图生图/Qwen+ZI二次元转真人，真实感洗图，亚洲风格-B站AIGC大赏_2021248304369115137.json, 图片生成/图生图/Qwen+ZI二次元转真人，真实感洗图，亚洲风格-B站AIGC大赏_2065316695910477824.json, 图片生成/图生图/空白工作流 Qwen+KREA2二次元转真人，真实感洗图，亚洲风格-B站AIGC大赏_2075765007878545409.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_2

> 由 `engine/knowledge_consolidation` 从 29 个 workflow 归纳得出（图片生成/图生图/26313-动漫转真人_2032308024513138690.json、图片生成/图生图/Qwen   Z_image   zimage  线稿转效果图  线稿上色 图生图_2039882255182602241.json、图片生成/图生图/Qwen  Z_image  线稿转效果图  手稿转效果图 建筑设计_2039689984633999361.json、图片生成/图生图/Qwen  zimage 图生图  线稿转效果图 线稿上色_2039891477131698177.json、图片生成/图生图/Qwen ZI 二次元 转真人 真实感  洗图_2008160677533323265.json…）

- **类型**：Image To Image
- **样本数**：29
- **可信度**：中等可信
- **平均知识覆盖**：68%

## 共有节点

全部 29 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TextEncodeQwenImageEdit`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `Qwen3_VQA` —— 28/29 个有
- `ShowText|pysssss` —— 28/29 个有
- `WD14Tagger|pysssss` —— 28/29 个有
- `easy clearCacheAll` —— 28/29 个有
- `easy showAnything` —— 28/29 个有
- `SaveImage` —— 27/29 个有
- `ImageScaleBy` —— 26/29 个有
- `JoinStrings` —— 26/29 个有
- `Fast Groups Bypasser (rgthree)` —— 25/29 个有
- `GetNode` —— 24/29 个有
- `SetNode` —— 24/29 个有
- `PreviewImage` —— 11/29 个有
- `Image Comparer (rgthree)` —— 6/29 个有
- `CFGGuider` —— 4/29 个有
- `EmptyFlux2LatentImage` —— 4/29 个有
- `Flux2Scheduler` —— 4/29 个有
- `GetImageSize` —— 4/29 个有
- `KSamplerSelect` —— 4/29 个有
- `RandomNoise` —— 4/29 个有
- `ReferenceLatent` —— 4/29 个有
- `SamplerCustomAdvanced` —— 4/29 个有
- `Checkpoint Loader (Simple)` —— 3/29 个有
- `CompressImages` —— 3/29 个有
- `ImageColorMatch+` —— 3/29 个有
- `LayerUtility: PurgeVRAM` —— 3/29 个有
- `llama_cpp_instruct_adv` —— 3/29 个有
- `llama_cpp_model_loader` —— 3/29 个有
- `llama_cpp_parameters` —— 3/29 个有
- `CR Text` —— 1/29 个有
- `CheckpointLoaderSimple` —— 1/29 个有
- `MuyeTextEditOutput` —— 1/29 个有
- `PrimitiveStringMultiline` —— 1/29 个有
- `StringMergeNode` —— 1/29 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 5 - 10 | 29 | 84% |
| Prompt 约束强度(CFG) | 1.6 | 1 - 1.6 | 29 | 78% |
| 采样算法 | euler | - | 29 | 55% |
| 调度器 | simple | - | 29 | 59% |
| 重绘幅度 | 0.35 | 0.2 - 1 | 29 | 47% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 61/29 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 5 - 10，29 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 1.6，观测区间 1 - 1.6，29 个样本
- 采样算法 最常用 euler，29 个样本，一致性 55%
- 调度器 最常用 simple，29 个样本，一致性 59%
- 重绘幅度 中位数 0.35，观测区间 0.2 - 1，29 个样本，取值分散，一致性仅 47%
- 高发问题（61/29 个样本）：Steps较低可能导致细节不足
