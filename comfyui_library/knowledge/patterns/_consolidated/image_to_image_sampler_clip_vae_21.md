---
name: image_to_image_sampler_clip_vae_21
type: Image To Image
frequency: 7
level: strong
coverage: 0.929571
common_nodes: [CLIPTextEncode, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, ReferenceLatent, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Kontext去水印史上最强去除水印——水印移除King（watermark killer）_1941296156943216642.json, 图片生成/图生图/Kontext图像万能编辑_1962166621970305026.json, 图片生成/图生图/Kontext图像编辑_1957981327398203394.json, 图片生成/图生图/Kontext图片去水印_2050191399424933890.json, 图片生成/图生图/Kontext基础编辑工作流_1948946546302824449.json, 图片生成/图生图/Kontext开源版双图融合工作流_1941885913607913473.json, 图片生成/图生图/Kontext智能移除_1943132802625781761.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_21

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Kontext去水印史上最强去除水印——水印移除King（watermark killer）_1941296156943216642.json、图片生成/图生图/Kontext图像万能编辑_1962166621970305026.json、图片生成/图生图/Kontext图像编辑_1957981327398203394.json、图片生成/图生图/Kontext图片去水印_2050191399424933890.json、图片生成/图生图/Kontext基础编辑工作流_1948946546302824449.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 6/7 个有
- `FluxKontextImageScale` —— 6/7 个有
- `SaveImage` —— 6/7 个有
- `UNETLoader` —— 6/7 个有
- `DeepTranslatorTextNode` —— 4/7 个有
- `PreviewImage` —— 4/7 个有
- `Image Comparer (rgthree)` —— 2/7 个有
- `ImageStitch` —— 2/7 个有
- `NunchakuFluxDiTLoader` —— 2/7 个有
- `CR Text` —— 1/7 个有
- `CR Text Input Switch (4 way)` —— 1/7 个有
- `CompressImages` —— 1/7 个有
- `ImageAndMaskPreview` —— 1/7 个有
- `LayerUtility: ImageScaleRestore V2` —— 1/7 个有
- `LoraLoader` —— 1/7 个有
- `SetLatentNoiseMask` —— 1/7 个有
- `easy imageColorMatch` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 7 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 86% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 86%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
