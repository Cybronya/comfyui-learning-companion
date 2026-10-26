---
name: unknown_workflow_upscale_latent_upscale_lora_18
type: Unknown Workflow
frequency: 14
level: strong
coverage: 0.845286
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, CreateVideo, EmptyLTXVLatentVideo, KSampler, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, SaveVideo, VAEDecodeTiled]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [视频生成/文生视频/LTX2.3文生视频_2042483704538337282.json, 视频生成/文生视频/LTX2.3文生视频_2061743726724214786.json, 视频生成/文生视频/LTX2.3文生视频_2075471317587030018.json, 视频生成/文生视频/LTX2.3文生视频工作流，相比2.0提升！_2030996350036353025.json, 视频生成/文生视频/LTX2.3文生视频短剧分镜人物11秒1080p_2031152573197062146.json, 视频生成/文生视频/LTX2.3文生视频短剧分镜人物12秒_2030776760257744898.json, 视频生成/文生视频/LTX2.3文生视频（带教学）_2031634765140463617.json, 视频生成/文生视频/LTX2.3文生长视频_2044236089275195394.json, 视频生成/文生视频/LTX2.3文生音画同步视频_2030052722820521985.json, 视频生成/文生视频/LTX2.3文生音画同步视频竖屏_2030056979279908865.json, 视频生成/文生视频/LTX2.3文生音画同步视频竖屏场景11秒_2030427600178384898.json, 视频生成/文生视频/LTX2.3音画同步文生视频 提示词自动优化分镜_2049920413463007233.json, 视频生成/文生视频/ltx2.3 文生视频_2042444641810784257.json, 视频生成/文生视频/自由创作-LTX2.3-手动提示词-文生视频--搭配LTX2.3创作辅助使用！_2034597884850606081.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_18

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/文生视频/LTX2.3文生视频_2042483704538337282.json、视频生成/文生视频/LTX2.3文生视频_2061743726724214786.json、视频生成/文生视频/LTX2.3文生视频_2075471317587030018.json、视频生成/文生视频/LTX2.3文生视频工作流，相比2.0提升！_2030996350036353025.json、视频生成/文生视频/LTX2.3文生视频短剧分镜人物11秒1080p_2031152573197062146.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 14 个 workflow 都包含：
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
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `PrimitiveInt` —— 12/14 个有
- `DualCLIPLoader` —— 11/14 个有
- `EmptyImage` —— 11/14 个有
- `GetImageSize` —— 11/14 个有
- `ImageScaleBy` —— 11/14 个有
- `PrimitiveFloat` —— 11/14 个有
- `TextGenerateLTX2Prompt` —— 11/14 个有
- `PreviewAny` —— 9/14 个有
- `VAEDecode` —— 4/14 个有
- `Int` —— 3/14 个有
- `CR Prompt Text` —— 2/14 个有
- `JjkText` —— 2/14 个有
- `RH_LLMAPI_Pro_Node` —— 2/14 个有
- `easy showAnything` —— 2/14 个有
- `CombinationText` —— 1/14 个有
- `GetNode` —— 1/14 个有
- `MathExpression_UTK` —— 1/14 个有
- `MathExpression|pysssss` —— 1/14 个有
- `RH_Translator` —— 1/14 个有
- `SetNode` —— 1/14 个有
- `SimpleMath+` —— 1/14 个有
- `Text` —— 1/14 个有
- `easy convertAnything` —— 1/14 个有
- `easy mathInt` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 14 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 14 | 100% |
| 采样算法 | euler | - | 14 | 100% |
| 调度器 | simple | - | 14 | 100% |
| 重绘幅度 | 0.4 | 0.4 - 0.4 | 14 | 100% |
| 宽度 | 97 | 97 - 241 | 14 | 65% |
| 高度 | 25 | 24 - 25 | 14 | 98% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 10/14 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，14 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，14 个样本，一致性 100%
- 调度器 最常用 simple，14 个样本，一致性 100%
- 重绘幅度 中位数 0.4，观测区间 0.4 - 0.4，14 个样本，取值集中（一致性 100%）
- 宽度 中位数 97，观测区间 97 - 241，14 个样本
- 高度 中位数 25，观测区间 24 - 25，14 个样本，取值集中（一致性 98%）
- 高发问题（14/14 个样本）：Steps较低可能导致细节不足
- 高发问题（10/14 个样本）：发现KSampler但没有VAEDecode
