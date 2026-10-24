---
name: image_to_image_sampler_vae_34
type: Image To Image
frequency: 2
level: weak
coverage: 0.605
common_nodes: [CFGNorm, CLIPLoader, DWPreprocessor, EmptySD3LatentImage, GetImageSize, GetNode, ImageScaleToTotalPixels, ImageStitch, KSampler, LoadImage, ModelSamplingAuraFlow, NunchakuQwenImageDiTLoader, PreviewImage, SaveImage, SetNode, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/双节棍版Qwen-Image模型2509多图编辑_1976884280855085057.json, 图片生成/图生图/双节棍版千问编辑模型_1987197398025965570.json]
source: knowledge_consolidation
---

# image_to_image_sampler_vae_34

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/双节棍版Qwen-Image模型2509多图编辑_1976884280855085057.json、图片生成/图生图/双节棍版千问编辑模型_1987197398025965570.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：60%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `DWPreprocessor`
- `EmptySD3LatentImage`
- `GetImageSize`
- `GetNode`
- `ImageScaleToTotalPixels`
- `ImageStitch`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `NunchakuQwenImageDiTLoader`
- `PreviewImage`
- `SaveImage`
- `SetNode`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Text Multiline` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 50 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 4 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 50，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
