---
name: unknown_workflow_sampler_checkpoint_vae_53
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.5935
common_nodes: [AudioEncoderLoader, CheckpointLoaderSimple, EmptyYuE2LatentAudio, KSampler, LoadAudio, PreviewAny, PrimitiveStringMultiline, SaveAudioAdvanced, SheetSage2AudioToABC, VAEDecodeAudio, YuE2GenerateABC, YuE2GenerateMusic]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [音频生成/音频生成/YuE2歌曲生成_2106388409039286274.json, 音频生成/音频生成/yue2音乐生成_翻唱_编辑_2104119571052584962.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_checkpoint_vae_53

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/YuE2歌曲生成_2106388409039286274.json、音频生成/音频生成/yue2音乐生成_翻唱_编辑_2104119571052584962.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：59%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioEncoderLoader`
- `CheckpointLoaderSimple`
- `EmptyYuE2LatentAudio`
- `KSampler`
- `LoadAudio`
- `PreviewAny`
- `PrimitiveStringMultiline`
- `SaveAudioAdvanced`
- `SheetSage2AudioToABC`
- `VAEDecodeAudio`
- `YuE2GenerateABC`
- `YuE2GenerateMusic`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 1/2 个有
- `CLIPLoader` —— 1/2 个有
- `JsonExtractString` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `StringConcatenate` —— 1/2 个有
- `TextGenerate` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 32 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1.05 | - | 2 | 95% |
| 采样算法 | dpm_2 | - | 2 | 100% |
| 调度器 | sgm_uniform | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 2/2 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 32，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1.05，样本不足，未给区间，2 个样本，取值集中（一致性 95%）
- 采样算法 最常用 dpm_2，2 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：发现KSampler但没有VAEDecode
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
