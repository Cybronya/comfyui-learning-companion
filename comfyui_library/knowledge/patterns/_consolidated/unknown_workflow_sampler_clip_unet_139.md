---
name: unknown_workflow_sampler_clip_unet_139
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.844778
common_nodes: [CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLTXVLatentVideo, LTXVAddGuide, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVDualCFGGuider, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LoadImage, ManualSigmas, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SamplerEulerAncestral, UNETLoader, VAEDecodeTiled, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/LTX2.5 首尾帧图生视频（提示词全自动）_2087475047052173314.json, 视频生成/图生视频/LTX2.5-首尾帧(自动提示词)_2087515085420974081.json, 视频生成/图生视频/LTX2.5首尾帧-自动扩写提示词-高质量直出1K_2087739429011148802.json, 视频生成/图生视频/LTX2.5首尾帧_2087405087823060994.json, 视频生成/图生视频/LTX2.5首尾帧_2087756807111528449.json, 视频生成/图生视频/LTX2.5首尾帧生视频-高质量直出1K_2087559262871572481.json, 视频生成/图生视频/Ltx2.5首尾帧生视频-极速版_2090424622050275330.json, 视频生成/图生视频/首尾帧 极速 LTX2.5 音画同出_2087530951474765826.json, 视频生成/文生视频/LTX 2.5 首尾帧视频生成_2087469648844513282.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_139

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/LTX2.5 首尾帧图生视频（提示词全自动）_2087475047052173314.json、视频生成/图生视频/LTX2.5-首尾帧(自动提示词)_2087515085420974081.json、视频生成/图生视频/LTX2.5首尾帧-自动扩写提示词-高质量直出1K_2087739429011148802.json、视频生成/图生视频/LTX2.5首尾帧_2087405087823060994.json、视频生成/图生视频/LTX2.5首尾帧_2087756807111528449.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `LTXVAddGuide`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVDualCFGGuider`
- `LTXVEmptyLatentAudio`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `ManualSigmas`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SamplerEulerAncestral`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LTXVPreprocess` —— 8/9 个有
- `PrimitiveStringMultiline` —— 8/9 个有
- `GetImageSize` —— 7/9 个有
- `ResizeImageMaskNode` —— 6/9 个有
- `PreviewAny` —— 5/9 个有
- `VHS_VideoCombine` —— 5/9 个有
- `CreateVideo` —— 4/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/9 个有
- `SaveVideo` —— 4/9 个有
- `RH_LLMAPI_Pro_Node` —— 3/9 个有
- `ResolutionSelector` —— 3/9 个有
- `TextGenerateLTX2Prompt` —— 3/9 个有
- `CR Text` —— 2/9 个有
- `ComfySwitchNode` —— 2/9 个有
- `PrimitiveBoolean` —— 2/9 个有
- `CR Prompt Text` —— 1/9 个有
- `ImageConcanate` —— 1/9 个有
- `Label (rgthree)` —— 1/9 个有
- `ShellAgentPluginOutputText` —— 1/9 个有
- `Text` —— 1/9 个有
- `easy showAnything` —— 1/9 个有
- `llama_cpp_instruct_adv` —— 1/9 个有
- `llama_cpp_model_loader` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 9 | 100% |
| 高度 | 25 | 25 - 25 | 9 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，9 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，9 个样本，取值集中（一致性 100%）
