---
name: unknown_workflow_sampler_checkpoint_vae_54
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8545
common_nodes: [Audio Duration, AudioCrop, AudioEncoderLoader, CheckpointLoaderSimple, ConditioningZeroOut, EmptyYuE2LatentAudio, KSampler, PrimitiveStringMultiline, SaveAudioAdvanced, SheetSage2AudioToABC, VAEDecodeAudio, YuE2GenerateMusic]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [音频生成/音频生成/yue2翻唱_2104470636260315138.json, 音频生成/音频生成/开源版suno -- YU2音乐创作与翻唱工作流_2112503480509358082.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_checkpoint_vae_54

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/yue2翻唱_2104470636260315138.json、音频生成/音频生成/开源版suno -- YU2音乐创作与翻唱工作流_2112503480509358082.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `Audio Duration`
- `AudioCrop`
- `AudioEncoderLoader`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `EmptyYuE2LatentAudio`
- `KSampler`
- `PrimitiveStringMultiline`
- `SaveAudioAdvanced`
- `SheetSage2AudioToABC`
- `VAEDecodeAudio`
- `YuE2GenerateMusic`

**可变部分**（部分 workflow 才有）：
- `AudioSeparation` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `LoadAudio` —— 1/2 个有
- `LoadAudioUI` —— 1/2 个有
- `Qwen3ASRLoader` —— 1/2 个有
- `Qwen3ASRTranscribe` —— 1/2 个有
- `ShowAnything|Mie` —— 1/2 个有
- `忽略多组孤海` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 32 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | dpm_2 | - | 2 | 100% |
| 调度器 | sgm_uniform | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 2/2 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 32，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpm_2，2 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：发现KSampler但没有VAEDecode
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
