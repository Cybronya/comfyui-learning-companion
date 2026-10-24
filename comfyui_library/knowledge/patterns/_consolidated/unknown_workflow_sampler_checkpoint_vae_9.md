---
name: unknown_workflow_sampler_checkpoint_vae_9
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.763
common_nodes: [CheckpointLoaderSimple, ConditioningZeroOut, EmptyAceStep1.5LatentAudio, KSampler, ModelSamplingAuraFlow, TextEncodeAceStepAudio1.5, VAEDecodeAudio]
problems: [发现KSampler但没有VAEDecode, Steps较低可能导致细节不足]
missing: []
members: [comfyui-workflow-templates-json/audio_ace_step_1_5_checkpoint.json, 音频生成/音频生成/ACE-STEP 1.5 音乐创作_2019331075352305666.json, 音频生成/音频生成/ACE-Step 1.5大模型：4G显存就能生成AI音乐！_2019019272000905218.json, 音频生成/音频生成/ACE-Step 1.5音乐生成 文本转音乐 长歌曲生成 翻唱 Demo快速生成_2019647657949532162.json, 音频生成/音频生成/Ace Step 1.5 AIO_2019698387427266561.json, 音频生成/音频生成/Ace Step 1.5 AIO_2049505390836060161.json, 音频生成/音频生成/audio_ace_step_1_5_2020710390254014465.json, 音频生成/音频生成/作曲家 秒速歌曲生成 ACE Step_2019579794433773570.json, 音频生成/音频生成/免费音乐创作（堪比suno）AceStep1.5_2020044996040200193.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_checkpoint_vae_9

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（comfyui-workflow-templates-json/audio_ace_step_1_5_checkpoint.json、音频生成/音频生成/ACE-STEP 1.5 音乐创作_2019331075352305666.json、音频生成/音频生成/ACE-Step 1.5大模型：4G显存就能生成AI音乐！_2019019272000905218.json、音频生成/音频生成/ACE-Step 1.5音乐生成 文本转音乐 长歌曲生成 翻唱 Demo快速生成_2019647657949532162.json、音频生成/音频生成/Ace Step 1.5 AIO_2019698387427266561.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：76%

## 共有节点

全部 9 个 workflow 都包含：
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `EmptyAceStep1.5LatentAudio`
- `KSampler`
- `ModelSamplingAuraFlow`
- `TextEncodeAceStepAudio1.5`
- `VAEDecodeAudio`

**可变部分**（部分 workflow 才有）：
- `SaveAudioMP3` —— 8/9 个有
- `CR Text` —— 4/9 个有
- `PreviewAudio` —— 3/9 个有
- `DF_Int_to_Float` —— 1/9 个有
- `JWInteger` —— 1/9 个有
- `Label (rgthree)` —— 1/9 个有
- `PrimitiveFloat` —— 1/9 个有
- `SaveAudioAdvanced` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 12 | 9 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 67% |
| 调度器 | simple | - | 9 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 9/9 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |
| Steps较低可能导致细节不足 | 6/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 12，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 67%
- 调度器 最常用 simple，9 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：发现KSampler但没有VAEDecode
- 高发问题（6/9 个样本）：Steps较低可能导致细节不足
