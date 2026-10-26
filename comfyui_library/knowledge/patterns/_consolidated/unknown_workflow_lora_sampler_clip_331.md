---
name: unknown_workflow_lora_sampler_clip_331
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.735
common_nodes: [CLIPLoader, CLIPTextEncode, Canny, KSampler, LoadImage, LoraLoader, ModelSamplingSD3, PreviewImage, TrimVideoLatent, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, WanVaceToVideo]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/WAN-线稿控制_2004076239071657986.json, 视频生成/图生视频/video_wan_vace_14B_v2v (2)动作控制_1951169906266058753.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_331

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/WAN-线稿控制_2004076239071657986.json、视频生成/图生视频/video_wan_vace_14B_v2v (2)动作控制_1951169906266058753.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：74%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Canny`
- `KSampler`
- `LoadImage`
- `LoraLoader`
- `ModelSamplingSD3`
- `PreviewImage`
- `TrimVideoLatent`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `WanVaceToVideo`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 1/2 个有
- `GetImage` —— 1/2 个有
- `ImageConcatMulti` —— 1/2 个有
- `OpenposePreprocessor` —— 1/2 个有
- `PathchSageAttentionKJ` —— 1/2 个有
- `SaveVideo` —— 1/2 个有
- `VHS_VideoCombine` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | - | 2 | 67% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | uni_pc | - | 2 | 50% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| LoRA 模型强度 | 0.3 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，2 个样本，一致性 50%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.3，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
