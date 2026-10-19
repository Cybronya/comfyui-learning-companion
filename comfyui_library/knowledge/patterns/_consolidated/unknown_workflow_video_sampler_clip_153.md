---
name: unknown_workflow_video_sampler_clip_153
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.93125
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LoadImage, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/1963965754733416450.json, 视频生成/图生视频/1956634658516471809.json, 视频生成/图生视频/2066459393683705858.json, 视频生成/图生视频/2055627357901336578.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_153

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/1963965754733416450.json、视频生成/图生视频/1956634658516471809.json、视频生成/图生视频/2066459393683705858.json、视频生成/图生视频/2055627357901336578.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `LoadImage`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `WanImageToVideo` —— 3/4 个有
- `CreateVideo` —— 2/4 个有
- `RIFE VFI` —— 2/4 个有
- `FlashVSRNode` —— 1/4 个有
- `MemoryCleaner` —— 1/4 个有
- `PathchSageAttentionKJ` —— 1/4 个有
- `Power Lora Loader (rgthree)` —— 1/4 个有
- `SaveVideo` —— 1/4 个有
- `WanFunInpaintToVideo` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 4 | 75% |
| Prompt 约束强度(CFG) | 5 | 4 - 8 | 4 | 70% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | euler | - | 4 | 100% |
| 重绘幅度 | simple | - | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，4 个样本，一致性 75%
- Prompt 约束强度(CFG) 中位数 5，观测区间 4 - 8，4 个样本
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，4 个样本，一致性 100%
- 重绘幅度 最常用 simple，4 个样本，一致性 100%
