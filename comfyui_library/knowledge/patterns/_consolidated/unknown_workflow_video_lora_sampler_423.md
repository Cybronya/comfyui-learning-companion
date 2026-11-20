---
name: unknown_workflow_video_lora_sampler_423
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.506571
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, GetImageRangeFromBatch, ImageConcatMulti, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PreviewImage, SAM3_VideoTrack, SCAIL2ColoredMask, SamplerCustom, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanSCAILToVideo, easy imageRemBg]
problems: []
missing: []
members: [平台全量/SCAIL-2 万能高还原动作迁移视频工作流_2067257650504617985.json, 平台全量/SCAIL-2影视级角色动作驱动动作迁移_角色替换_2066064371016626178.json, 平台全量/循环-SCAIL-2影视级角色动作驱动(动作迁移_角色替换)_2066107755626328066.json, 视频生成/图生视频/SCAIL-2 影视级角色动作驱动与替换_2064580143158480898.json, 视频生成/图生视频/新王驾到 SCAIL2-人物替换，极速循环长视频_2065696343452110850.json, 视频生成/图生视频/新王驾到 SCAIL2-动作迁移，极速循环长视频_2065580332925145090.json, 视频生成/文生视频/SCAIL2-动作迁移（二创、跳舞、动作）_2064755609194549249.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_423

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（平台全量/SCAIL-2 万能高还原动作迁移视频工作流_2067257650504617985.json、平台全量/SCAIL-2影视级角色动作驱动动作迁移_角色替换_2066064371016626178.json、平台全量/循环-SCAIL-2影视级角色动作驱动(动作迁移_角色替换)_2066107755626328066.json、视频生成/图生视频/SCAIL-2 影视级角色动作驱动与替换_2064580143158480898.json、视频生成/图生视频/新王驾到 SCAIL2-人物替换，极速循环长视频_2065696343452110850.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：51%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `GetImageRangeFromBatch`
- `ImageConcatMulti`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PreviewImage`
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
- `GetNode` —— 6/7 个有
- `ImageResizeKJv2` —— 6/7 个有
- `MathExpression|pysssss` —— 6/7 个有
- `PrimitiveBoolean` —— 6/7 个有
- `SetNode` —— 6/7 个有
- `ImpactConditionalBranch` —— 5/7 个有
- `VHS_VideoInfoLoaded` —— 5/7 个有
- `easy forLoopEnd` —— 5/7 个有
- `easy forLoopStart` —— 5/7 个有
- `Fast Groups Muter (rgthree)` —— 4/7 个有
- `Mute / Bypass Relay (rgthree)` —— 4/7 个有
- `Mute / Bypass Repeater (rgthree)` —— 4/7 个有
- `PrimitiveInt` —— 4/7 个有
- `UNETLoader` —— 4/7 个有
- `easy batchAnything` —— 4/7 个有
- `BatchImagesNode` —— 3/7 个有
- `ColorTransfer` —— 3/7 个有
- `DiffusionModelLoaderKJ` —— 3/7 个有
- `Int` —— 3/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/7 个有
- `Bjornulf_ShowInt` —— 2/7 个有
- `JjkText` —— 2/7 个有
- `easy cleanGpuUsed` —— 2/7 个有
- `easy imageSwitch` —— 2/7 个有
- `DisTorchPurgeVRAMV2` —— 1/7 个有
- `LayerUtility: PurgeVRAM V2` —— 1/7 个有
- `PrimitiveStringMultiline` —— 1/7 个有
- `easy compare` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
