---
name: unknown_workflow_lora_sampler_clip_4
type: Unknown Workflow
frequency: 32
level: strong
coverage: 0.937312
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVPreprocess, LTXVScheduler, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, SaveVideo]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/2078466505645314049.json, 视频生成/图生视频/2039676993360367617.json, 视频生成/图生视频/2029765472027152386.json, 视频生成/图生视频/2076010082961281026.json, 视频生成/图生视频/2076893159560400897.json, 视频生成/图生视频/2078358572626436098.json, 视频生成/图生视频/2076924327534092290.json, 视频生成/图生视频/2076943198865412098.json, 视频生成/图生视频/2078072773007724545.json, 视频生成/图生视频/2078080157293826049.json, 视频生成/图生视频/2046116877214158850.json, 视频生成/图生视频/2046154956708777986.json, 视频生成/图生视频/2046402792507576321.json, 视频生成/图生视频/2046547736006234113.json, 视频生成/图生视频/2046799074531217409.json, 视频生成/图生视频/2047721004167860225.json, 视频生成/图生视频/2048019971762032641.json, 视频生成/图生视频/LTX2.3& qwen3.6提示词图生视频_2089610911387574273.json, 视频生成/图生视频/2064178415359586305.json, 视频生成/图生视频/2065262381550358529.json, 视频生成/图生视频/LTX2.3++图生视频++视频生成+++最强开源_2087381685796167681.json, 视频生成/图生视频/2066688936931581953.json, 视频生成/图生视频/2067242779092279297.json, 视频生成/图生视频/2029780080481800193.json, 视频生成/图生视频/2030630367857741826.json, 视频生成/图生视频/2030232084618420226.json, 视频生成/图生视频/2029890967838400513.json, 视频生成/图生视频/LTX2.3图生视频Sparkvideo2.0平替短剧漫剧短视频工作流_2031942517490458625.json, 视频生成/图生视频/2033924678502322178.json, 视频生成/图生视频/2049272623229571073.json, 视频生成/图生视频/2048744630820278273.json, 视频生成/图生视频/2042871628979249154.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_4

> 由 `engine/knowledge_consolidation` 从 32 个 workflow 归纳得出（视频生成/图生视频/2078466505645314049.json、视频生成/图生视频/2039676993360367617.json、视频生成/图生视频/2029765472027152386.json、视频生成/图生视频/2076010082961281026.json、视频生成/图生视频/2076893159560400897.json…）

- **类型**：Unknown Workflow
- **样本数**：32
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 32 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplace`
- `LTXVPreprocess`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 31/32 个有
- `GetImageSize` —— 31/32 个有
- `ImageScaleBy` —— 31/32 个有
- `LTXVCropGuides` —— 31/32 个有
- `LTXVLatentUpsampler` —— 31/32 个有
- `LatentUpscaleModelLoader` —— 31/32 个有
- `PrimitiveInt` —— 31/32 个有
- `ResizeImagesByLongerEdge` —— 31/32 个有
- `VAEDecode` —— 31/32 个有
- `KSampler` —— 30/32 个有
- `ResizeImageMaskNode` —— 30/32 个有
- `PreviewAny` —— 29/32 个有
- `DualCLIPLoader` —— 26/32 个有
- `TextGenerateLTX2Prompt` —— 26/32 个有
- `Int` —— 10/32 个有
- `Text` —— 9/32 个有
- `llama_cpp_instruct_adv` —— 6/32 个有
- `llama_cpp_model_loader` —— 6/32 个有
- `easy saveText` —— 5/32 个有
- `llama_cpp_parameters` —— 5/32 个有
- `easy cleanGpuUsed` —— 3/32 个有
- `ImageResizeKJv2` —— 2/32 个有
- `JjkText` —— 2/32 个有
- `Label (rgthree)` —— 2/32 个有
- `SimpleMath+` —— 2/32 个有
- `easy showAnything` —— 2/32 个有
- `CustomAddLabel` —— 1/32 个有
- `Float` —— 1/32 个有
- `INTConstant` —— 1/32 个有
- `ImageResize+` —— 1/32 个有
- `JWFloat` —— 1/32 个有
- `PrimitiveFloat` —— 1/32 个有
- `SeargeIntegerMath` —— 1/32 个有
- `ShowText|pysssss` —— 1/32 个有
- `VAEDecodeTiled` —— 1/32 个有
- `VHS_VideoCombine` —— 1/32 个有
- `llama_cpp_unload_model` —— 1/32 个有
- `ttN int` —— 1/32 个有
- `数学运算_孤海` —— 1/32 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 32 | 100% |
| 高度 | 25 | 24 - 25 | 32 | 99% |
| 采样步数 | 4 | 4 - 6 | 30 | 91% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 30 | 100% |
| 采样算法 | euler | - | 30 | 100% |
| 调度器 | simple | - | 30 | 100% |
| 重绘幅度 | 0.35 | 0 - 0.35 | 30 | 81% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 30/32 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，32 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 24 - 25，32 个样本，取值集中（一致性 99%）
- 采样步数 中位数 4，观测区间 4 - 6，30 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，30 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，30 个样本，一致性 100%
- 调度器 最常用 simple，30 个样本，一致性 100%
- 重绘幅度 中位数 0.35，观测区间 0 - 0.35，30 个样本，取值集中（一致性 81%）
- 风险：重绘幅度 观测到 0，低于常用下限 0.1（）
- 高发问题（30/32 个样本）：Steps较低可能导致细节不足
