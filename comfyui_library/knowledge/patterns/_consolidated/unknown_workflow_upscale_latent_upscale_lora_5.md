---
name: unknown_workflow_upscale_latent_upscale_lora_5
type: Unknown Workflow
frequency: 32
level: strong
coverage: 0.891281
common_nodes: [CFGGuider, CLIPTextEncode, CreateVideo, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SaveVideo]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/2031025711103873026.json, 视频生成/图生视频/2029651380855640065.json, 视频生成/图生视频/2029732416155295745.json, 视频生成/图生视频/2029823149398827010.json, 视频生成/图生视频/2029938786079084546.json, 视频生成/图生视频/2029943442415034369.json, 视频生成/图生视频/2030295867214794753.json, 视频生成/图生视频/2032301246597570562.json, 视频生成/图生视频/2033385858308513793.json, 视频生成/图生视频/2043172438292303874.json, 视频生成/图生视频/2043525547841556482.json, 视频生成/图生视频/2045494998765936642.json, 视频生成/图生视频/2046935031586758657.json, 视频生成/图生视频/2047144762221797378.json, 视频生成/图生视频/2047212324209041410.json, 视频生成/图生视频/2032347634245050369.json, 视频生成/图生视频/2035236470159577090.json, 视频生成/图生视频/2030057331559505922.json, 视频生成/图生视频/2030149051974422529.json, 视频生成/图生视频/LTX2.3高质量图生视频_2083082295870840833.json, 视频生成/图生视频/2030258370564857858.json, 视频生成/图生视频/2031186570014887938.json, 视频生成/图生视频/2028654571588952066.json, 视频生成/文生视频/LTX-2.3-图生视频_文生视频_2030340655863570434.json, 视频生成/文生视频/LTX2.3 文生视频 v1.1+VBVR_2030533262598213634.json, 视频生成/文生视频/LTX2.3 文生视频_2029978568398213122.json, 视频生成/文生视频/LTX2.3 文生视频工作流_2029878986880327681.json, 视频生成/文生视频/LTX2.3 文生视频工作流_2031938415188516866.json, 视频生成/文生视频/LTX2.3低显存图生视频生成ai漫剧短剧视频 保持人物一致性性价比超高LTX2.3-首尾帧视频_2031606525608857601.json, 视频生成/文生视频/LTX2.3图生视频短剧漫剧短视频工作流_2063583232725180417.json, 视频生成/文生视频/LTX2.3音视频同步，数字人、图生视频、文生视频高清画质工作流_2030665052986023938.json, 视频生成/文生视频/图生视频极速版LTX2.3  数字人话 唱歌对口型_2044214545626963970.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_5

> 由 `engine/knowledge_consolidation` 从 32 个 workflow 归纳得出（视频生成/图生视频/2031025711103873026.json、视频生成/图生视频/2029651380855640065.json、视频生成/图生视频/2029732416155295745.json、视频生成/图生视频/2029823149398827010.json、视频生成/图生视频/2029938786079084546.json…）

- **类型**：Unknown Workflow
- **样本数**：32
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 32 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CreateVideo`
- `EmptyImage`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 31/32 个有
- `ImageScaleBy` —— 31/32 个有
- `LTXAVTextEncoderLoader` —— 31/32 个有
- `LTXVAudioVAELoader` —— 31/32 个有
- `LTXVCropGuides` —— 31/32 个有
- `LTXVScheduler` —— 31/32 个有
- `VAEDecode` —— 31/32 个有
- `PreviewAny` —— 29/32 个有
- `TextGenerateLTX2Prompt` —— 29/32 个有
- `KSampler` —— 28/32 个有
- `LTXVImgToVideoInplace` —— 28/32 个有
- `LTXVPreprocess` —— 28/32 个有
- `LoadImage` —— 28/32 个有
- `ResizeImagesByLongerEdge` —— 28/32 个有
- `DualCLIPLoader` —— 27/32 个有
- `ResizeImageMaskNode` —— 27/32 个有
- `PrimitiveFloat` —— 7/32 个有
- `VAEDecodeTiled` —— 7/32 个有
- `Text` —— 5/32 个有
- `ManualSigmas` —— 4/32 个有
- `PrimitiveStringMultiline` —— 3/32 个有
- `CR SDXL Aspect Ratio` —— 1/32 个有
- `CR Text` —— 1/32 个有
- `CR Text Concatenate` —— 1/32 个有
- `IntToString` —— 1/32 个有
- `PrimitiveString` —— 1/32 个有
- `RH_LLMAPI_NODE` —— 1/32 个有
- `RH_LLMAPI_Pro_Node` —— 1/32 个有
- `RH_Translator` —— 1/32 个有
- `StringReplace` —— 1/32 个有
- `Text _O` —— 1/32 个有
- `UnetLoaderGGUF` —— 1/32 个有
- `VAELoaderKJ` —— 1/32 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 32 | 100% |
| 高度 | 25 | 24 - 25 | 32 | 99% |
| 采样步数 | 4 | 4 - 4 | 28 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 28 | 100% |
| 采样算法 | euler | - | 28 | 100% |
| 调度器 | simple | - | 28 | 100% |
| 重绘幅度 | 0.35 | 0.35 - 0.4 | 28 | 95% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 30/32 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，32 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 24 - 25，32 个样本，取值集中（一致性 99%）
- 采样步数 中位数 4，观测区间 4 - 4，28 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，28 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，28 个样本，一致性 100%
- 调度器 最常用 simple，28 个样本，一致性 100%
- 重绘幅度 中位数 0.35，观测区间 0.35 - 0.4，28 个样本，取值集中（一致性 95%）
- 高发问题（30/32 个样本）：Steps较低可能导致细节不足
