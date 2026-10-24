---
name: text_to_image_lora_sampler_clip_220
type: Text To Image
frequency: 8
level: weak
coverage: 0.899125
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/Image2.5光影迁移重打光｜一键换光线换氛围光，画面光影重塑_2104512814172954625.json, 图片生成/反推提示词/Krea2局部重绘PS版本，风格化反推提示词图生图精准区域编辑工具_2103567391509794817.json, 图片生成/图生图/10图Qwen Image 2.1多图编辑工作流，图生图多图编辑处理工具_2108330608001896449.json, 图片生成/图生图/FLUX3图像编辑方案，局部重绘换背景随心控_2111588628790071298.json, 图片生成/图生图/Klein 9B-动漫上色+室内风格迁移_2071151331997474818.json, 图片生成/图生图/Krea2局部重绘PS版工作流｜提示词反推写实图生图_2097491218342178818.json, 图片生成/图生图/Qwen Image 2.1 Turbo八步极速图像编辑 高效精准改图必备方案_2110370961915727874.json, 图片生成/图生图/Qwen Image 2.1 Turbo官方8步图像编辑 高效改图方案_2109720316372152321.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_220

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/反推提示词/Image2.5光影迁移重打光｜一键换光线换氛围光，画面光影重塑_2104512814172954625.json、图片生成/反推提示词/Krea2局部重绘PS版本，风格化反推提示词图生图精准区域编辑工具_2103567391509794817.json、图片生成/图生图/10图Qwen Image 2.1多图编辑工作流，图生图多图编辑处理工具_2108330608001896449.json、图片生成/图生图/FLUX3图像编辑方案，局部重绘换背景随心控_2111588628790071298.json、图片生成/图生图/Klein 9B-动漫上色+室内风格迁移_2071151331997474818.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 7/8 个有
- `solarL_SaveImagesToZip` —— 7/8 个有
- `孤海注释` —— 7/8 个有
- `Image Comparer (rgthree)` —— 6/8 个有
- `Int` —— 5/8 个有
- `ConditioningZeroOut` —— 4/8 个有
- `VAEEncode` —— 4/8 个有
- `CR Text` —— 3/8 个有
- `QwenImage21Cache` —— 3/8 个有
- `TextEncodeQwenImage21` —— 3/8 个有
- `ImageResizeKJv2` —— 2/8 个有
- `KSamplerAdvanced` —— 2/8 个有
- `KSamplerSelect` —— 2/8 个有
- `ManualSigmas` —— 2/8 个有
- `ReferenceLatent` —— 2/8 个有
- `SamplerCustom` —— 2/8 个有
- `GoogleTranslator` —— 1/8 个有
- `RH_RhartImageG25FlareImageToImage` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 512 | 8 | 0% |
| 高度 | 80 | 80 - 512 | 8 | 0% |
| 采样步数 | 4 | 4 - 8 | 8 | 71% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 8 | 72% |
| 采样算法 | er_sde | - | 8 | 88% |
| 调度器 | beta | - | 8 | 88% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 512，8 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 512，8 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 4，观测区间 4 - 8，8 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，8 个样本
- 采样算法 最常用 er_sde，8 个样本，一致性 88%
- 调度器 最常用 beta，8 个样本，一致性 88%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（10/8 个样本）：Steps较低可能导致细节不足
