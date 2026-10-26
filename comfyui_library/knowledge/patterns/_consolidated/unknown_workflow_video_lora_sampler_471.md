---
name: unknown_workflow_video_lora_sampler_471
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.4458
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, GetNode, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PreviewImage, SAM3_VideoTrack, SCAIL2ColoredMask, SamplerCustom, SetNode, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanSCAILToVideo]
problems: []
missing: []
members: [数字人/数字人/视频人物替换 动作迁移 SCAIL 2（支持多人）_2065647705745084418.json, 数字人/数字人/视频人物替换 视频动作迁移 SCAIL 2（单人和多人）_2065655949918031874.json, 视频生成/图生视频/SCAIL 2 角色替换+动作迁移+表情迁移（长视频续航版）_2065651452084834306.json, 视频生成/图生视频/SCAIL-2 影视级角色动作驱动与替换_2064580143158480898.json, 视频生成/图生视频/SCAIL2 Animation & Replacement 动作迁移&角色替换_2075056544013709313.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_471

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（数字人/数字人/视频人物替换 动作迁移 SCAIL 2（支持多人）_2065647705745084418.json、数字人/数字人/视频人物替换 视频动作迁移 SCAIL 2（单人和多人）_2065655949918031874.json、视频生成/图生视频/SCAIL 2 角色替换+动作迁移+表情迁移（长视频续航版）_2065651452084834306.json、视频生成/图生视频/SCAIL-2 影视级角色动作驱动与替换_2064580143158480898.json、视频生成/图生视频/SCAIL2 Animation & Replacement 动作迁移&角色替换_2075056544013709313.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：45%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `GetNode`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PreviewImage`
- `SAM3_VideoTrack`
- `SCAIL2ColoredMask`
- `SamplerCustom`
- `SetNode`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanSCAILToVideo`

**可变部分**（部分 workflow 才有）：
- `BatchImagesNode` —— 4/5 个有
- `ColorTransfer` —— 4/5 个有
- `Fast Groups Bypasser (rgthree)` —— 4/5 个有
- `GetImageRangeFromBatch` —— 4/5 个有
- `ImageConcatMulti` —— 4/5 个有
- `SimpleMath+` —— 4/5 个有
- `UNETLoader` —— 4/5 个有
- `VHS_VideoInfo` —— 4/5 个有
- `ApplySageAttention` —— 3/5 个有
- `CR Text` —— 3/5 个有
- `Int` —— 3/5 个有
- `Seed` —— 3/5 个有
- `easy imageRemBg` —— 3/5 个有
- `ImageFromBatch` —— 2/5 个有
- `PrimitiveInt` —— 2/5 个有
- `SaveImage` —— 2/5 个有
- `Text` —— 2/5 个有
- `easy showAnything` —— 2/5 个有
- `DiffusionModelLoaderKJ` —— 1/5 个有
- `GoogleTranslateTextNode` —— 1/5 个有
- `ImageResizeKJv2` —— 1/5 个有
- `JjkText` —— 1/5 个有
- `Label (rgthree)` —— 1/5 个有
- `ModelPatchTorchSettings` —— 1/5 个有
- `PathchSageAttentionKJ` —— 1/5 个有
- `PrimitiveBoolean` —— 1/5 个有
- `PrimitiveStringMultiline` —— 1/5 个有
- `ShowText|pysssss` —— 1/5 个有
- `WanChunkFeedForward` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
