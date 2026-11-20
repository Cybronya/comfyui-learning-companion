---
name: unknown_workflow_upscale_latent_upscale_lora_61
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.811
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, CreateVideo, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, ImageScaleBy, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, PrimitiveFloat, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SaveVideo, VAEDecode, VAEDecodeTiled]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/LTX2.0-低显存版-自动提示词-动态强化-运镜加速-文生视频V1_2011665816391000065.json, 视频生成/文生视频/LTX2.0智能提示词动态强化运镜加速低显存版文生视频V1_2009271528722010113.json, 视频生成/文生视频/LTX2.3文生哭泣视频_2073302607023656962.json, 视频生成/文生视频/LTX2.3文生视频-生成音画同步的视频-自动提示词_2033390949191131138.json, 视频生成/文生视频/LTX2.3文生视频-生成音画同步的视频_2029767452879491074.json, 视频生成/文生视频/LTX2.3文生视频_2061743726724214786.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_61

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/文生视频/LTX2.0-低显存版-自动提示词-动态强化-运镜加速-文生视频V1_2011665816391000065.json、视频生成/文生视频/LTX2.0智能提示词动态强化运镜加速低显存版文生视频V1_2009271528722010113.json、视频生成/文生视频/LTX2.3文生哭泣视频_2073302607023656962.json、视频生成/文生视频/LTX2.3文生视频-生成音画同步的视频-自动提示词_2033390949191131138.json、视频生成/文生视频/LTX2.3文生视频-生成音画同步的视频_2029767452879491074.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `CreateVideo`
- `EmptyImage`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `ImageScaleBy`
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
- `PrimitiveFloat`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecode`
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `Int` —— 4/6 个有
- `KSampler` —— 4/6 个有
- `CR Prompt Text` —— 3/6 个有
- `DualCLIPLoader` —— 3/6 个有
- `PreviewAny` —— 3/6 个有
- `RH_LLMAPI_Pro_Node` —— 3/6 个有
- `TextGenerateLTX2Prompt` —— 3/6 个有
- `easy anythingIndexSwitch` —— 3/6 个有
- `CustomAddLabel` —— 2/6 个有
- `JWInteger` —— 2/6 个有
- `ManualSigmas` —— 2/6 个有
- `SimpleMath+` —— 2/6 个有
- `Text` —— 2/6 个有
- `VHS_VideoCombine` —— 2/6 个有
- `VRAMReserver` —— 2/6 个有
- `数学运算_孤海` —— 2/6 个有
- `AddLabel` —— 1/6 个有
- `Any To Any` —— 1/6 个有
- `JoinStrings` —— 1/6 个有
- `MultiTextConcatenate` —— 1/6 个有
- `Qwen3_VQA` —— 1/6 个有
- `ShowText` —— 1/6 个有
- `TextInput_` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有
- `easy convertAnything` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 6 | 100% |
| 高度 | 25 | 25 - 25 | 6 | 100% |
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 0.4 | 0.4 - 0.4 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，6 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，6 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 0.4，观测区间 0.4 - 0.4，4 个样本，取值集中（一致性 100%）
- 高发问题（4/6 个样本）：Steps较低可能导致细节不足
