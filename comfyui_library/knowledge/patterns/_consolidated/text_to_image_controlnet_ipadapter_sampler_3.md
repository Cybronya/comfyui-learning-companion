---
name: text_to_image_controlnet_ipadapter_sampler_3
type: Text To Image
frequency: 2
level: weak
coverage: 0.756
common_nodes: [AIO_Preprocessor, CLIPTextEncode, CM_NearestSDXLResolution, CR Simple Image Compare, CR Text Concatenate, CannyEdgePreprocessor, CheckpointLoaderSimple, ControlNetApply, ControlNetLoader, ConvertGreyscaleNode, EmptyLatentImage, GetNode, IPAdapterAdvanced, IPAdapterUnifiedLoader, ImageBatchMultiple+, ImageResize+, KSampler, LayerUtility: ColorImage, LayerUtility: ImageBlend, LoadImage, PreviewImage, SaveImage, Seed (rgthree), SetNode, ShowText|pysssss, VAEDecode, WD14Tagger|pysssss, workflow>BiRefNet]
problems: []
missing: []
members: [图片生成/图生图/任何图片提取线稿图片转线搞_1928421640558825473.json, 图片生成/图生图/任意图片(真人、动漫都可以)提取线稿图片+转线搞_2039541554855022594.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_ipadapter_sampler_3

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/任何图片提取线稿图片转线搞_1928421640558825473.json、图片生成/图生图/任意图片(真人、动漫都可以)提取线稿图片+转线搞_2039541554855022594.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：76%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPTextEncode`
- `CM_NearestSDXLResolution`
- `CR Simple Image Compare`
- `CR Text Concatenate`
- `CannyEdgePreprocessor`
- `CheckpointLoaderSimple`
- `ControlNetApply`
- `ControlNetLoader`
- `ConvertGreyscaleNode`
- `EmptyLatentImage`
- `GetNode`
- `IPAdapterAdvanced`
- `IPAdapterUnifiedLoader`
- `ImageBatchMultiple+`
- `ImageResize+`
- `KSampler`
- `LayerUtility: ColorImage`
- `LayerUtility: ImageBlend`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `Seed (rgthree)`
- `SetNode`
- `ShowText|pysssss`
- `VAEDecode`
- `WD14Tagger|pysssss`
- `workflow>BiRefNet`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.5 | - | 2 | 100% |
| 采样步数 | 30 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 7 | - | 2 | 100% |
| 采样算法 | dpmpp_2m | - | 2 | 100% |
| 调度器 | karras | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 1 | - | 1 | 100% |
| 高度 | 512 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 30，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 7，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m，2 个样本，一致性 100%
- 调度器 最常用 karras，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
