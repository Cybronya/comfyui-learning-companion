---
name: unknown_workflow_lora_sampler_clip_312
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.4755
common_nodes: [BlockifyMask, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CreateVideo, DownloadAndLoadSAM2Model, DrawMaskOnImage, DrawViTPose, GrowMaskWithBlur, ImageFromBatch, ImageScale, KSampler, LoadImage, LoraLoaderModelOnly, OnnxDetectionModelLoader, PoseAndFaceDetection, PrimitiveInt, Sam2Segmentation, SaveVideo, TrimVideoLatent, UNETLoader, VAEDecode, VAELoader, WanAnimateToVideo]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/WanAnimate Native角色替换动作迁移不限时长_2074164248804159489.json, 视频生成/图生视频/wan22_animate_auto_character_replace+全节点注释_2055788920813703169.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_312

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/WanAnimate Native角色替换动作迁移不限时长_2074164248804159489.json、视频生成/图生视频/wan22_animate_auto_character_replace+全节点注释_2055788920813703169.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：48%

## 共有节点

全部 2 个 workflow 都包含：
- `BlockifyMask`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CreateVideo`
- `DownloadAndLoadSAM2Model`
- `DrawMaskOnImage`
- `DrawViTPose`
- `GrowMaskWithBlur`
- `ImageFromBatch`
- `ImageScale`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `PrimitiveInt`
- `Sam2Segmentation`
- `SaveVideo`
- `TrimVideoLatent`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `WanAnimateToVideo`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 1/2 个有
- `ContextWindowsManual` —— 1/2 个有
- `GetImageSize` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `GetVideoComponents` —— 1/2 个有
- `ImageStitch` —— 1/2 个有
- `LoadVideo` —— 1/2 个有
- `ModelSamplingSD3` —— 1/2 个有
- `PreviewAny` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `VHS_LoadVideo` —— 1/2 个有
- `VHS_VideoInfo` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 7 | - | 2 | 86% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | beta | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 7，样本不足，未给区间，2 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
