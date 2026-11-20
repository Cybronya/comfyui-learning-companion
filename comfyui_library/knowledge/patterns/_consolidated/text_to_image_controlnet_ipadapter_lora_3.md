---
name: text_to_image_controlnet_ipadapter_lora_3
type: Text To Image
frequency: 2
level: weak
coverage: 0.853
common_nodes: [ApplyFBCacheAndSkipBlocks, ApplyIPAdapterFlux, CLIPTextEncode, CLIPVisionLoader, ControlNetApplyAdvanced, ControlNetLoader, DualCLIPLoader, EmptyLatentImage, IPAdapterFluxLoader, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, PreviewImage, ReduxAdvanced, SaveImage, ShowText|pysssss, StyleModelLoader, Text, Text Load Line From File, UNETLoader, VAEDecode, VAELoader, easy batchAnything, easy forLoopEnd, easy forLoopStart, easy loadImagesForLoop]
problems: []
missing: []
members: [图片生成/文生图/flux批量文生图工作流_2097368126051676161.json, 图片生成/文生图/flux批量文生图工作流（自媒体批量出图专用）_1922169754801356801.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_ipadapter_lora_3

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/flux批量文生图工作流_2097368126051676161.json、图片生成/文生图/flux批量文生图工作流（自媒体批量出图专用）_1922169754801356801.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `ApplyFBCacheAndSkipBlocks`
- `ApplyIPAdapterFlux`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `IPAdapterFluxLoader`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `ReduxAdvanced`
- `SaveImage`
- `ShowText|pysssss`
- `StyleModelLoader`
- `Text`
- `Text Load Line From File`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy batchAnything`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy loadImagesForLoop`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 1 | - | 2 | 100% |
| 宽度 | 1368 | - | 2 | 100% |
| 高度 | 768 | - | 2 | 100% |
| 采样步数 | 25 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 1368，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 768，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
