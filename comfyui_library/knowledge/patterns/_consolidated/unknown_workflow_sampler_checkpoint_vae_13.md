---
name: unknown_workflow_sampler_checkpoint_vae_13
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.699125
common_nodes: [CheckpointLoaderSimple, EmptyYuE2LatentAudio, KSampler, PrimitiveStringMultiline, SaveAudioAdvanced, VAEDecodeAudio, YuE2GenerateMusic]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/图生图/YUe2音乐模型文生音乐基础工作流_2101872989762580482.json, 图片生成/图生图/YUe2音乐模型，音乐参考ABC+新歌词做歌曲翻唱_2101872219881304065.json, 音频生成/音频生成/YUE2 歌曲翻唱（上传要翻唱的音乐）_2109788535506161665.json, 音频生成/音频生成/YUE2翻唱_2099445891001311234.json, 音频生成/音频生成/YuE2 音乐翻唱_2108808387176783873.json, 音频生成/音频生成/YuE2 音乐翻唱_2108812860787879937.json, 音频生成/音频生成/Yue2音乐翻唱——堪比闭源模型的开源工作流_2107213273505550337.json, 音频生成/音频生成/yinyueshengcheng_2104844494637191169.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_checkpoint_vae_13

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/YUe2音乐模型文生音乐基础工作流_2101872989762580482.json、图片生成/图生图/YUe2音乐模型，音乐参考ABC+新歌词做歌曲翻唱_2101872219881304065.json、音频生成/音频生成/YUE2 歌曲翻唱（上传要翻唱的音乐）_2109788535506161665.json、音频生成/音频生成/YUE2翻唱_2099445891001311234.json、音频生成/音频生成/YuE2 音乐翻唱_2108808387176783873.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：70%

## 共有节点

全部 8 个 workflow 都包含：
- `CheckpointLoaderSimple`
- `EmptyYuE2LatentAudio`
- `KSampler`
- `PrimitiveStringMultiline`
- `SaveAudioAdvanced`
- `VAEDecodeAudio`
- `YuE2GenerateMusic`

**可变部分**（部分 workflow 才有）：
- `AudioEncoderLoader` —— 7/8 个有
- `ConditioningZeroOut` —— 7/8 个有
- `LoadAudio` —— 7/8 个有
- `SheetSage2AudioToABC` —— 7/8 个有
- `PreviewAny` —— 6/8 个有
- `LoadImage` —— 3/8 个有
- `SeedNode` —— 3/8 个有
- `Audio Duration` —— 2/8 个有
- `AudioCrop` —— 2/8 个有
- `EmptyImage` —— 2/8 个有
- `PreviewImage` —— 2/8 个有
- `PrimitiveFloat` —— 1/8 个有
- `PrimitiveString` —— 1/8 个有
- `easy showAnything` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 32 | 32 - 32 | 8 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | dpm_2 | - | 8 | 100% |
| 调度器 | sgm_uniform | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 8/8 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 32，观测区间 32 - 32，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpm_2，8 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：发现KSampler但没有VAEDecode
