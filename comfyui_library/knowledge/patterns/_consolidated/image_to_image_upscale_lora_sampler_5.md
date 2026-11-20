---
name: image_to_image_upscale_lora_sampler_5
type: Image To Image
frequency: 19
level: moderate
coverage: 0.657316
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, GetNode, ImageScaleBy, ImageScaleToTotalPixels, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, Qwen3_VQA, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, TextEncodeQwenImageEdit, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy clearCacheAll]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/【动漫转真人】Qwen+Z-image_支持文本修改&去水印&加密_真实洗图_2030319073132814338.json, 图片生成/图生图/二次元转真人，真实感照片_2006712889599594497.json, 图片生成/图生图/二次元转真人，真实感照片aa_2050942539259232257.json, 图片生成/图生图/动漫变成了真实的人_漫画变真人_2010983846753341442.json, 图片生成/图生图/动漫转真人 真实感洗图 Qwen-image-edit +SeedVR2 高清放大_2048284125894811649.json, 图片生成/图生图/动漫转真人Qwen-Image真实感洗图 Qwen-image-edit_2048279564601794562.json, 图片生成/图生图/动漫转真人Qwen-Image真实感洗图_2033005129380667394.json, 图片生成/图生图/动漫转真人Qwen-Image真实感洗图_2038437424535179266.json, 图片生成/图生图/动漫转真人_2061420701457928194.json, 图片生成/图生图/动漫转真人_漫画生成真实的人_2011682779901206530.json, 图片生成/图生图/动漫转真人无限制Qwen+ZI真实感洗图_2025213284500115457.json, 图片生成/图生图/洗图+写实人物_2042946044908015618.json, 图片生成/图生图/超丝滑~Qwen+ZI二次元转真人！_2064229382738235394.json, 图片生成/图生图/超好用Qwen+ZI二次元转真人_2100059570327609346.json, 图片生成/图生图/超好用Qwen+ZI二次元转真人_2100752802795573250.json, 图片生成/图生图/超好用Qwen+ZI二次元转真人_2100754627636580354.json, 图片生成/图生图/（质感超强）Qwen+ZI二次元转真人，真实感转绘_2033341653011931137.json, 图片生成/图生图/（超好用）Qwen+ZI风格迁移，动漫转真人_2039899405108645890.json, 视频生成/图生视频/圆梦（二次元来现实）_2066322228135940097.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_5

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（图片生成/图生图/【动漫转真人】Qwen+Z-image_支持文本修改&去水印&加密_真实洗图_2030319073132814338.json、图片生成/图生图/二次元转真人，真实感照片_2006712889599594497.json、图片生成/图生图/二次元转真人，真实感照片aa_2050942539259232257.json、图片生成/图生图/动漫变成了真实的人_漫画变真人_2010983846753341442.json、图片生成/图生图/动漫转真人 真实感洗图 Qwen-image-edit +SeedVR2 高清放大_2048284125894811649.json…）

- **类型**：Image To Image
- **样本数**：19
- **可信度**：中等可信
- **平均知识覆盖**：66%

## 共有节点

全部 19 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `GetNode`
- `ImageScaleBy`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `Qwen3_VQA`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `TextEncodeQwenImageEdit`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy clearCacheAll`

**可变部分**（部分 workflow 才有）：
- `JoinStrings` —— 18/19 个有
- `WD14Tagger|pysssss` —— 18/19 个有
- `easy showAnything` —— 18/19 个有
- `ShowText|pysssss` —— 17/19 个有
- `Fast Groups Bypasser (rgthree)` —— 15/19 个有
- `CompressImages` —— 3/19 个有
- `AILab_ImageStitch` —— 1/19 个有
- `CR Text Concatenate` —— 1/19 个有
- `DF_Text_Box` —— 1/19 个有
- `GetImageSize` —— 1/19 个有
- `Int` —— 1/19 个有
- `PreviewImage` —— 1/19 个有
- `ResizeImageNode` —— 1/19 个有
- `TT_img_enc` —— 1/19 个有
- `TextInput_` —— 1/19 个有
- `easy boolean` —— 1/19 个有
- `easy imageSwitch` —— 1/19 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 5 - 10 | 19 | 85% |
| Prompt 约束强度(CFG) | 1 | 1 - 1.6 | 19 | 76% |
| 采样算法 | res_2m | - | 19 | 53% |
| 调度器 | sgm_uniform | - | 19 | 53% |
| 重绘幅度 | 1 | 0.35 - 1 | 19 | 55% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 40/19 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 5 - 10，19 个样本，取值集中（一致性 85%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1.6，19 个样本
- 采样算法 最常用 res_2m，19 个样本，一致性 53%
- 调度器 最常用 sgm_uniform，19 个样本，一致性 53%
- 重绘幅度 中位数 1，观测区间 0.35 - 1，19 个样本
- 高发问题（40/19 个样本）：Steps较低可能导致细节不足
