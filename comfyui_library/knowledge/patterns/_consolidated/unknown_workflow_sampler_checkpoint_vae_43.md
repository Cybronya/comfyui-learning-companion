---
name: unknown_workflow_sampler_checkpoint_vae_43
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.669667
common_nodes: [AudioEncoderLoader, CheckpointLoaderSimple, EmptyYuE2LatentAudio, KSampler, LoadAudio, SaveAudioAdvanced, SheetSage2AudioToABC, VAEDecodeAudio, YuE2GenerateMusic]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [音频生成/音频生成/【翻唱】YuE2-音乐生成_2099610843628531714.json, 音频生成/音频生成/【遇见AI】YUe2音乐模型，音乐参考ABC+新歌词做歌曲翻唱_2100118618569793537.json, 音频生成/音频生成/音乐翻唱_YuE2_2107047578494918658.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_checkpoint_vae_43

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（音频生成/音频生成/【翻唱】YuE2-音乐生成_2099610843628531714.json、音频生成/音频生成/【遇见AI】YUe2音乐模型，音乐参考ABC+新歌词做歌曲翻唱_2100118618569793537.json、音频生成/音频生成/音乐翻唱_YuE2_2107047578494918658.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：67%

## 共有节点

全部 3 个 workflow 都包含：
- `AudioEncoderLoader`
- `CheckpointLoaderSimple`
- `EmptyYuE2LatentAudio`
- `KSampler`
- `LoadAudio`
- `SaveAudioAdvanced`
- `SheetSage2AudioToABC`
- `VAEDecodeAudio`
- `YuE2GenerateMusic`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 2/3 个有
- `PreviewAny` —— 2/3 个有
- `PrimitiveStringMultiline` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `Any Switch (rgthree)` —— 1/3 个有
- `Fast Groups Muter (rgthree)` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `SeedNode` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 32 | 32 - 32 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1.1 | 3 | 95% |
| 采样算法 | dpm_2 | - | 3 | 100% |
| 调度器 | sgm_uniform | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 3/3 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 32，观测区间 32 - 32，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1.1，3 个样本，取值集中（一致性 95%）
- 采样算法 最常用 dpm_2，3 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：发现KSampler但没有VAEDecode
