---
name: unknown_workflow_sampler_checkpoint_vae_18
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.614333
common_nodes: [CheckpointLoaderSimple, EmptyYuE2LatentAudio, KSampler, PrimitiveStringMultiline, SaveAudioAdvanced, VAEDecodeAudio, YuE2GenerateMusic]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/图生图/YUe2音乐模型文生音乐基础工作流_2101872989762580482.json, 图片生成/图生图/YUe2音乐模型，音乐参考ABC+新歌词做歌曲翻唱_2101872219881304065.json, 数字人/数字人/【翻唱-女生清唱版】YuE2-音乐生成_2117079569273548802.json, 音频生成/音频生成/YUE2翻唱_2099445891001311234.json, 音频生成/音频生成/【翻唱】YuE2-音乐生成_2099610843628531714.json, 音频生成/音频生成/【遇见AI】YUe2音乐模型，音乐参考ABC+新歌词做歌曲翻唱_2100118618569793537.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_checkpoint_vae_18

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/YUe2音乐模型文生音乐基础工作流_2101872989762580482.json、图片生成/图生图/YUe2音乐模型，音乐参考ABC+新歌词做歌曲翻唱_2101872219881304065.json、数字人/数字人/【翻唱-女生清唱版】YuE2-音乐生成_2117079569273548802.json、音频生成/音频生成/YUE2翻唱_2099445891001311234.json、音频生成/音频生成/【翻唱】YuE2-音乐生成_2099610843628531714.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：61%

## 共有节点

全部 6 个 workflow 都包含：
- `CheckpointLoaderSimple`
- `EmptyYuE2LatentAudio`
- `KSampler`
- `PrimitiveStringMultiline`
- `SaveAudioAdvanced`
- `VAEDecodeAudio`
- `YuE2GenerateMusic`

**可变部分**（部分 workflow 才有）：
- `AudioEncoderLoader` —— 5/6 个有
- `LoadAudio` —— 5/6 个有
- `SheetSage2AudioToABC` —— 5/6 个有
- `LoadImage` —— 4/6 个有
- `PreviewAny` —— 4/6 个有
- `easy showAnything` —— 4/6 个有
- `ConditioningZeroOut` —— 3/6 个有
- `Any Switch (rgthree)` —— 2/6 个有
- `EmptyImage` —— 2/6 个有
- `Fast Groups Muter (rgthree)` —— 2/6 个有
- `PreviewImage` —— 2/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 32 | 32 - 32 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1.1 | 6 | 95% |
| 采样算法 | dpm_2 | - | 6 | 100% |
| 调度器 | sgm_uniform | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 6/6 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 32，观测区间 32 - 32，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1.1，6 个样本，取值集中（一致性 95%）
- 采样算法 最常用 dpm_2，6 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：发现KSampler但没有VAEDecode
