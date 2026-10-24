---
name: unknown_workflow_sampler_unet_vae_217
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8452
common_nodes: [ConditioningZeroOut, DualCLIPLoader, EmptyAceStep1.5LatentAudio, KSampler, ModelSamplingAuraFlow, SaveAudioMP3, TextEncodeAceStepAudio1.5, UNETLoader, VAEDecodeAudio, VAELoader]
problems: [发现KSampler但没有VAEDecode, Steps较低可能导致细节不足]
missing: []
members: [音频生成/音频生成/ACE STEP1.5 音乐生成_2019710020950167553.json, 音频生成/音频生成/ACE Step v1.5 歌曲创作_2048677518881853442.json, 音频生成/音频生成/ACE Step1.5+qwen3.5歌词歌曲创作_2046534389982564354.json, 音频生成/音频生成/ACE step-XL-turbo-自动歌词音乐生成_2048231420753092609.json, 音频生成/音频生成/音频-音乐歌曲生成-Acestep-xl-turbo_2043627967057764353.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_217

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（音频生成/音频生成/ACE STEP1.5 音乐生成_2019710020950167553.json、音频生成/音频生成/ACE Step v1.5 歌曲创作_2048677518881853442.json、音频生成/音频生成/ACE Step1.5+qwen3.5歌词歌曲创作_2046534389982564354.json、音频生成/音频生成/ACE step-XL-turbo-自动歌词音乐生成_2048231420753092609.json、音频生成/音频生成/音频-音乐歌曲生成-Acestep-xl-turbo_2043627967057764353.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 5 个 workflow 都包含：
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyAceStep1.5LatentAudio`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveAudioMP3`
- `TextEncodeAceStepAudio1.5`
- `UNETLoader`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 3/5 个有
- `PrimitiveFloat` —— 3/5 个有
- `easy seed` —— 3/5 个有
- `RegexExtract` —— 2/5 个有
- `ShowText|pysssss` —— 2/5 个有
- `Text` —— 2/5 个有
- `llama_cpp_instruct_adv` —— 2/5 个有
- `llama_cpp_model_loader` —— 2/5 个有
- `Fast Groups Muter (rgthree)` —— 1/5 个有
- `Float` —— 1/5 个有
- `PreviewAny` —— 1/5 个有
- `RH_LLMAPI_Pro_Node` —— 1/5 个有
- `llama_cpp_parameters` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 10 | 5 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 5/5 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |
| Steps较低可能导致细节不足 | 4/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 10，5 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：发现KSampler但没有VAEDecode
- 高发问题（4/5 个样本）：Steps较低可能导致细节不足
