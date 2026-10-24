---
name: unknown_workflow_video_lora_sampler_531
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.5915
common_nodes: [CLIPLoader, CLIPTextEncode, DiffusionModelLoaderKJ, GetNode, ImageBatchExtendWithOverlap, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, SetNode, VAEDecode, VAEEncode, VAELoader, VHS_VideoCombine, WanImageToVideoSVIPro]
problems: []
missing: []
members: [视频生成/图生视频/图生视频-SVI 2.0 Pro-无限长度视频生成_2005789262182313985.json, 视频生成/图生视频/图生视频超长视频分镜SVI+2.0Pro一镜到底（10分钟20秒超长分镜视频）_2005875077147226114.json, 视频生成/图生视频/很好用的无限长视频SVI 2.0 Pro-Wan 2.2_2007775909079683073.json, 视频生成/文生视频/Wan 2.2-SVI 2.0 Pro-十秒_2015412503383117826.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_531

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/图生视频-SVI 2.0 Pro-无限长度视频生成_2005789262182313985.json、视频生成/图生视频/图生视频超长视频分镜SVI+2.0Pro一镜到底（10分钟20秒超长分镜视频）_2005875077147226114.json、视频生成/图生视频/很好用的无限长视频SVI 2.0 Pro-Wan 2.2_2007775909079683073.json、视频生成/文生视频/Wan 2.2-SVI 2.0 Pro-十秒_2015412503383117826.json）

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
- `INTConstant` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `Int` —— 2/4 个有
- `ShowText|pysssss` —— 2/4 个有
- `easy indexAnything` —— 2/4 个有
- `easy promptLine` —— 2/4 个有
- `DuckHideNode` —— 1/4 个有
- `ImageBatch` —— 1/4 个有
- `PreviewAny` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `SaveImage` —— 1/4 个有
- `WanVideoImageResizeToClosest` —— 1/4 个有
- `easy promptList` —— 1/4 个有
- `ttN text` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 4 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 4 | 100% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | euler | - | 4 | 75% |
| 重绘幅度 | simple | - | 4 | 75% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，4 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，4 个样本，一致性 75%
- 重绘幅度 最常用 simple，4 个样本，一致性 75%
