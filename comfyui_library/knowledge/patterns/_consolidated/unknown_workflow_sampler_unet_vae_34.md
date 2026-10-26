---
name: unknown_workflow_sampler_unet_vae_34
type: Unknown Workflow
frequency: 16
level: weak
coverage: 0.777937
common_nodes: [ConditioningZeroOut, DualCLIPLoader, EmptyAceStep1.5LatentAudio, KSampler, ModelSamplingAuraFlow, TextEncodeAceStepAudio1.5, UNETLoader, VAELoader]
problems: [发现KSampler但没有VAEDecode, Steps较低可能导致细节不足]
missing: []
members: [comfyui-workflow-templates-json/audio_ace_step1_5_xl_base.json, comfyui-workflow-templates-json/audio_ace_step1_5_xl_sft.json, comfyui-workflow-templates-json/audio_ace_step1_5_xl_turbo.json, comfyui-workflow-templates-json/audio_ace_step_1_5_split.json, comfyui-workflow-templates-json/audio_ace_step_1_5_split_4b.json, 图片生成/图生图/ACE音乐双采_2073319447737225218.json, 数字人/数字人/▶▶ACE-Step-音乐&歌曲生成流_2055507809432817666.json, 音频生成/音频生成/5-ACE-Step 1.5 XL（音乐生成）_2053473138737991682.json, 音频生成/音频生成/ACE STEP1.5 音乐生成_2019436598701596673.json, 音频生成/音频生成/ACE-STEP 1.5XL turbo-文生音乐_2077369725973254146.json, 音频生成/音频生成/ACE-Step 1.5 XL 音乐制作 SFT版_2064539276913762305.json, 音频生成/音频生成/ACE-Step 生成音乐&歌曲_2082371968904548353.json, 音频生成/音频生成/ACE-Step-音乐&歌曲生成 三合一_2043622653143031809.json, 音频生成/音频生成/▶▶ACE-Step-音乐&歌曲生成流_2043662562075615233.json, 音频生成/音频生成/编曲、bgm生成_2053301419213631490.json, 音频生成/音频生成/编曲、歌曲生成、bgm_2048663825725001730.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_34

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（comfyui-workflow-templates-json/audio_ace_step1_5_xl_base.json、comfyui-workflow-templates-json/audio_ace_step1_5_xl_sft.json、comfyui-workflow-templates-json/audio_ace_step1_5_xl_turbo.json、comfyui-workflow-templates-json/audio_ace_step_1_5_split.json、comfyui-workflow-templates-json/audio_ace_step_1_5_split_4b.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：78%

## 共有节点

全部 16 个 workflow 都包含：
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyAceStep1.5LatentAudio`
- `KSampler`
- `ModelSamplingAuraFlow`
- `TextEncodeAceStepAudio1.5`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `VAEDecodeAudio` —— 15/16 个有
- `PrimitiveInt` —— 13/16 个有
- `SaveAudioMP3` —— 13/16 个有
- `Fast Groups Bypasser (rgthree)` —— 3/16 个有
- `SaveAudioAdvanced` —— 3/16 个有
- `Fast Groups Muter (rgthree)` —— 1/16 个有
- `LoraLoaderModelOnly` —— 1/16 个有
- `SaveAudio` —— 1/16 个有
- `VAEDecodeAudioTiled` —— 1/16 个有
- `VRAM_Debug` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 50 | 8 - 50 | 16 | 39% |
| Prompt 约束强度(CFG) | 4 | 1 - 7 | 16 | 33% |
| 采样算法 | euler | - | 16 | 100% |
| 调度器 | simple | - | 16 | 100% |
| 重绘幅度 | 1 | 0.22 - 1 | 16 | 80% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 16/16 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |
| Steps较低可能导致细节不足 | 11/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 50，观测区间 8 - 50，16 个样本，取值分散，一致性仅 39%
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 7，16 个样本，取值分散，一致性仅 33%
- 采样算法 最常用 euler，16 个样本，一致性 100%
- 调度器 最常用 simple，16 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.22 - 1，16 个样本，取值集中（一致性 80%）
- 高发问题（16/16 个样本）：发现KSampler但没有VAEDecode
- 高发问题（11/16 个样本）：Steps较低可能导致细节不足
