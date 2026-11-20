---
name: image_to_image_lora_sampler_clip_155
type: Image To Image
frequency: 3
level: strong
coverage: 0.948667
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [平台全量/Kontext人物姿态迁移_1962596062647173122.json, 平台全量/Kontext动漫转真人_1996941027942535170.json, 平台全量/浮雕转AO灰度图_2037507740679016449.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_155

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/Kontext人物姿态迁移_1962596062647173122.json、平台全量/Kontext动漫转真人_1996941027942535170.json、平台全量/浮雕转AO灰度图_2037507740679016449.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `DepthAnything_V2` —— 1/3 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 1/3 个有
- `ETN_CropImage` —— 1/3 个有
- `GetImageSize` —— 1/3 个有
- `ImageScale` —— 1/3 个有
- `ImageStitch` —— 1/3 个有
- `MathExpression|pysssss` —— 1/3 个有
- `OpenposePreprocessor` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 20 - 30 | 3 | 84% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 20 - 30，3 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
