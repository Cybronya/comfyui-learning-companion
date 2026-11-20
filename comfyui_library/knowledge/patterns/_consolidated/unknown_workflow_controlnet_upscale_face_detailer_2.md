---
name: unknown_workflow_controlnet_upscale_face_detailer_2
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.9154
common_nodes: [BNK_CLIPTextEncodeAdvanced, CLIPSetLastLayer, CheckpointLoaderSimple, ControlNetLoader, DF_Image_scale_to_side, FaceDetailer, KSamplerAdvanced //Inspire, LineArtPreprocessor, LoadImage, SAMLoader, SaveImage, UltralyticsDetectorProvider, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, WD14Tagger|pysssss]
problems: []
missing: []
members: [图片生成/图生图/【从二次元到现实】动漫转真人_1926848322751897601.json, 图片生成/图生图/一键真实人物转成卡通动漫形象 真人转动漫_1996751947497623553.json, 图片生成/图生图/动漫活人【一秒切换动漫→现实】_1909573083613622274.json, 图片生成/图生图/动漫转真人_1895406663535362050.json, 图片生成/图生图/动漫转真人_1900359506700939265.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_upscale_face_detailer_2

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/【从二次元到现实】动漫转真人_1926848322751897601.json、图片生成/图生图/一键真实人物转成卡通动漫形象 真人转动漫_1996751947497623553.json、图片生成/图生图/动漫活人【一秒切换动漫→现实】_1909573083613622274.json、图片生成/图生图/动漫转真人_1895406663535362050.json、图片生成/图生图/动漫转真人_1900359506700939265.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 5 个 workflow 都包含：
- `BNK_CLIPTextEncodeAdvanced`
- `CLIPSetLastLayer`
- `CheckpointLoaderSimple`
- `ControlNetLoader`
- `DF_Image_scale_to_side`
- `FaceDetailer`
- `KSamplerAdvanced //Inspire`
- `LineArtPreprocessor`
- `LoadImage`
- `SAMLoader`
- `SaveImage`
- `UltralyticsDetectorProvider`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `WD14Tagger|pysssss`

**可变部分**（部分 workflow 才有）：
- `Upscale by Factor with Model (WLSH)` —— 4/5 个有
- `ACN_AdvancedControlNetApply` —— 3/5 个有
- `CR Latent Batch Size` —— 3/5 个有
- `ControlNetApplyAdvanced` —— 2/5 个有
- `Image Comparer (rgthree)` —— 2/5 个有
- `ImageScaleToTotalPixels` —— 2/5 个有
- `ImageSmartSharpen+` —— 2/5 个有
- `LoraLoader` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `ReActorFaceSwap` —— 2/5 个有
- `ImageUpscaleWithModel` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 5 | 100% |
| Prompt 约束强度(CFG) | 25 | 25 - 40 | 5 | 76% |
| 采样算法 | 4.5 | 4.5 - 8 | 5 | 71% |
| 调度器 | euler | - | 5 | 100% |
| 重绘幅度 | normal | - | 5 | 100% |
| ControlNet 权重 | 1 | 1 - 1 | 5 | 100% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，5 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 25，观测区间 25 - 40，5 个样本
- 采样算法 中位数 4.5，观测区间 4.5 - 8，5 个样本
- 调度器 最常用 euler，5 个样本，一致性 100%
- 重绘幅度 最常用 normal，5 个样本，一致性 100%
- ControlNet 权重 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 40，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
