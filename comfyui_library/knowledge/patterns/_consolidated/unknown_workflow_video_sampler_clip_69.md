---
name: unknown_workflow_video_sampler_clip_69
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.616222
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CM_IntToFloat, GetNode, ImageResizeKJv2, Int, KSampler, LoadImage, PreviewImage, SetNode, SimpleMath+, TrimVideoLatent, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanAnimateToVideo, easy seed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/动作迁移一致性保持效果好，会保持原图场景 Wan2.2 Animate_2029801515057160193.json, 平台全量/动作迁移（一致性、表情、胸部调节，手部、胸部抖动优化版）_2010159152059912193.json, 平台全量/原图背景_动作迁移_学着视频跳舞_抖起来~_2047746991177863169.json, 平台全量/可用动作迁移+长时间35秒+低显存24G_2046254757504880642.json, 平台全量/高清动作模仿_2043926753491558401.json, 平台全量/高质量动作迁移V1.2_2037477747609571329.json, 数字人/数字人/动作模仿（Animate）支持无限时长（手指稳定、支持更高分辨率）_2032027443770429442.json, 数字人/数字人/抖音 & 快手 AI 舞蹈视频（支持胸部抖动、超清、无限时长）Animate_2033906472924483586.json, 视频生成/图生视频/3-3Piao-动作迁移（一致性、表情、手部、抖动）Wan2.2-Animate-V5_2002747679463620610.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_69

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（平台全量/动作迁移一致性保持效果好，会保持原图场景 Wan2.2 Animate_2029801515057160193.json、平台全量/动作迁移（一致性、表情、胸部调节，手部、胸部抖动优化版）_2010159152059912193.json、平台全量/原图背景_动作迁移_学着视频跳舞_抖起来~_2047746991177863169.json、平台全量/可用动作迁移+长时间35秒+低显存24G_2046254757504880642.json、平台全量/高清动作模仿_2043926753491558401.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：62%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CM_IntToFloat`
- `GetNode`
- `ImageResizeKJv2`
- `Int`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `SetNode`
- `SimpleMath+`
- `TrimVideoLatent`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanAnimateToVideo`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `GetImageRangeFromBatch` —— 8/9 个有
- `VHS_GetImageCount` —— 8/9 个有
- `VHS_VideoInfoLoaded` —— 8/9 个有
- `ImageBatchMulti` —— 7/9 个有
- `LoraLoaderModelOnly` —— 7/9 个有
- `ModelSamplingSD3` —— 7/9 个有
- `PoseAndFaceDetection` —— 7/9 个有
- `UNETLoader` —— 7/9 个有
- `Display Int (rgthree)` —— 6/9 个有
- `ImageScale` —— 6/9 个有
- `OnnxDetectionModelLoader` —— 6/9 个有
- `DrawViTPose` —— 5/9 个有
- `DWPreprocessor` —— 4/9 个有
- `PathchSageAttentionKJ` —— 4/9 个有
- `Primitive integer [Crystools]` —— 4/9 个有
- `RHHiddenNodes` —— 4/9 个有
- `easy float` —— 4/9 个有
- `ImageFromBatch` —— 2/9 个有
- `BatchCount+` —— 1/9 个有
- `CRTFirstLastFrameSelector` —— 1/9 个有
- `Fast Groups Bypasser (rgthree)` —— 1/9 个有
- `GetImageSizeAndCount` —— 1/9 个有
- `ImageBatch` —— 1/9 个有
- `Make Image Batch` —— 1/9 个有
- `MathExpression_UTK` —— 1/9 个有
- `PixelPerfectResolution` —— 1/9 个有
- `RIFE VFI` —— 1/9 个有
- `RMBG` —— 1/9 个有
- `RepeatImageBatch` —— 1/9 个有
- `easy batchAnything` —— 1/9 个有
- `easy imageCount` —— 1/9 个有
- `easy mathInt` —— 1/9 个有
- `easy showAnything` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 6 | 9 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 30/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 6，9 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（30/9 个样本）：Steps较低可能导致细节不足
