---
name: image_to_image_inpaint_sampler_clip_14
type: Image To Image
frequency: 2
level: weak
coverage: 0.6715
common_nodes: [CLIPLoader, CLIPTextEncode, GetNode, GrowMaskWithBlur, ImageCompositeMasked, ImageCrop, ImageScale, ImageToMask, InpaintModelConditioning, KSampler, LoadImage, Mask Crop Region, MaskToImage, SaveImage, SetNode, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/【精准手部修复】手部修复-局部重绘方案_1997141701527539714.json, 平台全量/wan2.1百分百成功的万能修复工作流_低像素修复_面部_手部_任意错误修复_1921116357608292353.json]
source: knowledge_consolidation
---

# image_to_image_inpaint_sampler_clip_14

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/【精准手部修复】手部修复-局部重绘方案_1997141701527539714.json、平台全量/wan2.1百分百成功的万能修复工作流_低像素修复_面部_手部_任意错误修复_1921116357608292353.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：67%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `GetNode`
- `GrowMaskWithBlur`
- `ImageCompositeMasked`
- `ImageCrop`
- `ImageScale`
- `ImageToMask`
- `InpaintModelConditioning`
- `KSampler`
- `LoadImage`
- `Mask Crop Region`
- `MaskToImage`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere3` —— 1/2 个有
- `ColorMatch` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `LayerMask: MaskPreview` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `ModelSamplingAuraFlow` —— 1/2 个有
- `ModelSamplingSD3` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `RH_Translator` —— 1/2 个有
- `ReferenceLatent` —— 1/2 个有
- `WanVideoNAG` —— 1/2 个有
- `easy float` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 12.5 | - | 2 | 80% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 50% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 0.39 | - | 2 | 8% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 12.5，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 50%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 0.39，样本不足，未给区间，2 个样本，取值分散，一致性仅 8%
- 风险：重绘幅度 观测到 0.03，低于常用下限 0.1（）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
