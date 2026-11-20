---
name: unknown_workflow_upscale_latent_upscale_lora_7
type: Unknown Workflow
frequency: 22
level: strong
coverage: 0.912227
common_nodes: [CFGGuider, CLIPTextEncode, CreateVideo, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, ImageScaleBy, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, PrimitiveInt, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, SaveVideo]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/LTX2.3-I2V-GGUF_2031025711103873026.json, 视频生成/图生视频/LTX2.3图生视频_2030295867214794753.json, 视频生成/图生视频/LTX2.3图生视频_2031246343607422977.json, 视频生成/图生视频/LTX2.3图生视频_2032301246597570562.json, 视频生成/图生视频/LTX2.3图生视频_2033385858308513793.json, 视频生成/图生视频/LTX2.3图生视频_2043172438292303874.json, 视频生成/图生视频/LTX2.3图生视频_2043525547841556482.json, 视频生成/图生视频/LTX2.3图生视频_2045494998765936642.json, 视频生成/图生视频/LTX2.3图生视频_2046935031586758657.json, 视频生成/图生视频/LTX2.3图生视频_2047144762221797378.json, 视频生成/图生视频/LTX2.3图生视频_2047212324209041410.json, 视频生成/图生视频/LTX2.3高质量图生视频_2083082295870840833.json, 视频生成/图生视频/图生视频优化版  视频生成  视频   LTX2.3 最强开源_2079077960786735105.json, 视频生成/图生视频/视频生成  LTX2.3 图生视频 最强开源_2082716206850727937.json, 视频生成/图生视频/视频生成  视频   LTX2.3 图生视频 最强开源_2079495472238129153.json, 视频生成/图生视频/视频生成  视频   LTX2.3 图生视频 最强开源_2080734800876490753.json, 视频生成/图生视频/视频生成  视频   LTX2.3 图生视频 最强开源_2082761804425555970.json, 视频生成/图生视频/视频生成  视频   LTX2.3 图生视频 最强开源_2083263132746731521.json, 视频生成/图生视频/视频生成  视频   LTX2.3 图生视频 最强开源_2083951843780161538.json, 视频生成/图生视频/视频生成  视频   LTX2.3 图生视频 最强开源_2084169351942463489.json, 视频生成/图生视频/视频生成改进版  LTX2.3 图生视频 最强开源_2078761295033225218.json, 视频生成/文生视频/LTX2.3图生视频—最佳效果_2062858202403926018.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_7

> 由 `engine/knowledge_consolidation` 从 22 个 workflow 归纳得出（视频生成/图生视频/LTX2.3-I2V-GGUF_2031025711103873026.json、视频生成/图生视频/LTX2.3图生视频_2030295867214794753.json、视频生成/图生视频/LTX2.3图生视频_2031246343607422977.json、视频生成/图生视频/LTX2.3图生视频_2032301246597570562.json、视频生成/图生视频/LTX2.3图生视频_2033385858308513793.json…）

- **类型**：Unknown Workflow
- **样本数**：22
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 22 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CreateVideo`
- `EmptyImage`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `ImageScaleBy`
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
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 21/22 个有
- `DualCLIPLoader` —— 21/22 个有
- `KSampler` —— 21/22 个有
- `LTXAVTextEncoderLoader` —— 21/22 个有
- `LTXVAudioVAELoader` —— 21/22 个有
- `LTXVCropGuides` —— 21/22 个有
- `LTXVScheduler` —— 21/22 个有
- `ResizeImageMaskNode` —— 21/22 个有
- `VAEDecode` —— 21/22 个有
- `TextGenerateLTX2Prompt` —— 20/22 个有
- `PreviewAny` —— 16/22 个有
- `GetNode` —— 10/22 个有
- `SetNode` —— 10/22 个有
- `Int` —— 2/22 个有
- `PrimitiveFloat` —— 2/22 个有
- `SimpleMath+` —— 2/22 个有
- `CR Text Concatenate` —— 1/22 个有
- `DF_Int_to_Float` —— 1/22 个有
- `DF_Integer` —— 1/22 个有
- `IntToString` —— 1/22 个有
- `ManualSigmas` —— 1/22 个有
- `PrimitiveString` —— 1/22 个有
- `RH_LLMAPI_NODE` —— 1/22 个有
- `RH_Translator` —— 1/22 个有
- `StringReplace` —— 1/22 个有
- `UnetLoaderGGUF` —— 1/22 个有
- `VAEDecodeTiled` —— 1/22 个有
- `VAELoaderKJ` —— 1/22 个有
- `easy int` —— 1/22 个有
- `intToFloat _O` —— 1/22 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 22 | 100% |
| 高度 | 25 | 25 - 40 | 22 | 88% |
| 采样步数 | 4 | 4 - 4 | 21 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 21 | 100% |
| 采样算法 | euler | - | 21 | 100% |
| 调度器 | simple | - | 21 | 100% |
| 重绘幅度 | 0.35 | 0.25 - 0.35 | 21 | 94% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 21/22 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，22 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 40，22 个样本，取值集中（一致性 88%）
- 采样步数 中位数 4，观测区间 4 - 4，21 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，21 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，21 个样本，一致性 100%
- 调度器 最常用 simple，21 个样本，一致性 100%
- 重绘幅度 中位数 0.35，观测区间 0.25 - 0.35，21 个样本，取值集中（一致性 94%）
- 高发问题（21/22 个样本）：Steps较低可能导致细节不足
