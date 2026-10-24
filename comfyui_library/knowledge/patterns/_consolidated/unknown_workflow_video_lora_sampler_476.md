---
name: unknown_workflow_video_lora_sampler_476
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.4705
common_nodes: [BlockifyMask, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DWPreprocessor, DownloadAndLoadSAM2Model, DrawMaskOnImage, GetNode, GrowMask, ImageFromBatch, ImageResizeKJv2, ImageScale, KSampler, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, ModelSamplingSD3, PixelPerfectResolution, PointsEditor, PrimitiveInt, Sam2Segmentation, SetNode, TrimVideoLatent, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanAnimateToVideo, easy forLoopEnd, easy forLoopStart, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/46. 官流 animate bf16 模型 循环长视频 没有白光和频闪_1977644957609664514.json, 视频生成/图生视频/Wan2_2_14B_Animate_自动循环-动作迁移_1973652058060533761.json, 视频生成/图生视频/官方 wan22_animate 长视频生成 遮罩编辑版_1971013854891282433.json, 视频生成/图生视频/官流 wan22_animate 循环长视频的生成_1972488378526724098.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_476

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/46. 官流 animate bf16 模型 循环长视频 没有白光和频闪_1977644957609664514.json、视频生成/图生视频/Wan2_2_14B_Animate_自动循环-动作迁移_1973652058060533761.json、视频生成/图生视频/官方 wan22_animate 长视频生成 遮罩编辑版_1971013854891282433.json、视频生成/图生视频/官流 wan22_animate 循环长视频的生成_1972488378526724098.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：47%

## 共有节点

全部 4 个 workflow 都包含：
- `BlockifyMask`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DWPreprocessor`
- `DownloadAndLoadSAM2Model`
- `DrawMaskOnImage`
- `GetNode`
- `GrowMask`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `ImageScale`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `ModelSamplingSD3`
- `PixelPerfectResolution`
- `PointsEditor`
- `PrimitiveInt`
- `Sam2Segmentation`
- `SetNode`
- `TrimVideoLatent`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanAnimateToVideo`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `EG_SS_RYZH` —— 3/4 个有
- `GetImageRangeFromBatch` —— 3/4 个有
- `ImageConcatMulti` —— 3/4 个有
- `PathchSageAttentionKJ` —— 3/4 个有
- `VHS_VideoInfoLoaded` —— 3/4 个有
- `easy batchAnything` —— 3/4 个有
- `easy cleanGpuUsed` —— 3/4 个有
- `easy int` —— 3/4 个有
- `FaceMaskFromPoseKeypoints` —— 2/4 个有
- `ImageCropByMaskAndResize` —— 2/4 个有
- `Bjornulf_ShowFloat` —— 1/4 个有
- `Bjornulf_ShowInt` —— 1/4 个有
- `Bool` —— 1/4 个有
- `ImageBatch` —— 1/4 个有
- `MaskToImage` —— 1/4 个有
- `SoundFlow_TrimAudio` —— 1/4 个有
- `VHS_VideoInfo` —— 1/4 个有
- `easy convertAnything` —— 1/4 个有
- `easy ifElse` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 5 | 4 - 6 | 4 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 5，观测区间 4 - 6，4 个样本，取值集中（一致性 80%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（5/4 个样本）：Steps较低可能导致细节不足
