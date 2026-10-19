---
name: unknown_workflow_upscale_latent_upscale_lora_3
type: Unknown Workflow
frequency: 33
level: strong
coverage: 0.906152
common_nodes: [CFGGuider, CLIPTextEncode, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, PrimitiveInt, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [视频生成/图生视频/2031025711103873026.json, 视频生成/图生视频/2029651380855640065.json, 视频生成/图生视频/2029732416155295745.json, 视频生成/图生视频/2029823149398827010.json, 视频生成/图生视频/2029938786079084546.json, 视频生成/图生视频/2029943442415034369.json, 视频生成/图生视频/2030295867214794753.json, 视频生成/图生视频/2032301246597570562.json, 视频生成/图生视频/2033385858308513793.json, 视频生成/图生视频/2043172438292303874.json, 视频生成/图生视频/2043525547841556482.json, 视频生成/图生视频/2045494998765936642.json, 视频生成/图生视频/2046935031586758657.json, 视频生成/图生视频/2047144762221797378.json, 视频生成/图生视频/2047212324209041410.json, 视频生成/图生视频/2032347634245050369.json, 视频生成/图生视频/2035236470159577090.json, 视频生成/图生视频/2030057331559505922.json, 视频生成/图生视频/2030149051974422529.json, 视频生成/图生视频/2030258370564857858.json, 视频生成/图生视频/2031186570014887938.json, 视频生成/图生视频/2028654571588952066.json, 视频生成/图生视频/2052091652172468226.json, 视频生成/图生视频/2052083920916762625.json, 视频生成/图生视频/2079077960786735105.json, 视频生成/图生视频/视频生成  LTX2.3 图生视频 最强开源_2082716206850727937.json, 视频生成/图生视频/2079495472238129153.json, 视频生成/图生视频/2080734800876490753.json, 视频生成/图生视频/视频生成  视频   LTX2.3 图生视频 最强开源_2082761804425555970.json, 视频生成/图生视频/视频生成  视频   LTX2.3 图生视频 最强开源_2083263132746731521.json, 视频生成/图生视频/视频生成  视频   LTX2.3 图生视频 最强开源_2083951843780161538.json, 视频生成/图生视频/视频生成  视频   LTX2.3 图生视频 最强开源_2084169351942463489.json, 视频生成/图生视频/2078761295033225218.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_3

> 由 `engine/knowledge_consolidation` 从 33 个 workflow 归纳得出（视频生成/图生视频/2031025711103873026.json、视频生成/图生视频/2029651380855640065.json、视频生成/图生视频/2029732416155295745.json、视频生成/图生视频/2029823149398827010.json、视频生成/图生视频/2029938786079084546.json…）

- **类型**：Unknown Workflow
- **样本数**：33
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 33 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `EmptyImage`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveInt`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 32/33 个有
- `ImageScaleBy` —— 32/33 个有
- `LTXAVTextEncoderLoader` —— 32/33 个有
- `LTXVAudioVAELoader` —— 32/33 个有
- `LTXVCropGuides` —— 32/33 个有
- `LTXVScheduler` —— 32/33 个有
- `ResizeImageMaskNode` —— 32/33 个有
- `CreateVideo` —— 31/33 个有
- `SaveVideo` —— 31/33 个有
- `VAEDecode` —— 31/33 个有
- `TextGenerateLTX2Prompt` —— 30/33 个有
- `KSampler` —— 29/33 个有
- `DualCLIPLoader` —— 28/33 个有
- `PreviewAny` —— 27/33 个有
- `GetNode` —— 11/33 个有
- `SetNode` —— 11/33 个有
- `ManualSigmas` —— 4/33 个有
- `Text` —— 4/33 个有
- `RH_LLMAPI_Pro_Node` —— 3/33 个有
- `CR Text Replace` —— 2/33 个有
- `MultiTextConcatenate` —— 2/33 个有
- `PrimitiveStringMultiline` —— 2/33 个有
- `RH_Utils` —— 2/33 个有
- `VAEDecodeTiled` —— 2/33 个有
- `VHS_VideoCombine` —— 2/33 个有
- `CR SDXL Aspect Ratio` —— 1/33 个有
- `CR Text` —— 1/33 个有
- `CR Text Concatenate` —— 1/33 个有
- `IntToString` —— 1/33 个有
- `PrimitiveFloat` —— 1/33 个有
- `PrimitiveString` —— 1/33 个有
- `RH_LLMAPI_NODE` —— 1/33 个有
- `RH_Translator` —— 1/33 个有
- `StringReplace` —— 1/33 个有
- `Text _O` —— 1/33 个有
- `UnetLoaderGGUF` —— 1/33 个有
- `VAELoaderKJ` —— 1/33 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 33 | 100% |
| 高度 | 25 | 24 - 25 | 33 | 99% |
| 采样步数 | 4 | 4 - 4 | 29 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 29 | 100% |
| 采样算法 | euler | - | 29 | 100% |
| 调度器 | simple | - | 29 | 100% |
| 重绘幅度 | 0.35 | 0.35 - 0.35 | 29 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 29/33 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 1/33 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，33 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 24 - 25，33 个样本，取值集中（一致性 99%）
- 采样步数 中位数 4，观测区间 4 - 4，29 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，29 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，29 个样本，一致性 100%
- 调度器 最常用 simple，29 个样本，一致性 100%
- 重绘幅度 中位数 0.35，观测区间 0.35 - 0.35，29 个样本，取值集中（一致性 100%）
- 高发问题（29/33 个样本）：Steps较低可能导致细节不足
