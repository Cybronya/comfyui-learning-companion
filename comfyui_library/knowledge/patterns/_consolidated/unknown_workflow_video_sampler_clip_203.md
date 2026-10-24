---
name: unknown_workflow_video_sampler_clip_203
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.912333
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, KSampler, LoadImage, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/电商首尾帧生图（高清稳定版）wan21 flf2v_2012067791884521474.json, 视频生成/图生视频/简单挤压捏爆工作流_1906949243003707394.json, 视频生成/图生视频/转身开枪射击+通义万相=艾橘溪_1900090706587967489.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_203

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/电商首尾帧生图（高清稳定版）wan21 flf2v_2012067791884521474.json、视频生成/图生视频/简单挤压捏爆工作流_1906949243003707394.json、视频生成/图生视频/转身开枪射击+通义万相=艾橘溪_1900090706587967489.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `KSampler`
- `LoadImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `WanImageToVideo` —— 2/3 个有
- `ImageResizeAdvanced` —— 1/3 个有
- `LayerUtility: PurgeVRAM` —— 1/3 个有
- `LoraLoader` —— 1/3 个有
- `ModelSamplingSD3` —— 1/3 个有
- `Seed Everywhere` —— 1/3 个有
- `WanFirstLastFrameToVideo` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 4 - 30 | 3 | 41% |
| Prompt 约束强度(CFG) | 5 | 1 - 6 | 3 | 46% |
| 采样算法 | uni_pc | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 4 - 30，3 个样本，取值分散，一致性仅 41%
- Prompt 约束强度(CFG) 中位数 5，观测区间 1 - 6，3 个样本，取值分散，一致性仅 46%
- 采样算法 最常用 uni_pc，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
