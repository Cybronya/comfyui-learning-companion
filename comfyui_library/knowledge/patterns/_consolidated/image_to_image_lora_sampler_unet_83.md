---
name: image_to_image_lora_sampler_unet_83
type: Image To Image
frequency: 8
level: strong
coverage: 0.9645
common_nodes: [CLIPLoader, FluxKontextMultiReferenceLatentMethod, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/再也不用C4D建模了——Qwen-Image-Edit 2511 高斯泼溅场景专用_2011599789628071937.json, 图片生成/图生图/千问2511三图编辑_2004810240099053569.json, 图片生成/图生图/千问2511双图编辑_2004808317312663553.json, 图片生成/图生图/千问Edit2511三图编辑_2004489688587141122.json, 图片生成/图生图/千问Edit2511单图编辑_2003703669726035969.json, 图片生成/图生图/千问Edit2511双图编辑_2004435367468167169.json, 图片生成/图生图/千问Qwen-edit-2511-高斯泼溅视角调整_2062810566829363201.json, 图片生成/图生图/图片去水印_2038881204849610753.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_83

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/再也不用C4D建模了——Qwen-Image-Edit 2511 高斯泼溅场景专用_2011599789628071937.json、图片生成/图生图/千问2511三图编辑_2004810240099053569.json、图片生成/图生图/千问2511双图编辑_2004808317312663553.json、图片生成/图生图/千问Edit2511三图编辑_2004489688587141122.json、图片生成/图生图/千问Edit2511单图编辑_2003703669726035969.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `FluxKontextMultiReferenceLatentMethod`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 7/8 个有
- `ImageScaleToTotalPixels` —— 7/8 个有
- `ModelSamplingAuraFlow` —— 7/8 个有
- `CR Text` —— 6/8 个有
- `Fast Groups Bypasser (rgthree)` —— 2/8 个有
- `GaussianViewer` —— 2/8 个有
- `Image Comparer (rgthree)` —— 2/8 个有
- `LoadSharpModel` —— 2/8 个有
- `PreviewImage` —— 2/8 个有
- `SharpPredict` —— 2/8 个有
- `ImageConcanate` —— 1/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/8 个有
- `WujiCleaner` —— 1/8 个有
- `easy imageScaleDownToSize` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 10 | 8 | 58% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 10，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（7/8 个样本）：Steps较低可能导致细节不足
