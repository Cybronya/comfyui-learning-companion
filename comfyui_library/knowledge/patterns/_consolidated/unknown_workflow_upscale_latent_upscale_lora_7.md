---
name: unknown_workflow_upscale_latent_upscale_lora_7
type: Unknown Workflow
frequency: 20
level: strong
coverage: 0.86615
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [视频生成/图生视频/LTX2.3图生视频（带教学）_2032347634245050369.json, 视频生成/图生视频/LTX2.3图生视频，基于爱屋研究所_2035236470159577090.json, 视频生成/图生视频/LTX2.3图生音画同步运镜视频_2030057331559505922.json, 视频生成/图生视频/LTX2.3声画同步开源模型_2030149051974422529.json, 视频生成/图生视频/LTX2.3批量图生视频_2046078723471974401.json, 视频生成/图生视频/LTX2.3画音同步图生视频-基本无字幕-手动提示词版_2033079847349653505.json, 视频生成/图生视频/LTX2.3短剧漫剧短视频图生视频人物一致性_2081705419873017857.json, 视频生成/图生视频/LTX2.3音画同步随机动作提示词版 图生视频_2082783625594105858.json, 视频生成/图生视频/LTX2.3音画同步随机动作提示词版+图生视频_2068601277344477186.json, 视频生成/图生视频/LTX2.3高质量图生视频_2083082295870840833.json, 视频生成/图生视频/LTXV2.3 图生视频_2030258370564857858.json, 视频生成/图生视频/LTXV2.3 图生视频_2031186570014887938.json, 视频生成/图生视频/ltx_final (2)_2052091652172468226.json, 视频生成/图生视频/ltx_final_2052083920916762625.json, 视频生成/图生视频/极速图生视频 LTX2.3（随机提示词）B站艾橘溪!_2068335067583307778.json, 视频生成/图生视频/音画同步+图生视频 LTX2.3（随机动作提示词）_2073934539000475650.json, 视频生成/图生视频/音画同步+图生视频 LTX2.3（随机动作提示词）_2073938374595010562.json, 视频生成/图生视频/音画同步+图生视频 LTX2.3（随机动作提示词）_2075025699286634498.json, 视频生成/图生视频/音画同步+图生视频+LTX2.3（随机动作提示词）_2074378391851192322.json, 视频生成/图生视频/音画同步+图生视频+LTX2.3（随机动作提示词）_2074389452264398849.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_7

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（视频生成/图生视频/LTX2.3图生视频（带教学）_2032347634245050369.json、视频生成/图生视频/LTX2.3图生视频，基于爱屋研究所_2035236470159577090.json、视频生成/图生视频/LTX2.3图生音画同步运镜视频_2030057331559505922.json、视频生成/图生视频/LTX2.3声画同步开源模型_2030149051974422529.json、视频生成/图生视频/LTX2.3批量图生视频_2046078723471974401.json…）

- **类型**：Unknown Workflow
- **样本数**：20
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 20 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyImage`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`

**可变部分**（部分 workflow 才有）：
- `ImageScaleBy` —— 19/20 个有
- `LTXVScheduler` —— 19/20 个有
- `LoadImage` —— 19/20 个有
- `PrimitiveInt` —— 19/20 个有
- `VAEDecode` —— 19/20 个有
- `PreviewAny` —— 18/20 个有
- `ResizeImageMaskNode` —— 18/20 个有
- `TextGenerateLTX2Prompt` —— 18/20 个有
- `KSampler` —— 17/20 个有
- `DualCLIPLoader` —— 16/20 个有
- `Text` —— 13/20 个有
- `CreateVideo` —— 10/20 个有
- `GetNode` —— 10/20 个有
- `SaveVideo` —— 10/20 个有
- `SetNode` —— 10/20 个有
- `VHS_VideoCombine` —— 10/20 个有
- `Int` —— 9/20 个有
- `SimpleMath+` —— 9/20 个有
- `DF_Int_to_Float` —— 8/20 个有
- `ImageResizeKJv2` —— 8/20 个有
- `ManualSigmas` —— 3/20 个有
- `CR Text` —— 2/20 个有
- `CR Text Replace` —— 2/20 个有
- `MultiTextConcatenate` —— 2/20 个有
- `RH_LLMAPI_Pro_Node` —— 2/20 个有
- `RH_Utils` —— 2/20 个有
- `easy showAnything` —— 2/20 个有
- `DapaoImageAspectRatioResizeNode` —— 1/20 个有
- `HAIGC_LoadImagesFromZip` —— 1/20 个有
- `HAIGC_SaveImagesToZip` —— 1/20 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/20 个有
- `PreviewImage` —— 1/20 个有
- `PromptBatchQueue` —— 1/20 个有
- `RHBatchImages:` —— 1/20 个有
- `VAEDecodeTiled` —— 1/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 17 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 17 | 100% |
| 采样算法 | euler | - | 17 | 100% |
| 调度器 | simple | - | 17 | 100% |
| 重绘幅度 | 0.35 | 0.35 - 0.35 | 17 | 100% |
| 宽度 | 97 | 97 - 97 | 20 | 100% |
| 高度 | 25 | 24 - 25 | 20 | 99% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/20 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 1/20 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，17 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，17 个样本，一致性 100%
- 调度器 最常用 simple，17 个样本，一致性 100%
- 重绘幅度 中位数 0.35，观测区间 0.35 - 0.35，17 个样本，取值集中（一致性 100%）
- 宽度 中位数 97，观测区间 97 - 97，20 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 24 - 25，20 个样本，取值集中（一致性 99%）
- 高发问题（17/20 个样本）：Steps较低可能导致细节不足
