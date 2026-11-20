---
name: unknown_workflow_sampler_checkpoint_vae_20
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.613
common_nodes: [CheckpointLoaderSimple, ConditioningZeroOut, EmptyYuE2LatentAudio, KSampler, PreviewAny, PrimitiveStringMultiline, SaveAudioAdvanced, SeedNode, VAEDecodeAudio, YuE2GenerateMusic]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [音频生成/音频生成/YuE2-文生音乐-ComfyUI官方版本(非常好 好听)_2109834100810018818.json, 音频生成/音频生成/YuE2-文生音乐-ComfyUI官方版本_2100799504231526401.json, 音频生成/音频生成/YuE2-文生音乐-ComfyUI官方版本_2101632211412938753.json, 音频生成/音频生成/YuE2-音乐翻唱-ComfyUI官方版本_2100774608726216705.json, 音频生成/音频生成/YuE2文生音乐官方_2103060900860223490.json, 音频生成/音频生成/audio_yue2_music_cover_2104470509722365954.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_checkpoint_vae_20

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（音频生成/音频生成/YuE2-文生音乐-ComfyUI官方版本(非常好 好听)_2109834100810018818.json、音频生成/音频生成/YuE2-文生音乐-ComfyUI官方版本_2100799504231526401.json、音频生成/音频生成/YuE2-文生音乐-ComfyUI官方版本_2101632211412938753.json、音频生成/音频生成/YuE2-音乐翻唱-ComfyUI官方版本_2100774608726216705.json、音频生成/音频生成/YuE2文生音乐官方_2103060900860223490.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：61%

## 共有节点

全部 6 个 workflow 都包含：
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `EmptyYuE2LatentAudio`
- `KSampler`
- `PreviewAny`
- `PrimitiveStringMultiline`
- `SaveAudioAdvanced`
- `SeedNode`
- `VAEDecodeAudio`
- `YuE2GenerateMusic`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 5/6 个有
- `PrimitiveBoolean` —— 5/6 个有
- `PrimitiveFloat` —— 5/6 个有
- `PrimitiveString` —— 4/6 个有
- `YuE2GenerateABC` —— 4/6 个有
- `Audio Duration (mtb)` —— 3/6 个有
- `LoadImage` —— 3/6 个有
- `MathExpression|pysssss` —— 3/6 个有
- `RepeatImageBatch` —— 3/6 个有
- `VHS_VideoCombine` —— 3/6 个有
- `AudioEncoderLoader` —— 2/6 个有
- `LoadAudio` —— 2/6 个有
- `PrimitiveInt` —— 2/6 个有
- `SheetSage2AudioToABC` —— 2/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 32 | 32 - 32 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | dpm_2 | - | 6 | 100% |
| 调度器 | sgm_uniform | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 6/6 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 32，观测区间 32 - 32，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpm_2，6 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：发现KSampler但没有VAEDecode
