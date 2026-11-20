---
name: unknown_workflow_upscale_latent_upscale_lora_6
type: Unknown Workflow
frequency: 23
level: strong
coverage: 0.925522
common_nodes: [CFGGuider, CLIPTextEncode, CreateVideo, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, ImageScaleBy, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, PrimitiveInt, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, SaveVideo]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/LTX2.3 V2V 视频续写 GGUF KJ版_2029780398972080129.json, 视频生成/图生视频/LTX-2 GGUF 12GB图生有声视频工作流-B站UP主@好奇漫步_2018342004555522049.json, 视频生成/图生视频/LTX2.0图生视频（须运行plus）_2009279040347185153.json, 视频生成/图生视频/LTX2.3 官方基础工作流_2029765472027152386.json, 视频生成/图生视频/LTX2.3 视频生成  图生视频  最强开源_2076010082961281026.json, 视频生成/图生视频/LTX2.3 视频生成  图生视频 最强开源_2076893159560400897.json, 视频生成/图生视频/LTX2.3 视频生成  图生视频 最强开源_2078358572626436098.json, 视频生成/图生视频/LTX2.3 视频生成 图生视频 最强开源_2076924327534092290.json, 视频生成/图生视频/LTX2.3 视频生成 图生视频 最强开源_2076943198865412098.json, 视频生成/图生视频/LTX2.3 视频生成 图生视频 最强开源_2078072773007724545.json, 视频生成/图生视频/LTX2.3 视频生成 图生视频 最强开源_2078080157293826049.json, 视频生成/图生视频/LTX2.3 超强图生视频 最强开源_2046116877214158850.json, 视频生成/图生视频/LTX2.3 超强图生视频 最强开源_2046154956708777986.json, 视频生成/图生视频/LTX2.3 超强图生视频 最强开源_2046402792507576321.json, 视频生成/图生视频/LTX2.3 超强图生视频 最强开源_2046547736006234113.json, 视频生成/图生视频/LTX2.3 超强图生视频 最强开源_2046799074531217409.json, 视频生成/图生视频/LTX2.3 超强图生视频 最强开源_2047721004167860225.json, 视频生成/图生视频/LTX2.3 超强图生视频 最强开源_2048019971762032641.json, 视频生成/图生视频/LTX2.3& qwen3.6提示词图生视频_2089610911387574273.json, 视频生成/图生视频/LTX2.3图生视频_2029823149398827010.json, 视频生成/图生视频/LTX2.3图生视频_2029938786079084546.json, 视频生成/图生视频/【Supermate】LTX2.3& qwen3.5提示词图生视频_2033924678502322178.json, 视频生成/图生视频/【Supermate】LTX2.3& qwen3.6提示词图生视频Plus_2049272623229571073.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_6

> 由 `engine/knowledge_consolidation` 从 23 个 workflow 归纳得出（平台全量/LTX2.3 V2V 视频续写 GGUF KJ版_2029780398972080129.json、视频生成/图生视频/LTX-2 GGUF 12GB图生有声视频工作流-B站UP主@好奇漫步_2018342004555522049.json、视频生成/图生视频/LTX2.0图生视频（须运行plus）_2009279040347185153.json、视频生成/图生视频/LTX2.3 官方基础工作流_2029765472027152386.json、视频生成/图生视频/LTX2.3 视频生成  图生视频  最强开源_2076010082961281026.json…）

- **类型**：Unknown Workflow
- **样本数**：23
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 23 个 workflow 都包含：
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
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly`
- `PrimitiveInt`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `LTXVCropGuides` —— 22/23 个有
- `LTXVEmptyLatentAudio` —— 22/23 个有
- `LTXVScheduler` —— 22/23 个有
- `LoadImage` —— 22/23 个有
- `CheckpointLoaderSimple` —— 21/23 个有
- `LTXAVTextEncoderLoader` —— 21/23 个有
- `LTXVAudioVAELoader` —— 21/23 个有
- `KSampler` —— 20/23 个有
- `PreviewAny` —— 20/23 个有
- `ResizeImageMaskNode` —— 20/23 个有
- `VAEDecode` —— 20/23 个有
- `DualCLIPLoader` —— 19/23 个有
- `TextGenerateLTX2Prompt` —— 17/23 个有
- `Int` —— 4/23 个有
- `ManualSigmas` —— 3/23 个有
- `PrimitiveFloat` —— 3/23 个有
- `Text` —— 3/23 个有
- `VAEDecodeTiled` —— 3/23 个有
- `easy saveText` —— 3/23 个有
- `llama_cpp_instruct_adv` —— 3/23 个有
- `llama_cpp_model_loader` —— 3/23 个有
- `llama_cpp_parameters` —— 3/23 个有
- `Float` —— 2/23 个有
- `ImageResize+` —— 2/23 个有
- `JjkText` —— 2/23 个有
- `UnetLoaderGGUF` —— 2/23 个有
- `VAELoaderKJ` —— 2/23 个有
- `CR Text` —— 1/23 个有
- `LTXVAudioVAEEncode` —— 1/23 个有
- `LTXVAudioVideoMask` —— 1/23 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/23 个有
- `SimpleCalculatorKJ` —— 1/23 个有
- `SimpleMath+` —— 1/23 个有
- `VHS_LoadVideo` —— 1/23 个有
- `VHS_VideoInfo` —— 1/23 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 22 | 100% |
| 高度 | 25 | 25 - 25 | 22 | 100% |
| 采样步数 | 4 | 4 - 4 | 20 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 20 | 100% |
| 采样算法 | euler | - | 20 | 100% |
| 调度器 | simple | - | 20 | 100% |
| 重绘幅度 | 0.35 | 0.35 - 0.35 | 20 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 20/23 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，22 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，22 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，20 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，20 个样本，一致性 100%
- 调度器 最常用 simple，20 个样本，一致性 100%
- 重绘幅度 中位数 0.35，观测区间 0.35 - 0.35，20 个样本，取值集中（一致性 100%）
- 高发问题（20/23 个样本）：Steps较低可能导致细节不足
