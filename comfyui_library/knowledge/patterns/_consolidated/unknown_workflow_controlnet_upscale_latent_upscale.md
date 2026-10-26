---
name: unknown_workflow_controlnet_upscale_latent_upscale
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.750333
common_nodes: [BNK_CLIPTextEncodeAdvanced, BboxDetectorSEGS, CLIPSetLastLayer, CheckpointLoaderSimple, ConstrainImage|pysssss, ControlNetApplyAdvanced, DWPreprocessor, DetailerForEach, DiffControlNetLoader, GetNode, ImpactSegsAndMask, IterativeLatentUpscale, KSampler //Inspire, LineArtPreprocessor, LoadImage, SAMDetectorCombined, SAMLoader, SaveImage, SetNode, ShowText|pysssss, UltralyticsDetectorProvider, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, WD14Tagger|pysssss]
problems: []
missing: []
members: [图片生成/反推提示词/反推关键词，一键动漫转真人_1906322162880548866.json, 图片生成/图生图/一键动漫转真人_1923349289450262530.json, 图片生成/图生图/一键动漫转真人（SD1.5）-模型效果很好_1912137373873045506.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_upscale_latent_upscale

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/反推提示词/反推关键词，一键动漫转真人_1906322162880548866.json、图片生成/图生图/一键动漫转真人_1923349289450262530.json、图片生成/图生图/一键动漫转真人（SD1.5）-模型效果很好_1912137373873045506.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 3 个 workflow 都包含：
- `BNK_CLIPTextEncodeAdvanced`
- `BboxDetectorSEGS`
- `CLIPSetLastLayer`
- `CheckpointLoaderSimple`
- `ConstrainImage|pysssss`
- `ControlNetApplyAdvanced`
- `DWPreprocessor`
- `DetailerForEach`
- `DiffControlNetLoader`
- `GetNode`
- `ImpactSegsAndMask`
- `IterativeLatentUpscale`
- `KSampler //Inspire`
- `LineArtPreprocessor`
- `LoadImage`
- `SAMDetectorCombined`
- `SAMLoader`
- `SaveImage`
- `SetNode`
- `ShowText|pysssss`
- `UltralyticsDetectorProvider`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `WD14Tagger|pysssss`

**可变部分**（部分 workflow 才有）：
- `PixelKSampleUpscalerProvider` —— 2/3 个有
- `PreviewImage` —— 1/3 个有
- `RHHiddenNodes` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.9 | 0.9 - 1 | 3 | 95% |
| 采样步数 | 30 | 30 - 35 | 3 | 93% |
| Prompt 约束强度(CFG) | 7 | 7 - 7 | 3 | 100% |
| 采样算法 | dpmpp_2m | - | 3 | 100% |
| 调度器 | karras | - | 3 | 100% |
| 重绘幅度 | 0.6 | 0.6 - 0.6 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.9，观测区间 0.9 - 1，3 个样本，取值集中（一致性 95%）
- 采样步数 中位数 30，观测区间 30 - 35，3 个样本，取值集中（一致性 93%）
- Prompt 约束强度(CFG) 中位数 7，观测区间 7 - 7，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m，3 个样本，一致性 100%
- 调度器 最常用 karras，3 个样本，一致性 100%
- 重绘幅度 中位数 0.6，观测区间 0.6 - 0.6，3 个样本，取值集中（一致性 100%）
