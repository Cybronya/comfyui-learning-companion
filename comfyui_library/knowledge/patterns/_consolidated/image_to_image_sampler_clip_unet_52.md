---
name: image_to_image_sampler_clip_unet_52
type: Image To Image
frequency: 7
level: strong
coverage: 0.896286
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DetailTransfer, DualCLIPLoader, FastCanvas, FastCanvasTool, FluxGuidance, Image Comparer (rgthree), KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/(冰爷老杨)kontext万物融图进阶版_1966533540433309697.json, 图片生成/图生图/(冰爷老杨开源版)万物融图V1_1965930686555295745.json, 图片生成/图生图/Kontext万物溶图 细致打光_1974016071105687553.json, 图片生成/图生图/【电商】最强完美溶图工作流_1966387381639262209.json, 图片生成/图生图/万物融图V1（开源版）_2008480047656603649.json, 图片生成/图生图/万物融图，透明融图，玻璃融图_1965994482065903617.json, 图片生成/图生图/冰爷老杨简单溶图-有钱人版_1965783485795471362.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_52

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/(冰爷老杨)kontext万物融图进阶版_1966533540433309697.json、图片生成/图生图/(冰爷老杨开源版)万物融图V1_1965930686555295745.json、图片生成/图生图/Kontext万物溶图 细致打光_1974016071105687553.json、图片生成/图生图/【电商】最强完美溶图工作流_1966387381639262209.json、图片生成/图生图/万物融图V1（开源版）_2008480047656603649.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DetailTransfer`
- `DualCLIPLoader`
- `FastCanvas`
- `FastCanvasTool`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerMask: BiRefNetUltraV2` —— 6/7 个有
- `LayerMask: LoadBiRefNetModelV2` —— 6/7 个有
- `LoraLoaderModelOnly` —— 6/7 个有
- `Text Multiline` —— 6/7 个有
- `easy cleanGpuUsed` —— 6/7 个有
- `CR Color Panel` —— 5/7 个有
- `Text Concatenate` —— 5/7 个有
- `Seed (rgthree)` —— 4/7 个有
- `CR Text Concatenate` —— 2/7 个有
- `ImageConcatMulti` —— 1/7 个有
- `JjkText` —— 1/7 个有
- `LayerMask: RmBgUltra V2` —— 1/7 个有
- `Note _O` —— 1/7 个有
- `RHHiddenNodes` —— 1/7 个有
- `TextInput_` —— 1/7 个有
- `easy imageConcat` —— 1/7 个有
- `easy imageRemBg` —— 1/7 个有
- `easy seed` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 7 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | deis | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 deis，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
