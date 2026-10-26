---
name: unknown_workflow_video_lora_sampler_421
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.4605
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, DiffusionModelLoaderKJ, ImageResizeKJv2, Int, KSamplerSelect, LoadImage, LoraLoaderModelOnly, SAM3_VideoTrack, SCAIL2ColoredMask, SamplerCustom, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanSCAILToVideo, easy imageRemBg]
problems: []
missing: []
members: [视频生成/图生视频/scall2  单人动作迁移_2069034704543764482.json, 视频生成/图生视频/scall2单人循环动作迁移_2069027789755469826.json, 视频生成/图生视频/女装带货_2074116583454236674.json, 视频生成/图生视频/数字人女装带货视频_2082802589850230786.json, 视频生成/图生视频/视频主角想换就换！SCAIL2人物替换工作流｜全节点注释直接抄_2065014891525795842.json, 视频生成/文生视频/SCAIL2-动作迁移（二创、跳舞、动作）_2064755609194549249.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_421

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/scall2  单人动作迁移_2069034704543764482.json、视频生成/图生视频/scall2单人循环动作迁移_2069027789755469826.json、视频生成/图生视频/女装带货_2074116583454236674.json、视频生成/图生视频/数字人女装带货视频_2082802589850230786.json、视频生成/图生视频/视频主角想换就换！SCAIL2人物替换工作流｜全节点注释直接抄_2065014891525795842.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：46%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `DiffusionModelLoaderKJ`
- `ImageResizeKJv2`
- `Int`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SAM3_VideoTrack`
- `SCAIL2ColoredMask`
- `SamplerCustom`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanSCAILToVideo`
- `easy imageRemBg`

**可变部分**（部分 workflow 才有）：
- `GetImageRangeFromBatch` —— 5/6 个有
- `GetNode` —— 5/6 个有
- `PreviewImage` —— 5/6 个有
- `SetNode` —— 5/6 个有
- `easy batchAnything` —— 5/6 个有
- `easy forLoopEnd` —— 5/6 个有
- `easy forLoopStart` —— 5/6 个有
- `VHS_VideoInfo` —— 4/6 个有
- `easy showAnything` —— 4/6 个有
- `ComfyMathExpression` —— 3/6 个有
- `DF_Int_to_Float` —— 2/6 个有
- `ImageConcatMulti` —— 2/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/6 个有
- `MathExpression|pysssss` —— 2/6 个有
- `ModelSamplingSD3` —— 2/6 个有
- `TTResolutionSelector` —— 2/6 个有
- `VHS_VideoInfoLoaded` —— 2/6 个有
- `CR Text` —— 1/6 个有
- `Fast Groups Muter (rgthree)` —— 1/6 个有
- `ImpactConditionalBranch` —— 1/6 个有
- `Mute / Bypass Relay (rgthree)` —— 1/6 个有
- `Mute / Bypass Repeater (rgthree)` —— 1/6 个有
- `PrimitiveBoolean` —— 1/6 个有
- `SimpleMath+` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
