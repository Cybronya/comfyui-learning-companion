---
name: text_to_image_upscale_lora_sampler_99
type: Text To Image
frequency: 3
level: weak
coverage: 0.924667
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, ImageScaleToTotalPixels, KSampler, LoraLoaderModelOnly, PreviewImage, RH_LLMAPI_NODE, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, Text Multiline, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed, easy clearCacheAll, easy imageSize, easy seed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-Image文生图直出4K，速度快效果好的高清生成_2110801569057955842.json, 图片生成/文生图/Z-Image文生图直出4K｜速度更快效果更好商用首选_2110752276745904129.json, 图片生成/文生图/文生图-直出4K-速度更快-效果更好Z-Image_1996506151086866434.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_99

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Z-Image文生图直出4K，速度快效果好的高清生成_2110801569057955842.json、图片生成/文生图/Z-Image文生图直出4K｜速度更快效果更好商用首选_2110752276745904129.json、图片生成/文生图/文生图-直出4K-速度更快-效果更好Z-Image_1996506151086866434.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 3 个 workflow 都包含：
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
- `JjkText` —— 2/3 个有
- `solarL_SaveImagesToZip` —— 2/3 个有
- `孤海注释` —— 2/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 10 | 3 | 53% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 3 | 51% |
| 采样算法 | er_sde | - | 3 | 67% |
| 调度器 | beta | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 80 | 80 - 1536 | 3 | 0% |
| 高度 | 80 | 80 - 1536 | 3 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 10，3 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，3 个样本
- 采样算法 最常用 er_sde，3 个样本，一致性 67%
- 调度器 最常用 beta，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 1536，3 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1536，3 个样本，取值分散，一致性仅 0%
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
