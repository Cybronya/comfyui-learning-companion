---
name: unknown_workflow_sampler_unet_vae_61
type: Unknown Workflow
frequency: 14
level: weak
coverage: 0.8405
common_nodes: [ConditioningZeroOut, DualCLIPLoader, EmptyAceStep1.5LatentAudio, KSampler, ModelSamplingAuraFlow, TextEncodeAceStepAudio1.5, UNETLoader, VAELoader]
problems: [发现KSampler但没有VAEDecode, Steps较低可能导致细节不足]
missing: []
members: [comfyui-workflow-templates-json/audio_ace_step1_5_xl_base.json, comfyui-workflow-templates-json/audio_ace_step1_5_xl_sft.json, comfyui-workflow-templates-json/audio_ace_step1_5_xl_turbo.json, comfyui-workflow-templates-json/audio_ace_step_1_5_split.json, comfyui-workflow-templates-json/audio_ace_step_1_5_split_4b.json, 图片生成/图生图/ACE音乐双采_2073319447737225218.json, 数字人/数字人/ace-step 1.5 _ 音乐生成最佳搭档_2115348339779792898.json, 音频生成/音频生成/ACE-STEP1.5XL  Ai音乐歌曲创作工作流_2044312736724684802.json, 音频生成/音频生成/ACE-STEP1.5XL_2044231615613767681.json, 音频生成/音频生成/ACE-Step 1.5 XL base音乐生成_2045373190855200769.json, 音频生成/音频生成/ace-step 1.5 _ 音乐生成最佳搭档_2075297299286286338.json, 音频生成/音频生成/多人合唱-音乐生成-ACE-STEP1.5XL_2045332746666516482.json, 音频生成/音频生成/方格智联-ACE-1.5音乐_2086670840938192898.json, 音频生成/音频生成/音乐生成-ACE-STEP1.5XL_2045321458674573313.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_61

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（comfyui-workflow-templates-json/audio_ace_step1_5_xl_base.json、comfyui-workflow-templates-json/audio_ace_step1_5_xl_sft.json、comfyui-workflow-templates-json/audio_ace_step1_5_xl_turbo.json、comfyui-workflow-templates-json/audio_ace_step_1_5_split.json、comfyui-workflow-templates-json/audio_ace_step_1_5_split_4b.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 14 个 workflow 都包含：
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyAceStep1.5LatentAudio`
- `KSampler`
- `ModelSamplingAuraFlow`
- `TextEncodeAceStepAudio1.5`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `VAEDecodeAudio` —— 13/14 个有
- `PrimitiveInt` —— 12/14 个有
- `SaveAudioMP3` —— 11/14 个有
- `CR Text` —— 8/14 个有
- `Float` —— 7/14 个有
- `Int` —— 7/14 个有
- `SaveAudioAdvanced` —— 3/14 个有
- `JjkText` —— 2/14 个有
- `LoadImage` —— 2/14 个有
- `LoraLoaderModelOnly` —— 1/14 个有
- `VAEDecodeAudioTiled` —— 1/14 个有
- `VRAM_Debug` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 50 | 14 | 3% |
| Prompt 约束强度(CFG) | 1 | 1 - 7 | 14 | 0% |
| 采样算法 | euler | - | 14 | 100% |
| 调度器 | simple | - | 14 | 100% |
| 重绘幅度 | 1 | 0.22 - 1 | 14 | 79% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 14/14 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |
| Steps较低可能导致细节不足 | 12/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 50，14 个样本，取值分散，一致性仅 3%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 7，14 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，14 个样本，一致性 100%
- 调度器 最常用 simple，14 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.22 - 1，14 个样本
- 高发问题（14/14 个样本）：发现KSampler但没有VAEDecode
- 高发问题（12/14 个样本）：Steps较低可能导致细节不足
