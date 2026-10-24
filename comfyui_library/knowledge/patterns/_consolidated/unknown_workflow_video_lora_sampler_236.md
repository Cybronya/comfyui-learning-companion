---
name: unknown_workflow_video_lora_sampler_236
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.636875
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, CLIPVisionLoader, CheckpointLoaderSimple, DiffusionModelLoaderKJ, GetNode, ImageColorMatch+, ImageResizeKJv2, Int, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, SAM3_VideoTrack, SCAIL2SimpleVideo, SetNode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded]
problems: []
missing: []
members: [数字人/数字人/S2动作迁移-20秒视频不用plus背景不会动_2097242408995082241.json, 视频生成/图生视频/SCAIL2-人物替换_动作迁移-超长视频急速流 (1)_2071423701639323649.json, 视频生成/图生视频/SCAIL2-人物替换_动作迁移-超长视频急速流_2069615585679462402.json, 视频生成/图生视频/SCAIL2-人物替换_动作迁移-超长视频急速流_2069666503523389441.json, 视频生成/图生视频/SCAIL2-人物替换_动作迁移-超长视频急速流_2070043341298954242.json, 视频生成/图生视频/Scail-2.0_2095776718383575042.json, 视频生成/图生视频/Scail-2_2095778171303059458.json, 视频生成/图生视频/pipiai-SCAIL2-超快超长视频_2071797776257732609.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_236

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（数字人/数字人/S2动作迁移-20秒视频不用plus背景不会动_2097242408995082241.json、视频生成/图生视频/SCAIL2-人物替换_动作迁移-超长视频急速流 (1)_2071423701639323649.json、视频生成/图生视频/SCAIL2-人物替换_动作迁移-超长视频急速流_2069615585679462402.json、视频生成/图生视频/SCAIL2-人物替换_动作迁移-超长视频急速流_2069666503523389441.json、视频生成/图生视频/SCAIL2-人物替换_动作迁移-超长视频急速流_2070043341298954242.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：64%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `DiffusionModelLoaderKJ`
- `GetNode`
- `ImageColorMatch+`
- `ImageResizeKJv2`
- `Int`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `SAM3_VideoTrack`
- `SCAIL2SimpleVideo`
- `SetNode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`

**可变部分**（部分 workflow 才有）：
- `PreviewAny` —— 7/8 个有
- `WanChunkFeedForward` —— 5/8 个有
- `AILab_QwenVL` —— 2/8 个有
- `Text` —— 2/8 个有
- `ZML_MergeText` —— 2/8 个有
- `Float to Int` —— 1/8 个有
- `easy mathInt` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
