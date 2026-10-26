---
name: unknown_workflow_sampler_clip_checkpoint_16
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.7846
common_nodes: [CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentAudio, KSampler, VAEDecodeAudio]
problems: [发现KSampler但没有VAEDecode, Steps较低可能导致细节不足]
missing: []
members: [comfyui-workflow-templates-json/audio_stable_audio_example.json, 音频生成/音频生成/Stable Audio3，音乐生成，音频生成，背景音乐生成，视频bgm_2058786934591410178.json, 音频生成/音频生成/【遇见AI】stable-audio-3 背景音模型medium_2057667229650608129.json, 音频生成/音频生成/【遇见AI】stable-audio-3 背景音模型small_music_2041013207766142977.json, 音频生成/音频生成/【遇见AI】stable-audio-3 音效模型small_sfx_2040651445770395650.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_checkpoint_16

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（comfyui-workflow-templates-json/audio_stable_audio_example.json、音频生成/音频生成/Stable Audio3，音乐生成，音频生成，背景音乐生成，视频bgm_2058786934591410178.json、音频生成/音频生成/【遇见AI】stable-audio-3 背景音模型medium_2057667229650608129.json、音频生成/音频生成/【遇见AI】stable-audio-3 背景音模型small_music_2041013207766142977.json、音频生成/音频生成/【遇见AI】stable-audio-3 音效模型small_sfx_2040651445770395650.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentAudio`
- `KSampler`
- `VAEDecodeAudio`

**可变部分**（部分 workflow 才有）：
- `SaveAudioMP3` —— 4/5 个有
- `LoadImage` —— 3/5 个有
- `PrimitiveFloat` —— 1/5 个有
- `PrimitiveStringMultiline` —— 1/5 个有
- `SaveAudioAdvanced` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 60 | 47.6 - 60 | 5 | 91% |
| 高度 | 1 | 1 - 1 | 5 | 100% |
| 采样步数 | 8 | 8 - 50 | 5 | 0% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.98 | 5 | 11% |
| 采样算法 | lcm | - | 5 | 80% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 5/5 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |
| Steps较低可能导致细节不足 | 4/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 60，观测区间 47.6 - 60，5 个样本，取值集中（一致性 91%）
- 高度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 8 - 50，5 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.98，5 个样本，取值分散，一致性仅 11%
- 采样算法 最常用 lcm，5 个样本，一致性 80%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：发现KSampler但没有VAEDecode
- 高发问题（4/5 个样本）：Steps较低可能导致细节不足
