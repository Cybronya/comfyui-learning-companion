---
name: unknown_workflow_sampler_checkpoint_vae_25
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.7342
common_nodes: [CheckpointLoaderSimple, EmptyYuE2LatentAudio, KSampler, SaveAudioAdvanced, VAEDecodeAudio, YuE2GenerateMusic]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [音频生成/音频生成/YuE2 音乐生成｜让文字唤醒旋律_2099846452192301058.json, 音频生成/音频生成/Yue2文生音乐_2099713882154688514.json, 音频生成/音频生成/yue2官方音乐生成_2099479292316053506.json, 音频生成/音频生成/yue2音乐生成_2099423871081476097.json, 音频生成/音频生成/【遇见AI】YUe2音乐模型文生音乐基础工作流_2099708088843587586.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_checkpoint_vae_25

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（音频生成/音频生成/YuE2 音乐生成｜让文字唤醒旋律_2099846452192301058.json、音频生成/音频生成/Yue2文生音乐_2099713882154688514.json、音频生成/音频生成/yue2官方音乐生成_2099479292316053506.json、音频生成/音频生成/yue2音乐生成_2099423871081476097.json、音频生成/音频生成/【遇见AI】YUe2音乐模型文生音乐基础工作流_2099708088843587586.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：73%

## 共有节点

全部 5 个 workflow 都包含：
- `CheckpointLoaderSimple`
- `EmptyYuE2LatentAudio`
- `KSampler`
- `SaveAudioAdvanced`
- `VAEDecodeAudio`
- `YuE2GenerateMusic`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 4/5 个有
- `YuE2GenerateABC` —— 4/5 个有
- `PreviewAny` —— 3/5 个有
- `LoadImage` —— 2/5 个有
- `CR Prompt Text` —— 1/5 个有
- `ConditioningZeroOut` —— 1/5 个有
- `PreviewAudio` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 32 | 32 - 32 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 0.5 - 1 | 5 | 78% |
| 采样算法 | dpm_2 | - | 5 | 80% |
| 调度器 | sgm_uniform | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 5/5 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 32，观测区间 32 - 32，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 0.5 - 1，5 个样本
- 采样算法 最常用 dpm_2，5 个样本，一致性 80%
- 调度器 最常用 sgm_uniform，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 0.5，低于常用下限 1（CFG 过低可能导致 Prompt 约束不足、结果偏离描述）
- 高发问题（5/5 个样本）：发现KSampler但没有VAEDecode
