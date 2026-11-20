---
name: unknown_workflow_sampler_clip_unet_124
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.792455
common_nodes: [CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLTXVLatentVideo, GetImageSize, LTXVAddGuide, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVDualCFGGuider, LTXVEmptyLatentAudio, LTXVPreprocess, LTXVSeparateAVLatent, LoadImage, ManualSigmas, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SamplerEulerAncestral, UNETLoader, VAEDecodeTiled, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/A-10 LTX-2.5 首尾帧生视频 （FLF2V）_2087395088770097154.json, 视频生成/图生视频/LTX 2.5 首尾帧生视频版_2094313555356119041.json, 视频生成/图生视频/LTX2.5 首尾帧图生视频（提示词全自动）_2087475047052173314.json, 视频生成/图生视频/LTX2.5-首尾帧(自动提示词)_2087515085420974081.json, 视频生成/图生视频/LTX2.5首尾帧_2087368525567582209.json, 视频生成/图生视频/LTX2.5首尾帧_2087405087823060994.json, 视频生成/图生视频/LTX2.5首尾帧_2087526366265827329.json, 视频生成/图生视频/LTX2.5首尾帧_2088696578835046402.json, 视频生成/图生视频/LTX2.5首尾帧生视频2608_2095393045469556738.json, 视频生成/图生视频/LTX2_5_flf2v_2092797961985159170.json, 视频生成/文生视频/LTX 2.5 首尾帧视频生成_2087469648844513282.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_124

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/A-10 LTX-2.5 首尾帧生视频 （FLF2V）_2087395088770097154.json、视频生成/图生视频/LTX 2.5 首尾帧生视频版_2094313555356119041.json、视频生成/图生视频/LTX2.5 首尾帧图生视频（提示词全自动）_2087475047052173314.json、视频生成/图生视频/LTX2.5-首尾帧(自动提示词)_2087515085420974081.json、视频生成/图生视频/LTX2.5首尾帧_2087368525567582209.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `LTXVAddGuide`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVDualCFGGuider`
- `LTXVEmptyLatentAudio`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `ManualSigmas`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SamplerEulerAncestral`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewAny` —— 10/11 个有
- `ResizeImageMaskNode` —— 10/11 个有
- `ComfySwitchNode` —— 8/11 个有
- `PrimitiveBoolean` —— 8/11 个有
- `TextGenerateLTX2Prompt` —— 8/11 个有
- `CreateVideo` —— 6/11 个有
- `SaveVideo` —— 6/11 个有
- `VHS_VideoCombine` —— 6/11 个有
- `CR Text` —— 2/11 个有
- `RH_LLMAPI_Pro_Node` —— 2/11 个有
- `FlashVSRNode` —— 1/11 个有
- `ImageConcanate` —— 1/11 个有
- `ImageFromBatch` —— 1/11 个有
- `ImageScale` —— 1/11 个有
- `Label (rgthree)` —— 1/11 个有
- `SaveAudio` —— 1/11 个有
- `SaveImage` —— 1/11 个有
- `Text` —— 1/11 个有
- `llama_cpp_instruct_adv` —— 1/11 个有
- `llama_cpp_model_loader` —— 1/11 个有
- `孤海注释` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 11 | 100% |
| 高度 | 25 | 25 - 25 | 11 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，11 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，11 个样本，取值集中（一致性 100%）
