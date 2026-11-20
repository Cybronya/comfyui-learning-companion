---
name: unknown_workflow_video_sampler_clip_102
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.62
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CM_IntToFloat, GetImageRangeFromBatch, GetNode, ImageBatchMulti, ImageResizeKJv2, Int, KSampler, LoadImage, PreviewImage, SetNode, SimpleMath+, TrimVideoLatent, VAEDecode, VAELoader, VHS_GetImageCount, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanAnimateToVideo, easy seed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/11characterreplacement_2048960943010353154.json, 图片生成/图生图/Wan2.2-Animate 跳舞打拳动作丝滑、不变背景 动作迁移，长视频稳定输出新标杆_1986748092575903745.json, 图片生成/图生图/Wan2.2-Animate-图生视频 官方原版更稳定 动作迁移（不变背景）+长视频 稳如老狗_1983452230231760897.json, 平台全量/wan2.2动作迁移+姿势对齐BodyRatioMapper 解决Q版人物+多人一致性问题+自动时长最高50秒_2052662659287404545.json, 平台全量/动作模仿+抠像（Animate+SAM3）支持无限时长（手指稳定、支持更高分辨率）_2034881058252005377.json, 平台全量/动作迁移 V4（人物一致性、面部表情、对口型、肢体手部优化、胸部抖动优化版）_2063143197127307265.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_102

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/反推提示词/11characterreplacement_2048960943010353154.json、图片生成/图生图/Wan2.2-Animate 跳舞打拳动作丝滑、不变背景 动作迁移，长视频稳定输出新标杆_1986748092575903745.json、图片生成/图生图/Wan2.2-Animate-图生视频 官方原版更稳定 动作迁移（不变背景）+长视频 稳如老狗_1983452230231760897.json、平台全量/wan2.2动作迁移+姿势对齐BodyRatioMapper 解决Q版人物+多人一致性问题+自动时长最高50秒_2052662659287404545.json、平台全量/动作模仿+抠像（Animate+SAM3）支持无限时长（手指稳定、支持更高分辨率）_2034881058252005377.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：62%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CM_IntToFloat`
- `GetImageRangeFromBatch`
- `GetNode`
- `ImageBatchMulti`
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
- `VHS_GetImageCount`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `WanAnimateToVideo`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 5/6 个有
- `ModelSamplingSD3` —— 5/6 个有
- `UNETLoader` —— 5/6 个有
- `PoseAndFaceDetection` —— 4/6 个有
- `DWPreprocessor` —— 3/6 个有
- `Display Int (rgthree)` —— 3/6 个有
- `DrawViTPose` —— 3/6 个有
- `ImageScale` —— 3/6 个有
- `OnnxDetectionModelLoader` —— 3/6 个有
- `RHHiddenNodes` —— 3/6 个有
- `PathchSageAttentionKJ` —— 2/6 个有
- `Primitive integer [Crystools]` —— 2/6 个有
- `BBoxYOLO` —— 1/6 个有
- `BlockifyMask` —— 1/6 个有
- `BodyRatioMapperProportionTransfer` —— 1/6 个有
- `BodyRatioMapperSDPoseRender` —— 1/6 个有
- `CheckpointLoaderSimple` —— 1/6 个有
- `DrawMaskOnImage` —— 1/6 个有
- `LayerMask: MaskGrow` —— 1/6 个有
- `PixelPerfectResolution` —— 1/6 个有
- `RMBG` —— 1/6 个有
- `RTXVideoSuperResolution` —— 1/6 个有
- `SDPoseKeypointExtractor` —— 1/6 个有
- `Text` —— 1/6 个有
- `YOLOModelLoader` —— 1/6 个有
- `easy float` —— 1/6 个有
- `easy sam3ModelLoader` —— 1/6 个有
- `easy sam3VideoSegmentation` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 6 | 6 | 87% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 6，6 个样本，取值集中（一致性 87%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（18/6 个样本）：Steps较低可能导致细节不足
