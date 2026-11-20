---
name: unknown_workflow_lora_sampler_clip_166
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9752
common_nodes: [CFGGuider, CLIPTextEncode, EmptyLTXVLatentVideo, INTConstant, KSamplerSelect, LTXAVTextEncoderLoader, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LiconMSR, LoadImage, LowVRAMCheckpointLoader, ManualSigmas, RandomNoise, SamplerCustomAdvanced, VAEDecode]
problems: []
missing: []
members: [视频生成/图生视频/ltx2.3多图参考生视频_2070392828198481921.json, 视频生成/图生视频/全能参考_2066143110995992578.json, 视频生成/图生视频/最新版 LTX 漫剧多参分镜视频-落水漫剧电商服装分镜真人_2072573274269241345.json, 视频生成/图生视频/最新版 LTX 漫剧多参分镜视频-追逐漫剧电商服装分镜真人_2072526155609104386.json, 视频生成/图生视频/（高帧率）Ltx2.3 Licon-MSR全能参考生视频正式版V1_2063444223206191106.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_166

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/ltx2.3多图参考生视频_2070392828198481921.json、视频生成/图生视频/全能参考_2066143110995992578.json、视频生成/图生视频/最新版 LTX 漫剧多参分镜视频-落水漫剧电商服装分镜真人_2072573274269241345.json、视频生成/图生视频/最新版 LTX 漫剧多参分镜视频-追逐漫剧电商服装分镜真人_2072526155609104386.json、视频生成/图生视频/（高帧率）Ltx2.3 Licon-MSR全能参考生视频正式版V1_2063444223206191106.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `EmptyLTXVLatentVideo`
- `INTConstant`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXAddVideoICLoRAGuide`
- `LTXICLoRALoaderModelOnly`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVSeparateAVLatent`
- `LiconMSR`
- `LoadImage`
- `LowVRAMCheckpointLoader`
- `ManualSigmas`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `LTXVAudioVAELoader` —— 4/5 个有
- `VHS_VideoCombine` —— 3/5 个有
- `CreateVideo` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `RHHiddenNodes` —— 2/5 个有
- `SaveVideo` —— 2/5 个有
- `Text` —— 2/5 个有
- `CR Float To Integer` —— 1/5 个有
- `LTXVAddGuideMulti` —— 1/5 个有
- `LoraLoaderModelOnly` —— 1/5 个有
- `PrimitiveFloat` —— 1/5 个有
- `VAELoaderKJ` —— 1/5 个有
- `easy indexAnything` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 241 | 145 - 241 | 5 | 83% |
| 高度 | 50 | 24 - 50 | 5 | 77% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 241，观测区间 145 - 241，5 个样本，取值集中（一致性 83%）
- 高度 中位数 50，观测区间 24 - 50，5 个样本
