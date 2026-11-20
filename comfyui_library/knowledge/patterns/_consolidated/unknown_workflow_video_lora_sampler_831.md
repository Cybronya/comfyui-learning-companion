---
name: unknown_workflow_video_lora_sampler_831
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.584
common_nodes: [CLIPLoader, CLIPTextEncode, DiffusionModelLoaderKJ, GetImageRangeFromBatch, GetNode, INTConstant, ImageBatchExtendWithOverlap, KSamplerAdvanced, LoraLoaderModelOnly, SetNode, SimpleMath+, VAEDecode, VAEEncode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanImageToVideoSVIPro]
problems: []
missing: []
members: [平台全量/视频延长smoothMixWan22+超清放大_2012798357684621314.json, 平台全量/👾怪獸SVI-Pro视频无限延长👾_2005875049108303874.json, 视频生成/图生视频/SVIpro视频延长-Aiwood_2005629100242993154.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_831

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/视频延长smoothMixWan22+超清放大_2012798357684621314.json、平台全量/👾怪獸SVI-Pro视频无限延长👾_2005875049108303874.json、视频生成/图生视频/SVIpro视频延长-Aiwood_2005629100242993154.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：58%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `DiffusionModelLoaderKJ`
- `GetImageRangeFromBatch`
- `GetNode`
- `INTConstant`
- `ImageBatchExtendWithOverlap`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `SetNode`
- `SimpleMath+`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanImageToVideoSVIPro`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 2/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `ImageResize+` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `SeedVR2LoadDiTModel` —— 1/3 个有
- `SeedVR2LoadVAEModel` —— 1/3 个有
- `SeedVR2VideoUpscaler` —— 1/3 个有
- `easy imageColorMatch` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 3 | 100% |
| Prompt 约束强度(CFG) | 14 | 14 - 14 | 3 | 100% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | euler | - | 3 | 100% |
| 重绘幅度 | simple | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 14，观测区间 14 - 14，3 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，3 个样本，一致性 100%
- 重绘幅度 最常用 simple，3 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 14，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
