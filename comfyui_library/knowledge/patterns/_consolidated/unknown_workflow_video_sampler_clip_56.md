---
name: unknown_workflow_video_sampler_clip_56
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.5588
common_nodes: [CLIPLoader, CLIPTextEncode, GetNode, INTConstant, ImageBatchExtendWithOverlap, KSamplerAdvanced, SetNode, VAEDecode, VAEEncode, VAELoader, VHS_VideoCombine, WanImageToVideoSVIPro]
problems: []
missing: []
members: [图片生成/图生图/SVI 2.0长视频制作，1分钟以上视频制作_2005595717286723586.json, 平台全量/SmoothMixWan2.2+SVI无限长视频_2005987580808216578.json, 平台全量/SmoothMixWan2.2+SVI无限长视频_2005992601192972290.json, 视频生成/图生视频/(Kj强化版)SVI 2.0 Pro Wan2.2 图生长视频V1_2005539201510764545.json, 视频生成/图生视频/74a.tonnie-SVI-2 Pro长视频_2011050860368891906.json, 视频生成/图生视频/74b.tonnie-SVI-2 Pro长视频（图生视频）_2011657504274522114.json, 视频生成/图生视频/RemixV3+SVI2_Pro+图生长视频_2006035498795540482.json, 视频生成/图生视频/SVI 2 Pro 自动提示词-图像生成长视频_2006716994556530690.json, 视频生成/图生视频/SVI 2.0 Pro Wan2.2 图生长视频标准版V1_2005359975482490882.json, 视频生成/文生视频/SVI 2 Pro 自动提示词-视频延长_2007103219394158593.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_56

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/SVI 2.0长视频制作，1分钟以上视频制作_2005595717286723586.json、平台全量/SmoothMixWan2.2+SVI无限长视频_2005987580808216578.json、平台全量/SmoothMixWan2.2+SVI无限长视频_2005992601192972290.json、视频生成/图生视频/(Kj强化版)SVI 2.0 Pro Wan2.2 图生长视频V1_2005539201510764545.json、视频生成/图生视频/74a.tonnie-SVI-2 Pro长视频_2011050860368891906.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：56%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `GetNode`
- `INTConstant`
- `ImageBatchExtendWithOverlap`
- `KSamplerAdvanced`
- `SetNode`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideoSVIPro`

**可变部分**（部分 workflow 才有）：
- `DiffusionModelLoaderKJ` —— 9/10 个有
- `ImageResizeKJv2` —— 9/10 个有
- `LoadImage` —— 9/10 个有
- `LoraLoaderModelOnly` —— 9/10 个有
- `CR Prompt Text` —— 6/10 个有
- `PreviewImage` —— 4/10 个有
- `JWInteger` —— 3/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/10 个有
- `AILab_QwenVL` —— 2/10 个有
- `CR Text Replace` —— 2/10 个有
- `JWStringGetLine` —— 2/10 个有
- `LayerUtility: PurgeVRAM V2` —— 2/10 个有
- `PreviewAny` —— 2/10 个有
- `Text` —— 2/10 个有
- `Float` —— 1/10 个有
- `GetImageRangeFromBatch` —— 1/10 个有
- `Int` —— 1/10 个有
- `RHHiddenNodes` —— 1/10 个有
- `SimpleMath+` —— 1/10 个有
- `VHS_LoadVideo` —— 1/10 个有
- `VHS_VideoInfo` —— 1/10 个有
- `easy showAnything` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 10 | 80% |
| Prompt 约束强度(CFG) | 8 | 1 - 20 | 10 | 50% |
| 采样算法 | 1 | 1 - 1 | 10 | 100% |
| 调度器 | euler | - | 10 | 100% |
| 重绘幅度 | simple | - | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，10 个样本，一致性 80%
- Prompt 约束强度(CFG) 中位数 8，观测区间 1 - 20，10 个样本，取值分散，一致性仅 50%
- 采样算法 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，10 个样本，一致性 100%
- 重绘幅度 最常用 simple，10 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
