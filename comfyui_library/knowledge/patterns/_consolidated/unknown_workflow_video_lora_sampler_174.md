---
name: unknown_workflow_video_lora_sampler_174
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.666846
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, CLIPVisionLoader, CheckpointLoaderSimple, DiffusionModelLoaderKJ, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, SAM3_VideoTrack, SCAIL2SimpleVideo, VAELoader, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/1. SCAIL2_simple_2072287190410948610.json, 平台全量/SCAIL2-人物替换_动作迁移-超长视频急速流_2067130430394028034.json, 平台全量/SCAIL2-动作迁移工作流_2070041638352801794.json, 平台全量/SCAIL2_人物替换_动作迁移-自由切换简化流_2066870773939265537.json, 平台全量/scail2-动作迁移-人物替换（26.9可用）_2095922307368841218.json, 数字人/数字人/S2动作迁移-20秒视频不用plus背景不会动_2097242408995082241.json, 视频生成/图生视频/SCAIL2-人物替换_动作迁移-超长视频急速流 (1)_2071423701639323649.json, 视频生成/图生视频/SCAIL2-人物替换_动作迁移-超长视频急速流_2069615585679462402.json, 视频生成/图生视频/SCAIL2-人物替换_动作迁移-超长视频急速流_2069666503523389441.json, 视频生成/图生视频/SCAIL2-人物替换_动作迁移-超长视频急速流_2070043341298954242.json, 视频生成/图生视频/Scail-2.0_2095776718383575042.json, 视频生成/图生视频/Scail-2_2095778171303059458.json, 视频生成/图生视频/pipiai-SCAIL2-超快超长视频_2071797776257732609.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_174

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（平台全量/1. SCAIL2_simple_2072287190410948610.json、平台全量/SCAIL2-人物替换_动作迁移-超长视频急速流_2067130430394028034.json、平台全量/SCAIL2-动作迁移工作流_2070041638352801794.json、平台全量/SCAIL2_人物替换_动作迁移-自由切换简化流_2066870773939265537.json、平台全量/scail2-动作迁移-人物替换（26.9可用）_2095922307368841218.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：67%

## 共有节点

全部 13 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `DiffusionModelLoaderKJ`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `SAM3_VideoTrack`
- `SCAIL2SimpleVideo`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 12/13 个有
- `ImageResizeKJv2` —— 12/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 12/13 个有
- `SetNode` —— 12/13 个有
- `VHS_VideoInfoLoaded` —— 12/13 个有
- `ImageColorMatch+` —— 11/13 个有
- `Int` —— 11/13 个有
- `WanChunkFeedForward` —— 10/13 个有
- `PreviewAny` —— 9/13 个有
- `easy mathInt` —— 3/13 个有
- `AILab_QwenVL` —— 2/13 个有
- `Text` —— 2/13 个有
- `ZML_MergeText` —— 2/13 个有
- `ComfyNumberConvert` —— 1/13 个有
- `Float to Int` —— 1/13 个有
- `MiniMaxLowVRAMAttention` —— 1/13 个有
- `PrimitiveInt` —— 1/13 个有
- `SAM3_TrackPreview` —— 1/13 个有
- `SCAIL2FitVideo` —— 1/13 个有
- `VHS_VideoInfo` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
