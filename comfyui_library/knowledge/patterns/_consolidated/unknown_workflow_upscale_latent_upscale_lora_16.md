---
name: unknown_workflow_upscale_latent_upscale_lora_16
type: Unknown Workflow
frequency: 14
level: strong
coverage: 0.822714
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, ImageScaleBy, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, PrimitiveInt, RandomNoise, SamplerCustomAdvanced]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [视频生成/文生视频/LTX-2图_3图NVFP4首尾帧_2009643807456890881.json, 视频生成/文生视频/LTX-2图_3图首尾帧_2009549891193806850.json, 视频生成/文生视频/LTX2 文生视频_2008738820421853186.json, 视频生成/文生视频/LTX2 文生视频原版_2008509004686823425.json, 视频生成/文生视频/LTX2 文生视频原版自动提示词_2008719056999813121.json, 视频生成/文生视频/LTX2.3文生哭泣视频_2073302607023656962.json, 视频生成/文生视频/LTX2.3文生视频_2029632742534680578.json, 视频生成/文生视频/LTX2.3文生视频_2029814808173879298.json, 视频生成/文生视频/LTX2.3文生视频_2029929479480545282.json, 视频生成/文生视频/LTX2.3文生视频_2030904134915854338.json, 视频生成/文生视频/LTX2.3文生视频_2032363107607126018.json, 视频生成/文生视频/LTX2.3文生视频_2033356584612532225.json, 视频生成/文生视频/LTX2.3文生视频_2040990526287122433.json, 视频生成/文生视频/LTX2.3文生视频_2061743726724214786.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_16

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/文生视频/LTX-2图_3图NVFP4首尾帧_2009643807456890881.json、视频生成/文生视频/LTX-2图_3图首尾帧_2009549891193806850.json、视频生成/文生视频/LTX2 文生视频_2008738820421853186.json、视频生成/文生视频/LTX2 文生视频原版_2008509004686823425.json、视频生成/文生视频/LTX2 文生视频原版自动提示词_2008719056999813121.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 14 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyImage`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `ImageScaleBy`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 12/14 个有
- `PrimitiveFloat` —— 12/14 个有
- `SaveVideo` —— 12/14 个有
- `VAEDecodeTiled` —— 12/14 个有
- `KSampler` —— 9/14 个有
- `PreviewAny` —— 9/14 个有
- `DualCLIPLoader` —— 8/14 个有
- `TextGenerateLTX2Prompt` —— 8/14 个有
- `VAEDecode` —— 6/14 个有
- `ManualSigmas` —— 5/14 个有
- `FloatConstant` —— 2/14 个有
- `INTConstant` —— 2/14 个有
- `ImageResizeKJv2` —— 2/14 个有
- `LTXVFirstLastFrameControl_TTP` —— 2/14 个有
- `LTXVMiddleFrame_TTP` —— 2/14 个有
- `LTXVPreprocess` —— 2/14 个有
- `LTXVSpatioTemporalTiledVAEDecode` —— 2/14 个有
- `LoadImage` —— 2/14 个有
- `ResizeImagesByLongerEdge` —— 2/14 个有
- `VHS_VideoCombine` —— 2/14 个有
- `CR Text` —— 1/14 个有
- `Int` —— 1/14 个有
- `PrimitiveStringMultiline` —— 1/14 个有
- `RH_LLMAPI_NODE` —— 1/14 个有
- `SimpleMath+` —— 1/14 个有
- `Wan_video_prompt_generator` —— 1/14 个有
- `easy cleanGpuUsed` —— 1/14 个有
- `easy convertAnything` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 14 | 100% |
| 高度 | 25 | 25 - 25 | 14 | 100% |
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 0.4 | 0.4 - 0.4 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 3/14 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，14 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，14 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 0.4，观测区间 0.4 - 0.4，9 个样本，取值集中（一致性 100%）
- 高发问题（9/14 个样本）：Steps较低可能导致细节不足
