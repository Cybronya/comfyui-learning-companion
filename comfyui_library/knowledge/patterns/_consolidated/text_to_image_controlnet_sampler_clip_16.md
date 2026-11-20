---
name: text_to_image_controlnet_sampler_clip_16
type: Text To Image
frequency: 4
level: moderate
coverage: 0.916
common_nodes: [ApplyEcomIDAdvanced, CLIPTextEncode, ControlNetLoader, EcomIDFaceAnalysis, EcomID_PulidModelLoader, EmptyLatentImage, InstantIDModelLoader, KSampler, LoadImage, PreviewImage, PulidEvaClipLoader, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/图生图/EcomID一键换脸，改变年龄_1948964814342238210.json, 图片生成/图生图/一键生成Q版卡通3D人物全身照_1953462840814436353.json, 平台全量/FLUX 真人变Q版手办形象一键盲盒手办IP形象_1921738488809472002.json, 平台全量/超高清8kFLUX超级高清放大修复_1884232069587914753.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_sampler_clip_16

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/EcomID一键换脸，改变年龄_1948964814342238210.json、图片生成/图生图/一键生成Q版卡通3D人物全身照_1953462840814436353.json、平台全量/FLUX 真人变Q版手办形象一键盲盒手办IP形象_1921738488809472002.json、平台全量/超高清8kFLUX超级高清放大修复_1884232069587914753.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 4 个 workflow 都包含：
- `ApplyEcomIDAdvanced`
- `CLIPTextEncode`
- `ControlNetLoader`
- `EcomIDFaceAnalysis`
- `EcomID_PulidModelLoader`
- `EmptyLatentImage`
- `InstantIDModelLoader`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `PulidEvaClipLoader`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 3/4 个有
- `SUPIR_Upscale` —— 3/4 个有
- `RH_Translator` —— 2/4 个有
- `Checkpoint Loader (Simple)` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/4 个有
- `Multi Text Merge` —— 1/4 个有
- `Text` —— 1/4 个有
- `VAEEncode` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 20 - 25 | 4 | 91% |
| Prompt 约束强度(CFG) | 6 | 2 - 6 | 4 | 65% |
| 采样算法 | dpmpp_2m | - | 4 | 75% |
| 调度器 | karras | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 768 | 512 - 768 | 4 | 84% |
| 高度 | 1024 | 512 - 1024 | 4 | 75% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 20 - 25，4 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 6，观测区间 2 - 6，4 个样本
- 采样算法 最常用 dpmpp_2m，4 个样本，一致性 75%
- 调度器 最常用 karras，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 768，观测区间 512 - 768，4 个样本，取值集中（一致性 84%）
- 高度 中位数 1024，观测区间 512 - 1024，4 个样本
