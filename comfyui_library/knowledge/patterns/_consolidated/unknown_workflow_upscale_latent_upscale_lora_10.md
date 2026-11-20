---
name: unknown_workflow_upscale_latent_upscale_lora_10
type: Unknown Workflow
frequency: 19
level: strong
coverage: 0.907632
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, CreateVideo, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, ImageScaleBy, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, SaveVideo]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/反推提示词/62wenshengship_2045718035482288130.json, 图片生成/反推提示词/66wenshengshipyouhua_2052441849985552385.json, 图片生成/反推提示词/71tushengshiping_2052472236904333314.json, 图片生成/反推提示词/75wsspok_2052623589165281281.json, 图片生成/反推提示词/LTX2.3图生视频（高流畅）_2053348936554950657.json, 图片生成/反推提示词/LTX2.3文生视频_2045702587688685569.json, 图片生成/图生图/LTX2.3   图生视频 最强开源_2063599059453173762.json, 图片生成/图生图/LTX2.3+图生视频+最强开源_2087714145914408962.json, 图片生成/图生图/LTX2.3图生视频_2056533481278238722.json, 图片生成/图生图/图生视频_2052557107181965314.json, 图片生成/图生图/视频生成  LTX2.3 图生视频 最强开源_2075155399342379010.json, 图片生成/图生图/视频生成工作流v1.0++视频+++LTX2.3+图生视频+最强开源 (1)_2085263449885601793.json, 图片生成/文生图/YJ-APP-LTX2.3图生视频_2038208858090381313.json, 视频生成/图生视频/LTX2.3 图生视频 对镜自拍_2071503238007975937.json, 视频生成/图生视频/LTX2.3 图生视频_2059205820864352257.json, 视频生成/图生视频/LTX2.3图生视频Sparkvideo2.0平替短剧漫剧短视频工作流_2029890967838400513.json, 视频生成/图生视频/LTX2.3图生视频Sparkvideo2.0平替短剧漫剧短视频工作流_2031942517490458625.json, 视频生成/图生视频/LTX2.3图生视频_2029651380855640065.json, 视频生成/图生视频/LTX2.3图生视频_2029732416155295745.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_10

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（图片生成/反推提示词/62wenshengship_2045718035482288130.json、图片生成/反推提示词/66wenshengshipyouhua_2052441849985552385.json、图片生成/反推提示词/71tushengshiping_2052472236904333314.json、图片生成/反推提示词/75wsspok_2052623589165281281.json、图片生成/反推提示词/LTX2.3图生视频（高流畅）_2053348936554950657.json…）

- **类型**：Unknown Workflow
- **样本数**：19
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 19 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `CreateVideo`
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
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `DualCLIPLoader` —— 18/19 个有
- `KSampler` —— 18/19 个有
- `PrimitiveInt` —— 18/19 个有
- `TextGenerateLTX2Prompt` —— 18/19 个有
- `PreviewAny` —— 17/19 个有
- `VAEDecode` —— 16/19 个有
- `LTXVImgToVideoInplace` —— 15/19 个有
- `LTXVPreprocess` —— 15/19 个有
- `LoadImage` —— 15/19 个有
- `ResizeImagesByLongerEdge` —— 15/19 个有
- `ResizeImageMaskNode` —— 13/19 个有
- `RTXVideoSuperResolution` —— 7/19 个有
- `JjkText` —— 6/19 个有
- `Int` —— 5/19 个有
- `SimpleMath+` —— 5/19 个有
- `Text` —— 5/19 个有
- `PrimitiveFloat` —— 4/19 个有
- `VAEDecodeTiled` —— 4/19 个有
- `RHHiddenNodes` —— 3/19 个有
- `DF_Int_to_Float` —— 2/19 个有
- `scale` —— 2/19 个有
- `INTConstant` —— 1/19 个有
- `ImageFromBatch` —— 1/19 个有
- `ImpactInt` —— 1/19 个有
- `ImpactSwitch` —— 1/19 个有
- `ManualSigmas` —— 1/19 个有
- `MathExpression|pysssss` —— 1/19 个有
- `PrimitiveStringMultiline` —— 1/19 个有
- `RH_LLMAPI_NODE` —— 1/19 个有
- `SaveImage` —— 1/19 个有
- `TextInput_` —— 1/19 个有
- `easy showAnything` —— 1/19 个有
- `floatToInt _O` —— 1/19 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 19 | 100% |
| 高度 | 25 | 25 - 25 | 19 | 100% |
| 采样步数 | 4 | 4 - 4 | 18 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 18 | 100% |
| 采样算法 | euler | - | 18 | 100% |
| 调度器 | simple | - | 18 | 100% |
| 重绘幅度 | 0.35 | 0.35 - 0.4 | 18 | 95% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/19 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 3/19 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，19 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，19 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，18 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，18 个样本，一致性 100%
- 调度器 最常用 simple，18 个样本，一致性 100%
- 重绘幅度 中位数 0.35，观测区间 0.35 - 0.4，18 个样本，取值集中（一致性 95%）
- 高发问题（18/19 个样本）：Steps较低可能导致细节不足
