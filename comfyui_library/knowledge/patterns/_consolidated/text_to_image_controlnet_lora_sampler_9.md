---
name: text_to_image_controlnet_lora_sampler_9
type: Text To Image
frequency: 3
level: strong
coverage: 0.882333
common_nodes: [CLIPTextEncode, ConditioningZeroOut, ControlNetLoader, DualCLIPLoader, EmptyLatentImage, FluxGuidance, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, SetUnionControlNetType, TextInput_, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX动漫线稿一键上色_1935493622219603970.json, 图片生成/图生图/动漫线稿图一键上色_1914670880616841217.json, 图片生成/文生图/pose 姿态 flux版本_1897223021747195906.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_lora_sampler_9

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/FLUX动漫线稿一键上色_1935493622219603970.json、图片生成/图生图/动漫线稿图一键上色_1914670880616841217.json、图片生成/文生图/pose 姿态 flux版本_1897223021747195906.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `ControlNetLoader`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `SetUnionControlNetType`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AnimeLineArtPreprocessor` —— 2/3 个有
- `ControlNetApplySD3` —— 2/3 个有
- `Image Comparer (rgthree)` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `LayerUtility: TextJoin` —— 2/3 个有
- `RH_Translator` —— 2/3 个有
- `ControlNetApplyAdvanced` —— 1/3 个有
- `LatentUpscaleBy` —— 1/3 个有
- `OpenposePreprocessor` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.8 | 0.75 - 0.8 | 3 | 97% |
| 采样步数 | 25 | 20 - 25 | 3 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | normal | - | 3 | 67% |
| 重绘幅度 | 1 | 0.6 - 1 | 3 | 78% |
| 宽度 | 768 | 768 - 768 | 3 | 100% |
| 高度 | 1024 | 1024 - 1248 | 3 | 90% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.8，观测区间 0.75 - 0.8，3 个样本，取值集中（一致性 97%）
- 采样步数 中位数 25，观测区间 20 - 25，3 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 normal，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 0.6 - 1，3 个样本
- 宽度 中位数 768，观测区间 768 - 768，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1248，3 个样本，取值集中（一致性 90%）
