---
name: unknown_workflow_video_lora_sampler_338
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.499571
common_nodes: [BlockifyMask, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DWPreprocessor, DrawMaskOnImage, GetImageRangeFromBatch, GetNode, GrowMask, ImageScale, KSampler, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, ModelSamplingSD3, PixelPerfectResolution, SetNode, TrimVideoLatent, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanAnimateToVideo, easy batchAnything, easy forLoopEnd, easy forLoopStart, easy int, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/SEC Wan2.2 Animate 替换循环工作流_1989236544387035137.json, 数字人/数字人/Wan2.2 Animate 循环工作流，支持长视频，支持多人_1976591232627511298.json, 视频生成/图生视频/46. 官流 animate bf16 模型 循环长视频 没有白光和频闪_1977644957609664514.json, 视频生成/图生视频/Animate人物替换，无需标点，支持长视频，多人可指定其中一个_1993140564954726401.json, 视频生成/图生视频/SEC DWWan2.2 Animate 替换循环工作流成功_1993239739520270338.json, 视频生成/图生视频/官方 wan22_animate 长视频生成 遮罩编辑版_1971013854891282433.json, 视频生成/图生视频/官流 wan22_animate 循环长视频的生成_1972488378526724098.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_338

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（数字人/数字人/SEC Wan2.2 Animate 替换循环工作流_1989236544387035137.json、数字人/数字人/Wan2.2 Animate 循环工作流，支持长视频，支持多人_1976591232627511298.json、视频生成/图生视频/46. 官流 animate bf16 模型 循环长视频 没有白光和频闪_1977644957609664514.json、视频生成/图生视频/Animate人物替换，无需标点，支持长视频，多人可指定其中一个_1993140564954726401.json、视频生成/图生视频/SEC DWWan2.2 Animate 替换循环工作流成功_1993239739520270338.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：50%

## 共有节点

全部 7 个 workflow 都包含：
- `BlockifyMask`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DWPreprocessor`
- `DrawMaskOnImage`
- `GetImageRangeFromBatch`
- `GetNode`
- `GrowMask`
- `ImageScale`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `ModelSamplingSD3`
- `PixelPerfectResolution`
- `SetNode`
- `TrimVideoLatent`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanAnimateToVideo`
- `easy batchAnything`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy int`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `DownloadAndLoadSAM2Model` —— 6/7 个有
- `FaceMaskFromPoseKeypoints` —— 6/7 个有
- `ImageCropByMaskAndResize` —— 6/7 个有
- `PointsEditor` —— 6/7 个有
- `Sam2Segmentation` —— 6/7 个有
- `ImageFromBatch` —— 5/7 个有
- `ImageConcanate` —— 4/7 个有
- `InvertMask (segment anything)` —— 4/7 个有
- `VHS_GetImageCount` —— 4/7 个有
- `easy mathInt` —— 4/7 个有
- `CM_IntToFloat` —— 3/7 个有
- `EG_SS_RYZH` —— 3/7 个有
- `ImageResizeKJv2` —— 3/7 个有
- `PathchSageAttentionKJ` —— 3/7 个有
- `PrimitiveInt` —— 3/7 个有
- `SeCModelLoader` —— 3/7 个有
- `SeCVideoSegmentation` —— 3/7 个有
- `Text Multiline` —— 3/7 个有
- `VHS_VideoInfoLoaded` —— 3/7 个有
- `easy cleanGpuUsed` —— 3/7 个有
- `ImageConcatMulti` —— 2/7 个有
- `JWInteger` —— 2/7 个有
- `PreviewImage` —— 2/7 个有
- `easy ifElse` —— 2/7 个有
- `Bool` —— 1/7 个有
- `CM_FloatToInt` —— 1/7 个有
- `PrimitiveStringMultiline` —— 1/7 个有
- `Sa2VANodeTpl` —— 1/7 个有
- `SimpleComparison+` —— 1/7 个有
- `SoundFlow_TrimAudio` —— 1/7 个有
- `VHS_VideoInfo` —— 1/7 个有
- `easy convertAnything` —— 1/7 个有
- `easy float` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 6 | 7 | 83% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 6，7 个样本，取值集中（一致性 83%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（11/7 个样本）：Steps较低可能导致细节不足
