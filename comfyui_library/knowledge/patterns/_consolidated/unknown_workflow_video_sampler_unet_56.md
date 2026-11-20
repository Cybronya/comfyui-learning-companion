---
name: unknown_workflow_video_sampler_unet_56
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9538
common_nodes: [CFGGuider, DualCLIPLoader, KSamplerSelect, LTXDirectorGuide, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVSeparateAVLatent, ManualSigmas, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAELoaderKJ, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/Ltx2.3 导演流（自用）_2063841095607476225.json, 视频生成/图生视频/亮哥aigcLTX23漫剧_2063614975846993922.json, 视频生成/图生视频/电商图片音频提示词生成视频 LtxDirector_2059242196313919490.json, 视频生成/文生视频/Ltx2.3 导演流_2059463273585664002.json, 视频生成/文生视频/视频分段精准控制_ LTX Director_2062416320737669122.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_56

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/Ltx2.3 导演流（自用）_2063841095607476225.json、视频生成/图生视频/亮哥aigcLTX23漫剧_2063614975846993922.json、视频生成/图生视频/电商图片音频提示词生成视频 LtxDirector_2059242196313919490.json、视频生成/文生视频/Ltx2.3 导演流_2059463273585664002.json、视频生成/文生视频/视频分段精准控制_ LTX Director_2062416320737669122.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGGuider`
- `DualCLIPLoader`
- `KSamplerSelect`
- `LTXDirectorGuide`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `ManualSigmas`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 4/5 个有
- `ConditioningZeroOut` —— 4/5 个有
- `LTXDirector` —— 4/5 个有
- `LTXVLatentUpsampler` —— 4/5 个有
- `LatentUpscaleModelLoader` —— 4/5 个有
- `CLIPTextEncode` —— 3/5 个有
- `LTX2SamplingPreviewOverride` —— 3/5 个有
- `LTX2_NAG` —— 3/5 个有
- `LoraLoaderModelOnly` —— 3/5 个有
- `VAEDecodeTiled` —— 3/5 个有
- `ComfyMathExpression` —— 2/5 个有
- `LayerUtility: PurgeVRAM` —— 2/5 个有
- `TTResolutionSelector` —— 2/5 个有
- `VAEDecode` —— 2/5 个有
- `ComfySwitchNode` —— 1/5 个有
- `PrimitiveBoolean` —— 1/5 个有
- `Yusu-LTXDirector` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
