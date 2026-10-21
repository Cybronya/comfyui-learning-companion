---
name: unknown_workflow_video_sampler_clip_41
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.814182
common_nodes: [CLIPTextEncode, Fast Groups Bypasser (rgthree), INTConstant, ImageResizeKJ, KSampler, LoadImage, ModelSamplingSD3, VAEDecode, VHS_LoadVideo, VHS_VideoCombine, WanVaceToVideo, WanVideoVACEStartToEndFrame]
problems: [Steps较低可能导致细节不足]
missing: [Primitive integer [Crystools], Zoe-DepthMapPreprocessor]
members: [图片生成/文生图/1968219641325715457.json, 视频生成/图生视频/1968267698775969793.json, 视频生成/图生视频/1968241987252047874.json, 视频生成/图生视频/1970889841762308097.json, 视频生成/图生视频/2044946900876529666.json, 视频生成/图生视频/2045881265131360258.json, 视频生成/图生视频/1969030335826718722.json, 视频生成/图生视频/2011257602096766978.json, 视频生成/图生视频/1971574546153336834.json, 视频生成/文生视频/1968982500666195970.json, 视频生成/文生视频/Wan2.2 多合一V2.0_2046237389487611905.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_41

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/1968219641325715457.json、视频生成/图生视频/1968267698775969793.json、视频生成/图生视频/1968241987252047874.json、视频生成/图生视频/1970889841762308097.json、视频生成/图生视频/2044946900876529666.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPTextEncode`
- `Fast Groups Bypasser (rgthree)`
- `INTConstant`
- `ImageResizeKJ`
- `KSampler`
- `LoadImage`
- `ModelSamplingSD3`
- `VAEDecode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVaceToVideo`
- `WanVideoVACEStartToEndFrame`

**可变部分**（部分 workflow 才有）：
- `DWPreprocessor` —— 10/11 个有
- `ImageBlend` —— 10/11 个有
- `Zoe-DepthMapPreprocessor` —— 10/11 个有
- `CheckpointLoaderSimple` —— 9/11 个有
- `Primitive integer [Crystools]` —— 9/11 个有
- `SimpleMath+` —— 3/11 个有
- `CLIPLoader` —— 2/11 个有
- `CR Text` —— 2/11 个有
- `GetNode` —— 2/11 个有
- `PathchSageAttentionKJ` —— 2/11 个有
- `SetNode` —— 2/11 个有
- `UNETLoader` —— 2/11 个有
- `VAELoader` —— 2/11 个有
- `GroundingDinoModelLoader_SDPose` —— 1/11 个有
- `RH_Nano_Banana_Image2Image` —— 1/11 个有
- `SDPoseOODLoader` —— 1/11 个有
- `SDPoseOODProcessor` —— 1/11 个有
- `SaveImage` —— 1/11 个有
- `TextBox` —— 1/11 个有
- `YOLOModelLoader` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 6 | 11 | 82% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | ipndm | - | 11 | 100% |
| 调度器 | sgm_uniform | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 6，11 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 ipndm，11 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（11/11 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：Primitive integer [Crystools]、Zoe-DepthMapPreprocessor
