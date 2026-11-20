---
name: unknown_workflow_sampler_clip_unet_89
type: Unknown Workflow
frequency: 13
level: strong
coverage: 0.841077
common_nodes: [CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLTXVLatentVideo, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVDualCFGGuider, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, ManualSigmas, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecodeTiled, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/LTX2.5首尾帧-自动扩写提示词-高质量直出1K_2087739429011148802.json, 视频生成/图生视频/LTX2.5首尾帧_2087756807111528449.json, 视频生成/图生视频/LTX2.5首尾帧生视频-高质量直出1K_2087559262871572481.json, 视频生成/图生视频/Ltx2.5首尾帧生视频-极速版_2090424622050275330.json, 视频生成/图生视频/video_ltx2_5_flf2v_2087422059310833666.json, 视频生成/图生视频/【开源】LTX2.5 图生视频_2087455802314547201.json, 视频生成/图生视频/【开源】LTX2.5 首尾帧生视频_2087467308766814210.json, 视频生成/图生视频/图生视频  极速  LTX2.5 音画同出_2087530924060798978.json, 视频生成/图生视频/极速图生视频音画同出   LTX2.5_2095738668177780738.json, 视频生成/图生视频/首尾帧 极速 LTX2.5 音画同出_2087530951474765826.json, 视频生成/文生视频/A-8 LTX-2.5 文生视频（T2V）· 音画同步生成_2087369134014291970.json, 视频生成/文生视频/A-8_LTX-2.5_文生视频T2V·_音画同步生成_2104390729396211714.json, 视频生成/文生视频/图生视频 文生视频 首尾帧 极速 LTX2.5全家桶 音画同出_2087552830658924545.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_89

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/LTX2.5首尾帧-自动扩写提示词-高质量直出1K_2087739429011148802.json、视频生成/图生视频/LTX2.5首尾帧_2087756807111528449.json、视频生成/图生视频/LTX2.5首尾帧生视频-高质量直出1K_2087559262871572481.json、视频生成/图生视频/Ltx2.5首尾帧生视频-极速版_2090424622050275330.json、视频生成/图生视频/video_ltx2_5_flf2v_2087422059310833666.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVDualCFGGuider`
- `LTXVEmptyLatentAudio`
- `LTXVSeparateAVLatent`
- `ManualSigmas`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 11/13 个有
- `PrimitiveStringMultiline` —— 11/13 个有
- `LTXVPreprocess` —— 10/13 个有
- `ResolutionSelector` —— 10/13 个有
- `TextGenerateLTX2Prompt` —— 10/13 个有
- `ComfySwitchNode` —— 9/13 个有
- `PrimitiveBoolean` —— 9/13 个有
- `LTXVAddGuide` —— 8/13 个有
- `LTXVCropGuides` —— 8/13 个有
- `PreviewAny` —— 8/13 个有
- `ResizeImageMaskNode` —— 8/13 个有
- `SamplerEulerAncestral` —— 8/13 个有
- `VHS_VideoCombine` —— 8/13 个有
- `CreateVideo` —— 7/13 个有
- `SaveVideo` —— 7/13 个有
- `GetImageSize` —— 6/13 个有
- `KSamplerSelect` —— 6/13 个有
- `LTXVLatentUpsampler` —— 6/13 个有
- `LatentUpscaleModelLoader` —— 6/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/13 个有
- `LTXVImgToVideoInplace` —— 4/13 个有
- `easy showAnything` —— 3/13 个有
- `ImageFromBatch` —— 2/13 个有
- `SaveAudio` —— 2/13 个有
- `SaveImage` —— 2/13 个有
- `easy cleanGpuUsed` —— 2/13 个有
- `CR Prompt Text` —— 1/13 个有
- `Fast Groups Bypasser (rgthree)` —— 1/13 个有
- `RH_LLMAPI_Pro_Node` —— 1/13 个有
- `ShellAgentPluginOutputText` —— 1/13 个有
- `Text` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 13 | 100% |
| 高度 | 25 | 25 - 25 | 13 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，13 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，13 个样本，取值集中（一致性 100%）
