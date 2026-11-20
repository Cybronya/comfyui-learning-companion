---
name: unknown_workflow_upscale_latent_upscale_lora_4
type: Unknown Workflow
frequency: 27
level: strong
coverage: 0.846037
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, ImageScaleBy, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, PrimitiveInt, RandomNoise, SamplerCustomAdvanced]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [视频生成/文生视频/LTX-2.3  文生视频 MV视频_2037159958583709697.json, 视频生成/文生视频/LTX-2.3-T2V-文生音视频_2029816055798964226.json, 视频生成/文生视频/LTX-2.3-T2V_2043499040456839169.json, 视频生成/文生视频/LTX-2.3-图生视频_文生视频_2030340655863570434.json, 视频生成/文生视频/LTX-2.3-文生视频 长视频_2032729674383626241.json, 视频生成/文生视频/LTX-2.3-文生视频_2031191268642004993.json, 视频生成/文生视频/LTX-2.3-文生视频_2037040523202007042.json, 视频生成/文生视频/LTX2.3  图生视频  超强开源视频模型_2044752658199744513.json, 视频生成/文生视频/LTX2.3 图生视频 音画同步   万能图生视频 优化加速版_2030092123399262210.json, 视频生成/文生视频/LTX2.3 文生视频 v1.1+VBVR_2030533262598213634.json, 视频生成/文生视频/LTX2.3 文生视频_2029978568398213122.json, 视频生成/文生视频/LTX2.3 文生视频工作流_2029878986880327681.json, 视频生成/文生视频/LTX2.3 文生视频工作流_2031938415188516866.json, 视频生成/文生视频/LTX2.3 超强图生视频 ZJ_2047879462942937089.json, 视频生成/文生视频/LTX2.3-文生视频_2066069178989240321.json, 视频生成/文生视频/LTX2.3图生视频短剧漫剧短视频工作流_2063583232725180417.json, 视频生成/文生视频/LTX2.3文生视频_2029632742534680578.json, 视频生成/文生视频/LTX2.3文生视频_2029814808173879298.json, 视频生成/文生视频/LTX2.3文生视频_2029929479480545282.json, 视频生成/文生视频/LTX2.3文生视频_2030904134915854338.json, 视频生成/文生视频/LTX2.3文生视频_2032363107607126018.json, 视频生成/文生视频/LTX2.3文生视频_2033356584612532225.json, 视频生成/文生视频/LTX2.3文生视频_2040990526287122433.json, 视频生成/文生视频/LTX2.3音视频同步，数字人、图生视频、文生视频高清画质工作流_2030665052986023938.json, 视频生成/文生视频/Ltx2.3反推提示词 文生音视频_2044962799889162242.json, 视频生成/文生视频/NVFP4非蒸馏高质量LXT2镜头控制图生视频_2009643815291854849.json, 视频生成/文生视频/非蒸馏高质量LXT2镜头控制图生视频_2009191002166267905.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_4

> 由 `engine/knowledge_consolidation` 从 27 个 workflow 归纳得出（视频生成/文生视频/LTX-2.3  文生视频 MV视频_2037159958583709697.json、视频生成/文生视频/LTX-2.3-T2V-文生音视频_2029816055798964226.json、视频生成/文生视频/LTX-2.3-T2V_2043499040456839169.json、视频生成/文生视频/LTX-2.3-图生视频_文生视频_2030340655863570434.json、视频生成/文生视频/LTX-2.3-文生视频 长视频_2032729674383626241.json…）

- **类型**：Unknown Workflow
- **样本数**：27
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 27 个 workflow 都包含：
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
- `CreateVideo` —— 25/27 个有
- `LTXVCropGuides` —— 25/27 个有
- `SaveVideo` —— 25/27 个有
- `DualCLIPLoader` —— 24/27 个有
- `PreviewAny` —— 24/27 个有
- `TextGenerateLTX2Prompt` —— 24/27 个有
- `KSampler` —— 22/27 个有
- `PrimitiveFloat` —— 22/27 个有
- `VAEDecodeTiled` —— 21/27 个有
- `VAEDecode` —— 19/27 个有
- `LoadImage` —— 9/27 个有
- `LTXVImgToVideoInplace` —— 8/27 个有
- `LTXVPreprocess` —— 8/27 个有
- `ResizeImagesByLongerEdge` —— 8/27 个有
- `ResizeImageMaskNode` —— 6/27 个有
- `ManualSigmas` —— 5/27 个有
- `Fast Groups Bypasser (rgthree)` —— 3/27 个有
- `ImpactExecutionOrderController` —— 3/27 个有
- `Text` —— 3/27 个有
- `CM_FloatToInt` —— 2/27 个有
- `CR Text` —— 2/27 个有
- `LTXVSpatioTemporalTiledVAEDecode` —— 2/27 个有
- `PrimitiveStringMultiline` —— 2/27 个有
- `VHS_VideoCombine` —— 2/27 个有
- `CM_IntToFloat` —— 1/27 个有
- `CR Prompt Text` —— 1/27 个有
- `PreviewImage` —— 1/27 个有
- `Seed (rgthree)` —— 1/27 个有
- `UnetLoaderGGUF` —— 1/27 个有
- `VAELoader` —— 1/27 个有
- `VAELoaderKJ` —— 1/27 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 22 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 22 | 100% |
| 采样算法 | euler | - | 22 | 100% |
| 调度器 | simple | - | 22 | 100% |
| 重绘幅度 | 0.4 | 0.35 - 0.4 | 22 | 94% |
| 宽度 | 97 | 97 - 121 | 27 | 94% |
| 高度 | 25 | 25 - 25 | 27 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 24/27 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 4/27 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，22 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，22 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，22 个样本，一致性 100%
- 调度器 最常用 simple，22 个样本，一致性 100%
- 重绘幅度 中位数 0.4，观测区间 0.35 - 0.4，22 个样本，取值集中（一致性 94%）
- 宽度 中位数 97，观测区间 97 - 121，27 个样本，取值集中（一致性 94%）
- 高度 中位数 25，观测区间 25 - 25，27 个样本，取值集中（一致性 100%）
- 高发问题（24/27 个样本）：Steps较低可能导致细节不足
