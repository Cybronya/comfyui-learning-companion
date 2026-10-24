---
name: text_to_image_lora_sampler_clip_623
type: Text To Image
frequency: 2
level: weak
coverage: 0.6925
common_nodes: [CLIPTextEncode, CR Text, DWPreprocessor, DualCLIPLoader, EmptyLatentImage, Flex2Conditioner, GetNode, Image Comparer (rgthree), ImageScaleToTotalPixels, KSampler, LayerUtility: TextJoin, LoadImage, LoraLoaderModelOnly, PreviewImage, RH_Captioner, SaveImage, SetNode, ShowText|pysssss, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Flux最新Controlnet--Flex.2_1916356826265489409.json, 图片生成/文生图/Flux最新cn-Flex.2-depth+openpose_1916072736811323393.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_623

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Flux最新Controlnet--Flex.2_1916356826265489409.json、图片生成/文生图/Flux最新cn-Flex.2-depth+openpose_1916072736811323393.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：69%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CR Text`
- `DWPreprocessor`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `Flex2Conditioner`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LayerUtility: TextJoin`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RH_Captioner`
- `SaveImage`
- `SetNode`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DepthAnythingPreprocessor` —— 1/2 个有
- `DepthAnything_V2` —— 1/2 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 896 | - | 2 | 86% |
| 高度 | 1408 | - | 2 | 91% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 896，样本不足，未给区间，2 个样本，取值集中（一致性 86%）
- 高度 中位数 1408，样本不足，未给区间，2 个样本，取值集中（一致性 91%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
