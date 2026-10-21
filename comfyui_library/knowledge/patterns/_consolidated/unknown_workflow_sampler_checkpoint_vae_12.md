---
name: unknown_workflow_sampler_checkpoint_vae_12
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.5852
common_nodes: [CheckpointLoaderSimple, ConditioningZeroOut, EmptyYuE2LatentAudio, KSampler, PreviewAny, PrimitiveStringMultiline, SaveAudioAdvanced, VAEDecodeAudio, YuE2GenerateMusic]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [音频生成/音频生成/YuE2音乐模型文生音乐基础工作流_2100397111375384577.json, 音频生成/音频生成/Yue 2 文生成音乐标准版_2108072659945877506.json, 音频生成/音频生成/堪比闭源模型的Yue2_文生音乐最强开源工作流_2107213236771840002.json, 音频生成/音频生成/文本转音乐_YuE2_2107035173647904769.json, 音频生成/音频生成/（写歌 音质非常好）-YuE2-文生音乐_2109775294411399170.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_checkpoint_vae_12

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（音频生成/音频生成/YuE2音乐模型文生音乐基础工作流_2100397111375384577.json、音频生成/音频生成/Yue 2 文生成音乐标准版_2108072659945877506.json、音频生成/音频生成/堪比闭源模型的Yue2_文生音乐最强开源工作流_2107213236771840002.json、音频生成/音频生成/文本转音乐_YuE2_2107035173647904769.json、音频生成/音频生成/（写歌 音质非常好）-YuE2-文生音乐_2109775294411399170.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：59%

## 共有节点

全部 5 个 workflow 都包含：
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `EmptyYuE2LatentAudio`
- `KSampler`
- `PreviewAny`
- `PrimitiveStringMultiline`
- `SaveAudioAdvanced`
- `VAEDecodeAudio`
- `YuE2GenerateMusic`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 4/5 个有
- `PrimitiveBoolean` —— 4/5 个有
- `PrimitiveString` —— 4/5 个有
- `SeedNode` —— 4/5 个有
- `YuE2GenerateABC` —— 4/5 个有
- `PrimitiveFloat` —— 1/5 个有
- `easy float` —— 1/5 个有
- `孤海注释` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 32 | 32 - 32 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | dpm_2 | - | 5 | 100% |
| 调度器 | sgm_uniform | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 5/5 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 32，观测区间 32 - 32，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpm_2，5 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：发现KSampler但没有VAEDecode
