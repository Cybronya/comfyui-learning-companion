---
name: unknown_workflow_video_sampler_clip_122
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9558
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, UNETLoader, VAELoader, VHS_VideoCombine]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [视频生成/图生视频/Wan2.1-ComfyUI-Wan2.1(阿里万相)-最强开源文生视频_1894981008754343938.json, 视频生成/图生视频/Wan2.1-ComfyUI-阿里万相-最强开源图生视频_1894918771771572226.json, 视频生成/图生视频/通义万相-图生视频-快速工作流_1896444966992478209.json, 视频生成/文生视频/Wan2.1-ComfyUI-Wan2.1(阿里万相)-最强开源文生视频_2053727976885366786.json, 视频生成/文生视频/满血MoviiGen+LLM_仅需主题词一键生成电影级视频镜头_1923170079112876033.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_122

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/Wan2.1-ComfyUI-Wan2.1(阿里万相)-最强开源文生视频_1894981008754343938.json、视频生成/图生视频/Wan2.1-ComfyUI-阿里万相-最强开源图生视频_1894918771771572226.json、视频生成/图生视频/通义万相-图生视频-快速工作流_1896444966992478209.json、视频生成/文生视频/Wan2.1-ComfyUI-Wan2.1(阿里万相)-最强开源文生视频_2053727976885366786.json、视频生成/文生视频/满血MoviiGen+LLM_仅需主题词一键生成电影级视频镜头_1923170079112876033.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CM_IntToFloat` —— 4/5 个有
- `EmptyHunyuanLatentVideo` —— 4/5 个有
- `Fast Groups Bypasser (rgthree)` —— 4/5 个有
- `Primitive integer [Crystools]` —— 4/5 个有
- `VAEDecodeTiled` —— 4/5 个有
- `CLIPVisionEncode` —— 2/5 个有
- `CLIPVisionLoader` —— 2/5 个有
- `LoadImage` —— 2/5 个有
- `Text Multiline` —— 2/5 个有
- `VAEDecode` —— 2/5 个有
- `WanImageToVideo` —— 2/5 个有
- `RHHiddenNodes` —— 1/5 个有
- `ShowText` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 10 - 30 | 5 | 67% |
| Prompt 约束强度(CFG) | 6 | 6 - 8 | 5 | 88% |
| 采样算法 | uni_pc | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 3/5 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 30，观测区间 10 - 30，5 个样本
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 8，5 个样本，取值集中（一致性 88%）
- 采样算法 最常用 uni_pc，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（3/5 个样本）：发现KSampler但没有VAEDecode
