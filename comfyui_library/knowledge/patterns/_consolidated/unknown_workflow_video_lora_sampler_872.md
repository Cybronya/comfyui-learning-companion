---
name: unknown_workflow_video_lora_sampler_872
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.944667
common_nodes: [CFGGuider, CLIPTextEncode, DualCLIPLoader, KSamplerSelect, LTX2SamplingPreviewOverride, LTX2_NAG, LTXDirectorGuide, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVSeparateAVLatent, LoraLoaderModelOnly, ManualSigmas, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/Ltx2.3 导演流（自用）_2063841095607476225.json, 视频生成/图生视频/亮哥aigcLTX23漫剧_2063614975846993922.json, 视频生成/文生视频/Ltx2.3 导演流_2059463273585664002.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_872

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/Ltx2.3 导演流（自用）_2063841095607476225.json、视频生成/图生视频/亮哥aigcLTX23漫剧_2063614975846993922.json、视频生成/文生视频/Ltx2.3 导演流_2059463273585664002.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `LTXDirectorGuide`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 2/3 个有
- `ComfyMathExpression` —— 2/3 个有
- `ConditioningZeroOut` —— 2/3 个有
- `LTXDirector` —— 2/3 个有
- `LTXVLatentUpsampler` —— 2/3 个有
- `LatentUpscaleModelLoader` —— 2/3 个有
- `LayerUtility: PurgeVRAM` —— 2/3 个有
- `TTResolutionSelector` —— 2/3 个有
- `ComfySwitchNode` —— 1/3 个有
- `PrimitiveBoolean` —— 1/3 个有
- `Yusu-LTXDirector` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
