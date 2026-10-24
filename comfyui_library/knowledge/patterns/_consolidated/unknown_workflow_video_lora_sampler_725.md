---
name: unknown_workflow_video_lora_sampler_725
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, TrimVideoLatent, UNETLoader, VAEDecodeTiled, VAELoader, VHS_VideoCombine, WanVaceToVideo]
problems: [发现KSampler但没有VAEDecode, Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/6G显存也可用的图片转视频流程_1936195885694898177.json, 视频生成/图生视频/Self-Forcing极速1280高清质量图生视频_1933136630100176897.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_725

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/6G显存也可用的图片转视频流程_1936195885694898177.json、视频生成/图生视频/Self-Forcing极速1280高清质量图生视频_1933136630100176897.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `TrimVideoLatent`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`
- `VHS_VideoCombine`
- `WanVaceToVideo`

**可变部分**（部分 workflow 才有）：
- `Primitive integer [Crystools]` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 7.5 | - | 2 | 67% |
| Prompt 约束强度(CFG) | 0.85 | - | 2 | 82% |
| 采样算法 | lcm | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 2/2 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 7.5，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 0.85，样本不足，未给区间，2 个样本，取值集中（一致性 82%）
- 采样算法 最常用 lcm，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 0.7，低于常用下限 1（CFG 过低可能导致 Prompt 约束不足、结果偏离描述）
- 高发问题（2/2 个样本）：发现KSampler但没有VAEDecode
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
