---
name: unknown_workflow_video_lora_sampler_495
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.9185
common_nodes: [CFGGuider, CLIPTextEncode, DualCLIPLoader, KSamplerSelect, LTX2_NAG, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVSeparateAVLatent, LoraLoaderModelOnly, ManualSigmas, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/Ltx2.3 导演流（自用）_2063841095607476225.json, 视频生成/图生视频/亮哥aigcLTX23漫剧_2063614975846993922.json, 视频生成/文生视频/LTX2.3 自用版 T2V_2063969490962042881.json, 视频生成/文生视频/Ltx2.3 导演流_2059463273585664002.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_495

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/Ltx2.3 导演流（自用）_2063841095607476225.json、视频生成/图生视频/亮哥aigcLTX23漫剧_2063614975846993922.json、视频生成/文生视频/LTX2.3 自用版 T2V_2063969490962042881.json、视频生成/文生视频/Ltx2.3 导演流_2059463273585664002.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `KSamplerSelect`
- `LTX2_NAG`
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
- `BasicScheduler` —— 3/4 个有
- `ComfyMathExpression` —— 3/4 个有
- `LTX2SamplingPreviewOverride` —— 3/4 个有
- `LTXDirectorGuide` —— 3/4 个有
- `LTXVLatentUpsampler` —— 3/4 个有
- `LatentUpscaleModelLoader` —— 3/4 个有
- `LayerUtility: PurgeVRAM` —— 3/4 个有
- `ConditioningZeroOut` —— 2/4 个有
- `LTXDirector` —— 2/4 个有
- `TTResolutionSelector` —— 2/4 个有
- `ComfySwitchNode` —— 1/4 个有
- `EmptyLTXVLatentVideo` —— 1/4 个有
- `LTXTiledSampler` —— 1/4 个有
- `LTXVEmptyLatentAudio` —— 1/4 个有
- `PrimitiveBoolean` —— 1/4 个有
- `PrimitiveInt` —— 1/4 个有
- `PrimitiveStringMultiline` —— 1/4 个有
- `PromptRelayEncode` —— 1/4 个有
- `SimpleMath+` —— 1/4 个有
- `Yusu-LTXDirector` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | - | 1 | 100% |
| 高度 | 25 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
