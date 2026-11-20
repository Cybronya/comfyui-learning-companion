---
name: unknown_workflow_sampler_checkpoint_vae_16
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.868167
common_nodes: [CheckpointLoaderSimple, ConditioningZeroOut, KSampler, LatentApplyOperationCFG, LatentOperationTonemapReinhard, ModelSamplingSD3, TextEncodeAceStepAudio, VAEDecodeAudio]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [comfyui-workflow-templates-json/audio_ace_step_1_m2m_editing.json, comfyui-workflow-templates-json/audio_ace_step_1_t2a_instrumentals.json, comfyui-workflow-templates-json/audio_ace_step_1_t2a_song.json, 平台全量/【AI音乐大模型】ACE-Step炸裂登场！20秒定制多风格+多语种MV音乐！_1924766261710868481.json, 音频生成/音频生成/原生文生音乐AceStep_1928498081749217281.json, 音频生成/音频生成/文生歌曲_1960649204559413249.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_checkpoint_vae_16

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（comfyui-workflow-templates-json/audio_ace_step_1_m2m_editing.json、comfyui-workflow-templates-json/audio_ace_step_1_t2a_instrumentals.json、comfyui-workflow-templates-json/audio_ace_step_1_t2a_song.json、平台全量/【AI音乐大模型】ACE-Step炸裂登场！20秒定制多风格+多语种MV音乐！_1924766261710868481.json、音频生成/音频生成/原生文生音乐AceStep_1928498081749217281.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 6 个 workflow 都包含：
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `KSampler`
- `LatentApplyOperationCFG`
- `LatentOperationTonemapReinhard`
- `ModelSamplingSD3`
- `TextEncodeAceStepAudio`
- `VAEDecodeAudio`

**可变部分**（部分 workflow 才有）：
- `EmptyAceStepLatentAudio` —— 5/6 个有
- `LoadAudio` —— 4/6 个有
- `VAEEncodeAudio` —— 4/6 个有
- `SaveAudio` —— 3/6 个有
- `SaveAudioMP3` —— 3/6 个有
- `SaveAudioAdvanced` —— 2/6 个有
- `SaveAudioOpus` —— 2/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 50 | 50 - 50 | 6 | 100% |
| Prompt 约束强度(CFG) | 5 | 5 - 5 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 0.3 - 1 | 6 | 70% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 6/6 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 50，观测区间 50 - 50，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 5，观测区间 5 - 5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.3 - 1，6 个样本
- 高发问题（6/6 个样本）：发现KSampler但没有VAEDecode
