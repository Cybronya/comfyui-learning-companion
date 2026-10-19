---
name: text_to_image_lora_sampler_clip_70
type: Text To Image
frequency: 11
level: weak
coverage: 0.889727
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImage21, TextGenerateLTX2Prompt, UNETLoader, VAEDecode, VAELoader, easy showAnything, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen Image 2.1文生图带优化，开源最强图片模型文本到图像方案_2103623073571368962.json, 图片生成/文生图/Qwen-image2.1开源文生图｜提示词自动优化直出好图_2105261065113264129.json, 图片生成/文生图/Qwen-image2.1文生图开源王者｜优化提示词一步到位_2105264371466334209.json, 图片生成/文生图/千问2.1文生图_2103829231951241218.json, 图片生成/文生图/千问2.1文生图自动优化版｜一句话提示词直出精美图片_2103726338984210433.json, 图片生成/文生图/千问2.1文生图｜轻量好上手 文生图出图稳定效果在线_2104035483096539138.json, 图片生成/文生图/千问iamge2.1文生图工作流｜官方同款画质一键直出_2103062439452569601.json, 图片生成/文生图/开源最强Qwen-image2.1文生图｜自带提示词优化加持_2105257763684311042.json, 图片生成/文生图/开源最强图片模型Qwen image2.1文生图带优化 高质量画面直出_2105421946069536770.json, 图片生成/文生图/开源最强图片模型Qwen image2.1文生图带优化 高质量画面直出_2105423398204698625.json, 数字人/数字人/Qwen Image 2.1文生图处理生成工具_2102554303809544193.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_70

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/Qwen Image 2.1文生图带优化，开源最强图片模型文本到图像方案_2103623073571368962.json、图片生成/文生图/Qwen-image2.1开源文生图｜提示词自动优化直出好图_2105261065113264129.json、图片生成/文生图/Qwen-image2.1文生图开源王者｜优化提示词一步到位_2105264371466334209.json、图片生成/文生图/千问2.1文生图_2103829231951241218.json、图片生成/文生图/千问2.1文生图自动优化版｜一句话提示词直出精美图片_2103726338984210433.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImage21`
- `TextGenerateLTX2Prompt`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 10/11 个有
- `CR Text` —— 7/11 个有
- `CR Prompt List` —— 6/11 个有
- `ImpactInt` —— 6/11 个有
- `Seed (rgthree)` —— 6/11 个有
- `String Literal` —— 6/11 个有
- `FastGroupsBypassSwitch` —— 4/11 个有
- `PreviewImage` —— 4/11 个有
- `ResolutionSelector` —— 3/11 个有
- `CM_FloatToInt` —— 2/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 1024 | 11 | 0% |
| 高度 | 80 | 80 - 1024 | 11 | 0% |
| 采样步数 | 4 | 4 - 50 | 11 | 0% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 11 | 76% |
| 采样算法 | er_sde | - | 11 | 91% |
| 调度器 | beta | - | 11 | 91% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 1024，11 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1024，11 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 4，观测区间 4 - 50，11 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，11 个样本
- 采样算法 最常用 er_sde，11 个样本，一致性 91%
- 调度器 最常用 beta，11 个样本，一致性 91%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（12/11 个样本）：Steps较低可能导致细节不足
