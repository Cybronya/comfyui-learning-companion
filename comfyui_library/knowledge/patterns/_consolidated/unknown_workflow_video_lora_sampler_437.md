---
name: unknown_workflow_video_lora_sampler_437
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.946333
common_nodes: [CLIPTextEncode, CM_FloatToInt, DualCLIPLoader, EmptyLTXVLatentVideo, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVPreprocess, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, PrimitiveBoolean, PrimitiveFloat, PrimitiveInt, RandomNoise, ResizeImageMaskNode, SamplerCustomAdvanced, UNETLoader, UnetLoaderGGUF, VAEDecodeTiled, VAELoader, VAELoaderKJ, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/ltx-2.3图生视频单阶段双轨_2030336847670415362.json, 视频生成/文生视频/ltx-2.3图生视频单阶段最优_2030348888535732226.json, 视频生成/文生视频/ltx-2.3图生视频单阶段蒸馏生产最优_2030352240698986497.json, 视频生成/文生视频/ltx-2.3文生视频一阶段非加速+二阶段放大_2030336819816046593.json, 视频生成/文生视频/ltx-2.3文生视频单阶段双轨_2030335561520648193.json, 视频生成/文生视频/ltx-2.3文生视频蒸馏二阶段放大_2030336856772059137.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_437

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/文生视频/ltx-2.3图生视频单阶段双轨_2030336847670415362.json、视频生成/文生视频/ltx-2.3图生视频单阶段最优_2030348888535732226.json、视频生成/文生视频/ltx-2.3图生视频单阶段蒸馏生产最优_2030352240698986497.json、视频生成/文生视频/ltx-2.3文生视频一阶段非加速+二阶段放大_2030336819816046593.json、视频生成/文生视频/ltx-2.3文生视频单阶段双轨_2030335561520648193.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `CM_FloatToInt`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoConditionOnly`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `PrimitiveInt`
- `RandomNoise`
- `ResizeImageMaskNode`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `UnetLoaderGGUF`
- `VAEDecodeTiled`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CFGGuider` —— 5/6 个有
- `KSamplerSelect` —— 5/6 个有
- `ManualSigmas` —— 5/6 个有
- `ClownSampler_Beta` —— 4/6 个有
- `GuiderParameters` —— 4/6 个有
- `LTXVScheduler` —— 4/6 个有
- `MultimodalGuider` —— 4/6 个有
- `LTXVLatentUpsampler` —— 2/6 个有
- `LatentUpscaleModelLoader` —— 2/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 6 | 100% |
| 高度 | 25 | 25 - 25 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，6 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，6 个样本，取值集中（一致性 100%）
