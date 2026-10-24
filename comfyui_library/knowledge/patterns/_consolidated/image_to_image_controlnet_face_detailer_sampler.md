---
name: image_to_image_controlnet_face_detailer_sampler
type: Image To Image
frequency: 7
level: strong
coverage: 0.894857
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ConditioningConcat, ControlNetApplyAdvanced, DepthAnythingPreprocessor, FaceDetailer, ImageScaleToTotalPixels, KSampler, LoadImage, PreviewImage, SAMLoader, SaveImage, SeedSelector, Text Concatenate, TilePreprocessor, UltralyticsDetectorProvider, VAEDecode, VAEEncode, easy imageColorMatch, ttN text]
problems: []
missing: []
members: [图片生成/图生图/AI应用【动漫变真人】轻松cos写真照_1949108565693407233.json, 图片生成/图生图/XL+joy+cn一键动漫转真人摄影风格_1933347414889930753.json, 图片生成/图生图/一键动漫转真人摄影风格_2048962797861609473.json, 图片生成/图生图/动漫转真人摄影风格｜一键生图系列_1907351173031202818.json, 图片生成/图生图/风格迁移_动漫转真人_2001468357331349505.json, 图片生成/文生图/一键动漫转真人摄影风格_1902386654504497154.json, 图片生成/文生图/一键动漫转真人摄影风格_2046774353353773057.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_face_detailer_sampler

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/AI应用【动漫变真人】轻松cos写真照_1949108565693407233.json、图片生成/图生图/XL+joy+cn一键动漫转真人摄影风格_1933347414889930753.json、图片生成/图生图/一键动漫转真人摄影风格_2048962797861609473.json、图片生成/图生图/动漫转真人摄影风格｜一键生图系列_1907351173031202818.json、图片生成/图生图/风格迁移_动漫转真人_2001468357331349505.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ConditioningConcat`
- `ControlNetApplyAdvanced`
- `DepthAnythingPreprocessor`
- `FaceDetailer`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `SAMLoader`
- `SaveImage`
- `SeedSelector`
- `Text Concatenate`
- `TilePreprocessor`
- `UltralyticsDetectorProvider`
- `VAEDecode`
- `VAEEncode`
- `easy imageColorMatch`
- `ttN text`

**可变部分**（部分 workflow 才有）：
- `ACN_ControlNet++LoaderSingle` —— 6/7 个有
- `CLIPTextEncodeA1111` —— 6/7 个有
- `OpenposePreprocessor` —— 6/7 个有
- `WD14Tagger|pysssss` —— 6/7 个有
- `easy cleanGpuUsed` —— 6/7 个有
- `AnyLineArtPreprocessor_aux` —— 1/7 个有
- `Bjornulf_ShowJson` —— 1/7 个有
- `ControlNetLoader` —— 1/7 个有
- `Joy_caption_two` —— 1/7 个有
- `Joy_caption_two_load` —— 1/7 个有
- `LoraLoader` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.2 | 0.2 - 0.2 | 7 | 100% |
| 采样步数 | 30 | 30 - 30 | 7 | 100% |
| Prompt 约束强度(CFG) | 3 | 3 - 3 | 7 | 100% |
| 采样算法 | dpmpp_2m | - | 7 | 100% |
| 调度器 | karras | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| LoRA 模型强度 | 0.8 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.2，观测区间 0.2 - 0.2，7 个样本，取值集中（一致性 100%）
- 采样步数 中位数 30，观测区间 30 - 30，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 3，观测区间 3 - 3，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m，7 个样本，一致性 100%
- 调度器 最常用 karras，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
