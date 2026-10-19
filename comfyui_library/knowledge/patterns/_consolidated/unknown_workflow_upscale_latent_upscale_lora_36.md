---
name: unknown_workflow_upscale_latent_upscale_lora_36
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.8595
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, CreateVideo, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, ImageScaleBy, KSampler, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SaveVideo, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/LTX2.3-文生视频_2066069178989240321.json, 视频生成/文生视频/LTX2.3低显存图生视频生成ai漫剧短剧视频 保持人物一致性性价比超高LTX2.3-首尾帧视频_2031606525608857601.json, 视频生成/文生视频/LTX2.3图生视频—最佳效果_2062858202403926018.json, 视频生成/文生视频/LTX2.3图生视频短剧漫剧短视频工作流_2063583232725180417.json, 视频生成/文生视频/LTX2.3文_图生视频_2031625412933062658.json, 视频生成/文生视频/LTX2.3文生哭泣视频_2073302607023656962.json, 视频生成/文生视频/LTX2.3文生视频-生成音画同步的视频-自动提示词_2033390949191131138.json, 视频生成/文生视频/LTX2.3文生视频-生成音画同步的视频_2029767452879491074.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_36

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/文生视频/LTX2.3-文生视频_2066069178989240321.json、视频生成/文生视频/LTX2.3低显存图生视频生成ai漫剧短剧视频 保持人物一致性性价比超高LTX2.3-首尾帧视频_2031606525608857601.json、视频生成/文生视频/LTX2.3图生视频—最佳效果_2062858202403926018.json、视频生成/文生视频/LTX2.3图生视频短剧漫剧短视频工作流_2063583232725180417.json、视频生成/文生视频/LTX2.3文_图生视频_2031625412933062658.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `CreateVideo`
- `EmptyImage`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `ImageScaleBy`
- `KSampler`
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
- `SaveVideo`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `PreviewAny` —— 7/8 个有
- `DualCLIPLoader` —— 6/8 个有
- `TextGenerateLTX2Prompt` —— 6/8 个有
- `PrimitiveFloat` —— 5/8 个有
- `LTXVImgToVideoInplace` —— 4/8 个有
- `LTXVPreprocess` —— 4/8 个有
- `LoadImage` —— 4/8 个有
- `ResizeImagesByLongerEdge` —— 4/8 个有
- `VAEDecodeTiled` —— 4/8 个有
- `Int` —— 3/8 个有
- `ResizeImageMaskNode` —— 3/8 个有
- `Text` —— 3/8 个有
- `CustomAddLabel` —— 2/8 个有
- `VHS_VideoCombine` —— 2/8 个有
- `数学运算_孤海` —— 2/8 个有
- `CR Prompt Text` —— 1/8 个有
- `LTX2_NAG` —— 1/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/8 个有
- `MultiTextConcatenate` —— 1/8 个有
- `PrimitiveStringMultiline` —— 1/8 个有
- `RH_LLMAPI_NODE` —— 1/8 个有
- `RH_LLMAPI_Pro_Node` —— 1/8 个有
- `Seed (rgthree)` —— 1/8 个有
- `ShowText` —— 1/8 个有
- `SimpleMath+` —— 1/8 个有
- `easy anythingIndexSwitch` —— 1/8 个有
- `intToFloat _O` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 8 | 100% |
| 高度 | 25 | 25 - 25 | 8 | 100% |
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 0.375 | 0.25 - 0.4 | 8 | 87% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，8 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，8 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 0.375，观测区间 0.25 - 0.4，8 个样本，取值集中（一致性 87%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
