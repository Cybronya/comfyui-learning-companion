---
name: text_to_image_sampler_clip_unet_66
type: Text To Image
frequency: 10
level: weak
coverage: 0.8496
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, ResolutionSelector, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/MOSS_BASE_SFT的人像资产测试_2111781812916801538.json, 图片生成/文生图/Moss_Image_SFT_2113276107721105409.json, 图片生成/文生图/Moss文生图+8步加速_2112030480005689345.json, 图片生成/文生图/Qwen Image 2.1文生图人像写真处理生成工具_2102490947526418434.json, 图片生成/文生图/Qwen Image 2.1文生图纯净官流40步无PE工作流，文生图高质量文本到图像_2107569921352884226.json, 图片生成/文生图/Qwen image 2.1文生图角色四视图V1.1 角色设定批量产出_2109347086192963585.json, 图片生成/文生图/Qwen-Image-2.1 T2I文生图｜人像写真级出图质感｜写实人像一步生成_2102229026680164354.json, 视频生成/文生视频/Qwen Image 2.1 T2I文生图人像写真级质感 写实人像一步生成_2104696107367489538.json, 视频生成/文生视频/Qwen-Image-2.1_T2I文生图｜人像写真级出图质感｜写实人像一步生成_2104043820429176833.json, 视频生成/文生视频/qwen_image_2.1提示词扩写｜一句话自动扩成专业描述｜文生图更省心_2102309278647406593.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_66

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/MOSS_BASE_SFT的人像资产测试_2111781812916801538.json、图片生成/文生图/Moss_Image_SFT_2113276107721105409.json、图片生成/文生图/Moss文生图+8步加速_2112030480005689345.json、图片生成/文生图/Qwen Image 2.1文生图人像写真处理生成工具_2102490947526418434.json、图片生成/文生图/Qwen Image 2.1文生图纯净官流40步无PE工作流，文生图高质量文本到图像_2107569921352884226.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `ResolutionSelector`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 9/10 个有
- `LoraLoaderModelOnly` —— 8/10 个有
- `JjkText` —— 7/10 个有
- `TextEncodeQwenImage21` —— 7/10 个有
- `TextGenerate` —— 7/10 个有
- `easy showAnything` —— 7/10 个有
- `solarL_SaveImagesToZip` —— 7/10 个有
- `Fast Groups Bypasser (rgthree)` —— 6/10 个有
- `孤海注释` —— 6/10 个有
- `Seed (rgthree)` —— 5/10 个有
- `easy promptList` —— 4/10 个有
- `EmptyImage` —— 3/10 个有
- `PreviewImage` —— 3/10 个有
- `SkipLayerGuidanceDiTSimple` —— 3/10 个有
- `ComfySwitchNode` —— 2/10 个有
- `FacialCustomization` —— 1/10 个有
- `PrimitiveBoolean` —— 1/10 个有
- `StringConcatenate` —— 1/10 个有
- `TextGenerateLTX2Prompt` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 50 | 10 | 0% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 5 | 10 | 70% |
| 采样算法 | er_sde | - | 10 | 80% |
| 调度器 | beta | - | 10 | 70% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| 宽度 | 80 | 80 - 1024 | 10 | 0% |
| 高度 | 80 | 80 - 1024 | 10 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 50，10 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 5，10 个样本
- 采样算法 最常用 er_sde，10 个样本，一致性 80%
- 调度器 最常用 beta，10 个样本，一致性 70%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 1024，10 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1024，10 个样本，取值分散，一致性仅 0%
- 高发问题（9/10 个样本）：Steps较低可能导致细节不足
