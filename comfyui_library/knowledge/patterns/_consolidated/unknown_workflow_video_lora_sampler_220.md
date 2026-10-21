---
name: unknown_workflow_video_lora_sampler_220
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.563333
common_nodes: [CLIPLoader, CLIPTextEncode, DiffusionModelLoaderKJ, GetNode, INTConstant, ImageBatchExtendWithOverlap, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, SetNode, VAEDecode, VAEEncode, VAELoader, VHS_VideoCombine, WanImageToVideoSVIPro]
problems: []
missing: []
members: [视频生成/图生视频/2005649937650118658.json, 视频生成/图生视频/2013437129388462081.json, 视频生成/图生视频/2007322836368625665.json, 视频生成/图生视频/2008463179042529282.json, 视频生成/图生视频/2005892831866744833.json, 视频生成/图生视频/2005667775693684738.json, 视频生成/图生视频/2007775909079683073.json, 视频生成/图生视频/2006221064216514562.json, 视频生成/图生视频/2005914209638645762.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_220

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/2005649937650118658.json、视频生成/图生视频/2013437129388462081.json、视频生成/图生视频/2007322836368625665.json、视频生成/图生视频/2008463179042529282.json、视频生成/图生视频/2005892831866744833.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：56%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `DiffusionModelLoaderKJ`
- `GetNode`
- `INTConstant`
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
- `LayerUtility: ImageScaleByAspectRatio V2` —— 8/9 个有
- `ShowText|pysssss` —— 5/9 个有
- `easy indexAnything` —— 5/9 个有
- `easy promptLine` —— 5/9 个有
- `ImageResizeKJv2` —— 3/9 个有
- `JWInteger` —— 3/9 个有
- `CR Prompt Text` —— 2/9 个有
- `Text` —— 2/9 个有
- `CM_IntToFloat` —— 1/9 个有
- `CR Text` —— 1/9 个有
- `easy mathInt` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 9 | 89% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 9 | 100% |
| 采样算法 | 1 | 1 - 1 | 9 | 100% |
| 调度器 | euler | - | 9 | 100% |
| 重绘幅度 | simple | - | 9 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，9 个样本，一致性 89%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，9 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，9 个样本，一致性 100%
- 重绘幅度 最常用 simple，9 个样本，一致性 100%
