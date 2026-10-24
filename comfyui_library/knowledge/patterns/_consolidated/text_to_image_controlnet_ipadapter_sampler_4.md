---
name: text_to_image_controlnet_ipadapter_sampler_4
type: Text To Image
frequency: 2
level: weak
coverage: 0.87
common_nodes: [AIO_Preprocessor, CLIPTextEncode, CannyEdgePreprocessor, CheckpointLoaderSimple, ConstrainImage|pysssss, ControlNetApply, ControlNetLoader, ConvertGreyscaleNode, EmptyLatentImage, GetImageSize+, IPAdapterAdvanced, IPAdapterUnifiedLoader, KSampler, LoadImage, PreviewImage, SaveImage, ShowText|pysssss, VAEDecode, WD14Tagger|pysssss]
problems: []
missing: []
members: [图片生成/图生图/实景真人转动漫风格丨导入图片一键生成_1908441898703593473.json, 图片生成/图生图/真人动漫风格转绘_1908387513273360385.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_ipadapter_sampler_4

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/实景真人转动漫风格丨导入图片一键生成_1908441898703593473.json、图片生成/图生图/真人动漫风格转绘_1908387513273360385.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPTextEncode`
- `CannyEdgePreprocessor`
- `CheckpointLoaderSimple`
- `ConstrainImage|pysssss`
- `ControlNetApply`
- `ControlNetLoader`
- `ConvertGreyscaleNode`
- `EmptyLatentImage`
- `GetImageSize+`
- `IPAdapterAdvanced`
- `IPAdapterUnifiedLoader`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `ShowText|pysssss`
- `VAEDecode`
- `WD14Tagger|pysssss`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 1024 | - | 2 | 100% |
| ControlNet 权重 | 0.5 | - | 2 | 100% |
| 采样步数 | 30 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 7 | - | 2 | 100% |
| 采样算法 | dpmpp_2m | - | 2 | 100% |
| 调度器 | karras | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 30，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 7，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m，2 个样本，一致性 100%
- 调度器 最常用 karras，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
