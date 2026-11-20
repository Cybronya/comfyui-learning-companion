---
name: unknown_workflow_sampler_clip_unet_17
type: Unknown Workflow
frequency: 28
level: strong
coverage: 0.841821
common_nodes: [CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLTXVLatentVideo, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVPreprocess, LTXVSeparateAVLatent, LoadImage, ManualSigmas, PrimitiveInt, RandomNoise, ResizeImageMaskNode, SamplerCustomAdvanced, UNETLoader, VAEDecodeTiled, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/LTX-2.5图生视频（提示词指南）_2087560099316453378.json, 视频生成/图生视频/LTX-2.5首尾帧生视频（提示词指南）_2087552277501530114.json, 视频生成/图生视频/LTX2.5 图生视频 视频生成  二次采样_2087976019419557889.json, 视频生成/图生视频/LTX2.5 图生视频 视频生成  二次采样_2088139583937662977.json, 视频生成/图生视频/LTX2.5 图生视频 视频生成  二次采样_2088145977638215681.json, 视频生成/图生视频/LTX2.5 图生视频 视频生成  二次采样_2088158559048650753.json, 视频生成/图生视频/LTX2.5 图生视频 视频生成  二次采样_2088327502329638913.json, 视频生成/图生视频/LTX2.5 图生视频 视频生成  二次采样_2088508046191452161.json, 视频生成/图生视频/LTX2.5 图生视频 视频生成  二次采样_2088508469056991233.json, 视频生成/图生视频/LTX2.5 图生视频 视频生成  二次采样_2088516027708694530.json, 视频生成/图生视频/LTX2.5 图生视频 视频生成  二次采样_2089038486316871681.json, 视频生成/图生视频/LTX2.5 图生视频 视频生成  二次采样_2089204054537891841.json, 视频生成/图生视频/LTX2.5 图生视频 视频生成  二次采样_2089770769709621250.json, 视频生成/图生视频/LTX2.5 图生视频 视频生成  二次采样_2091566207215431682.json, 视频生成/图生视频/LTX2.5 图生视频 视频生成  二次采样_2093745280222064641.json, 视频生成/图生视频/LTX2.5 图生视频 视频生成  二次采样_2102437970862231554.json, 视频生成/图生视频/LTX2.5 图生视频 视频生成_2091803227397378050.json, 视频生成/图生视频/LTX2.5-图生视频_2087412034005725185.json, 视频生成/图生视频/LTX2.5-图生视频_2087515101900402690.json, 视频生成/图生视频/LTX2.5_i2v_2092791658453753857.json, 视频生成/图生视频/LTX2.5图生视频 -自动扩写提示词-高质量直出1K_2087739505318129665.json, 视频生成/图生视频/LTX2.5图生视频2608_2095393021843038209.json, 视频生成/图生视频/LTX2.5图生视频_2087332188219068417.json, 视频生成/图生视频/LTX2.5图生视频_2087422859705667585.json, 视频生成/图生视频/LTX2.5图生视频_2087443699126071298.json, 视频生成/图生视频/LTX2.5图生视频_2087526346007339010.json, 视频生成/图生视频/LTX2.5图生视频一致性强化版+提示词优化_2087504758146949121.json, 视频生成/图生视频/LTX2.5图生视频一致性强化版V1_2087405102549262338.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_17

> 由 `engine/knowledge_consolidation` 从 28 个 workflow 归纳得出（视频生成/图生视频/LTX-2.5图生视频（提示词指南）_2087560099316453378.json、视频生成/图生视频/LTX-2.5首尾帧生视频（提示词指南）_2087552277501530114.json、视频生成/图生视频/LTX2.5 图生视频 视频生成  二次采样_2087976019419557889.json、视频生成/图生视频/LTX2.5 图生视频 视频生成  二次采样_2088139583937662977.json、视频生成/图生视频/LTX2.5 图生视频 视频生成  二次采样_2088145977638215681.json…）

- **类型**：Unknown Workflow
- **样本数**：28
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 28 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `ManualSigmas`
- `PrimitiveInt`
- `RandomNoise`
- `ResizeImageMaskNode`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LTXVDualCFGGuider` —— 27/28 个有
- `LTXVImgToVideoInplace` —— 27/28 个有
- `LTXVLatentUpsampler` —— 26/28 个有
- `LatentUpscaleModelLoader` —— 26/28 个有
- `PrimitiveBoolean` —— 26/28 个有
- `ResolutionSelector` —— 26/28 个有
- `CreateVideo` —— 25/28 个有
- `SaveVideo` —— 25/28 个有
- `TextGenerateLTX2Prompt` —— 25/28 个有
- `PrimitiveStringMultiline` —— 24/28 个有
- `ComfySwitchNode` —— 22/28 个有
- `PurgeVRAM_UTK` —— 15/28 个有
- `PreviewAny` —— 8/28 个有
- `VHS_VideoCombine` —— 5/28 个有
- `easy showAnything` —— 5/28 个有
- `RH_LLMAPI_Pro_Node` —— 4/28 个有
- `CR Text` —— 3/28 个有
- `DF_Get_image_size` —— 2/28 个有
- `Int` —— 2/28 个有
- `LTXFloatToInt` —— 2/28 个有
- `PreviewImage` —— 2/28 个有
- `PrimitiveFloat` —— 2/28 个有
- `CFGGuider` —— 1/28 个有
- `CR Prompt Text` —— 1/28 个有
- `FlashVSRNode` —— 1/28 个有
- `LTXVAddGuide` —— 1/28 个有
- `LTXVCropGuides` —— 1/28 个有
- `ShellAgentPluginOutputText` —— 1/28 个有
- `孤海注释` —— 1/28 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 121 | 28 | 94% |
| 高度 | 25 | 25 - 25 | 28 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 121，28 个样本，取值集中（一致性 94%）
- 高度 中位数 25，观测区间 25 - 25，28 个样本，取值集中（一致性 100%）
