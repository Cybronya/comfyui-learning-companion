---
name: unknown_workflow_video_sampler_clip_194
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.971
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, UNETLoader, VAELoader, VHS_VideoCombine]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [视频生成/图生视频/Wan2.1-ComfyUI-阿里万相-最强开源图生视频_1894918771771572226.json, 视频生成/图生视频/通义万相-图生视频-快速工作流_1896444966992478209.json, 视频生成/文生视频/满血MoviiGen+LLM_仅需主题词一键生成电影级视频镜头_1923170079112876033.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_194

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/Wan2.1-ComfyUI-阿里万相-最强开源图生视频_1894918771771572226.json、视频生成/图生视频/通义万相-图生视频-快速工作流_1896444966992478209.json、视频生成/文生视频/满血MoviiGen+LLM_仅需主题词一键生成电影级视频镜头_1923170079112876033.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionEncode` —— 2/3 个有
- `CLIPVisionLoader` —— 2/3 个有
- `CM_IntToFloat` —— 2/3 个有
- `EmptyHunyuanLatentVideo` —— 2/3 个有
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `Primitive integer [Crystools]` —— 2/3 个有
- `Text Multiline` —— 2/3 个有
- `VAEDecode` —— 2/3 个有
- `VAEDecodeTiled` —— 2/3 个有
- `WanImageToVideo` —— 2/3 个有
- `RHHiddenNodes` —— 1/3 个有
- `ShowText` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 10 - 30 | 3 | 59% |
| Prompt 约束强度(CFG) | 6 | 6 - 8 | 3 | 86% |
| 采样算法 | uni_pc | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 1/3 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 20，观测区间 10 - 30，3 个样本
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 8，3 个样本，取值集中（一致性 86%）
- 采样算法 最常用 uni_pc，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
