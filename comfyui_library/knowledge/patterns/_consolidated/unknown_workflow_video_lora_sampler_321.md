---
name: unknown_workflow_video_lora_sampler_321
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.965
common_nodes: [CLIPLoader, CLIPTextEncode, DF_Integer, LoadImage, LoraLoaderModelOnly, ModelPatchTorchSettings, PathchSageAttentionKJ, SimpleMath+, UnetLoaderGGUF, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo, WanMoeKSampler, wanBlockSwap]
problems: []
missing: []
members: [视频生成/图生视频/1967569328524664834.json, 视频生成/图生视频/2017158132522295297.json, 视频生成/图生视频/2047219095740878849.json, 视频生成/图生视频/2021611971048640514.json, 视频生成/图生视频/2046770688064753666.json, 视频生成/图生视频/2052569740140392450.json, 视频生成/文生视频/WAN2.2GGUF终极加速_1982992575873331201.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_321

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/1967569328524664834.json、视频生成/图生视频/2017158132522295297.json、视频生成/图生视频/2047219095740878849.json、视频生成/图生视频/2021611971048640514.json、视频生成/图生视频/2046770688064753666.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `DF_Integer`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `SimpleMath+`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`
- `WanMoeKSampler`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `FILM VFI` —— 1/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有
- `Float` —— 1/7 个有
- `GetImageRangeFromBatch` —— 1/7 个有
- `PreviewImage` —— 1/7 个有
- `Primitive integer [Crystools]` —— 1/7 个有
- `WanFirstLastFrameToVideo` —— 1/7 个有
- `easy cleanGpuUsed` —— 1/7 个有
- `easy clearCacheAll` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 7 | 71% |
| Prompt 约束强度(CFG) | 4 | 4 - 5 | 7 | 92% |
| 采样算法 | 1 | 1 - 1.5 | 7 | 84% |
| 调度器 | 1 | 1 - 1 | 7 | 100% |
| 重绘幅度 | euler | - | 7 | 86% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，7 个样本，一致性 71%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 5，7 个样本，取值集中（一致性 92%）
- 采样算法 中位数 1，观测区间 1 - 1.5，7 个样本，取值集中（一致性 84%）
- 调度器 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 重绘幅度 最常用 euler，7 个样本，一致性 86%
