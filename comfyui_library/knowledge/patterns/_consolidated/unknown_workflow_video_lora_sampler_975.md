---
name: unknown_workflow_video_lora_sampler_975
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.4075
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DiffusionModelLoaderKJ, GetNode, ImageBatchMulti, ImageResizeKJv2, Int, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PreviewImage, SamplerCustom, SetNode, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanContextWindowsManual, WanSCAILToVideo, easy showAnything]
problems: []
missing: []
members: [平台全量/Scail2 动作迁移（多参考图）超级加长版_2068968411945852930.json, 平台全量/官流scail2 上下文长视频(适合大显存，大内存）_2072520377162616833.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_975

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/Scail2 动作迁移（多参考图）超级加长版_2068968411945852930.json、平台全量/官流scail2 上下文长视频(适合大显存，大内存）_2072520377162616833.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：41%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DiffusionModelLoaderKJ`
- `GetNode`
- `ImageBatchMulti`
- `ImageResizeKJv2`
- `Int`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PreviewImage`
- `SamplerCustom`
- `SetNode`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanContextWindowsManual`
- `WanSCAILToVideo`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `BatchCount+` —— 1/2 个有
- `ColorTransfer` —— 1/2 个有
- `ComfyMathExpression` —— 1/2 个有
- `Float to Int` —— 1/2 个有
- `FloatConstant` —— 1/2 个有
- `ImageBatchExtendWithOverlap` —— 1/2 个有
- `ImpactControlBridge` —— 1/2 个有
- `ImpactSwitch` —— 1/2 个有
- `LazySwitchKJ` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有
- `VHS_SplitImages` —— 1/2 个有
- `WanChunkFeedForward` —— 1/2 个有
- `easy anythingIndexSwitch` —— 1/2 个有
- `easy compare` —— 1/2 个有
- `easy float` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
