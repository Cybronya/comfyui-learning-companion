---
name: unknown_workflow_upscale_latent_upscale_lora_9
type: Unknown Workflow
frequency: 17
level: strong
coverage: 0.861941
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, ImageScaleBy, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [视频生成/文生视频/CG少女风格文生视频_图生视频2合1自由切换版-LTX2.3_2038339473397784578.json, 视频生成/文生视频/LTX2.0 图生视频工作流（48G）_2008873261282627585.json, 视频生成/文生视频/LTX2.3  图生视频  超强开源视频模型_2044752658199744513.json, 视频生成/文生视频/LTX2.3 图生视频 音画同步   万能图生视频 优化加速版_2030092123399262210.json, 视频生成/文生视频/LTX2.3 超强图生视频 ZJ_2047879462942937089.json, 视频生成/文生视频/LTX2.3-文生视频_2066069178989240321.json, 视频生成/文生视频/LTX2.3低显存图生视频生成ai漫剧短剧视频 保持人物一致性性价比超高LTX2.3-首尾帧视频_2031606525608857601.json, 视频生成/文生视频/LTX2.3文生视频_2029632742534680578.json, 视频生成/文生视频/LTX2.3文生视频_2029814808173879298.json, 视频生成/文生视频/LTX2.3文生视频_2029929479480545282.json, 视频生成/文生视频/LTX2.3文生视频_2030904134915854338.json, 视频生成/文生视频/LTX2.3文生视频_2032363107607126018.json, 视频生成/文生视频/LTX2.3文生视频_2033356584612532225.json, 视频生成/文生视频/LTX2.3文生视频_2040990526287122433.json, 视频生成/文生视频/LTX2.3音视频同步，数字人、图生视频、文生视频高清画质工作流_2030665052986023938.json, 视频生成/文生视频/图生视频极速版LTX2.3  数字人话 唱歌对口型_2044214545626963970.json, 视频生成/文生视频/🐱LTX2.3图生视频工作流_2030298909729361921.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_9

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（视频生成/文生视频/CG少女风格文生视频_图生视频2合1自由切换版-LTX2.3_2038339473397784578.json、视频生成/文生视频/LTX2.0 图生视频工作流（48G）_2008873261282627585.json、视频生成/文生视频/LTX2.3  图生视频  超强开源视频模型_2044752658199744513.json、视频生成/文生视频/LTX2.3 图生视频 音画同步   万能图生视频 优化加速版_2030092123399262210.json、视频生成/文生视频/LTX2.3 超强图生视频 ZJ_2047879462942937089.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 17 个 workflow 都包含：
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
- `RandomNoise`
- `SamplerCustomAdvanced`

**可变部分**（部分 workflow 才有）：
- `KSampler` —— 16/17 个有
- `PrimitiveInt` —— 16/17 个有
- `CreateVideo` —— 15/17 个有
- `DualCLIPLoader` —— 15/17 个有
- `PreviewAny` —— 15/17 个有
- `SaveVideo` —— 15/17 个有
- `TextGenerateLTX2Prompt` —— 15/17 个有
- `VAEDecode` —— 14/17 个有
- `PrimitiveFloat` —— 10/17 个有
- `LTXVImgToVideoInplace` —— 9/17 个有
- `LTXVPreprocess` —— 9/17 个有
- `LoadImage` —— 9/17 个有
- `ResizeImagesByLongerEdge` —— 9/17 个有
- `VAEDecodeTiled` —— 9/17 个有
- `ResizeImageMaskNode` —— 7/17 个有
- `VHS_VideoCombine` —— 3/17 个有
- `CR Text` —— 2/17 个有
- `INTConstant` —— 2/17 个有
- `ManualSigmas` —— 2/17 个有
- `PreviewImage` —— 2/17 个有
- `PrimitiveBoolean` —— 2/17 个有
- `BasicScheduler` —— 1/17 个有
- `CM_FloatToInt` —— 1/17 个有
- `Fast Groups Bypasser (rgthree)` —— 1/17 个有
- `ImageResizeKJv2` —— 1/17 个有
- `LTX2SamplingPreviewOverride` —— 1/17 个有
- `LTX2_NAG` —— 1/17 个有
- `LTXVChunkFeedForward` —— 1/17 个有
- `LTXVImgToVideoConditionOnly` —— 1/17 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/17 个有
- `ModelPatchTorchSettings` —— 1/17 个有
- `PathchSageAttentionKJ` —— 1/17 个有
- `PrimitiveStringMultiline` —— 1/17 个有
- `RH_LLMAPI_Pro_Node` —— 1/17 个有
- `Seed (rgthree)` —— 1/17 个有
- `SetNode` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 16 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 16 | 100% |
| 采样算法 | euler | - | 16 | 100% |
| 调度器 | simple | - | 16 | 100% |
| 重绘幅度 | 0.375 | 0.35 - 0.4 | 16 | 93% |
| 宽度 | 97 | 97 - 97 | 17 | 100% |
| 高度 | 25 | 25 - 25 | 17 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 3/17 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，16 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，16 个样本，一致性 100%
- 调度器 最常用 simple，16 个样本，一致性 100%
- 重绘幅度 中位数 0.375，观测区间 0.35 - 0.4，16 个样本，取值集中（一致性 93%）
- 宽度 中位数 97，观测区间 97 - 97，17 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，17 个样本，取值集中（一致性 100%）
- 高发问题（17/17 个样本）：Steps较低可能导致细节不足
