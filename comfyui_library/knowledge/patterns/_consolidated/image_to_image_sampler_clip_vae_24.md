---
name: image_to_image_sampler_clip_vae_24
type: Image To Image
frequency: 6
level: strong
coverage: 0.801
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, ImageStitch, KSampler, LoadImage, PreviewImage, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/(自用)去水印文字效果最佳+高清无损放大_2051996438422405121.json, 图片生成/图生图/FLUX.1 Kontext [dev] 基础工作流_1938329277471330305.json, 图片生成/图生图/Kontext Dev 基础工作流ZGL_1943863852666617858.json, 图片生成/图生图/SeedVR2.5-去水印修复放大（有用）_2013859487152607234.json, 图片生成/图生图/去水印文字效果最佳+高清无损放大 zip_2052044034285285377.json, 图片生成/图生图/无损去图片水印，还原图片原本画质，ai去水印_2027795592591712258.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_24

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/(自用)去水印文字效果最佳+高清无损放大_2051996438422405121.json、图片生成/图生图/FLUX.1 Kontext [dev] 基础工作流_1938329277471330305.json、图片生成/图生图/Kontext Dev 基础工作流ZGL_1943863852666617858.json、图片生成/图生图/SeedVR2.5-去水印修复放大（有用）_2013859487152607234.json、图片生成/图生图/去水印文字效果最佳+高清无损放大 zip_2052044034285285377.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImageStitch`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `UNETLoader` —— 5/6 个有
- `SeedVR2LoadDiTModel` —— 4/6 个有
- `SeedVR2LoadVAEModel` —— 4/6 个有
- `SeedVR2VideoUpscaler` —— 4/6 个有
- `FluxKontextImageScale` —— 3/6 个有
- `ImageResize+` —— 3/6 个有
- `ImageScaleBy` —— 3/6 个有
- `easy cleanGpuUsed` —— 2/6 个有
- `EmptySD3LatentImage` —— 1/6 个有
- `HAIGC_SaveImagesToZip` —— 1/6 个有
- `ImageScale` —— 1/6 个有
- `Kontext Inpainting Conditioning` —— 1/6 个有
- `LayerUtility: ImageScaleRestore V2` —— 1/6 个有
- `NunchakuFluxDiTLoader` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
