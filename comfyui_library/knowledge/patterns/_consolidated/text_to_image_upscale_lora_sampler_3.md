---
name: text_to_image_upscale_lora_sampler_3
type: Text To Image
frequency: 19
level: weak
coverage: 0.785211
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), ImageScaleToTotalPixels, KSampler, LoraLoaderModelOnly, PathchSageAttentionKJ, PreviewImage, SaveImage, Seed (rgthree), SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/krea2🌸白玉AIO🌸参考图生图_2101879305545535489.json, 图片生成/文生图/Krea2⭐玉京仙宫玄幻风（注释内有模型、提示词下载链接）_2096061187103485953.json, 图片生成/文生图/Krea2白玉AIO文生图 全功能一体化图片生成工作流_2099205852929548289.json, 图片生成/文生图/Krea2白玉AIO文生图 全功能一体化图片生成工作流_2099579173265301506.json, 图片生成/文生图/Krea2白玉AIO文生图自用工作流，文生图高质量文本到图像生成方案_2107955833001832449.json, 图片生成/文生图/krea2-白玉AIO-文生图(自用)_2107455409173913602.json, 图片生成/文生图/krea2墨玉PRO版文生图_2088252923926114306.json, 图片生成/文生图/krea2文生图｜美少女人像写真生成_2095239847958106114.json, 图片生成/文生图/krea2🌸白玉AIO🌸文生图_2082446128871727105.json, 图片生成/文生图/krea2🌸白玉AIO🌸文生图_2098927912908058625.json, 图片生成/文生图/krea2🌸白玉AIO🌸文生图_2098985661717114882.json, 图片生成/文生图/krea2🌸白玉AIO🌸文生图_2099661599010287617.json, 图片生成/文生图/krea2🌸白玉AIO🌸文生图_2101522285130768385.json, 图片生成/文生图/krea2🔺墨玉PRO版🔺文生图_2075228124945666049.json, 图片生成/文生图/krea2🔺墨玉焚诀🔺文生图_无角标导出_2079555165958533121.json, 图片生成/文生图/krea2🔺墨玉焚诀🔺文生图_高清放大 无角标导出_2080176285283872770.json, 图片生成/文生图/中国风玄幻大作｜Krea2玉京仙宫场景文生图_2096621224637063170.json, 图片生成/文生图/玉京仙宫玄幻风场景｜Krea2中国风文生图生成_2096302133913145346.json, 图片生成/文生图/白玉AIO人像写真｜krea2美少女文生图_2095512968669782018.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_3

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（图片生成/图生图/krea2🌸白玉AIO🌸参考图生图_2101879305545535489.json、图片生成/文生图/Krea2⭐玉京仙宫玄幻风（注释内有模型、提示词下载链接）_2096061187103485953.json、图片生成/文生图/Krea2白玉AIO文生图 全功能一体化图片生成工作流_2099205852929548289.json、图片生成/文生图/Krea2白玉AIO文生图 全功能一体化图片生成工作流_2099579173265301506.json、图片生成/文生图/Krea2白玉AIO文生图自用工作流，文生图高质量文本到图像生成方案_2107955833001832449.json…）

- **类型**：Text To Image
- **样本数**：19
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：79%

## 共有节点

全部 19 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `SaveImage`
- `Seed (rgthree)`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `LayerColor: Brightness & Contrast` —— 16/19 个有
- `LayerFilter: AddGrain` —— 16/19 个有
- `TTResolutionSelector` —— 16/19 个有
- `CLIPLoader` —— 7/19 个有
- `JjkText` —— 7/19 个有
- `UNETLoader` —— 7/19 个有
- `VAELoader` —— 7/19 个有
- `solarL_SaveImagesToZip` —— 7/19 个有
- `孤海注释` —— 7/19 个有
- `EmptyImage` —— 5/19 个有
- `ImageResizeKJv2` —— 1/19 个有
- `LoadImage` —— 1/19 个有
- `PrimitiveStringMultiline` —— 1/19 个有
- `RMBG` —— 1/19 个有
- `TextEncodeQwenImageEditPlus` —— 1/19 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1088 | 80 - 2560 | 19 | 20% |
| 高度 | 1920 | 80 - 1920 | 19 | 27% |
| 采样步数 | 8 | 4 - 8 | 19 | 70% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 19 | 26% |
| 采样算法 | euler | - | 19 | 63% |
| 调度器 | simple | - | 19 | 63% |
| 重绘幅度 | 1 | 1 - 1 | 19 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 27/19 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1088，观测区间 80 - 2560，19 个样本，取值分散，一致性仅 20%
- 高度 中位数 1920，观测区间 80 - 1920，19 个样本，取值分散，一致性仅 27%
- 采样步数 中位数 8，观测区间 4 - 8，19 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，19 个样本，取值分散，一致性仅 26%
- 采样算法 最常用 euler，19 个样本，一致性 63%
- 调度器 最常用 simple，19 个样本，一致性 63%
- 重绘幅度 中位数 1，观测区间 1 - 1，19 个样本，取值集中（一致性 100%）
- 高发问题（27/19 个样本）：Steps较低可能导致细节不足
