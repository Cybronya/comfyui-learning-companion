---
name: text_to_image_lora_sampler_clip_10
type: Text To Image
frequency: 24
level: strong
coverage: 0.897
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, CheckpointLoaderSimple, ConditioningZeroOut, EmptyLatentImage, JjkText, KSampler, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: NumberCalculator, LoraLoaderModelOnly, ModelSamplingAuraFlow, PathchSageAttentionKJ, PreviewImage, QZ_ResolutionPreset, SaveImage, SimpleMathDual+, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy loraStack, easy loraStackApply, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2文生图超写实4K 高质量写实图片生成_2100286484011114498.json, 图片生成/文生图/Krea2文生图超写实4K 高质量写实图片生成_2100300774122283009.json, 图片生成/文生图/Krea2文生图超写实4K版｜二次元三次元大片随你出_2103745383041167361.json, 图片生成/文生图/Krea2文生图超写实4K｜美少女写真级质感 写实细节纤毫毕现_2104061166308909057.json, 图片生成/文生图/Krea2超写实4K文生图 照片级质感画面直出_2105120850289709058.json, 图片生成/文生图/Krea2超写实4K文生图去AI感处理工具_2100316137811693570.json, 图片生成/文生图/Krea2超写实4K文生图去AI感处理，写实风格高清图像生成工具_2103262027421675521.json, 图片生成/文生图/Krea2超写实4K文生图去AI感｜一张提示词直出大片，AI感全无更耐看_2100422023318171650.json, 图片生成/文生图/Krea2超写实4K文生图少女写真向｜发丝细节可见，美少女写实风_2107330754664558594.json, 图片生成/文生图/Krea2超写实4K文生图美少女版｜二次元美图写实化，质感细腻_2107329097591513089.json, 图片生成/文生图/Krea2超写实4K文生图，写实风格高质量文本到图像生成方案_2106124159733555201.json, 图片生成/文生图/Krea2超写实4K文生图，动漫角色写实风格高质量文本到图像生成_2103916989973614594.json, 图片生成/文生图/Krea2超写实4K文生图，美少女写实风格高质量文本到图像生成_2103276295567265794.json, 图片生成/文生图/Krea2超写实4K文生图，美少女写实风格高质量文本到图像生成_2103621438455500802.json, 图片生成/文生图/Krea2超写实4K文生图，美少女写实风格高质量文本到图像生成_2103962300368637953.json, 图片生成/文生图/Krea2超写实4K文生图，美少女写实风格高质量文本到图像生成_2105727853039013890.json, 图片生成/文生图/Krea2超写实4K文生图，美少女写实风格高质量文本到图像生成_2106114454051180545.json, 图片生成/文生图/Krea2超写实4K文生图｜写实人像质感天花板，出图即海报级_2107327523389534209.json, 图片生成/文生图/Krea2超写实4K文生图｜动漫写实角色大片质感直出_2103737646886506498.json, 图片生成/文生图/Krea2超写实4K文生图｜文生人物角色一念成图，写实质感直出可商用_2100418725001383938.json, 图片生成/文生图/Krea2超写实4K文生图｜美少女写实出图 细节拉满质感在线_2104054796482334721.json, 图片生成/文生图/Krea2超写实4K文生图｜美少女写实风一键直出_2105232736146518017.json, 图片生成/文生图/Krea2超写实4K文生图｜美少女写实风格出图 细节经得起放大_2105526213778427905.json, 图片生成/文生图/文生图Krea2超写实4K 照片级质感画面直出_2105075463394775042.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_10

> 由 `engine/knowledge_consolidation` 从 24 个 workflow 归纳得出（图片生成/文生图/Krea2文生图超写实4K 高质量写实图片生成_2100286484011114498.json、图片生成/文生图/Krea2文生图超写实4K 高质量写实图片生成_2100300774122283009.json、图片生成/文生图/Krea2文生图超写实4K版｜二次元三次元大片随你出_2103745383041167361.json、图片生成/文生图/Krea2文生图超写实4K｜美少女写真级质感 写实细节纤毫毕现_2104061166308909057.json、图片生成/文生图/Krea2超写实4K文生图 照片级质感画面直出_2105120850289709058.json…）

- **类型**：Text To Image
- **样本数**：24
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 24 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: NumberCalculator`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `QZ_ResolutionPreset`
- `SaveImage`
- `SimpleMathDual+`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy loraStack`
- `easy loraStackApply`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 23/24 个有
- `ImageScaleToTotalPixels` —— 23/24 个有
- `SeedVR2LoadDiTModel` —— 23/24 个有
- `SeedVR2LoadVAEModel` —— 23/24 个有
- `SeedVR2VideoUpscaler` —— 23/24 个有
- `easy seed` —— 23/24 个有
- `Fast Groups Bypasser (rgthree)` —— 5/24 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 24 | 100% |
| 高度 | 80 | 80 - 80 | 24 | 100% |
| 采样步数 | 4 | 4 - 4 | 24 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 24 | 100% |
| 采样算法 | er_sde | - | 24 | 100% |
| 调度器 | beta | - | 24 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 24 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 25/24 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，24 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，24 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，24 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，24 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，24 个样本，一致性 100%
- 调度器 最常用 beta，24 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，24 个样本，取值集中（一致性 100%）
- 高发问题（25/24 个样本）：Steps较低可能导致细节不足
