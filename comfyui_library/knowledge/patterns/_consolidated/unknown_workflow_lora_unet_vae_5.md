---
name: unknown_workflow_lora_unet_vae_5
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.659
common_nodes: [AddLabel, AddWater_MarkNode, Any Switch (rgthree), CLIPLoader, CR Image Grid Panel, CreateVideo, EmptyLatentImage, GetImageRangeFromBatch, GetImageSize, GetVideoComponents, ImageBatchMulti, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadVideoWithFilename, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, PrimitiveInt, SaveVideo, SimpleMath+, SimpleMathDual+, UNETLoader, VAELoader, easy blocker, easy imageBatchToImageList, easy imageListToImageBatch, easy imageScaleDownToSize, easy indexAnything, easy promptLine, easy seed, workflow>千问图像生成]
problems: []
missing: []
members: [图片生成/图生图/影视二创系列 · 角色多视图生成王改革_2004368991223246850.json, 图片生成/图生图/游戏影视多人二创 · 第一步角色多视图生成_2002433156378705922.json, 视频生成/图生视频/角色替换前置工作流：角色多视图生成_2001207766033235969.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_unet_vae_5

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/影视二创系列 · 角色多视图生成王改革_2004368991223246850.json、图片生成/图生图/游戏影视多人二创 · 第一步角色多视图生成_2002433156378705922.json、视频生成/图生视频/角色替换前置工作流：角色多视图生成_2001207766033235969.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：66%

## 共有节点

全部 3 个 workflow 都包含：
- `AddLabel`
- `AddWater_MarkNode`
- `Any Switch (rgthree)`
- `CLIPLoader`
- `CR Image Grid Panel`
- `CreateVideo`
- `EmptyLatentImage`
- `GetImageRangeFromBatch`
- `GetImageSize`
- `GetVideoComponents`
- `ImageBatchMulti`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadVideoWithFilename`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `PrimitiveInt`
- `SaveVideo`
- `SimpleMath+`
- `SimpleMathDual+`
- `UNETLoader`
- `VAELoader`
- `easy blocker`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`
- `easy imageScaleDownToSize`
- `easy indexAnything`
- `easy promptLine`
- `easy seed`
- `workflow>千问图像生成`

**可变部分**（部分 workflow 才有）：
- `ImpactSwitch` —— 2/3 个有
- `RH_Nano_Banana2_Image2Image` —— 2/3 个有
- `SeedVR2LoadDiTModel` —— 2/3 个有
- `SeedVR2LoadVAEModel` —— 2/3 个有
- `SeedVR2VideoUpscaler` —— 2/3 个有
- `GetNode` —— 1/3 个有
- `SaveImage` —— 1/3 个有
- `SetNode` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 512 | 3 | 100% |
| 高度 | 512 | 512 - 512 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
