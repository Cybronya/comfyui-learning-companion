---
name: unknown_workflow_lora_sampler_clip_208
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.921
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVPreprocess, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveBoolean, PrimitiveFloat, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SaveVideo]
problems: []
missing: []
members: [视频生成/图生视频/lix2.3图生视频（首帧）_2069607607387639810.json, 视频生成/文生视频/LTX 2.3 ComfyUI：三阶段 4K 工作流程（修复视频失真）_2038095391647862786.json, 视频生成/文生视频/LTX 2.3 的 100% 实力释放三阶段采样图生视频工作流_2033775150256103426.json, 视频生成/文生视频/LTX-2.3_基础文生图生视频双采样_2080467787033694209.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_208

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/lix2.3图生视频（首帧）_2069607607387639810.json、视频生成/文生视频/LTX 2.3 ComfyUI：三阶段 4K 工作流程（修复视频失真）_2038095391647862786.json、视频生成/文生视频/LTX 2.3 的 100% 实力释放三阶段采样图生视频工作流_2033775150256103426.json、视频生成/文生视频/LTX-2.3_基础文生图生视频双采样_2080467787033694209.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoConditionOnly`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `LTXVLatentUpsampler` —— 3/4 个有
- `LatentUpscaleModelLoader` —— 3/4 个有
- `CM_FloatToInt` —— 2/4 个有
- `GuiderParameters` —— 2/4 个有
- `LTXFloatToInt` —— 2/4 个有
- `LTXVTiledVAEDecode` —— 2/4 个有
- `MultimodalGuider` —— 2/4 个有
- `ResizeImageMaskNode` —— 2/4 个有
- `VAEDecodeTiled` —— 2/4 个有
- `ClownSampler_Beta` —— 1/4 个有
- `GemmaAPITextEncode` —— 1/4 个有
- `INTConstant` —— 1/4 个有
- `Image_Resize_longsize` —— 1/4 个有
- `LTXVScheduler` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/4 个有
- `PrimitiveString` —— 1/4 个有
- `SaveImage` —— 1/4 个有
- `image_scale_pixel_v2` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 4 | 100% |
| 高度 | 25 | 25 - 25 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，4 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，4 个样本，取值集中（一致性 100%）
