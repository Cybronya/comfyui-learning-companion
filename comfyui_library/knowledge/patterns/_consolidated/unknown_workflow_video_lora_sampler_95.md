---
name: unknown_workflow_video_lora_sampler_95
type: Unknown Workflow
frequency: 15
level: weak
coverage: 0.511733
common_nodes: [CLIPLoader, CLIPTextEncode, GetNode, INTConstant, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, SetNode, VAEDecode, VAEEncode, VAELoader, VHS_VideoCombine, WanImageToVideoSVIPro]
problems: []
missing: []
members: [视频生成/图生视频/2005539201510764545.json, 视频生成/图生视频/2030666773145587713.json, 视频生成/图生视频/2011050860368891906.json, 视频生成/图生视频/2011657504274522114.json, 视频生成/图生视频/2006035498795540482.json, 视频生成/图生视频/2005359975482490882.json, 视频生成/图生视频/2006030934327431170.json, 视频生成/图生视频/2008158274641731586.json, 视频生成/图生视频/2005641613118504962.json, 视频生成/图生视频/2005640178825920513.json, 视频生成/图生视频/2006214807296413698.json, 视频生成/图生视频/2017042085358080002.json, 视频生成/图生视频/2042238422814822401.json, 视频生成/图生视频/2018178886772727809.json, 视频生成/文生视频/SVI-pro2.0动画多分镜长视频_2008147706383966209.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_95

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/图生视频/2005539201510764545.json、视频生成/图生视频/2030666773145587713.json、视频生成/图生视频/2011050860368891906.json、视频生成/图生视频/2011657504274522114.json、视频生成/图生视频/2006035498795540482.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：51%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `GetNode`
- `INTConstant`
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
- `ImageBatchExtendWithOverlap` —— 14/15 个有
- `ImageResizeKJv2` —— 14/15 个有
- `CR Prompt Text` —— 11/15 个有
- `ModelPatchTorchSettings` —— 10/15 个有
- `PathchSageAttentionKJ` —— 10/15 个有
- `UNETLoader` —— 10/15 个有
- `Fast Groups Bypasser (rgthree)` —— 8/15 个有
- `PlaySound|pysssss` —— 8/15 个有
- `DiffusionModelLoaderKJ` —— 5/15 个有
- `JWInteger` —— 3/15 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/15 个有
- `LoadAudio` —— 2/15 个有
- `PreviewImage` —— 2/15 个有
- `PainterI2V` —— 1/15 个有
- `TTResolutionSelector` —— 1/15 个有
- `Text` —— 1/15 个有
- `easy float` —— 1/15 个有
- `easy indexAnything` —— 1/15 个有
- `easy promptList` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 15 | 80% |
| Prompt 约束强度(CFG) | 8 | 1 - 20 | 15 | 57% |
| 采样算法 | 1 | 1 - 2.5 | 15 | 53% |
| 调度器 | euler | - | 15 | 100% |
| 重绘幅度 | simple | - | 15 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，15 个样本，一致性 80%
- Prompt 约束强度(CFG) 中位数 8，观测区间 1 - 20，15 个样本
- 采样算法 中位数 1，观测区间 1 - 2.5，15 个样本
- 调度器 最常用 euler，15 个样本，一致性 100%
- 重绘幅度 最常用 simple，15 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
