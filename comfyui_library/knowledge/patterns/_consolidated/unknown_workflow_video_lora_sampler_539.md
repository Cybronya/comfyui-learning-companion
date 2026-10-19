---
name: unknown_workflow_video_lora_sampler_539
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.59
common_nodes: [CLIPLoader, CLIPTextEncode, DiffusionModelLoaderKJ, GetNode, ImageBatchExtendWithOverlap, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, SetNode, VAEDecode, VAEEncode, VAELoader, VHS_VideoCombine, WanImageToVideoSVIPro]
problems: []
missing: []
members: [视频生成/图生视频/2005789262182313985.json, 视频生成/图生视频/2005875077147226114.json, 视频生成/图生视频/2006635084027269121.json, 视频生成/文生视频/无限长度视频生成 图生视频 Wan SVI 2.0 Pro_2036250825735020545.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_539

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/2005789262182313985.json、视频生成/图生视频/2005875077147226114.json、视频生成/图生视频/2006635084027269121.json、视频生成/文生视频/无限长度视频生成 图生视频 Wan SVI 2.0 Pro_2036250825735020545.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：59%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `DiffusionModelLoaderKJ`
- `GetNode`
- `ImageBatchExtendWithOverlap`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SetNode`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideoSVIPro`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 3/4 个有
- `INTConstant` —— 2/4 个有
- `Int` —— 2/4 个有
- `WanVideoImageResizeToClosest` —— 2/4 个有
- `AddLabel` —— 1/4 个有
- `ImageResizeKJv2` —— 1/4 个有
- `JjkText` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/4 个有
- `PreviewAny` —— 1/4 个有
- `easy promptList` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 4 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 4 | 100% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | sa_solver | - | 4 | 50% |
| 重绘幅度 | beta | - | 4 | 50% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，4 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 sa_solver，4 个样本，一致性 50%
- 重绘幅度 最常用 beta，4 个样本，一致性 50%
