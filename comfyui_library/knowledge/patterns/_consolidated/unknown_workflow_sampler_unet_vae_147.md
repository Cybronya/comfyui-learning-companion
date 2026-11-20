---
name: unknown_workflow_sampler_unet_vae_147
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.819444
common_nodes: [ConditioningZeroOut, DualCLIPLoader, EmptyAceStep1.5LatentAudio, KSampler, ModelSamplingAuraFlow, SaveAudioMP3, TextEncodeAceStepAudio1.5, UNETLoader, VAEDecodeAudio]
problems: [发现KSampler但没有VAEDecode, Steps较低可能导致细节不足]
missing: []
members: [音频生成/音频生成/Acestep-xl-turbo音乐歌曲生成V1_2042470485371396097.json, 音频生成/音频生成/Acestep-xl-turbo音乐歌曲生成V1_2044010905905668097.json, 音频生成/音频生成/Acestep-xl-turbo音乐歌曲自动生成器_2042813080727461890.json, 音频生成/音频生成/Acestep-xl音乐生成_2043108252040306689.json, 音频生成/音频生成/acestep-v15-xl-turbo 音乐歌曲生成  Acestep-xl-turbo 开源霸主_2042573351738155009.json, 音频生成/音频生成/【遇见AI】ace-step-1.5音乐生成_2019270577105674242.json, 音频生成/音频生成/一键生成音乐，效果堪比SUNO!_2047582479183257601.json, 音频生成/音频生成/手_自动歌词-音乐歌曲生成Acestep-xl-turbo_2043000518099869697.json, 音频生成/音频生成/最新Acestep-xl-turbo音乐歌曲生成_2042652525186256898.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_147

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（音频生成/音频生成/Acestep-xl-turbo音乐歌曲生成V1_2042470485371396097.json、音频生成/音频生成/Acestep-xl-turbo音乐歌曲生成V1_2044010905905668097.json、音频生成/音频生成/Acestep-xl-turbo音乐歌曲自动生成器_2042813080727461890.json、音频生成/音频生成/Acestep-xl音乐生成_2043108252040306689.json、音频生成/音频生成/acestep-v15-xl-turbo 音乐歌曲生成  Acestep-xl-turbo 开源霸主_2042573351738155009.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：82%

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

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 8/9 个有
- `VAELoader` —— 8/9 个有
- `PreviewAny` —— 7/9 个有
- `RegexExtract` —— 7/9 个有
- `easy anythingIndexSwitch` —— 7/9 个有
- `RH_LLMAPI_Pro_Node` —— 6/9 个有
- `Fast Groups Bypasser (rgthree)` —— 1/9 个有
- `GetNode` —— 1/9 个有
- `Int` —— 1/9 个有
- `Label (rgthree)` —— 1/9 个有
- `RHHiddenNodes` —— 1/9 个有
- `SetNode` —— 1/9 个有
- `ShellAgentPluginOutputText` —— 1/9 个有
- `easy cleanGpuUsed` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 50 | 9 | 0% |
| Prompt 约束强度(CFG) | 1 | 1 - 1.2 | 9 | 94% |
| 采样算法 | euler | - | 9 | 89% |
| 调度器 | simple | - | 9 | 89% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 9/9 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |
| Steps较低可能导致细节不足 | 7/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 50，9 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1.2，9 个样本，取值集中（一致性 94%）
- 采样算法 最常用 euler，9 个样本，一致性 89%
- 调度器 最常用 simple，9 个样本，一致性 89%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：发现KSampler但没有VAEDecode
- 高发问题（7/9 个样本）：Steps较低可能导致细节不足
