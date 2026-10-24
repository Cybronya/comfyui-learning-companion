---
name: image_to_image_sampler_clip_unet_44
type: Image To Image
frequency: 8
level: strong
coverage: 0.92475
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, ReferenceLatent, SaveImage, UnetLoaderGGUF, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Body builder_1944541407313055746.json, 图片生成/图生图/Flux Kontext 360全景生成_1949689688109522946.json, 图片生成/图生图/Flux Kontext 3D环绕漫游工作流V1（可搭配Put it）_1949409132708823041.json, 图片生成/图生图/Flux Kontext Dev一句话图像编辑V3（单图）_1938371380234620929.json, 图片生成/图生图/Flux Kontext Dev一句话图像编辑V3（双图）_1938399471682387969.json, 图片生成/图生图/Flux Kontext Dev双人互动脸部一致性增强加速版V0.5_1940000386315096066.json, 图片生成/图生图/Flux Kontext Presets15种预设工作流（随机版）_1944323631671595010.json, 图片生成/文生图/Flux Kontext Presets15种提示词模板预设_1945286940809732097.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_44

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Body builder_1944541407313055746.json、图片生成/图生图/Flux Kontext 360全景生成_1949689688109522946.json、图片生成/图生图/Flux Kontext 3D环绕漫游工作流V1（可搭配Put it）_1949409132708823041.json、图片生成/图生图/Flux Kontext Dev一句话图像编辑V3（单图）_1938371380234620929.json、图片生成/图生图/Flux Kontext Dev一句话图像编辑V3（双图）_1938399471682387969.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageStitch` —— 7/8 个有
- `ImageConcatMulti` —— 5/8 个有
- `LoraLoaderModelOnly` —— 5/8 个有
- `TeaCache` —— 5/8 个有
- `ShowText|pysssss` —— 4/8 个有
- `ImageConcanate` —— 3/8 个有
- `LoadKontextPresets` —— 3/8 个有
- `MagCache` —— 3/8 个有
- `PreviewAny` —— 3/8 个有
- `RH_Captioner` —— 3/8 个有
- `RH_Translator` —— 3/8 个有
- `Text Multiline` —— 3/8 个有
- `CR Prompt Text` —— 2/8 个有
- `LoadImageOutput` —— 2/8 个有
- `PanoramaViewerNode` —— 2/8 个有
- `PreviewImage` —— 2/8 个有
- `ShowText` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 28 | 8 | 84% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 28，8 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
