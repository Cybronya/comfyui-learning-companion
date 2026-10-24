---
name: image_to_image_sampler_clip_unet_90
type: Image To Image
frequency: 5
level: strong
coverage: 0.8912
common_nodes: [CLIPTextEncode, CR SDXL Aspect Ratio, ImageResize+, KSampler, LoadImage, ModelSamplingSD3, QuadrupleCLIPLoader, RH_Captioner, SaveImage, Text Concatenate, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/HiDream-I1图生图_1915601249054425090.json, 图片生成/图生图/HiDreamFull图生图ComfyUI原生支持_1915248465113452546.json, 图片生成/图生图/hiddream图生图   高质量原生支持_1934832828377178113.json, 图片生成/文生图/图生图_1943252903802904578.json, 视频生成/文生视频/图生图   原生支持_1930884360281763841.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_90

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/HiDream-I1图生图_1915601249054425090.json、图片生成/图生图/HiDreamFull图生图ComfyUI原生支持_1915248465113452546.json、图片生成/图生图/hiddream图生图   高质量原生支持_1934832828377178113.json、图片生成/文生图/图生图_1943252903802904578.json、视频生成/文生视频/图生图   原生支持_1930884360281763841.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `CR SDXL Aspect Ratio`
- `ImageResize+`
- `KSampler`
- `LoadImage`
- `ModelSamplingSD3`
- `QuadrupleCLIPLoader`
- `RH_Captioner`
- `SaveImage`
- `Text Concatenate`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 4/5 个有
- `PrimitiveString` —— 4/5 个有
- `DeepTranslatorTextNode` —— 1/5 个有
- `EmptyImage` —— 1/5 个有
- `ImageConcatMulti` —— 1/5 个有
- `PreviewImage` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 35 | 35 - 35 | 5 | 100% |
| Prompt 约束强度(CFG) | 5 | 5 - 5 | 5 | 100% |
| 采样算法 | euler | - | 5 | 80% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 0.7 | 0.22 - 0.7 | 5 | 68% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 35，观测区间 35 - 35，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 5，观测区间 5 - 5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 80%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 0.7，观测区间 0.22 - 0.7，5 个样本
