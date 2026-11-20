---
name: unknown_workflow_video_sampler_clip_191
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.977667
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, ModelSamplingSD3, TrimVideoLatent, UnetLoaderGGUF, VAEDecode, VAELoader, VHS_VideoCombine, WanVaceToVideo]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/骨骼图驱动动画-轻量基础版_1945013921344573441.json, 视频生成/图生视频/ai有娃了-Wan2.1原始节点（非KJ节点）-FusionX加速_1937704868792418306.json, 视频生成/图生视频/猫厨师做饭-Wan2.1原始节点（非KJ节点）-lightX2V加速_1937081059626618882.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_191

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/骨骼图驱动动画-轻量基础版_1945013921344573441.json、视频生成/图生视频/ai有娃了-Wan2.1原始节点（非KJ节点）-FusionX加速_1937704868792418306.json、视频生成/图生视频/猫厨师做饭-Wan2.1原始节点（非KJ节点）-lightX2V加速_1937081059626618882.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `ModelSamplingSD3`
- `TrimVideoLatent`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanVaceToVideo`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 2/3 个有
- `easy cleanGpuUsed` —— 2/3 个有
- `AV_LoraLoader` —— 1/3 个有
- `LoraLoader` —— 1/3 个有
- `StringFunction|pysssss` —— 1/3 个有
- `Text Multiline` —— 1/3 个有
- `VHS_LoadVideo` —— 1/3 个有
- `VHS_VideoInfo` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 5 - 8 | 3 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | ddim | - | 3 | 33% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 5 - 8，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 ddim，3 个样本，一致性 33%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
