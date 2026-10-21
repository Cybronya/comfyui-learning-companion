---
name: unknown_workflow_lora_sampler_clip_46
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.97
common_nodes: [CFGGuider, CLIPTextEncode, EmptyLTXVLatentVideo, INTConstant, KSamplerSelect, LTXAVTextEncoderLoader, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LiconMSR, LoadImage, LowVRAMCheckpointLoader, ManualSigmas, RandomNoise, SamplerCustomAdvanced, VAEDecode]
problems: []
missing: []
members: [视频生成/图生视频/2070392828198481921.json, 视频生成/图生视频/2066143110995992578.json, 视频生成/图生视频/2072573274269241345.json, 视频生成/图生视频/2072526155609104386.json, 视频生成/图生视频/2063485331059601410.json, 视频生成/图生视频/2063464652104884226.json, 视频生成/文生视频/（高帧率图生视频）Ltx2.3 Licon-MSR自动提示词版全能参考视频_2064880215909814273.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_46

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/2070392828198481921.json、视频生成/图生视频/2066143110995992578.json、视频生成/图生视频/2072573274269241345.json、视频生成/图生视频/2072526155609104386.json、视频生成/图生视频/2063485331059601410.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 7 个 workflow 都包含：
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
- `LTXVAudioVAELoader` —— 6/7 个有
- `CreateVideo` —— 4/7 个有
- `SaveVideo` —— 4/7 个有
- `CR Prompt Text` —— 3/7 个有
- `RH_LLMAPI_Pro_Node` —— 3/7 个有
- `ShowText|pysssss` —— 3/7 个有
- `VHS_VideoCombine` —— 3/7 个有
- `PreviewImage` —— 2/7 个有
- `RHHiddenNodes` —— 2/7 个有
- `Text` —— 2/7 个有
- `CR Float To Integer` —— 1/7 个有
- `LTXVAddGuideMulti` —— 1/7 个有
- `LoraLoaderModelOnly` —— 1/7 个有
- `PrimitiveFloat` —— 1/7 个有
- `SaveImage` —— 1/7 个有
- `TT_img_enc` —— 1/7 个有
- `VAELoaderKJ` —— 1/7 个有
- `easy indexAnything` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 241 | 145 - 241 | 7 | 85% |
| 高度 | 50 | 24 - 50 | 7 | 80% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 241，观测区间 145 - 241，7 个样本，取值集中（一致性 85%）
- 高度 中位数 50，观测区间 24 - 50，7 个样本，取值集中（一致性 80%）
