---
name: unknown_workflow_lora_sampler_checkpoint
type: Unknown Workflow
frequency: 19
level: moderate
coverage: 0.949211
common_nodes: [BasicScheduler, CFGGuider, CheckpointLoaderSimple, ConditioningZeroOut, KSamplerSelect, LTXDirectorGuide, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVSeparateAVLatent, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced]
problems: []
missing: []
members: [图片生成/文生图/LTX2.3导演分镜流_2073321199618314242.json, 视频生成/图生视频/2055655934248144898.json, 视频生成/图生视频/2059487866354495489.json, 视频生成/图生视频/2058028747135217666.json, 视频生成/图生视频/2055524487839404034.json, 视频生成/图生视频/2055900601728421889.json, 视频生成/图生视频/2059815779062865922.json, 视频生成/图生视频/2057726231881281537.json, 视频生成/图生视频/2055076989958139906.json, 视频生成/图生视频/2061429598319104001.json, 视频生成/图生视频/2056296631754117121.json, 视频生成/图生视频/2057419629450063874.json, 视频生成/图生视频/2058649918318923777.json, 视频生成/图生视频/2055635483195133953.json, 视频生成/图生视频/2061446032973713410.json, 视频生成/图生视频/2055531778017906689.json, 视频生成/图生视频/2056691705071620098.json, 视频生成/文生视频/LTX 2.3 Director 导演工作台 ComfyUI 在线工作流_2060986578205503489.json, 视频生成/文生视频/LTX Director 导演工作台 (2采)_2064170624049827841.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_checkpoint

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（图片生成/文生图/LTX2.3导演分镜流_2073321199618314242.json、视频生成/图生视频/2055655934248144898.json、视频生成/图生视频/2059487866354495489.json、视频生成/图生视频/2058028747135217666.json、视频生成/图生视频/2055524487839404034.json…）

- **类型**：Unknown Workflow
- **样本数**：19
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 19 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `KSamplerSelect`
- `LTXDirectorGuide`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 18/19 个有
- `LTXDirector` —— 18/19 个有
- `SaveVideo` —— 18/19 个有
- `LTX2SamplingPreviewOverride` —— 17/19 个有
- `LTXVLatentUpsampler` —— 17/19 个有
- `LatentUpscaleModelLoader` —— 17/19 个有
- `DualCLIPLoader` —— 16/19 个有
- `VAELoaderKJ` —— 16/19 个有
- `VAEDecodeTiled` —— 15/19 个有
- `LTXAVTextEncoderLoader` —— 4/19 个有
- `VAEDecode` —— 4/19 个有
- `ImpactSwitch` —— 3/19 个有
- `Int` —— 3/19 个有
- `LTXVAudioVAELoader` —— 3/19 个有
- `LoadImage` —— 3/19 个有
- `ComfySwitchNode` —— 2/19 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/19 个有
- `PrimitiveBoolean` —— 2/19 个有
- `VHS_VideoCombine` —— 2/19 个有
- `CS-LTXGridDirector` —— 1/19 个有
- `GetNode` —— 1/19 个有
- `SetNode` —— 1/19 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
