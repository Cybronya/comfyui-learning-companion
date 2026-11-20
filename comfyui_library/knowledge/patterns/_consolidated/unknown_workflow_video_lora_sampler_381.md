---
name: unknown_workflow_video_lora_sampler_381
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.5645
common_nodes: [CLIPLoader, CLIPTextEncode, DiffusionModelLoaderKJ, GetNode, INTConstant, ImageBatchExtendWithOverlap, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, SetNode, VAEDecode, VAEEncode, VAELoader, VHS_VideoCombine, WanImageToVideoSVIPro]
problems: []
missing: []
members: [视频生成/图生视频/SVI 2.0 Pro for Wan 2.2长视频一镜到底！_2005649937650118658.json, 视频生成/图生视频/SVI 2.0 Pro 一镜到底-长视频生成_2013437129388462081.json, 视频生成/图生视频/SVI 2.0 Pro-Wan 2.2丝滑的长视频_2007322836368625665.json, 视频生成/图生视频/SVI 2.0 Pro-Wan 2.2丝滑的长视频_2008463179042529282.json, 视频生成/图生视频/SVI 2.0 Pro大模型升级啦：无限时长AI视频制作+ComfyUI工作流讲解_2006246427911000065.json, 视频生成/图生视频/Wan 2.2 SVI 2.0 PRO 长视频最新版！_2005892831866744833.json, 视频生成/图生视频/Wan2.2+SVI2_Pro+图生长视频_2005667775693684738.json, 视频生成/图生视频/很好用的无限长视频SVI 2.0 Pro-Wan 2.2_2007775909079683073.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_381

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/SVI 2.0 Pro for Wan 2.2长视频一镜到底！_2005649937650118658.json、视频生成/图生视频/SVI 2.0 Pro 一镜到底-长视频生成_2013437129388462081.json、视频生成/图生视频/SVI 2.0 Pro-Wan 2.2丝滑的长视频_2007322836368625665.json、视频生成/图生视频/SVI 2.0 Pro-Wan 2.2丝滑的长视频_2008463179042529282.json、视频生成/图生视频/SVI 2.0 Pro大模型升级啦：无限时长AI视频制作+ComfyUI工作流讲解_2006246427911000065.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：56%

## 共有节点

全部 8 个 workflow 都包含：
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
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/8 个有
- `ShowText|pysssss` —— 5/8 个有
- `easy indexAnything` —— 5/8 个有
- `easy promptLine` —— 5/8 个有
- `ImageResizeKJv2` —— 2/8 个有
- `Text` —— 2/8 个有
- `CM_IntToFloat` —— 1/8 个有
- `CR Text` —— 1/8 个有
- `JWInteger` —— 1/8 个有
- `Label (rgthree)` —— 1/8 个有
- `easy mathInt` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 8 | 88% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 8 | 100% |
| 采样算法 | 1 | 1 - 1 | 8 | 100% |
| 调度器 | euler | - | 8 | 100% |
| 重绘幅度 | simple | - | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，8 个样本，一致性 88%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，8 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，8 个样本，一致性 100%
- 重绘幅度 最常用 simple，8 个样本，一致性 100%
