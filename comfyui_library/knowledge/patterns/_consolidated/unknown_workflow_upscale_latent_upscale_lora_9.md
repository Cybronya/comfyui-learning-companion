---
name: unknown_workflow_upscale_latent_upscale_lora_9
type: Unknown Workflow
frequency: 20
level: strong
coverage: 0.8526
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, CreateVideo, EmptyLTXVLatentVideo, KSampler, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, SaveVideo]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [视频生成/文生视频/LTX2.3文生视频_2029632742534680578.json, 视频生成/文生视频/LTX2.3文生视频_2029814808173879298.json, 视频生成/文生视频/LTX2.3文生视频_2029929479480545282.json, 视频生成/文生视频/LTX2.3文生视频_2030904134915854338.json, 视频生成/文生视频/LTX2.3文生视频_2032363107607126018.json, 视频生成/文生视频/LTX2.3文生视频_2033356584612532225.json, 视频生成/文生视频/LTX2.3文生视频_2040990526287122433.json, 视频生成/文生视频/LTX2.3文生视频_2042483704538337282.json, 视频生成/文生视频/LTX2.3文生视频_2061743726724214786.json, 视频生成/文生视频/LTX2.3文生视频_2075471317587030018.json, 视频生成/文生视频/LTX2.3文生视频工作流，相比2.0提升！_2030996350036353025.json, 视频生成/文生视频/LTX2.3文生视频短剧分镜人物11秒1080p_2031152573197062146.json, 视频生成/文生视频/LTX2.3文生视频短剧分镜人物12秒_2030776760257744898.json, 视频生成/文生视频/LTX2.3文生长视频_2044236089275195394.json, 视频生成/文生视频/LTX2.3文生音画同步视频_2030052722820521985.json, 视频生成/文生视频/LTX2.3文生音画同步视频竖屏_2030056979279908865.json, 视频生成/文生视频/LTX2.3文生音画同步视频竖屏场景11秒_2030427600178384898.json, 视频生成/文生视频/LTX2.3音视频同步，数字人、图生视频、文生视频高清画质工作流_2030665052986023938.json, 视频生成/文生视频/ltx2.3 文生视频_2042444641810784257.json, 视频生成/文生视频/图生视频极速版LTX2.3  数字人话 唱歌对口型_2044214545626963970.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_9

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（视频生成/文生视频/LTX2.3文生视频_2029632742534680578.json、视频生成/文生视频/LTX2.3文生视频_2029814808173879298.json、视频生成/文生视频/LTX2.3文生视频_2029929479480545282.json、视频生成/文生视频/LTX2.3文生视频_2030904134915854338.json、视频生成/文生视频/LTX2.3文生视频_2032363107607126018.json…）

- **类型**：Unknown Workflow
- **样本数**：20
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 20 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
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
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `DualCLIPLoader` —— 19/20 个有
- `PrimitiveInt` —— 19/20 个有
- `TextGenerateLTX2Prompt` —— 19/20 个有
- `VAEDecodeTiled` —— 19/20 个有
- `EmptyImage` —— 18/20 个有
- `GetImageSize` —— 18/20 个有
- `ImageScaleBy` —— 18/20 个有
- `PreviewAny` —— 17/20 个有
- `PrimitiveFloat` —— 17/20 个有
- `VAEDecode` —— 9/20 个有
- `Int` —— 2/20 个有
- `JjkText` —— 2/20 个有
- `LTXVImgToVideoInplace` —— 2/20 个有
- `LTXVPreprocess` —— 2/20 个有
- `LoadImage` —— 2/20 个有
- `ResizeImageMaskNode` —— 2/20 个有
- `ResizeImagesByLongerEdge` —— 2/20 个有
- `CR Text` —— 1/20 个有
- `CombinationText` —— 1/20 个有
- `MathExpression_UTK` —— 1/20 个有
- `RH_Translator` —— 1/20 个有
- `SimpleMath+` —— 1/20 个有
- `Text` —— 1/20 个有
- `easy convertAnything` —— 1/20 个有
- `easy mathInt` —— 1/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 241 | 20 | 70% |
| 高度 | 25 | 24 - 25 | 20 | 99% |
| 采样步数 | 4 | 4 - 4 | 20 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 20 | 100% |
| 采样算法 | euler | - | 20 | 100% |
| 调度器 | simple | - | 20 | 100% |
| 重绘幅度 | 0.4 | 0.35 - 0.4 | 20 | 96% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 21/20 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 11/20 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 241，20 个样本
- 高度 中位数 25，观测区间 24 - 25，20 个样本，取值集中（一致性 99%）
- 采样步数 中位数 4，观测区间 4 - 4，20 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，20 个样本，一致性 100%
- 调度器 最常用 simple，20 个样本，一致性 100%
- 重绘幅度 中位数 0.4，观测区间 0.35 - 0.4，20 个样本，取值集中（一致性 96%）
- 高发问题（21/20 个样本）：Steps较低可能导致细节不足
- 高发问题（11/20 个样本）：发现KSampler但没有VAEDecode
