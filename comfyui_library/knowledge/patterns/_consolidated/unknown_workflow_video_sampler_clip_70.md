---
name: unknown_workflow_video_sampler_clip_70
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.974667
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, KSampler, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/WAN2.1 Comfy-Org 文生视频官方原始工作流_1895182420566212609.json, 视频生成/文生视频/WAN2.1文生视频_1977308765202587649.json, 视频生成/文生视频/WAN2.2 人物角色模特服装百变更换衣服_1954771341195960322.json, 视频生成/文生视频/Wan2.1+t2v Lora文生视频工作流_1951460131294883841.json, 视频生成/文生视频/Wan2.1文生视频工作流_1934444729025327105.json, 视频生成/文生视频/Wan2.2 -  图生视频+文生视频 韩国美女亚洲女性模特_1952571860477259777.json, 视频生成/文生视频/wan2.1基础文生视频001_1909164954489135106.json, 视频生成/文生视频/wan2.2_t2v 文生视频_2058371729084469249.json, 视频生成/文生视频/【文生视频】Wan2.2 14B文生视频高质量加速版_1953331235240202241.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_70

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/文生视频/WAN2.1 Comfy-Org 文生视频官方原始工作流_1895182420566212609.json、视频生成/文生视频/WAN2.1文生视频_1977308765202587649.json、视频生成/文生视频/WAN2.2 人物角色模特服装百变更换衣服_1954771341195960322.json、视频生成/文生视频/Wan2.1+t2v Lora文生视频工作流_1951460131294883841.json、视频生成/文生视频/Wan2.1文生视频工作流_1934444729025327105.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `KSampler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingSD3` —— 5/9 个有
- `LoraLoader` —— 4/9 个有
- `Fast Groups Bypasser (rgthree)` —— 3/9 个有
- `LoadImage` —— 3/9 个有
- `WanImageToVideo` —— 3/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 4 - 30 | 9 | 30% |
| Prompt 约束强度(CFG) | 6 | 1 - 6 | 9 | 34% |
| 采样算法 | uni_pc | - | 9 | 56% |
| 调度器 | simple | - | 9 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| LoRA 模型强度 | 1 | 1 - 1 | 4 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 30，观测区间 4 - 30，9 个样本，取值分散，一致性仅 30%
- Prompt 约束强度(CFG) 中位数 6，观测区间 1 - 6，9 个样本，取值分散，一致性仅 34%
- 采样算法 最常用 uni_pc，9 个样本，一致性 56%
- 调度器 最常用 simple，9 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（7/9 个样本）：Steps较低可能导致细节不足
