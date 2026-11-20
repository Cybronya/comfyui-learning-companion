---
name: unknown_workflow_lora_sampler_clip_6
type: Unknown Workflow
frequency: 34
level: strong
coverage: 0.933647
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVScheduler, LTXVSeparateAVLatent, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, SaveVideo]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/LTX2.3 图生视频极速版_2039676993360367617.json, 视频生成/图生视频/LTX2.3 视频生成  图生视频  最强开源_2076010082961281026.json, 视频生成/图生视频/LTX2.3 视频生成  图生视频 最强开源_2076893159560400897.json, 视频生成/图生视频/LTX2.3 视频生成  图生视频 最强开源_2078358572626436098.json, 视频生成/图生视频/LTX2.3 视频生成 图生视频 最强开源_2076924327534092290.json, 视频生成/图生视频/LTX2.3 视频生成 图生视频 最强开源_2076943198865412098.json, 视频生成/图生视频/LTX2.3 视频生成 图生视频 最强开源_2078072773007724545.json, 视频生成/图生视频/LTX2.3 视频生成 图生视频 最强开源_2078080157293826049.json, 视频生成/图生视频/LTX2.3 超强图生视频 最强开源_2046116877214158850.json, 视频生成/图生视频/LTX2.3 超强图生视频 最强开源_2046154956708777986.json, 视频生成/图生视频/LTX2.3 超强图生视频 最强开源_2046402792507576321.json, 视频生成/图生视频/LTX2.3 超强图生视频 最强开源_2046547736006234113.json, 视频生成/图生视频/LTX2.3 超强图生视频 最强开源_2046799074531217409.json, 视频生成/图生视频/LTX2.3 超强图生视频 最强开源_2047721004167860225.json, 视频生成/图生视频/LTX2.3 超强图生视频 最强开源_2048019971762032641.json, 视频生成/图生视频/LTX2.3& qwen3.6提示词图生视频_2089610911387574273.json, 视频生成/图生视频/LTX2.3+++图生视频+最强开源 (1)_2064178415359586305.json, 视频生成/图生视频/LTX2.3+++图生视频+最强开源 (2)_2065262381550358529.json, 视频生成/图生视频/LTX2.3++图生视频++视频生成+++最强开源_2087381685796167681.json, 视频生成/图生视频/LTX2.3+图生视频+最强开源_2066688936931581953.json, 视频生成/图生视频/LTX2.3+图生视频+最强开源_2067242779092279297.json, 视频生成/图生视频/LTX2.3--图生音视频_2029780080481800193.json, 视频生成/图生视频/LTX2.3-图生视频_2066084809260224514.json, 视频生成/图生视频/LTX2.3-图生视频升级版（自动提示词）_2030630367857741826.json, 视频生成/图生视频/LTX2.3图生视频 (1)_2056932845310009346.json, 视频生成/图生视频/LTX2.3图生视频-有人声极速版_2070027759010795521.json, 视频生成/图生视频/LTX2.3图生视频-生成音画同步的视频_2030232084618420226.json, 视频生成/图生视频/LTX2.3图生视频Sparkvideo2.0平替短剧漫剧短视频工作流_2029890967838400513.json, 视频生成/图生视频/LTX2.3图生视频Sparkvideo2.0平替短剧漫剧短视频工作流_2031942517490458625.json, 视频生成/图生视频/【Supermate】LTX2.3& qwen3.5提示词图生视频_2033924678502322178.json, 视频生成/图生视频/【Supermate】LTX2.3& qwen3.6提示词图生视频Plus_2049272623229571073.json, 视频生成/图生视频/【Supermate】LTX2.3单图视频(Gemma4））-还在调整_2048744630820278273.json, 视频生成/图生视频/【Supermate】LTX2.3单图视频(无反推）_2042871628979249154.json, 视频生成/文生视频/LTX2.3文生视频-生成音画同步的视频_2029767452879491074.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_6

> 由 `engine/knowledge_consolidation` 从 34 个 workflow 归纳得出（视频生成/图生视频/LTX2.3 图生视频极速版_2039676993360367617.json、视频生成/图生视频/LTX2.3 视频生成  图生视频  最强开源_2076010082961281026.json、视频生成/图生视频/LTX2.3 视频生成  图生视频 最强开源_2076893159560400897.json、视频生成/图生视频/LTX2.3 视频生成  图生视频 最强开源_2078358572626436098.json、视频生成/图生视频/LTX2.3 视频生成 图生视频 最强开源_2076924327534092290.json…）

- **类型**：Unknown Workflow
- **样本数**：34
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 34 个 workflow 都包含：
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
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 33/34 个有
- `GetImageSize` —— 33/34 个有
- `ImageScaleBy` —— 33/34 个有
- `LTXVCropGuides` —— 33/34 个有
- `LTXVImgToVideoInplace` —— 33/34 个有
- `LTXVLatentUpsampler` —— 33/34 个有
- `LTXVPreprocess` —— 33/34 个有
- `LatentUpscaleModelLoader` —— 33/34 个有
- `LoadImage` —— 33/34 个有
- `PrimitiveInt` —— 33/34 个有
- `VAEDecode` —— 33/34 个有
- `KSampler` —— 32/34 个有
- `ResizeImagesByLongerEdge` —— 32/34 个有
- `PreviewAny` —— 31/34 个有
- `ResizeImageMaskNode` —— 31/34 个有
- `DualCLIPLoader` —— 28/34 个有
- `TextGenerateLTX2Prompt` —— 28/34 个有
- `Int` —— 10/34 个有
- `Text` —— 10/34 个有
- `llama_cpp_instruct_adv` —— 6/34 个有
- `llama_cpp_model_loader` —— 6/34 个有
- `easy saveText` —— 5/34 个有
- `llama_cpp_parameters` —— 5/34 个有
- `easy cleanGpuUsed` —— 3/34 个有
- `CustomAddLabel` —— 2/34 个有
- `ImageResizeKJv2` —— 2/34 个有
- `Label (rgthree)` —— 2/34 个有
- `PrimitiveFloat` —— 2/34 个有
- `VAEDecodeTiled` —— 2/34 个有
- `VHS_VideoCombine` —— 2/34 个有
- `easy showAnything` —— 2/34 个有
- `数学运算_孤海` —— 2/34 个有
- `INTConstant` —— 1/34 个有
- `JWFloat` —— 1/34 个有
- `JjkText` —— 1/34 个有
- `SeargeIntegerMath` —— 1/34 个有
- `ShowText|pysssss` —— 1/34 个有
- `SimpleMath+` —— 1/34 个有
- `llama_cpp_unload_model` —— 1/34 个有
- `ttN int` —— 1/34 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 34 | 100% |
| 高度 | 25 | 24 - 25 | 34 | 99% |
| 采样步数 | 4 | 4 - 4 | 32 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 32 | 100% |
| 采样算法 | euler | - | 32 | 100% |
| 调度器 | simple | - | 32 | 100% |
| 重绘幅度 | 0.35 | 0.35 - 0.4 | 32 | 98% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 32/34 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，34 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 24 - 25，34 个样本，取值集中（一致性 99%）
- 采样步数 中位数 4，观测区间 4 - 4，32 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，32 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，32 个样本，一致性 100%
- 调度器 最常用 simple，32 个样本，一致性 100%
- 重绘幅度 中位数 0.35，观测区间 0.35 - 0.4，32 个样本，取值集中（一致性 98%）
- 高发问题（32/34 个样本）：Steps较低可能导致细节不足
