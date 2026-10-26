---
name: unknown_workflow_video_lora_sampler_360
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.563286
common_nodes: [CLIPLoader, CLIPTextEncode, DiffusionModelLoaderKJ, GetNode, INTConstant, ImageBatchExtendWithOverlap, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, SetNode, VAEDecode, VAEEncode, VAELoader, VHS_VideoCombine, WanImageToVideoSVIPro]
problems: []
missing: []
members: [视频生成/图生视频/SVI 2.0 Pro for Wan 2.2长视频一镜到底！_2005649937650118658.json, 视频生成/图生视频/SVI 2.0 Pro 一镜到底-长视频生成_2013437129388462081.json, 视频生成/图生视频/SVI 2.0 Pro-Wan 2.2丝滑的长视频_2007322836368625665.json, 视频生成/图生视频/SVI 2.0 Pro-Wan 2.2丝滑的长视频_2008463179042529282.json, 视频生成/图生视频/SVI 2.0 Pro大模型升级啦：无限时长AI视频制作+ComfyUI工作流讲解_2006246427911000065.json, 视频生成/图生视频/SVI全自动长视频生成工作流_2005886076633968641.json, 视频生成/图生视频/Wan 2.2 SVI 2.0 PRO 长视频最新版！_2005892831866744833.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_360

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/SVI 2.0 Pro for Wan 2.2长视频一镜到底！_2005649937650118658.json、视频生成/图生视频/SVI 2.0 Pro 一镜到底-长视频生成_2013437129388462081.json、视频生成/图生视频/SVI 2.0 Pro-Wan 2.2丝滑的长视频_2007322836368625665.json、视频生成/图生视频/SVI 2.0 Pro-Wan 2.2丝滑的长视频_2008463179042529282.json、视频生成/图生视频/SVI 2.0 Pro大模型升级啦：无限时长AI视频制作+ComfyUI工作流讲解_2006246427911000065.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：56%

## 共有节点

全部 7 个 workflow 都包含：
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
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/7 个有
- `ShowText|pysssss` —— 4/7 个有
- `easy indexAnything` —— 4/7 个有
- `easy promptLine` —— 4/7 个有
- `ImageResizeKJv2` —— 3/7 个有
- `Label (rgthree)` —— 2/7 个有
- `Text` —— 2/7 个有
- `Anything Everywhere` —— 1/7 个有
- `CM_IntToFloat` —— 1/7 个有
- `CRT_StringSplitter` —— 1/7 个有
- `PreviewAny` —— 1/7 个有
- `RH_LLMAPI_Pro_Node` —— 1/7 个有
- `easy mathInt` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 7 | 86% |
| Prompt 约束强度(CFG) | 8 | 8 - 14 | 7 | 76% |
| 采样算法 | 1 | 1 - 1 | 7 | 100% |
| 调度器 | euler | - | 7 | 100% |
| 重绘幅度 | simple | - | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，7 个样本，一致性 86%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 14，7 个样本
- 采样算法 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，7 个样本，一致性 100%
- 重绘幅度 最常用 simple，7 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 14，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
