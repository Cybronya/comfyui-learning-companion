---
name: unknown_workflow_sampler_unet_vae_104
type: Unknown Workflow
frequency: 10
level: weak
coverage: 0.8285
common_nodes: [ConditioningZeroOut, DualCLIPLoader, EmptyAceStep1.5LatentAudio, KSampler, ModelSamplingAuraFlow, SaveAudioMP3, TextEncodeAceStepAudio1.5, UNETLoader, VAEDecodeAudio, VAELoader]
problems: [发现KSampler但没有VAEDecode, Steps较低可能导致细节不足]
missing: []
members: [音频生成/音频生成/ACE-Step 1.5 XL 音乐制作 SFT版_2064539276913762305.json, 音频生成/音频生成/ACE-Step 生成音乐&歌曲_2082371968904548353.json, 音频生成/音频生成/ACE-Step-音乐&歌曲生成 三合一_2043622653143031809.json, 音频生成/音频生成/ACE-Step音乐（XL版）_2046143739214696450.json, 音频生成/音频生成/ACE-Step音乐（XL版）_2058748041024327682.json, 音频生成/音频生成/AI 纯音乐生成 ACE_Step 1.5_2034174640230244354.json, 音频生成/音频生成/Ace-Audio1.5-音乐生成（极速版）_2019745940843794433.json, 音频生成/音频生成/Acestep1.5-XL(pro)_2046234223622758402.json, 音频生成/音频生成/Acestep1.5-XL满血版&turbo版_2046207480346189825.json, 音频生成/音频生成/▶ACE 音乐_歌曲Turbo版(推荐)_2058375430863937537.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_104

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（音频生成/音频生成/ACE-Step 1.5 XL 音乐制作 SFT版_2064539276913762305.json、音频生成/音频生成/ACE-Step 生成音乐&歌曲_2082371968904548353.json、音频生成/音频生成/ACE-Step-音乐&歌曲生成 三合一_2043622653143031809.json、音频生成/音频生成/ACE-Step音乐（XL版）_2046143739214696450.json、音频生成/音频生成/ACE-Step音乐（XL版）_2058748041024327682.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 10 个 workflow 都包含：
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyAceStep1.5LatentAudio`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveAudioMP3`
- `TextEncodeAceStepAudio1.5`
- `UNETLoader`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 6/10 个有
- `PrimitiveInt` —— 6/10 个有
- `Fast Groups Bypasser (rgthree)` —— 4/10 个有
- `Fast Groups Muter (rgthree)` —— 2/10 个有
- `JjkText` —— 2/10 个有
- `CLIPTextEncode` —— 1/10 个有
- `LayerUtility: TextJoin` —— 1/10 个有
- `LoadImage` —— 1/10 个有
- `SaveAudio` —— 1/10 个有
- `Switch` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 29 | 8 - 50 | 10 | 28% |
| Prompt 约束强度(CFG) | 1 | 1 - 7 | 10 | 10% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 10/10 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |
| Steps较低可能导致细节不足 | 7/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 29，观测区间 8 - 50，10 个样本，取值分散，一致性仅 28%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 7，10 个样本，取值分散，一致性仅 10%
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：发现KSampler但没有VAEDecode
- 高发问题（7/10 个样本）：Steps较低可能导致细节不足
