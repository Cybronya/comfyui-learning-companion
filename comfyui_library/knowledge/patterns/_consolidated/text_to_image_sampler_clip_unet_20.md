---
name: text_to_image_sampler_clip_unet_20
type: Text To Image
frequency: 13
level: weak
coverage: 0.815308
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/2021581695731900418.json, 图片生成/文生图/1.阿清的z-image工作流_2037804089450438658.json, 图片生成/文生图/1903742090277195777.json, 图片生成/文生图/1911034174755799042.json, 图片生成/文生图/5.Krea2 文生图_2083469098800996354.json, 图片生成/文生图/K2模特级生成_2089374387597307906.json, 图片生成/文生图/KREA2_LORA人像工作流_2078646318087630849.json, 图片生成/文生图/Krea-2_ 文生图_2095794360649601025.json, 图片生成/文生图/Krea-2文生图官方版｜高质量图像生成工作流_2095956990584512513.json, 图片生成/文生图/Krea-2文生图工作流｜写实质感出图效果稳定可靠_2107695970124386305.json, 图片生成/文生图/Krea2 Turbo极速文生图 API写实人像高质量生成_2099221894967947265.json, 图片生成/文生图/opsv-krea2_t2i_2074897972374097921.json, 图片生成/文生图/opsv-krea2_t2i_2086450223353778178.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_20

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/2021581695731900418.json、图片生成/文生图/1.阿清的z-image工作流_2037804089450438658.json、图片生成/文生图/1903742090277195777.json、图片生成/文生图/1911034174755799042.json、图片生成/文生图/5.Krea2 文生图_2083469098800996354.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 12/13 个有
- `PreviewAny` —— 10/13 个有
- `PrimitiveStringMultiline` —— 10/13 个有
- `StringConcatenate` —— 10/13 个有
- `TextGenerate` —— 10/13 个有
- `ComfySwitchNode` —— 9/13 个有
- `LoraLoaderModelOnly` —— 9/13 个有
- `PrimitiveBoolean` —— 9/13 个有
- `ResolutionSelector` —— 8/13 个有
- `FaceDetailer` —— 3/13 个有
- `JjkText` —— 3/13 个有
- `RTXVideoSuperResolution` —— 3/13 个有
- `SAMLoader` —— 3/13 个有
- `UltralyticsDetectorProvider` —— 3/13 个有
- `solarL_SaveImagesToZip` —— 3/13 个有
- `孤海注释` —— 3/13 个有
- `CR Prompt Text` —— 2/13 个有
- `Int` —— 2/13 个有
- `PlaySound|pysssss` —— 1/13 个有
- `easy promptList` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 2 - 25 | 13 | 11% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 13 | 23% |
| 采样算法 | euler | - | 13 | 46% |
| 调度器 | simple | - | 13 | 46% |
| 重绘幅度 | 1 | 0.2 - 1 | 13 | 59% |
| 宽度 | 1024 | 80 - 2048 | 13 | 28% |
| 高度 | 1024 | 80 - 2048 | 13 | 39% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 2 - 25，13 个样本，取值分散，一致性仅 11%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，13 个样本，取值分散，一致性仅 23%
- 采样算法 最常用 euler，13 个样本，一致性 46%
- 调度器 最常用 simple，13 个样本，一致性 46%
- 重绘幅度 中位数 1，观测区间 0.2 - 1，13 个样本
- 宽度 中位数 1024，观测区间 80 - 2048，13 个样本，取值分散，一致性仅 28%
- 高度 中位数 1024，观测区间 80 - 2048，13 个样本，取值分散，一致性仅 39%
- 高发问题（17/13 个样本）：Steps较低可能导致细节不足
