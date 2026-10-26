---
name: image_to_image_sampler_clip_unet_108
type: Image To Image
frequency: 4
level: strong
coverage: 0.8875
common_nodes: [CLIPTextEncode, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/15.tonnie-kontext局部重绘2_1997554640071901186.json, 图片生成/图生图/8.tonnie-kontext官方工作流_1997531205258121218.json, 图片生成/图生图/Flux1-kontext图像转绘--低多边形风格_1948042005027913729.json, 图片生成/图生图/flux kontext 局部重绘（ inpainting）_1962171826392776705.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_108

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/15.tonnie-kontext局部重绘2_1997554640071901186.json、图片生成/图生图/8.tonnie-kontext官方工作流_1997531205258121218.json、图片生成/图生图/Flux1-kontext图像转绘--低多边形风格_1948042005027913729.json、图片生成/图生图/flux kontext 局部重绘（ inpainting）_1962171826392776705.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 3/4 个有
- `DifferentialDiffusion` —— 2/4 个有
- `FluxKontextImageScale` —— 2/4 个有
- `Kontext Inpainting Conditioning` —— 2/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `ModelSamplingFlux` —— 2/4 个有
- `ImageConcanate` —— 1/4 个有
- `ImageStitch` —— 1/4 个有
- `MZ_Flux1PartialLoad_Patch` —— 1/4 个有
- `Mask Fill Holes` —— 1/4 个有
- `MaskBlur+` —— 1/4 个有
- `easy imageConcat` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 10 - 20 | 4 | 75% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | beta | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 10 - 20，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
