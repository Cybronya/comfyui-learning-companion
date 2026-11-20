---
name: image_to_image_controlnet_sampler_clip_6
type: Image To Image
frequency: 7
level: strong
coverage: 0.950857
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ConditioningZeroOut, ControlNetApplyAdvanced, ControlNetLoader, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage, SaveImage, VAEDecode, VAEEncode, WD14Tagger|pysssss]
problems: []
missing: []
members: [图片生成/图生图/IPAdapterFaceID动漫风换脸_1937044464424882178.json, 图片生成/图生图/IPAdapterFaceID深度推算插画风换脸_1937046648038019074.json, 图片生成/图生图/IPAdapterFaceID真实感换脸_1936332844761272322.json, 图片生成/图生图/LABUBU转绘动漫游戏摄影风_1936665105587163138.json, 平台全量/IPuLID真实人像换脸_1937384110413529090.json, 平台全量/InstantID真实人像换脸_1937050033458155522.json, 平台全量/PuLID深度控制真实人像换脸_1937388891651653633.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_sampler_clip_6

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/IPAdapterFaceID动漫风换脸_1937044464424882178.json、图片生成/图生图/IPAdapterFaceID深度推算插画风换脸_1937046648038019074.json、图片生成/图生图/IPAdapterFaceID真实感换脸_1936332844761272322.json、图片生成/图生图/LABUBU转绘动漫游戏摄影风_1936665105587163138.json、平台全量/IPuLID真实人像换脸_1937384110413529090.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `WD14Tagger|pysssss`

**可变部分**（部分 workflow 才有）：
- `IPAdapterFaceID` —— 6/7 个有
- `IPAdapterUnifiedLoaderFaceID` —— 6/7 个有
- `AIO_Preprocessor` —— 5/7 个有
- `ApplyInstantID` —— 3/7 个有
- `ColorizeDepthmap` —— 3/7 个有
- `ImageInvert` —— 3/7 个有
- `InstantIDFaceAnalysis` —— 3/7 个有
- `InstantIDModelLoader` —— 3/7 个有
- `MarigoldDepthEstimation` —— 3/7 个有
- `RemapDepth` —— 3/7 个有
- `ApplyPulid` —— 1/7 个有
- `LoraLoaderModelOnly` —— 1/7 个有
- `PulidEvaClipLoader` —— 1/7 个有
- `PulidInsightFaceLoader` —— 1/7 个有
- `PulidModelLoader` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 30 | 7 | 93% |
| Prompt 约束强度(CFG) | 7 | 3.5 - 7 | 7 | 81% |
| 采样算法 | dpmpp_2m | - | 7 | 86% |
| 调度器 | karras | - | 7 | 86% |
| 重绘幅度 | 1 | 0.5 - 1 | 7 | 81% |
| ControlNet 权重 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 30，7 个样本，取值集中（一致性 93%）
- Prompt 约束强度(CFG) 中位数 7，观测区间 3.5 - 7，7 个样本，取值集中（一致性 81%）
- 采样算法 最常用 dpmpp_2m，7 个样本，一致性 86%
- 调度器 最常用 karras，7 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 0.5 - 1，7 个样本，取值集中（一致性 81%）
- ControlNet 权重 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
