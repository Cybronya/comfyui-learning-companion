---
name: unknown_workflow_lora_sampler_checkpoint
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.9587
common_nodes: [BasicScheduler, CFGGuider, CheckpointLoaderSimple, ConditioningZeroOut, CreateVideo, KSamplerSelect, LTXDirectorGuide, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVSeparateAVLatent, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, SaveVideo, VAEDecodeTiled]
problems: []
missing: []
members: [图片生成/文生图/LTX2.3导演分镜流_2073321199618314242.json, 视频生成/图生视频/LTX2.3导演分镜流V2_2059815779062865922.json, 视频生成/图生视频/LTX导演工作流-参考音频版数字人_2055639215265861633.json, 视频生成/图生视频/LTX导演工作流_2059458319999397889.json, 视频生成/图生视频/LTX导演工作流_2061429598319104001.json, 视频生成/图生视频/LTX导演工作流！运镜分镜随心所动！_2056296631754117121.json, 视频生成/图生视频/LTX导演工作流！运镜分镜随心所动！_2057419629450063874.json, 视频生成/图生视频/LTX导演工作流！运镜分镜随心所动！_2058649918318923777.json, 视频生成/图生视频/LTX导演工作流！音视频随心_2055635483195133953.json, 视频生成/图生视频/LTX导演面板_2061446032973713410.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_checkpoint

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/LTX2.3导演分镜流_2073321199618314242.json、视频生成/图生视频/LTX2.3导演分镜流V2_2059815779062865922.json、视频生成/图生视频/LTX导演工作流-参考音频版数字人_2055639215265861633.json、视频生成/图生视频/LTX导演工作流_2059458319999397889.json、视频生成/图生视频/LTX导演工作流_2061429598319104001.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `CreateVideo`
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
- `SaveVideo`
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `LTXDirector` —— 9/10 个有
- `DualCLIPLoader` —— 8/10 个有
- `LTX2SamplingPreviewOverride` —— 8/10 个有
- `LTXVLatentUpsampler` —— 8/10 个有
- `LatentUpscaleModelLoader` —— 8/10 个有
- `VAELoaderKJ` —— 8/10 个有
- `ComfySwitchNode` —— 2/10 个有
- `LTXAVTextEncoderLoader` —— 2/10 个有
- `LTXVAudioVAELoader` —— 2/10 个有
- `PrimitiveBoolean` —— 2/10 个有
- `CS-LTXGridDirector` —— 1/10 个有
- `LTXFloatToInt` —— 1/10 个有
- `LayerUtility: ColorImage` —— 1/10 个有
- `LoadImage` —— 1/10 个有
- `PrimitiveFloat` —— 1/10 个有
- `SaveAudio` —— 1/10 个有
- `UNETLoader` —— 1/10 个有
- `easy imageSize` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
