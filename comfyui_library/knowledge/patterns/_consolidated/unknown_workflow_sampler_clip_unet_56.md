---
name: unknown_workflow_sampler_clip_unet_56
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.8355
common_nodes: [CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLTXVLatentVideo, LTXVAddGuide, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVDualCFGGuider, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LoadImage, ManualSigmas, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SamplerEulerAncestral, UNETLoader, VAEDecodeTiled, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/LTX2.5-首尾帧(自动提示词)_2087515085420974081.json, 视频生成/图生视频/LTX2.5首尾帧-自动扩写提示词-高质量直出1K_2087739429011148802.json, 视频生成/图生视频/LTX2.5首尾帧_2087405087823060994.json, 视频生成/图生视频/LTX2.5首尾帧_2087756807111528449.json, 视频生成/图生视频/LTX2.5首尾帧生视频-高质量直出1K_2087559262871572481.json, 视频生成/图生视频/Ltx2.5首尾帧生视频-极速版_2090424622050275330.json, 视频生成/图生视频/video_ltx2_5_flf2v_2087422059310833666.json, 视频生成/图生视频/【开源】LTX2.5 首尾帧生视频_2087467308766814210.json, 视频生成/图生视频/首尾帧 极速 LTX2.5 音画同出_2087530951474765826.json, 视频生成/文生视频/LTX 2.5 首尾帧视频生成_2087469648844513282.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_56

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/LTX2.5-首尾帧(自动提示词)_2087515085420974081.json、视频生成/图生视频/LTX2.5首尾帧-自动扩写提示词-高质量直出1K_2087739429011148802.json、视频生成/图生视频/LTX2.5首尾帧_2087405087823060994.json、视频生成/图生视频/LTX2.5首尾帧_2087756807111528449.json、视频生成/图生视频/LTX2.5首尾帧生视频-高质量直出1K_2087559262871572481.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 10 个 workflow 都包含：
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
- `LTXVPreprocess` —— 9/10 个有
- `PrimitiveStringMultiline` —— 9/10 个有
- `GetImageSize` —— 8/10 个有
- `ResizeImageMaskNode` —— 7/10 个有
- `CreateVideo` —— 5/10 个有
- `PreviewAny` —— 5/10 个有
- `SaveVideo` —— 5/10 个有
- `TextGenerateLTX2Prompt` —— 5/10 个有
- `VHS_VideoCombine` —— 5/10 个有
- `ComfySwitchNode` —— 4/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/10 个有
- `PrimitiveBoolean` —— 4/10 个有
- `ResolutionSelector` —— 4/10 个有
- `RH_LLMAPI_Pro_Node` —— 2/10 个有
- `easy showAnything` —— 2/10 个有
- `CR Prompt Text` —— 1/10 个有
- `CR Text` —— 1/10 个有
- `ImageConcanate` —— 1/10 个有
- `ShellAgentPluginOutputText` —— 1/10 个有
- `Text` —— 1/10 个有
- `easy cleanGpuUsed` —— 1/10 个有
- `llama_cpp_instruct_adv` —— 1/10 个有
- `llama_cpp_model_loader` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 10 | 100% |
| 高度 | 25 | 25 - 25 | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，10 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，10 个样本，取值集中（一致性 100%）
