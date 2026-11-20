---
name: unknown_workflow_controlnet_sampler_vae_2
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.894
common_nodes: [AIO_Preprocessor, Control Net Stacker, ControlNetLoader, Efficient Loader, ImageConcanate, KSampler (Efficient), LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage, SaveImage, VAEEncode, WD14Tagger|pysssss]
problems: []
missing: []
members: [图片生成/图生图/DW+IPAdapter+人形细化-真人转动漫_1930465046667890690.json, 图片生成/图生图/DW+IPAdapter+脸形细化-真人转3D_1930472245070827522.json, 图片生成/图生图/DW+LineArt+IPAdapter+面部细化-真人转3D_1930501237202960385.json, 图片生成/图生图/DW+LineArt+IPAdapter-真人转动漫_1930096085539393538.json, 图片生成/图生图/DW+LineArt+IPAdapter-真人转动漫游戏_1930107060636041218.json, 图片生成/图生图/DW+LineArt-动漫转helloIP3D_1930117626280972289.json, 图片生成/图生图/DW姿态控制+面部细化-真人转动漫_1928308693547532290.json, 图片生成/图生图/IPAdapter+脸形细化-真人转3D_1930521704227880961.json, 平台全量/DW+LineArt+IPAdapter+面部细化-真人转儿童插画绘本_1930876679156072450.json, 平台全量/DW+LineArt+IPAdapter+面部细化-真人转动漫二次元_1930871161729822722.json, 平台全量/DW+LineArt+IPAdapterFaceID+面部细化-真人转日漫_1930881537016049666.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_sampler_vae_2

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/DW+IPAdapter+人形细化-真人转动漫_1930465046667890690.json、图片生成/图生图/DW+IPAdapter+脸形细化-真人转3D_1930472245070827522.json、图片生成/图生图/DW+LineArt+IPAdapter+面部细化-真人转3D_1930501237202960385.json、图片生成/图生图/DW+LineArt+IPAdapter-真人转动漫_1930096085539393538.json、图片生成/图生图/DW+LineArt+IPAdapter-真人转动漫游戏_1930107060636041218.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 11 个 workflow 都包含：
- `AIO_Preprocessor`
- `Control Net Stacker`
- `ControlNetLoader`
- `Efficient Loader`
- `ImageConcanate`
- `KSampler (Efficient)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `VAEEncode`
- `WD14Tagger|pysssss`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionLoader` —— 10/11 个有
- `IPAdapterModelLoader` —— 10/11 个有
- `IPAdapterAdvanced` —— 8/11 个有
- `MaskToImage` —— 8/11 个有
- `UltralyticsDetectorProvider` —— 8/11 个有
- `SAMLoader` —— 6/11 个有
- `DetailerForEach` —— 4/11 个有
- `FaceDetailer` —— 4/11 个有
- `MaskToSEGS` —— 4/11 个有
- `BboxDetectorSEGS` —— 3/11 个有
- `SAMDetectorCombined` —— 3/11 个有
- `BboxDetectorCombined_v2` —— 2/11 个有
- `IPAdapterFaceID` —— 2/11 个有
- `IPAdapterInsightFaceLoader` —— 2/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 25 | 11 | 100% |
| Prompt 约束强度(CFG) | 7 | 7 - 7 | 11 | 100% |
| 采样算法 | dpmpp_2m | - | 11 | 100% |
| 调度器 | karras | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 25，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 7，观测区间 7 - 7，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m，11 个样本，一致性 100%
- 调度器 最常用 karras，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
