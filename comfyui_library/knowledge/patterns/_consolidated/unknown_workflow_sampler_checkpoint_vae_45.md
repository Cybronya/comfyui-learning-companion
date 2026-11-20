---
name: unknown_workflow_sampler_checkpoint_vae_45
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.625
common_nodes: [AILab_QwenVL, CheckpointLoaderSimple, ComfyNumberConvert, ConditioningZeroOut, EmptyYuE2LatentAudio, JWStringSplit, KSampler, ModelAttentionBackend, PreviewAny, PrimitiveInt, PrimitiveStringMultiline, SaveAudio, SaveText, Seed (rgthree), SomethingToString, StringConcatenate, StringReplace, StringTrim, VAEDecodeAudio, YuE2GenerateABC, YuE2GenerateMusic, easy cleanGpuUsed, easy showAnything]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [音频生成/音频生成/音乐生成-YuE2-官流-歌曲生成一句话_2100390333661147138.json, 音频生成/音频生成/音乐生成-YuE2-官流-歌曲生成一句话_2100415196908052482.json, 音频生成/音频生成/音乐生成-YuE2-官流-歌曲生成（一句话）_2099778654258688002.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_checkpoint_vae_45

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（音频生成/音频生成/音乐生成-YuE2-官流-歌曲生成一句话_2100390333661147138.json、音频生成/音频生成/音乐生成-YuE2-官流-歌曲生成一句话_2100415196908052482.json、音频生成/音频生成/音乐生成-YuE2-官流-歌曲生成（一句话）_2099778654258688002.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：62%

## 共有节点

全部 3 个 workflow 都包含：
- `AILab_QwenVL`
- `CheckpointLoaderSimple`
- `ComfyNumberConvert`
- `ConditioningZeroOut`
- `EmptyYuE2LatentAudio`
- `JWStringSplit`
- `KSampler`
- `ModelAttentionBackend`
- `PreviewAny`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `SaveAudio`
- `SaveText`
- `Seed (rgthree)`
- `SomethingToString`
- `StringConcatenate`
- `StringReplace`
- `StringTrim`
- `VAEDecodeAudio`
- `YuE2GenerateABC`
- `YuE2GenerateMusic`
- `easy cleanGpuUsed`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 32 | 32 - 32 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | dpm_2 | - | 3 | 100% |
| 调度器 | sgm_uniform | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 3/3 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 32，观测区间 32 - 32，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpm_2，3 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：发现KSampler但没有VAEDecode
