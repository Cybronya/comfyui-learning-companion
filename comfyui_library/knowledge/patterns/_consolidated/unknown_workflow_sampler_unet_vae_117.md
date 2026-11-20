---
name: unknown_workflow_sampler_unet_vae_117
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.757222
common_nodes: [ConditioningZeroOut, DualCLIPLoader, EmptyAceStep1.5LatentAudio, KSampler, ModelSamplingAuraFlow, SaveAudioMP3, TextEncodeAceStepAudio1.5, UNETLoader, VAEDecodeAudio, VAELoader]
problems: [发现KSampler但没有VAEDecode, Steps较低可能导致细节不足]
missing: []
members: [音频生成/音频生成/AI 纯音乐生成 ACE_Step 1.5_2034174640230244354.json, 音频生成/音频生成/Ace-Audio1.5-音乐生成（极速版）_2019745940843794433.json, 音频生成/音频生成/Ace-Step 1.5歌曲生成_2019070986049560578.json, 音频生成/音频生成/Acestep1.5-XL(pro)_2046234223622758402.json, 音频生成/音频生成/Acestep1.5-XL满血版&turbo版_2046207480346189825.json, 音频生成/音频生成/Acestep1.5文生音乐_2029130325330239490.json, 音频生成/音频生成/Acestep1.5最新文生音乐_2020056560453558273.json, 音频生成/音频生成/[🛫书墨]Acestep1.5文生音乐创作工作流_2018940506566303746.json, 音频生成/音频生成/本地免费开源Acestep1.5文生音乐创作工作流_2019643265057824769.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_117

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（音频生成/音频生成/AI 纯音乐生成 ACE_Step 1.5_2034174640230244354.json、音频生成/音频生成/Ace-Audio1.5-音乐生成（极速版）_2019745940843794433.json、音频生成/音频生成/Ace-Step 1.5歌曲生成_2019070986049560578.json、音频生成/音频生成/Acestep1.5-XL(pro)_2046234223622758402.json、音频生成/音频生成/Acestep1.5-XL满血版&turbo版_2046207480346189825.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：76%

## 共有节点

全部 9 个 workflow 都包含：
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
- `Fast Groups Muter (rgthree)` —— 5/9 个有
- `Any Switch (rgthree)` —— 4/9 个有
- `CheckpointLoaderSimple` —— 4/9 个有
- `CR Text` —— 3/9 个有
- `CLIPTextEncode` —— 1/9 个有
- `DF_Text_Box` —— 1/9 个有
- `JjkText` —— 1/9 个有
- `Note Plus (mtb)` —— 1/9 个有
- `Text` —— 1/9 个有
- `Text Multiline` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 50 | 9 | 0% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 9/9 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |
| Steps较低可能导致细节不足 | 7/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 50，9 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：发现KSampler但没有VAEDecode
- 高发问题（7/9 个样本）：Steps较低可能导致细节不足
