---
name: unknown_workflow_video_lora_sampler_632
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.5882
common_nodes: [CLIPLoader, CLIPTextEncode, DiffusionModelLoaderKJ, GetNode, ImageBatchExtendWithOverlap, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, SetNode, VAEDecode, VAEEncode, VAELoader, VHS_VideoCombine, WanImageToVideoSVIPro]
problems: []
missing: []
members: [视频生成/图生视频/图生视频-SVI 2.0 Pro-无限长度视频生成_2005789262182313985.json, 视频生成/图生视频/图生视频超长视频分镜SVI+2.0Pro一镜到底（10分钟20秒超长分镜视频）_2005875077147226114.json, 视频生成/图生视频/无限时长-svi 2 pro 长视频生成-图生视频_2006635084027269121.json, 视频生成/图生视频/👾怪獸-SVI-Pro一镜到底👾_2005898003632320514.json, 视频生成/文生视频/无限长度视频生成 图生视频 Wan SVI 2.0 Pro_2036250825735020545.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_632

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/图生视频-SVI 2.0 Pro-无限长度视频生成_2005789262182313985.json、视频生成/图生视频/图生视频超长视频分镜SVI+2.0Pro一镜到底（10分钟20秒超长分镜视频）_2005875077147226114.json、视频生成/图生视频/无限时长-svi 2 pro 长视频生成-图生视频_2006635084027269121.json、视频生成/图生视频/👾怪獸-SVI-Pro一镜到底👾_2005898003632320514.json、视频生成/文生视频/无限长度视频生成 图生视频 Wan SVI 2.0 Pro_2036250825735020545.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：59%

## 共有节点

全部 5 个 workflow 都包含：
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
- `CR Text` —— 3/5 个有
- `INTConstant` —— 3/5 个有
- `ImageResizeKJv2` —— 2/5 个有
- `Int` —— 2/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/5 个有
- `WanVideoImageResizeToClosest` —— 2/5 个有
- `AddLabel` —— 1/5 个有
- `GetImageRangeFromBatch` —— 1/5 个有
- `JjkText` —— 1/5 个有
- `PreviewAny` —— 1/5 个有
- `SimpleMath+` —— 1/5 个有
- `easy promptList` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 5 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 14 | 5 | 74% |
| 采样算法 | 1 | 1 - 1 | 5 | 100% |
| 调度器 | euler | - | 5 | 60% |
| 重绘幅度 | simple | - | 5 | 60% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，5 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 14，5 个样本
- 采样算法 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，5 个样本，一致性 60%
- 重绘幅度 最常用 simple，5 个样本，一致性 60%
- 风险：Prompt 约束强度(CFG) 观测到 14，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
