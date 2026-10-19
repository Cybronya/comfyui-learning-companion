---
name: unknown_workflow_lora_sampler_checkpoint
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.96125
common_nodes: [BasicScheduler, CFGGuider, CheckpointLoaderSimple, ConditioningZeroOut, CreateVideo, KSamplerSelect, LTXDirectorGuide, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVSeparateAVLatent, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, VAEDecodeTiled]
problems: []
missing: []
members: [视频生成/图生视频/2059815779062865922.json, 视频生成/图生视频/2059858506483847169.json, 视频生成/图生视频/2057286566376202241.json, 视频生成/图生视频/2058019383724830722.json, 视频生成/图生视频/2055076989958139906.json, 视频生成/图生视频/2055639215265861633.json, 视频生成/图生视频/2059458319999397889.json, 视频生成/图生视频/2061429598319104001.json, 视频生成/图生视频/2056296631754117121.json, 视频生成/图生视频/2057419629450063874.json, 视频生成/图生视频/2055095279413669890.json, 视频生成/图生视频/2067766430577287169.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_checkpoint

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/2059815779062865922.json、视频生成/图生视频/2059858506483847169.json、视频生成/图生视频/2057286566376202241.json、视频生成/图生视频/2058019383724830722.json、视频生成/图生视频/2055076989958139906.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 12 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `CreateVideo`
- `KSamplerSelect`
- `LTXDirectorGuide`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `DualCLIPLoader` —— 11/12 个有
- `LTX2SamplingPreviewOverride` —— 11/12 个有
- `LTXDirector` —— 11/12 个有
- `LTXVLatentUpsampler` —— 11/12 个有
- `LatentUpscaleModelLoader` —— 11/12 个有
- `SaveVideo` —— 11/12 个有
- `VAELoaderKJ` —— 11/12 个有
- `LTXVAudioVAEDecode` —— 10/12 个有
- `LoadImage` —— 2/12 个有
- `CS-LTXGridDirector` —— 1/12 个有
- `ComfySwitchNode` —— 1/12 个有
- `GetVideoComponents` —— 1/12 个有
- `Int` —— 1/12 个有
- `LTXAVTextEncoderLoader` —— 1/12 个有
- `LTXFloatToInt` —— 1/12 个有
- `LTXVAudioVAELoader` —— 1/12 个有
- `LayerUtility: ColorImage` —— 1/12 个有
- `PrimitiveBoolean` —— 1/12 个有
- `PrimitiveFloat` —— 1/12 个有
- `SaveAudio` —— 1/12 个有
- `UNETLoader` —— 1/12 个有
- `VHS_VideoCombine` —— 1/12 个有
- `easy imageSize` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
