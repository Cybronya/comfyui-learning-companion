---
name: unknown_workflow_lora_sampler_clip_269
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.456333
common_nodes: [BlockifyMask, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CreateVideo, DownloadAndLoadSAM2Model, DrawMaskOnImage, ImageFromBatch, ImageScale, KSampler, LoadImage, LoraLoaderModelOnly, PrimitiveInt, Sam2Segmentation, SaveVideo, TrimVideoLatent, UNETLoader, VAEDecode, VAELoader, WanAnimateToVideo]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/WanAnimate Native角色替换动作迁移不限时长_2074164248804159489.json, 视频生成/图生视频/video_wan2_2_14B_animate_1970998862133530625.json, 视频生成/图生视频/wan22_animate_auto_character_replace+全节点注释_2055788920813703169.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_269

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/WanAnimate Native角色替换动作迁移不限时长_2074164248804159489.json、视频生成/图生视频/video_wan2_2_14B_animate_1970998862133530625.json、视频生成/图生视频/wan22_animate_auto_character_replace+全节点注释_2055788920813703169.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：46%

## 共有节点

全部 3 个 workflow 都包含：
- `BlockifyMask`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CreateVideo`
- `DownloadAndLoadSAM2Model`
- `DrawMaskOnImage`
- `ImageFromBatch`
- `ImageScale`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveInt`
- `Sam2Segmentation`
- `SaveVideo`
- `TrimVideoLatent`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `WanAnimateToVideo`

**可变部分**（部分 workflow 才有）：
- `DrawViTPose` —— 2/3 个有
- `GetNode` —— 2/3 个有
- `GetVideoComponents` —— 2/3 个有
- `GrowMaskWithBlur` —— 2/3 个有
- `LoadVideo` —— 2/3 个有
- `ModelSamplingSD3` —— 2/3 个有
- `OnnxDetectionModelLoader` —— 2/3 个有
- `PoseAndFaceDetection` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `ComfyMathExpression` —— 1/3 个有
- `ContextWindowsManual` —— 1/3 个有
- `DWPreprocessor` —— 1/3 个有
- `GetImageSize` —— 1/3 个有
- `GrowMask` —— 1/3 个有
- `ImageBatch` —— 1/3 个有
- `ImageStitch` —— 1/3 个有
- `PixelPerfectResolution` —— 1/3 个有
- `PointsEditor` —— 1/3 个有
- `PreviewAny` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `VHS_LoadVideo` —— 1/3 个有
- `VHS_VideoInfo` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 8 | 3 | 86% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 8，3 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（4/3 个样本）：Steps较低可能导致细节不足
