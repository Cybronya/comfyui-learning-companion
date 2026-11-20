---
name: unknown_workflow_video_lora_sampler_67
type: Unknown Workflow
frequency: 20
level: moderate
coverage: 0.5916
common_nodes: [CLIPLoader, CLIPTextEncode, DiffusionModelLoaderKJ, ImageBatchExtendWithOverlap, ImageResizeKJv2, KSamplerAdvanced, LoraLoaderModelOnly, VAEDecode, VAEEncode, VAELoader, VHS_VideoCombine, WanImageToVideoSVIPro]
problems: []
missing: []
members: [视频生成/图生视频/SVI 2.0 pro长视频分镜一致性_2007698027737255937.json, 视频生成/图生视频/SVI 2.0Pro 分段长视频_2005535565334413313.json, 视频生成/图生视频/SVI 2.0Pro 视频延长  一镜到底  效果炸裂_2007439423029383169.json, 视频生成/图生视频/SVI 2.0Pro一镜到底！_2005336541939597313.json, 视频生成/图生视频/SVI 2.0Pro一镜到底！_2032840589099671553.json, 视频生成/图生视频/SVI 2.0Pro一镜到底！_2053665458540294145.json, 视频生成/图生视频/SVI 2.0Pro一镜到底！_2068949443151491073.json, 视频生成/图生视频/SVI 2.0Pro长视频生成_2005593934388752385.json, 视频生成/图生视频/SVI+2.0Pro 一张图片一镜到底！_2066377373628592129.json, 视频生成/图生视频/SVI+2.0Pro一镜到底_2067252352830230529.json, 视频生成/图生视频/SVI+2.0Pro电影级分镜生成长视频_2005998121425522690.json, 视频生成/图生视频/SVI+2.0Pro电影级分镜生成长视频（升级版）_2006033971657842690.json, 视频生成/图生视频/SVI+2.0Pro长视频生成_2005982973738565633.json, 视频生成/图生视频/SVI+2.0Pro高质量动图_2009965288044896257.json, 视频生成/图生视频/SVI2.0Pro超长一镜到底！16S_2011274354910306306.json, 视频生成/图生视频/SVIpro视频延长-Aiwood_2005629100242993154.json, 视频生成/图生视频/顶峰--SVI+2.0Pro一镜到底！_2065196684543619074.json, 视频生成/图生视频/🐳SVI2.0PRO长视频生成 图生视频 KJ优化无限对接版 25-12-29🦋_2005505528635817986.json, 视频生成/图生视频/👾怪獸-SVI-Pro一镜到底👾_2005898003632320514.json, 视频生成/文生视频/一张图加一句话生成视频，图片文字生成视频_2066577714387177474.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_67

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（视频生成/图生视频/SVI 2.0 pro长视频分镜一致性_2007698027737255937.json、视频生成/图生视频/SVI 2.0Pro 分段长视频_2005535565334413313.json、视频生成/图生视频/SVI 2.0Pro 视频延长  一镜到底  效果炸裂_2007439423029383169.json、视频生成/图生视频/SVI 2.0Pro一镜到底！_2005336541939597313.json、视频生成/图生视频/SVI 2.0Pro一镜到底！_2032840589099671553.json…）

- **类型**：Unknown Workflow
- **样本数**：20
- **可信度**：中等可信
- **平均知识覆盖**：59%

## 共有节点

全部 20 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `DiffusionModelLoaderKJ`
- `ImageBatchExtendWithOverlap`
- `ImageResizeKJv2`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideoSVIPro`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 19/20 个有
- `INTConstant` —— 19/20 个有
- `LoadImage` —— 19/20 个有
- `SetNode` —— 19/20 个有
- `GetImageRangeFromBatch` —— 2/20 个有
- `Primitive integer [Crystools]` —— 2/20 个有
- `SimpleMath+` —— 2/20 个有
- `ConditioningZeroOut` —— 1/20 个有
- `ImpactInt` —— 1/20 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/20 个有
- `Note Plus (mtb)` —— 1/20 个有
- `VHS_LoadVideo` —— 1/20 个有
- `VHS_VideoInfo` —— 1/20 个有
- `easy imageColorMatch` —— 1/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 20 | 80% |
| Prompt 约束强度(CFG) | 8 | 1 - 20 | 20 | 53% |
| 采样算法 | 1 | 1 - 1 | 20 | 100% |
| 调度器 | euler | - | 20 | 100% |
| 重绘幅度 | simple | - | 20 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，20 个样本，一致性 80%
- Prompt 约束强度(CFG) 中位数 8，观测区间 1 - 20，20 个样本
- 采样算法 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，20 个样本，一致性 100%
- 重绘幅度 最常用 simple，20 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
