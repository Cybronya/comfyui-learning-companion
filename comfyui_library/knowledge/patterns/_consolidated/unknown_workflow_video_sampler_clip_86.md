---
name: unknown_workflow_video_sampler_clip_86
type: Unknown Workflow
frequency: 7
level: weak
coverage: 0.909429
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo]
problems: []
missing: []
members: [视频生成/图生视频/2043903106605387777.json, 视频生成/文生视频/Smooth Mix 2.0 混合 LightX2V T2V_2073240392568492034.json, 视频生成/文生视频/1952262518809022466.json, 视频生成/文生视频/1952999225413070849.json, 视频生成/文生视频/1955111888410460162.json, 视频生成/文生视频/1950004459780923393.json, 音频生成/音频生成/极速10s视频6步超极速图生视频V3只需3分钟_2046504111113248770.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_86

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/2043903106605387777.json、视频生成/文生视频/Smooth Mix 2.0 混合 LightX2V T2V_2073240392568492034.json、视频生成/文生视频/1952262518809022466.json、视频生成/文生视频/1952999225413070849.json、视频生成/文生视频/1955111888410460162.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: PurgeVRAM` —— 6/7 个有
- `LoadImage` —— 6/7 个有
- `LoraLoaderModelOnly` —— 6/7 个有
- `ModelSamplingSD3` —— 6/7 个有
- `JWInteger` —— 5/7 个有
- `PathchSageAttentionKJ` —— 4/7 个有
- `CR Prompt Text` —— 1/7 个有
- `Int` —— 1/7 个有
- `LoraLoader` —— 1/7 个有
- `RH_Translator` —— 1/7 个有
- `WujiAudioLoader` —— 1/7 个有
- `easy showAnything` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 7 | 86% |
| Prompt 约束强度(CFG) | 6 | 6 - 40 | 7 | 5% |
| 采样算法 | 1 | 1 - 1 | 7 | 100% |
| 调度器 | lcm | - | 7 | 57% |
| 重绘幅度 | simple | - | 7 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，7 个样本，一致性 86%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 40，7 个样本，取值分散，一致性仅 5%
- 采样算法 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 调度器 最常用 lcm，7 个样本，一致性 57%
- 重绘幅度 最常用 simple，7 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 40，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
