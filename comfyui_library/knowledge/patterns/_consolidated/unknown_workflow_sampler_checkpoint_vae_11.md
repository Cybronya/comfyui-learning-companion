---
name: unknown_workflow_sampler_checkpoint_vae_11
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.902
common_nodes: [Bjornulf_FreeVRAM, CM_IntToFloat, CheckpointLoaderSimple, EmptyYuE2LatentAudio, KSampler, MelBandRoFormerModelLoader, MelBandRoFormerSampler, PrimitiveStringMultiline, SaveAudio, SaveAudioAdvanced, VAEDecodeAudio, YuE2GenerateMusic]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/文生图/YuE2纯音乐bgm生成（无人声)_2102589555961585665.json, 音频生成/音频生成/YuE2纯音乐bgm生成无人声)_2101851412895461377.json, 音频生成/音频生成/YuE2纯音乐bgm生成无人声)_2102663661012738050.json, 音频生成/音频生成/YuE2纯音乐bgm生成（无人声)_2099828546146492417.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_checkpoint_vae_11

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/YuE2纯音乐bgm生成（无人声)_2102589555961585665.json、音频生成/音频生成/YuE2纯音乐bgm生成无人声)_2101851412895461377.json、音频生成/音频生成/YuE2纯音乐bgm生成无人声)_2102663661012738050.json、音频生成/音频生成/YuE2纯音乐bgm生成（无人声)_2099828546146492417.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 4 个 workflow 都包含：
- `Bjornulf_FreeVRAM`
- `CM_IntToFloat`
- `CheckpointLoaderSimple`
- `EmptyYuE2LatentAudio`
- `KSampler`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `PrimitiveStringMultiline`
- `SaveAudio`
- `SaveAudioAdvanced`
- `VAEDecodeAudio`
- `YuE2GenerateMusic`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 1/4 个有
- `PreviewImage` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 32 | 32 - 32 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | dpm_2 | - | 4 | 100% |
| 调度器 | sgm_uniform | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 4/4 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 32，观测区间 32 - 32，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpm_2，4 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：发现KSampler但没有VAEDecode
