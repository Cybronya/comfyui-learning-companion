---
name: unknown_workflow_upscale_latent_upscale_lora_3
type: Unknown Workflow
frequency: 56
level: strong
coverage: 0.940393
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, CreateVideo, EmptyLTXVLatentVideo, GetImageSize, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SaveVideo]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/2080553232316846081.json, 视频生成/图生视频/2081678936626520065.json, 视频生成/图生视频/2082011381305536514.json, 视频生成/图生视频/2082181727455367170.json, 视频生成/图生视频/2082380044353232897.json, 视频生成/图生视频/LTX2.3 图生视频 最强开源_2083110363893166082.json, 视频生成/图生视频/LTX2.3 图生视频 最强开源_2083491446019149826.json, 视频生成/图生视频/LTX2.3 图生视频 最强开源_2085421711637438465.json, 视频生成/图生视频/LTX2.3 图生视频 最强开源_2086080291315216386.json, 视频生成/图生视频/LTX2.3 图生视频 最强开源_2086692471563706370.json, 视频生成/图生视频/LTX2.3 图生视频 最强开源_2090000051115479041.json, 视频生成/图生视频/LTX2.3 图生视频 最强开源_2090003062298599426.json, 视频生成/图生视频/LTX2.3 图生视频 最强开源_2090700912884019201.json, 视频生成/图生视频/LTX2.3 图生视频 最强开源_2090703759528775682.json, 视频生成/图生视频/LTX2.3 图生视频 最强开源_2092500341219741697.json, 视频生成/图生视频/2079796340120449026.json, 视频生成/图生视频/LTX2.3 图生视频 视频生成  视频  最强开源_2083960497539477506.json, 视频生成/图生视频/2079632816270303234.json, 视频生成/图生视频/2067482692714844162.json, 视频生成/图生视频/2067686094627495937.json, 视频生成/图生视频/2067693480993972226.json, 视频生成/图生视频/2077666593999507458.json, 视频生成/图生视频/2078184458460680193.json, 视频生成/图生视频/2080543908022538242.json, 视频生成/图生视频/2082513047331106817.json, 视频生成/图生视频/LTX2.3 图生视频 音画同步 视频生成 最强开源_2085416956122984450.json, 视频生成/图生视频/2080568748666347521.json, 视频生成/图生视频/2029981008535228417.json, 视频生成/图生视频/2043581288925372417.json, 视频生成/图生视频/2059205820864352257.json, 视频生成/图生视频/2078466505645314049.json, 视频生成/图生视频/2029765472027152386.json, 视频生成/图生视频/2076010082961281026.json, 视频生成/图生视频/2076893159560400897.json, 视频生成/图生视频/2078358572626436098.json, 视频生成/图生视频/2076924327534092290.json, 视频生成/图生视频/2076943198865412098.json, 视频生成/图生视频/2078072773007724545.json, 视频生成/图生视频/2078080157293826049.json, 视频生成/图生视频/2046116877214158850.json, 视频生成/图生视频/2046154956708777986.json, 视频生成/图生视频/2046402792507576321.json, 视频生成/图生视频/2046547736006234113.json, 视频生成/图生视频/2046799074531217409.json, 视频生成/图生视频/2047721004167860225.json, 视频生成/图生视频/2048019971762032641.json, 视频生成/图生视频/LTX2.3& qwen3.6提示词图生视频_2089610911387574273.json, 视频生成/图生视频/2056932845310009346.json, 视频生成/图生视频/2070027759010795521.json, 视频生成/图生视频/2030232084618420226.json, 视频生成/图生视频/2029890967838400513.json, 视频生成/图生视频/LTX2.3图生视频Sparkvideo2.0平替短剧漫剧短视频工作流_2031942517490458625.json, 视频生成/图生视频/2033924678502322178.json, 视频生成/图生视频/2049272623229571073.json, 视频生成/图生视频/2048744630820278273.json, 视频生成/图生视频/2042871628979249154.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_3

> 由 `engine/knowledge_consolidation` 从 56 个 workflow 归纳得出（视频生成/图生视频/2080553232316846081.json、视频生成/图生视频/2081678936626520065.json、视频生成/图生视频/2082011381305536514.json、视频生成/图生视频/2082181727455367170.json、视频生成/图生视频/2082380044353232897.json…）

- **类型**：Unknown Workflow
- **样本数**：56
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 56 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `CreateVideo`
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
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 55/56 个有
- `ImageScaleBy` —— 55/56 个有
- `KSampler` —— 55/56 个有
- `LTXVScheduler` —— 55/56 个有
- `ResizeImageMaskNode` —— 55/56 个有
- `ResizeImagesByLongerEdge` —— 55/56 个有
- `VAEDecode` —— 55/56 个有
- `DualCLIPLoader` —— 50/56 个有
- `PreviewAny` —— 50/56 个有
- `TextGenerateLTX2Prompt` —— 50/56 个有
- `Int` —— 8/56 个有
- `Text` —— 8/56 个有
- `easy saveText` —— 5/56 个有
- `llama_cpp_instruct_adv` —— 5/56 个有
- `llama_cpp_model_loader` —— 5/56 个有
- `llama_cpp_parameters` —— 5/56 个有
- `GetNode` —— 3/56 个有
- `SetNode` —— 3/56 个有
- `JjkText` —— 2/56 个有
- `Label (rgthree)` —— 2/56 个有
- `easy cleanGpuUsed` —— 2/56 个有
- `easy showAnything` —— 2/56 个有
- `CustomAddLabel` —— 1/56 个有
- `DF_Int_to_Float` —— 1/56 个有
- `Float` —— 1/56 个有
- `ImageResize+` —— 1/56 个有
- `JWFloat` —— 1/56 个有
- `ManualSigmas` —— 1/56 个有
- `MathExpression|pysssss` —— 1/56 个有
- `PrimitiveFloat` —— 1/56 个有
- `RHHiddenNodes` —— 1/56 个有
- `SimpleMath+` —— 1/56 个有
- `VAEDecodeTiled` —— 1/56 个有
- `VHS_VideoCombine` —— 1/56 个有
- `scale` —— 1/56 个有
- `数学运算_孤海` —— 1/56 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 6 | 55 | 93% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 55 | 100% |
| 采样算法 | euler | - | 55 | 100% |
| 调度器 | simple | - | 55 | 100% |
| 重绘幅度 | 0.35 | 0 - 0.35 | 55 | 86% |
| 宽度 | 97 | 97 - 97 | 56 | 100% |
| 高度 | 25 | 24 - 25 | 56 | 99% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 55/56 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 6，55 个样本，取值集中（一致性 93%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，55 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，55 个样本，一致性 100%
- 调度器 最常用 simple，55 个样本，一致性 100%
- 重绘幅度 中位数 0.35，观测区间 0 - 0.35，55 个样本，取值集中（一致性 86%）
- 宽度 中位数 97，观测区间 97 - 97，56 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 24 - 25，56 个样本，取值集中（一致性 99%）
- 风险：重绘幅度 观测到 0，低于常用下限 0.1（）
- 高发问题（55/56 个样本）：Steps较低可能导致细节不足
