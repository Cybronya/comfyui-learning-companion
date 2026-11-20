---
name: text_to_image_sampler_clip_unet_74
type: Text To Image
frequency: 10
level: weak
coverage: 0.8558
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, ResolutionSelector, SaveImage, TextGenerate, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Moss-image SFT 文生图稳定版｜SFT调优出图更稳_2112416033981161473.json, 图片生成/文生图/Moss-image SFT文生图_2112104895800242178.json, 图片生成/文生图/Moss-image+Base 文生图带反推｜提示词一键获取_2112453139499667458.json, 图片生成/文生图/Moss-image+Sft 文生图反推版｜反推提示词更准_2112461263623254018.json, 图片生成/文生图/Moss_Image_sft无损加速工作流｜海报制作与字体设计一键搞定_2114168867571462145.json, 图片生成/文生图/QWen2.1文生图工作流｜千问模型文字生图轻松创作_2106996835603800065.json, 图片生成/文生图/Qwen 2.1文生图工作流，高质量文本到图像生成方案_2107183009446326274.json, 图片生成/文生图/Qwen Image 2.1文生图官方PE版，高质量文本到图像生成工作流_2105726358625284098.json, 图片生成/文生图/Qwen Image 2.1文生图工作流，高质量文本到图像生成方案_2107518180074807297.json, 图片生成/文生图/Qwen_Image_2.1文生图｜官方PE参数 老许Gary出品海报制作利器_2105515254531837953.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_74

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/Moss-image SFT 文生图稳定版｜SFT调优出图更稳_2112416033981161473.json、图片生成/文生图/Moss-image SFT文生图_2112104895800242178.json、图片生成/文生图/Moss-image+Base 文生图带反推｜提示词一键获取_2112453139499667458.json、图片生成/文生图/Moss-image+Sft 文生图反推版｜反推提示词更准_2112461263623254018.json、图片生成/文生图/Moss_Image_sft无损加速工作流｜海报制作与字体设计一键搞定_2114168867571462145.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `ResolutionSelector`
- `SaveImage`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 9/10 个有
- `solarL_SaveImagesToZip` —— 9/10 个有
- `孤海注释` —— 9/10 个有
- `PreviewAny` —— 8/10 个有
- `ComfySwitchNode` —— 6/10 个有
- `PrimitiveStringMultiline` —— 6/10 个有
- `PrimitiveBoolean` —— 5/10 个有
- `TextEncodeQwenImage21` —— 5/10 个有
- `CR Prompt Text` —— 4/10 个有
- `EmptyFlux2LatentImage` —— 3/10 个有
- `QwenImage21Cache` —— 3/10 个有
- `PreviewImage` —— 2/10 个有
- `PrimitiveInt` —— 2/10 个有
- `LazyCache` —— 1/10 个有
- `SaveImageAdvanced` —— 1/10 个有
- `SkipLayerGuidanceDiTSimple` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 50 | 10 | 0% |
| Prompt 约束强度(CFG) | 4.5 | 3 - 4.5 | 10 | 90% |
| 采样算法 | er_sde | - | 10 | 90% |
| 调度器 | beta | - | 10 | 90% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| 宽度 | 80 | 80 - 1024 | 10 | 0% |
| 高度 | 80 | 80 - 1024 | 10 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 50，10 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 3 - 4.5，10 个样本，取值集中（一致性 90%）
- 采样算法 最常用 er_sde，10 个样本，一致性 90%
- 调度器 最常用 beta，10 个样本，一致性 90%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 1024，10 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1024，10 个样本，取值分散，一致性仅 0%
- 高发问题（9/10 个样本）：Steps较低可能导致细节不足
