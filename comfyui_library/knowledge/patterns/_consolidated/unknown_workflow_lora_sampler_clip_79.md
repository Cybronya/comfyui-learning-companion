---
name: unknown_workflow_lora_sampler_clip_79
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.846
common_nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DualCLIPLoader, FramePackLoraSelect, FramePackSingleFrameSampler, LoadFramePackModel, LoadImage, PreviewImage, SaveImage, VAEDecodeTiled, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/TG_art姿势迁移_1974973230664560642.json, 图片生成/图生图/framepack 姿势迁移_1953751001843073025.json, 图片生成/图生图/framepack 姿势迁移_1954710027120590850.json, 图片生成/图生图/创艺姿势工作流_1958018520103661570.json, 图片生成/图生图/动作迁移（卡通类）_1957148113146404866.json, 图片生成/图生图/姿势迁移终结者_1958447750033653762.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_79

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/TG_art姿势迁移_1974973230664560642.json、图片生成/图生图/framepack 姿势迁移_1953751001843073025.json、图片生成/图生图/framepack 姿势迁移_1954710027120590850.json、图片生成/图生图/创艺姿势工作流_1958018520103661570.json、图片生成/图生图/动作迁移（卡通类）_1957148113146404866.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DualCLIPLoader`
- `FramePackLoraSelect`
- `FramePackSingleFrameSampler`
- `LoadFramePackModel`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 4/6 个有
- `ImageConcatMulti` —— 4/6 个有
- `ImageResizeKJv2` —— 4/6 个有
- `Image Comparer (rgthree)` —— 3/6 个有
- `FramePackFindNearestBucket` —— 2/6 个有
- `INTConstant` —— 2/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/6 个有
- `Seed (rgthree)` —— 2/6 个有
- `Checkpoint Loader` —— 1/6 个有
- `GetImageSize` —— 1/6 个有
- `ImageResize+` —— 1/6 个有
- `UltimateSDUpscale` —— 1/6 个有
- `UpscaleModelLoader` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
