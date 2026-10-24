---
name: text_to_image_controlnet_sampler_clip_23
type: Text To Image
frequency: 2
level: weak
coverage: 0.922
common_nodes: [ApplyEcomIDAdvanced, CLIPTextEncode, ControlNetLoader, EcomIDFaceAnalysis, EcomID_PulidModelLoader, EmptyLatentImage, InstantIDModelLoader, KSampler, LoadImage, PreviewImage, PulidEvaClipLoader, RH_Translator, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/图生图/EcomID一键换脸，改变年龄_1948964814342238210.json, 图片生成/图生图/一键生成Q版卡通3D人物全身照_1953462840814436353.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_sampler_clip_23

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/EcomID一键换脸，改变年龄_1948964814342238210.json、图片生成/图生图/一键生成Q版卡通3D人物全身照_1953462840814436353.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
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
- `RH_Translator`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `Checkpoint Loader (Simple)` —— 1/2 个有
- `CheckpointLoaderSimple` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `Multi Text Merge` —— 1/2 个有
- `SUPIR_Upscale` —— 1/2 个有
- `Text` —— 1/2 个有
- `VAEEncode` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 22.5 | - | 2 | 89% |
| Prompt 约束强度(CFG) | 4 | - | 2 | 50% |
| 采样算法 | dpmpp_sde | - | 2 | 50% |
| 调度器 | karras | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 640 | - | 2 | 80% |
| 高度 | 768 | - | 2 | 67% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 22.5，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 4，样本不足，未给区间，2 个样本
- 采样算法 最常用 dpmpp_sde，2 个样本，一致性 50%
- 调度器 最常用 karras，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 640，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- 高度 中位数 768，样本不足，未给区间，2 个样本
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
