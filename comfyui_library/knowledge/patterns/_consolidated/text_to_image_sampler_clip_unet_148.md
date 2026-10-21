---
name: text_to_image_sampler_clip_unet_148
type: Text To Image
frequency: 2
level: weak
coverage: 0.8255
common_nodes: [AIO_Preprocessor, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, Flex2Conditioner, KSampler, LoadImage, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [LayerUtility: ImageScaleByAspectRatio V2]
members: [图片生成/文生图/1920256323848437761.json, 图片生成/文生图/1927357381687283713.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_148

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1920256323848437761.json、图片生成/文生图/1927357381687283713.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `Flex2Conditioner`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DeepTranslatorTextNode` —— 1/2 个有
- `Florence2ModelLoader` —— 1/2 个有
- `Florence2Run` —— 1/2 个有
- `ImageScaleToTotalPixels` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1184 | - | 2 | 86% |
| 高度 | 960 | - | 2 | 93% |
| 采样步数 | 28 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | deis | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 0.8 | - | 2 | 75% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1184，样本不足，未给区间，2 个样本，取值集中（一致性 86%）
- 高度 中位数 960，样本不足，未给区间，2 个样本，取值集中（一致性 93%）
- 采样步数 中位数 28，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 deis，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 0.8，样本不足，未给区间，2 个样本
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
