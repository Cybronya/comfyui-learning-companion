---
name: text_to_image_controlnet_sampler_clip_9
type: Text To Image
frequency: 5
level: strong
coverage: 0.924
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, DeepTranslatorTextNode, EG_WB_KSH, EmptyLatentImage, ImageResize+, Joy_caption, Joy_caption_load, KSampler, LoadImage, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/10s图片转线稿工作流_1890737744954662914.json, 图片生成/图生图/一键图像转线稿工作流_1923659192727425026.json, 图片生成/图生图/一键图像转线稿工作流（加强版，含高清放大）_1923642750820864001.json, 图片生成/图生图/线稿控制生图（Anyline+MistoLine）_1828665904535138305.json, 图片生成/图生图/线稿控制生图（Anyline+MistoLine）_1830480475625541633.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_sampler_clip_9

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/10s图片转线稿工作流_1890737744954662914.json、图片生成/图生图/一键图像转线稿工作流_1923659192727425026.json、图片生成/图生图/一键图像转线稿工作流（加强版，含高清放大）_1923642750820864001.json、图片生成/图生图/线稿控制生图（Anyline+MistoLine）_1828665904535138305.json、图片生成/图生图/线稿控制生图（Anyline+MistoLine）_1830480475625541633.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DeepTranslatorTextNode`
- `EG_WB_KSH`
- `EmptyLatentImage`
- `ImageResize+`
- `Joy_caption`
- `Joy_caption_load`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AnimeLineArtPreprocessor` —— 3/5 个有
- `ImageInvert` —— 3/5 个有
- `LayerColor: Brightness & Contrast` —— 3/5 个有
- `LineartStandardPreprocessor` —— 3/5 个有
- `PreviewImage` —— 3/5 个有
- `ShowText|pysssss` —— 3/5 个有
- `TextCombinerTwo` —— 3/5 个有
- `VAEEncode` —— 3/5 个有
- `AnyLinePreprocessor` —— 2/5 个有
- `PMRF` —— 2/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 1 | 1 - 1 | 5 | 100% |
| 采样步数 | 30 | 30 - 30 | 5 | 100% |
| Prompt 约束强度(CFG) | 7 | 7 - 7 | 5 | 100% |
| 采样算法 | dpmpp_2m_sde | - | 5 | 100% |
| 调度器 | karras | - | 5 | 100% |
| 重绘幅度 | 0.65 | 0.65 - 0.93 | 5 | 82% |
| 宽度 | 1920 | 1920 - 1920 | 5 | 100% |
| 高度 | 1080 | 1080 - 1080 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 30，观测区间 30 - 30，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 7，观测区间 7 - 7，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m_sde，5 个样本，一致性 100%
- 调度器 最常用 karras，5 个样本，一致性 100%
- 重绘幅度 中位数 0.65，观测区间 0.65 - 0.93，5 个样本，取值集中（一致性 82%）
- 宽度 中位数 1920，观测区间 1920 - 1920，5 个样本，取值集中（一致性 100%）
- 高度 中位数 1080，观测区间 1080 - 1080，5 个样本，取值集中（一致性 100%）
