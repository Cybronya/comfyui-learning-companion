---
name: text_to_image_sampler_clip_unet_111
type: Text To Image
frequency: 7
level: weak
coverage: 0.886143
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Y1-Image_wan2_2_14B_t2v_1960231389213962242.json, 图片生成/文生图/Z-Anime-动漫文生图_2049110641390129153.json, 图片生成/文生图/boogu-base-文生图_2068132811814563841.json, 图片生成/文生图/boogu-文生图_2067591707537002497.json, 图片生成/文生图/文生图简单实用、真人、快速_2114370405342474242.json, 图片生成/文生图/极简中文生图工作流_2070152864193925122.json, 图片生成/文生图/电商生成真实人物图片 MagicWanImage_1991348310250467330.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_111

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/Y1-Image_wan2_2_14B_t2v_1960231389213962242.json、图片生成/文生图/Z-Anime-动漫文生图_2049110641390129153.json、图片生成/文生图/boogu-base-文生图_2068132811814563841.json、图片生成/文生图/boogu-文生图_2067591707537002497.json、图片生成/文生图/文生图简单实用、真人、快速_2114370405342474242.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 6/7 个有
- `ModelSamplingSD3` —— 2/7 个有
- `EmptyHunyuanLatentVideo` —— 1/7 个有
- `RH_Translator` —— 1/7 个有
- `SDXL Resolutions (JPS)` —— 1/7 个有
- `SeargePromptCombiner` —— 1/7 个有
- `easy cleanGpuUsed` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 720 - 1920 | 7 | 63% |
| 高度 | 1280 | 768 - 1288 | 7 | 84% |
| 采样步数 | 10 | 4 - 50 | 7 | 16% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 7 | 34% |
| 采样算法 | euler | - | 7 | 71% |
| 调度器 | simple | - | 7 | 57% |
| 重绘幅度 | 1 | 0.2 - 1 | 7 | 68% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 720 - 1920，7 个样本
- 高度 中位数 1280，观测区间 768 - 1288，7 个样本，取值集中（一致性 84%）
- 采样步数 中位数 10，观测区间 4 - 50，7 个样本，取值分散，一致性仅 16%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，7 个样本，取值分散，一致性仅 34%
- 采样算法 最常用 euler，7 个样本，一致性 71%
- 调度器 最常用 simple，7 个样本，一致性 57%
- 重绘幅度 中位数 1，观测区间 0.2 - 1，7 个样本
