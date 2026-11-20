---
name: unknown_workflow_sampler_clip_checkpoint_39
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9165
common_nodes: [CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentAudio, KSampler, SaveAudio, VAEDecodeAudio]
problems: [发现KSampler但没有VAEDecode, Steps较低可能导致细节不足]
missing: []
members: [音频生成/音频生成/VividMuse Stable Audio 3 Medium Workflow_2058890111261175809.json, 音频生成/音频生成/🔊 一句话生成游戏音效｜Stable Audio 3 Small SFX V1.1_2114675404417101825.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_checkpoint_39

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/VividMuse Stable Audio 3 Medium Workflow_2058890111261175809.json、音频生成/音频生成/🔊 一句话生成游戏音效｜Stable Audio 3 Small SFX V1.1_2114675404417101825.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentAudio`
- `KSampler`
- `SaveAudio`
- `VAEDecodeAudio`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有
- `Seed (rgthree)` —— 1/2 个有
- `easy promptList` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | - | 2 | 89% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | lcm | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 32 | - | 2 | 12% |
| 高度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 2/2 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 lcm，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 32，样本不足，未给区间，2 个样本，取值分散，一致性仅 12%
- 高度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：发现KSampler但没有VAEDecode
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
