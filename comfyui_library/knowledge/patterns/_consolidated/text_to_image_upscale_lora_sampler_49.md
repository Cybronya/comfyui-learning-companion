---
name: text_to_image_upscale_lora_sampler_49
type: Text To Image
frequency: 6
level: weak
coverage: 0.914167
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, ImageScaleToTotalPixels, KSampler, LoraLoaderModelOnly, PreviewImage, RH_LLMAPI_NODE, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, Text Multiline, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed, easy clearCacheAll, easy imageSize, easy seed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-Image文生图直出4K超高清，速度更快效果更好一键出大片_2114439166359597058.json, 图片生成/文生图/Z-Image文生图直出4K，速度快效果好的高清生成_2110801569057955842.json, 图片生成/文生图/Z-Image文生图直出4K｜速度更快效果更好商用首选_2110752276745904129.json, 图片生成/文生图/文生图-直出4K-速度更快-效果更好Z-Image_1996506151086866434.json, 图片生成/文生图/文生图-直出4K-速度更快-效果更好Z-Image_2113797085798686721.json, 图片生成/文生图/文生图-直出4K-速度更快-效果更好Z-Image_2113807855840223234.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_49

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/Z-Image文生图直出4K超高清，速度更快效果更好一键出大片_2114439166359597058.json、图片生成/文生图/Z-Image文生图直出4K，速度快效果好的高清生成_2110801569057955842.json、图片生成/文生图/Z-Image文生图直出4K｜速度更快效果更好商用首选_2110752276745904129.json、图片生成/文生图/文生图-直出4K-速度更快-效果更好Z-Image_1996506151086866434.json、图片生成/文生图/文生图-直出4K-速度更快-效果更好Z-Image_2113797085798686721.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RH_LLMAPI_NODE`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `easy imageSize`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 3/6 个有
- `JjkText` —— 3/6 个有
- `solarL_SaveImagesToZip` —— 3/6 个有
- `孤海注释` —— 3/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 7 | 4 - 10 | 6 | 57% |
| Prompt 约束强度(CFG) | 2.75 | 1 - 4.5 | 6 | 36% |
| 采样算法 | er_sde | - | 6 | 50% |
| 调度器 | beta | - | 6 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 808 | 80 - 1536 | 6 | 10% |
| 高度 | 808 | 80 - 1536 | 6 | 10% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 7，观测区间 4 - 10，6 个样本
- Prompt 约束强度(CFG) 中位数 2.75，观测区间 1 - 4.5，6 个样本，取值分散，一致性仅 36%
- 采样算法 最常用 er_sde，6 个样本，一致性 50%
- 调度器 最常用 beta，6 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 808，观测区间 80 - 1536，6 个样本，取值分散，一致性仅 10%
- 高度 中位数 808，观测区间 80 - 1536，6 个样本，取值分散，一致性仅 10%
- 高发问题（3/6 个样本）：Steps较低可能导致细节不足
