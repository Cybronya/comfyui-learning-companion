---
name: image_to_image_sampler_unet_vae_59
type: Image To Image
frequency: 2
level: weak
coverage: 0.733
common_nodes: [AnySwitch, Anything Everywhere, CLIPLoader, EmptyLatentImage, GetNode, Image Comparer (rgthree), ImageScaleToTotalPixels, KSampler, LoadImage, QwenImage21Cache, ResolutionSelector, SaveImage, SetNode, Text Multiline, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAEEncode, VAELoader, 孤海注释, 忽略多组孤海]
problems: []
missing: []
members: [图片生成/图生图/Qwen Image2.1 重磅发布：文生图与图像编辑综合工作流，开启高效创作新纪元_2106010163718221826.json, 图片生成/文生图/Qwen Image2.1文生图·图像编辑综合工作流 效果出色【AI小王子】_2104838096306130945.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_59

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Qwen Image2.1 重磅发布：文生图与图像编辑综合工作流，开启高效创作新纪元_2106010163718221826.json、图片生成/文生图/Qwen Image2.1文生图·图像编辑综合工作流 效果出色【AI小王子】_2104838096306130945.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：73%

## 共有节点

全部 2 个 workflow 都包含：
- `AnySwitch`
- `Anything Everywhere`
- `CLIPLoader`
- `EmptyLatentImage`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `SetNode`
- `Text Multiline`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `孤海注释`
- `忽略多组孤海`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 1024 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
