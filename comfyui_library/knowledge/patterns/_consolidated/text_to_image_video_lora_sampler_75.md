---
name: text_to_image_video_lora_sampler_75
type: Text To Image
frequency: 10
level: strong
coverage: 0.8185
common_nodes: [AILab_QwenVL_Advanced, BasicScheduler, CLIPLoader, CLIPTextEncode, DualCLIPLoader, EmptyLTXVLatentVideo, EmptyLatentImage, ImageResizeKJv2, Int, JjkText, KSampler, KSamplerSelect, LTX2SamplingPreviewOverride, LTX2_NAG, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoInplaceKJ, LTXVPreprocess, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, SamplerCustom, ShowText|pysssss, StringFunction|pysssss, UNETLoader, VAEDecode, VAELoader, VAELoaderKJ, VHS_VideoCombine, VisualizeSigmasKJ, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/LTX2.3一键自动生成视频图生视频｜数字人人物特效轻松做_2114236170795311105.json, 视频生成/图生视频/KJ版音画同步｜LTX2.3提示词润色图生视频_2091803663361728514.json, 视频生成/图生视频/LTX2.3 音画同步KJ优化版｜图片加文字直出带货视频_2096908247751028737.json, 视频生成/图生视频/LTX2.3一键图生视频流｜角色表演自动出片，动作表情都在线_2099489502615134210.json, 视频生成/图生视频/LTX2.3双人对话KJ优化版｜音画同步图生视频对话更自然_2103700832389783554.json, 视频生成/图生视频/LTX2.3图生视频KJ版｜音画同步提示词润色直出_2091641388155887618.json, 视频生成/图生视频/LTX2.3音画同步优化版｜图片文字直出短剧电商带货视频_2096712252907937793.json, 视频生成/图生视频/LTX2.3音画同步图生视频｜图片加文字直出带货视频_2098730879790178305.json, 视频生成/图生视频/LTX2.3音画同步图生视频｜图片加文字直出短剧电商带货制作_2096702295546359810.json, 视频生成/文生视频/LTX2.3图生视频音画同步KJ优化版｜图片加文字直出 短剧电商带货_2104073651317469186.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_75

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（数字人/数字人/LTX2.3一键自动生成视频图生视频｜数字人人物特效轻松做_2114236170795311105.json、视频生成/图生视频/KJ版音画同步｜LTX2.3提示词润色图生视频_2091803663361728514.json、视频生成/图生视频/LTX2.3 音画同步KJ优化版｜图片加文字直出带货视频_2096908247751028737.json、视频生成/图生视频/LTX2.3一键图生视频流｜角色表演自动出片，动作表情都在线_2099489502615134210.json、视频生成/图生视频/LTX2.3双人对话KJ优化版｜音画同步图生视频对话更自然_2103700832389783554.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 10 个 workflow 都包含：
- `AILab_QwenVL_Advanced`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `EmptyLatentImage`
- `ImageResizeKJv2`
- `Int`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplaceKJ`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `SamplerCustom`
- `ShowText|pysssss`
- `StringFunction|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `VisualizeSigmasKJ`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 9/10 个有
- `DF_Int_to_Float` —— 8/10 个有
- `GetNode` —— 8/10 个有
- `LayerUtility: BooleanOperatorV2` —— 8/10 个有
- `LayerUtility: If ` —— 8/10 个有
- `LayerUtility: NumberCalculatorV2` —— 8/10 个有
- `PathchSageAttentionKJ` —— 8/10 个有
- `PrimitiveInt` —— 8/10 个有
- `SetNode` —— 8/10 个有
- `SimpleMath+` —— 8/10 个有
- `easy positive` —— 8/10 个有
- `MathExpression|pysssss` —— 2/10 个有
- `JoinStrings` —— 1/10 个有
- `PrimitiveStringMultiline` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 10 | 100% |
| 高度 | 80 | 80 - 80 | 10 | 100% |
| 采样步数 | 4 | 4 - 4 | 10 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 10 | 100% |
| 采样算法 | er_sde | - | 10 | 100% |
| 调度器 | beta | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足
