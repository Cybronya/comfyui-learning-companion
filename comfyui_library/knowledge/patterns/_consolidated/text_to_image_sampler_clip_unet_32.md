---
name: text_to_image_sampler_clip_unet_32
type: Text To Image
frequency: 15
level: weak
coverage: 0.8782
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Moss-image SFT 文生图稳定版｜SFT调优出图更稳_2112416033981161473.json, 图片生成/文生图/Moss-image SFT文生图_2112104895800242178.json, 图片生成/文生图/MossImage文生分镜图V1.0 分镜图像批量生成处理工具_2113034314110820353.json, 图片生成/文生图/MossImage文生分镜图V1.0｜短剧漫画分镜批量出图神器_2112906492759334914.json, 图片生成/文生图/MossImage文生分镜图生成工作流V1.0_2112470399945625601.json, 图片生成/文生图/Qwen Image 2.1文生图处理生成工作流_2102097450449326081.json, 图片生成/文生图/Qwen Image 2.1文生图处理生成工具_2102510005793673217.json, 图片生成/文生图/Qwen Image 2.1文生图官方PE版，高质量文本到图像生成工作流_2105726358625284098.json, 图片生成/文生图/Qwen Image 2.1文生图官方工作流BF16版处理生成工具_2102484931288068098.json, 图片生成/文生图/Qwen Image 2.1文生图工作流，高质量文本到图像生成方案_2107518180074807297.json, 图片生成/文生图/Qwen Image 2.1文生图提示词增强，原生2K直出高质量文本到图像方案_2105766561448550401.json, 图片生成/文生图/Qwen Image 2.1自助捏脸肖像生成｜人物资产一套带走_2111760751525449729.json, 图片生成/文生图/Qwen Image 2.1自助捏脸，人物肖像资产生成利器_2111965062415081474.json, 图片生成/文生图/Qwen-Image-2.1-Turbo 7步出图，亚洲人像文生图优化_2111197034324779010.json, 图片生成/文生图/Qwen-Image-2.1-Turbo七步出图｜亚洲人像写真文生图极速版_2111055095529041921.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_32

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/文生图/Moss-image SFT 文生图稳定版｜SFT调优出图更稳_2112416033981161473.json、图片生成/文生图/Moss-image SFT文生图_2112104895800242178.json、图片生成/文生图/MossImage文生分镜图V1.0 分镜图像批量生成处理工具_2113034314110820353.json、图片生成/文生图/MossImage文生分镜图V1.0｜短剧漫画分镜批量出图神器_2112906492759334914.json、图片生成/文生图/MossImage文生分镜图生成工作流V1.0_2112470399945625601.json…）

- **类型**：Text To Image
- **样本数**：15
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 14/15 个有
- `ResolutionSelector` —— 14/15 个有
- `LoraLoaderModelOnly` —— 13/15 个有
- `solarL_SaveImagesToZip` —— 13/15 个有
- `孤海注释` —— 13/15 个有
- `TextEncodeQwenImage21` —— 10/15 个有
- `CR Prompt Text` —— 6/15 个有
- `SaveImageAdvanced` —— 6/15 个有
- `ComfySwitchNode` —— 5/15 个有
- `QwenImage21Cache` —— 5/15 个有
- `TextGenerate` —— 5/15 个有
- `easy cleanGpuUsed` —— 5/15 个有
- `PreviewImage` —— 4/15 个有
- `easy showAnything` —— 4/15 个有
- `ImageStitch` —— 3/15 个有
- `MOSSImagePromptEnhancerT8` —— 3/15 个有
- `PreviewAny` —— 3/15 个有
- `Color Grading JK` —— 2/15 个有
- `FacialCustomization` —— 2/15 个有
- `PrimitiveStringMultiline` —— 2/15 个有
- `QwenImage21_T2IPromptRewrite` —— 2/15 个有
- `QwenPERewriteT8` —— 2/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 50 | 15 | 0% |
| Prompt 约束强度(CFG) | 4.5 | 3 - 4.5 | 15 | 90% |
| 采样算法 | er_sde | - | 15 | 87% |
| 调度器 | beta | - | 15 | 87% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |
| 宽度 | 80 | 80 - 1024 | 15 | 0% |
| 高度 | 80 | 80 - 1024 | 15 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 50，15 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 3 - 4.5，15 个样本，取值集中（一致性 90%）
- 采样算法 最常用 er_sde，15 个样本，一致性 87%
- 调度器 最常用 beta，15 个样本，一致性 87%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 1024，15 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1024，15 个样本，取值分散，一致性仅 0%
- 高发问题（15/15 个样本）：Steps较低可能导致细节不足
