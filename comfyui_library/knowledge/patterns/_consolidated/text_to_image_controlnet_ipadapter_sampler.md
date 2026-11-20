---
name: text_to_image_controlnet_ipadapter_sampler
type: Text To Image
frequency: 4
level: moderate
coverage: 0.77175
common_nodes: [AIO_Preprocessor, CLIPTextEncode, CM_NearestSDXLResolution, CannyEdgePreprocessor, CheckpointLoaderSimple, ControlNetApply, ControlNetLoader, ConvertGreyscaleNode, EmptyLatentImage, IPAdapterAdvanced, IPAdapterUnifiedLoader, KSampler, LayerUtility: ColorImage, LayerUtility: ImageBlend, LoadImage, PreviewImage, SaveImage, Seed (rgthree), VAEDecode]
problems: []
missing: []
members: [图片生成/图生图/任何图片提取线稿图片转线搞_1928421640558825473.json, 图片生成/图生图/任意图片(真人、动漫都可以)提取线稿图片+转线搞_2039541554855022594.json, 平台全量/Awsome Line Art V3_1867754426046775298.json, 平台全量/制 作 漫 稿_1870545575602200578.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_ipadapter_sampler

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/任何图片提取线稿图片转线搞_1928421640558825473.json、图片生成/图生图/任意图片(真人、动漫都可以)提取线稿图片+转线搞_2039541554855022594.json、平台全量/Awsome Line Art V3_1867754426046775298.json、平台全量/制 作 漫 稿_1870545575602200578.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 4 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPTextEncode`
- `CM_NearestSDXLResolution`
- `CannyEdgePreprocessor`
- `CheckpointLoaderSimple`
- `ControlNetApply`
- `ControlNetLoader`
- `ConvertGreyscaleNode`
- `EmptyLatentImage`
- `IPAdapterAdvanced`
- `IPAdapterUnifiedLoader`
- `KSampler`
- `LayerUtility: ColorImage`
- `LayerUtility: ImageBlend`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `Seed (rgthree)`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `CR Simple Image Compare` —— 3/4 个有
- `CR Text Concatenate` —— 3/4 个有
- `GetNode` —— 3/4 个有
- `ImageBatchMultiple+` —— 3/4 个有
- `SetNode` —— 3/4 个有
- `ShowText|pysssss` —— 3/4 个有
- `WD14Tagger|pysssss` —— 3/4 个有
- `BiRefNet_Hugo` —— 2/4 个有
- `ImageResize+` —— 2/4 个有
- `ImageResizeKJ` —— 2/4 个有
- `workflow>BiRefNet` —— 2/4 个有
- `Any Switch (rgthree)` —— 1/4 个有
- `DeepTranslatorTextNode` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.525 | 0.5 - 0.55 | 4 | 95% |
| 采样步数 | 30 | 30 - 30 | 4 | 100% |
| Prompt 约束强度(CFG) | 7 | 7 - 7 | 4 | 100% |
| 采样算法 | dpmpp_2m | - | 4 | 100% |
| 调度器 | karras | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 1024 | 1 - 1024 | 3 | 29% |
| 高度 | 1024 | 512 - 1024 | 3 | 72% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.525，观测区间 0.5 - 0.55，4 个样本，取值集中（一致性 95%）
- 采样步数 中位数 30，观测区间 30 - 30，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 7，观测区间 7 - 7，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m，4 个样本，一致性 100%
- 调度器 最常用 karras，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1 - 1024，3 个样本，取值分散，一致性仅 29%
- 高度 中位数 1024，观测区间 512 - 1024，3 个样本
