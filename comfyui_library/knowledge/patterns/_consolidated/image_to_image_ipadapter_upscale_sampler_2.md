---
name: image_to_image_ipadapter_upscale_sampler_2
type: Image To Image
frequency: 3
level: strong
coverage: 0.952333
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, DF_Text_Box, IPAdapterFaceID, IPAdapterUnifiedLoaderFaceID, ImageResize+, ImageUpscaleWithModel, KSampler, LoadImage, SaveImage, VAEDecode, VAEEncode, VAELoader, WD14Tagger|pysssss]
problems: []
missing: []
members: [平台全量/漫改头像_1778020328258211842.json, 平台全量/漫画头像_1778053011847843841.json, 平台全量/秒生成漫画韩漫系头像工作流_1954376275756511233.json]
source: knowledge_consolidation
---

# image_to_image_ipadapter_upscale_sampler_2

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/漫改头像_1778020328258211842.json、平台全量/漫画头像_1778053011847843841.json、平台全量/秒生成漫画韩漫系头像工作流_1954376275756511233.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `DF_Text_Box`
- `IPAdapterFaceID`
- `IPAdapterUnifiedLoaderFaceID`
- `ImageResize+`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `WD14Tagger|pysssss`

**可变部分**（部分 workflow 才有）：
- `RepeatLatentBatch` —— 2/3 个有
- `Text Concatenate` —— 2/3 个有
- `UpscaleModelLoader` —— 2/3 个有
- `Concat Text _O` —— 1/3 个有
- `ControlNetApplyAdvanced` —— 1/3 个有
- `ControlNetLoader` —— 1/3 个有
- `LineArtPreprocessor` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有
- `Upscale Model Loader` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.7 | - | 1 | 100% |
| 采样步数 | 25 | 20 - 25 | 3 | 90% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 3 | 100% |
| 采样算法 | euler_ancestral | - | 3 | 100% |
| 调度器 | normal | - | 3 | 100% |
| 重绘幅度 | 0.4 | 0.4 - 0.7 | 3 | 72% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 20 - 25，3 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，3 个样本，一致性 100%
- 调度器 最常用 normal，3 个样本，一致性 100%
- 重绘幅度 中位数 0.4，观测区间 0.4 - 0.7，3 个样本
