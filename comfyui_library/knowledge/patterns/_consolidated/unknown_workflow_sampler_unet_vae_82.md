---
name: unknown_workflow_sampler_unet_vae_82
type: Unknown Workflow
frequency: 13
level: weak
coverage: 0.809308
common_nodes: [ConditioningZeroOut, DualCLIPLoader, EmptyAceStep1.5LatentAudio, KSampler, ModelSamplingAuraFlow, TextEncodeAceStepAudio1.5, UNETLoader, VAEDecodeAudio, VAELoader]
problems: [发现KSampler但没有VAEDecode, Steps较低可能导致细节不足]
missing: []
members: [平台全量/ACE-Step1.5 纯器乐背景音乐 V1_2117465799031087106.json, 平台全量/Acestep1.5开源音乐创作_2029091777650626562.json, 数字人/数字人/▶▶ACE-Step-音乐&歌曲生成流_2055507809432817666.json, 音频生成/音频生成/5-ACE-Step 1.5 XL（音乐生成）_2053473138737991682.json, 音频生成/音频生成/ACE STEP1.5 音乐生成_2019436598701596673.json, 音频生成/音频生成/ACE STEP1.5 音乐生成_2019710020950167553.json, 音频生成/音频生成/ACE-STEP 1.5XL turbo-文生音乐_2077369725973254146.json, 音频生成/音频生成/ACE-Step 1.5 XL Turbo音乐生成工作流_2044247312343502850.json, 音频生成/音频生成/ACE-Step 1.5 XL 音乐制作 SFT版_2064539276913762305.json, 音频生成/音频生成/ACE-Step 生成音乐&歌曲_2082371968904548353.json, 音频生成/音频生成/ACE-Step-音乐&歌曲生成 三合一_2043622653143031809.json, 音频生成/音频生成/ACE-Step音乐（XL版）_2046143739214696450.json, 音频生成/音频生成/ACE-Step音乐（XL版）_2058748041024327682.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_82

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（平台全量/ACE-Step1.5 纯器乐背景音乐 V1_2117465799031087106.json、平台全量/Acestep1.5开源音乐创作_2029091777650626562.json、数字人/数字人/▶▶ACE-Step-音乐&歌曲生成流_2055507809432817666.json、音频生成/音频生成/5-ACE-Step 1.5 XL（音乐生成）_2053473138737991682.json、音频生成/音频生成/ACE STEP1.5 音乐生成_2019436598701596673.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：81%

## 共有节点

全部 13 个 workflow 都包含：
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyAceStep1.5LatentAudio`
- `KSampler`
- `ModelSamplingAuraFlow`
- `TextEncodeAceStepAudio1.5`
- `UNETLoader`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `SaveAudioMP3` —— 12/13 个有
- `PrimitiveInt` —— 9/13 个有
- `Fast Groups Bypasser (rgthree)` —— 4/13 个有
- `CR Text` —— 3/13 个有
- `CR Prompt Text` —— 2/13 个有
- `SaveAudio` —— 2/13 个有
- `Fast Groups Muter (rgthree)` —— 1/13 个有
- `Float` —— 1/13 个有
- `Label (rgthree)` —— 1/13 个有
- `LoraLoaderModelOnly` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 50 | 13 | 24% |
| Prompt 约束强度(CFG) | 1 | 1 - 7 | 13 | 24% |
| 采样算法 | euler | - | 13 | 100% |
| 调度器 | simple | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 13/13 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |
| Steps较低可能导致细节不足 | 10/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 50，13 个样本，取值分散，一致性仅 24%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 7，13 个样本，取值分散，一致性仅 24%
- 采样算法 最常用 euler，13 个样本，一致性 100%
- 调度器 最常用 simple，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 高发问题（13/13 个样本）：发现KSampler但没有VAEDecode
- 高发问题（10/13 个样本）：Steps较低可能导致细节不足
