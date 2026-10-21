---
name: unknown_workflow_video_lora_sampler_414
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.901
common_nodes: [CFGGuider, CLIPTextEncode, LTX2_NAG, LTXDirector, LTXDirectorGuide, LTXVAudioVAEDecode, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVEnhanceAVideoKJ, LTXVSeparateAVLatent, LoraLoaderModelOnly, ModelPatchTorchSettings, PathchSageAttentionKJ, PlaySound|pysssss, RandomNoise, SamplerCustomAdvanced, VAELoaderKJ, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2072446244018016257.json, 视频生成/文生视频/LTX2.3 完全体全整合_2070098600666951681.json, 视频生成/文生视频/LTX2.3 导演台全能+OMNI音视频增强工作流_2053837157135069185.json, 视频生成/文生视频/LTX2.3导演节点全功能+动作优化工作流_2058768723879751682.json, 视频生成/文生视频/LTX2.3导演节点全功能+清晰度增强工作流_2058746144511062018.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_414

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/2072446244018016257.json、视频生成/文生视频/LTX2.3 完全体全整合_2070098600666951681.json、视频生成/文生视频/LTX2.3 导演台全能+OMNI音视频增强工作流_2053837157135069185.json、视频生成/文生视频/LTX2.3导演节点全功能+动作优化工作流_2058768723879751682.json、视频生成/文生视频/LTX2.3导演节点全功能+清晰度增强工作流_2058746144511062018.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `LTX2_NAG`
- `LTXDirector`
- `LTXDirectorGuide`
- `LTXVAudioVAEDecode`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEnhanceAVideoKJ`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PlaySound|pysssss`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAELoaderKJ`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 4/5 个有
- `DualCLIPLoaderGGUF` —— 4/5 个有
- `KSamplerSelect` —— 4/5 个有
- `LTXVLatentUpsampler` —— 4/5 个有
- `LatentUpscaleModelLoader` —— 4/5 个有
- `LTX2SamplingPreviewOverride` —— 3/5 个有
- `LTXVCropGuides` —— 3/5 个有
- `UnetLoaderGGUF` —— 3/5 个有
- `VAEDecodeTiled` —— 3/5 个有
- `Display Any (rgthree)` —— 2/5 个有
- `LTXDirectorCropGuides` —— 2/5 个有
- `LTXVTiledVAEDecode` —— 2/5 个有
- `Label (rgthree)` —— 2/5 个有
- `ModelPreviewOverrideKJ` —— 2/5 个有
- `TextGenerateLTX2Prompt` —— 2/5 个有
- `UNETLoader` —— 2/5 个有
- `DualCLIPLoader` —— 1/5 个有
- `ManualSigmas` —— 1/5 个有
- `SamplerEulerAncestral` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
