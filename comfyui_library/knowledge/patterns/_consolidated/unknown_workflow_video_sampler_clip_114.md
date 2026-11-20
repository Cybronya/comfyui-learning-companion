---
name: unknown_workflow_video_sampler_clip_114
type: Unknown Workflow
frequency: 6
level: weak
coverage: 0.800667
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo]
problems: []
missing: []
members: [视频生成/图生视频/基础：wan2.2=图生视频=高低噪（简单理解版）_2025730083717124097.json, 视频生成/图生视频/扩散模型_去噪过程演示_2043903106605387777.json, 视频生成/文生视频/Smooth Mix 2.0 混合 LightX2V T2V_2073240392568492034.json, 视频生成/文生视频/[极速生成] Wan2.2 1分钟 81帧6步 图生视频 影视级真实效果_1952262518809022466.json, 视频生成/文生视频/【美女跳舞】Wan2.2 14B+LightX2V 图片生成视频_1955111888410460162.json, 音频生成/音频生成/极速10s视频6步超极速图生视频V3只需3分钟_2046504111113248770.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_114

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/基础：wan2.2=图生视频=高低噪（简单理解版）_2025730083717124097.json、视频生成/图生视频/扩散模型_去噪过程演示_2043903106605387777.json、视频生成/文生视频/Smooth Mix 2.0 混合 LightX2V T2V_2073240392568492034.json、视频生成/文生视频/[极速生成] Wan2.2 1分钟 81帧6步 图生视频 影视级真实效果_1952262518809022466.json、视频生成/文生视频/【美女跳舞】Wan2.2 14B+LightX2V 图片生成视频_1955111888410460162.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：80%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `JWInteger` —— 5/6 个有
- `LayerUtility: PurgeVRAM` —— 5/6 个有
- `LoadImage` —— 5/6 个有
- `ModelSamplingSD3` —— 5/6 个有
- `LoraLoaderModelOnly` —— 4/6 个有
- `PathchSageAttentionKJ` —— 3/6 个有
- `CR Prompt Text` —— 1/6 个有
- `GetNode` —— 1/6 个有
- `LoraLoader` —— 1/6 个有
- `SetNode` —— 1/6 个有
- `WujiAudioLoader` —— 1/6 个有
- `easy showAnything` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 6 | 83% |
| Prompt 约束强度(CFG) | 7 | 6 - 40 | 6 | 13% |
| 采样算法 | 1 | 1 - 3.5 | 6 | 34% |
| 调度器 | lcm | - | 6 | 50% |
| 重绘幅度 | simple | - | 6 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，6 个样本，一致性 83%
- Prompt 约束强度(CFG) 中位数 7，观测区间 6 - 40，6 个样本，取值分散，一致性仅 13%
- 采样算法 中位数 1，观测区间 1 - 3.5，6 个样本，取值分散，一致性仅 34%
- 调度器 最常用 lcm，6 个样本，一致性 50%
- 重绘幅度 最常用 simple，6 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 40，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
