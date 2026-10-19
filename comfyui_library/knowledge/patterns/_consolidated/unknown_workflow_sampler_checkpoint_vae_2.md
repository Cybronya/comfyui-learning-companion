---
name: unknown_workflow_sampler_checkpoint_vae_2
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.717286
common_nodes: [AudioEncoderLoader, CheckpointLoaderSimple, EmptyYuE2LatentAudio, KSampler, LoadAudio, SaveAudioAdvanced, SheetSage2AudioToABC, VAEDecodeAudio, YuE2GenerateMusic]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [音频生成/音频生成/YUE2 歌曲翻唱（上传要翻唱的音乐）_2109788535506161665.json, 音频生成/音频生成/YUE2翻唱_2099445891001311234.json, 音频生成/音频生成/YuE2 音乐翻唱_2108808387176783873.json, 音频生成/音频生成/YuE2 音乐翻唱_2108812860787879937.json, 音频生成/音频生成/Yue2音乐翻唱——堪比闭源模型的开源工作流_2107213273505550337.json, 音频生成/音频生成/【遇见AI】YUe2音乐模型，音乐参考ABC+新歌词做歌曲翻唱_2100118618569793537.json, 音频生成/音频生成/音乐翻唱_YuE2_2107047578494918658.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_checkpoint_vae_2

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（音频生成/音频生成/YUE2 歌曲翻唱（上传要翻唱的音乐）_2109788535506161665.json、音频生成/音频生成/YUE2翻唱_2099445891001311234.json、音频生成/音频生成/YuE2 音乐翻唱_2108808387176783873.json、音频生成/音频生成/YuE2 音乐翻唱_2108812860787879937.json、音频生成/音频生成/Yue2音乐翻唱——堪比闭源模型的开源工作流_2107213273505550337.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：72%

## 共有节点

全部 7 个 workflow 都包含：
- `AudioEncoderLoader`
- `CheckpointLoaderSimple`
- `EmptyYuE2LatentAudio`
- `KSampler`
- `LoadAudio`
- `SaveAudioAdvanced`
- `SheetSage2AudioToABC`
- `VAEDecodeAudio`
- `YuE2GenerateMusic`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 6/7 个有
- `PreviewAny` —— 6/7 个有
- `PrimitiveStringMultiline` —— 6/7 个有
- `SeedNode` —— 4/7 个有
- `LoadImage` —— 2/7 个有
- `Audio Duration` —— 1/7 个有
- `AudioCrop` —— 1/7 个有
- `PrimitiveFloat` —— 1/7 个有
- `easy showAnything` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 32 | 32 - 32 | 7 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | dpm_2 | - | 7 | 100% |
| 调度器 | sgm_uniform | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 7/7 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 32，观测区间 32 - 32，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpm_2，7 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：发现KSampler但没有VAEDecode
