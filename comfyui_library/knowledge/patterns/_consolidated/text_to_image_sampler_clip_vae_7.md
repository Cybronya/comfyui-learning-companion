---
name: text_to_image_sampler_clip_vae_7
type: Text To Image
frequency: 16
level: moderate
coverage: 0.903937
common_nodes: [CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/图生图/潜空间放大_1836393548236353537.json, 图片生成/文生图/03.混元模型_文生图_1991131442067648514.json, 图片生成/文生图/0728-8_2084094584849780737.json, 图片生成/文生图/0803-2-1_2084239294272729089.json, 图片生成/文生图/0803-2_2084192746373468161.json, 图片生成/文生图/1.文生图基础0609_2064914782632890370.json, 图片生成/文生图/20260528_小易第二课_图像放大对比【成功】_2059554361151418370.json, 图片生成/文生图/AI真人短剧风格 _ SDXL电影级写真 _ 4倍超分高清修复 _ 一键出片_2074013871483998209.json, 图片生成/文生图/FLUX Krea 图生图高清放大_1960144611694030850.json, 图片生成/文生图/FLUX文生图+三种图片高清放大组_2075176156214677505.json, 图片生成/文生图/Flux文生图+三种图片高清放大组（Supir放大+图像通过模型放大+Latent放大）_1985297339466326018.json, 图片生成/文生图/Flux文生图+三种图片高清放大（Supir放大+图像通过模型放大+Latent放大）_2002988961075195905.json, 图片生成/文生图/Flux文生图+三种放大组_1989259967058374657.json, 图片生成/文生图/Krea+SDXL 登峰造极的胶片写实风_1975059549734481921.json, 图片生成/文生图/工作流基础篇-8-FLUX文生图+三种图片高清放大组_2016402394782900226.json, 图片生成/文生图/文生图后可选3种放大变清晰_2106549757798871041.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_7

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/图生图/潜空间放大_1836393548236353537.json、图片生成/文生图/03.混元模型_文生图_1991131442067648514.json、图片生成/文生图/0728-8_2084094584849780737.json、图片生成/文生图/0803-2-1_2084239294272729089.json、图片生成/文生图/0803-2_2084192746373468161.json…）

- **类型**：Text To Image
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 16 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `ImageUpscaleWithModel` —— 10/16 个有
- `UpscaleModelLoader` —— 10/16 个有
- `VAELoader` —— 10/16 个有
- `CheckpointLoaderSimple` —— 9/16 个有
- `Image Comparer (rgthree)` —— 9/16 个有
- `VAEEncode` —— 9/16 个有
- `DualCLIPLoader` —— 8/16 个有
- `ImageScaleBy` —— 7/16 个有
- `LatentUpscaleBy` —— 7/16 个有
- `UNETLoader` —— 7/16 个有
- `CLIPTextEncodeFlux` —— 6/16 个有
- `DF_Text_Box` —— 6/16 个有
- `FluxLoraLoader` —— 6/16 个有
- `SUPIR_Upscale` —— 6/16 个有
- `PreviewImage` —— 3/16 个有
- `FluxGuidance` —— 1/16 个有
- `NunchakuFluxDiTLoader` —— 1/16 个有
- `RH_Translator` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 20 - 30 | 16 | 86% |
| Prompt 约束强度(CFG) | 5.5 | 1 - 8 | 16 | 29% |
| 采样算法 | dpmpp_2m | - | 16 | 56% |
| 调度器 | sgm_uniform | - | 16 | 44% |
| 重绘幅度 | 0.8 | 0.25 - 1 | 16 | 61% |
| 宽度 | 768 | 512 - 1024 | 16 | 79% |
| 高度 | 1024 | 512 - 1280 | 16 | 71% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 20 - 30，16 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 中位数 5.5，观测区间 1 - 8，16 个样本，取值分散，一致性仅 29%
- 采样算法 最常用 dpmpp_2m，16 个样本，一致性 56%
- 调度器 最常用 sgm_uniform，16 个样本，一致性 44%
- 重绘幅度 中位数 0.8，观测区间 0.25 - 1，16 个样本
- 宽度 中位数 768，观测区间 512 - 1024，16 个样本
- 高度 中位数 1024，观测区间 512 - 1280，16 个样本
