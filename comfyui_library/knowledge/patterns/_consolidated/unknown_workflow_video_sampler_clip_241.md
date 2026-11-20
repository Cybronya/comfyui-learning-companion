---
name: unknown_workflow_video_sampler_clip_241
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9305
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, ModelSamplingSD3, UNETLoader, VAEDecode, VAEEncode, VAELoader, VHS_LoadVideo, VHS_VideoCombine]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/视频修复工作流_2067898491430592514.json, 音频生成/音频生成/一句话编辑你的视频，放弃vace吧_1970462951100608514.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_241

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/视频修复工作流_2067898491430592514.json、音频生成/音频生成/一句话编辑你的视频，放弃vace吧_1970462951100608514.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ImageConcanate` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `LucyConditionConcatNode` —— 1/2 个有
- `PrimitiveFloat` —— 1/2 个有
- `VHS_VideoInfo` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 27 | - | 2 | 15% |
| Prompt 约束强度(CFG) | 3 | - | 2 | 33% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 0.65 | - | 2 | 46% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 27，样本不足，未给区间，2 个样本，取值分散，一致性仅 15%
- Prompt 约束强度(CFG) 中位数 3，样本不足，未给区间，2 个样本，取值分散，一致性仅 33%
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 0.65，样本不足，未给区间，2 个样本，取值分散，一致性仅 46%
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
