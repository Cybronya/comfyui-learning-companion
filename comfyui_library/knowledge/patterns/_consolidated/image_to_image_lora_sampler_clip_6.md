---
name: image_to_image_lora_sampler_clip_6
type: Image To Image
frequency: 3
level: strong
coverage: 0.710667
common_nodes: [CLIPLoader, CLIPTextEncode, Canny, DepthAnything_V2, DownloadAndLoadDepthAnythingV2Model, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, MiDaS-NormalMapPreprocessor]
members: [图片生成/文生图/1960239683160715266.json, 图片生成/文生图/1960550214228672513.json, 图片生成/文生图/1961145405088186369.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_6

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1960239683160715266.json、图片生成/文生图/1960550214228672513.json、图片生成/文生图/1961145405088186369.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：71%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Canny`
- `DepthAnything_V2`
- `DownloadAndLoadDepthAnythingV2Model`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ControlNetApplyAdvanced` —— 2/3 个有
- `ControlNetLoader` —— 2/3 个有
- `ImageScaleToTotalPixels` —— 2/3 个有
- `DWPreprocessor` —— 1/3 个有
- `ImpactSwitch` —— 1/3 个有
- `Int` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `MiDaS-NormalMapPreprocessor` —— 1/3 个有
- `OpenposePreprocessor` —— 1/3 个有
- `ReferenceLatent` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 22 | 3 | 95% |
| Prompt 约束强度(CFG) | 2.5 | 2.5 - 2.5 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| ControlNet 权重 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 22，3 个样本，取值集中（一致性 95%）
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 2.5 - 2.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2、MiDaS-NormalMapPreprocessor
