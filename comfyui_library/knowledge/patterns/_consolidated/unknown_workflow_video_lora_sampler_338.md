---
name: unknown_workflow_video_lora_sampler_338
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.877833
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/4步首尾帧+自动提示词（短剧专用）_2000837178416656386.json, 视频生成/图生视频/8步首帧+自动提示词（短剧专用）_2000842508747800577.json, 视频生成/图生视频/Smooth Mix i2V v2.0首尾帧生视频8步加速版_2026846377501790209.json, 视频生成/图生视频/Smooth Mix i2V v2.0首尾帧生视频8步加速版_2038172701340213249.json, 视频生成/图生视频/WAN2.2首尾帧_2021954787742326786.json, 视频生成/图生视频/Wan2.2 14B 首尾帧_1989350434903085058.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_338

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/4步首尾帧+自动提示词（短剧专用）_2000837178416656386.json、视频生成/图生视频/8步首帧+自动提示词（短剧专用）_2000842508747800577.json、视频生成/图生视频/Smooth Mix i2V v2.0首尾帧生视频8步加速版_2026846377501790209.json、视频生成/图生视频/Smooth Mix i2V v2.0首尾帧生视频8步加速版_2038172701340213249.json、视频生成/图生视频/WAN2.2首尾帧_2021954787742326786.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `WanFirstLastFrameToVideo` —— 5/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/6 个有
- `LayerUtility: PurgeVRAM V2` —— 4/6 个有
- `ImageResize+` —— 3/6 个有
- `RH_LLMAPI_NODE` —— 3/6 个有
- `ShowText|pysssss` —— 3/6 个有
- `easy imageConcat` —— 2/6 个有
- `ImpactInt` —— 1/6 个有
- `PathchSageAttentionKJ` —— 1/6 个有
- `SimpleMath+` —— 1/6 个有
- `WanImageToVideo` —— 1/6 个有
- `WanVideoNAG` —— 1/6 个有
- `easy convertAnything` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 6 | 83% |
| Prompt 约束强度(CFG) | 6 | 4 - 10 | 6 | 59% |
| 采样算法 | 1 | 1 - 1 | 6 | 100% |
| 调度器 | euler | - | 6 | 100% |
| 重绘幅度 | simple | - | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，6 个样本，一致性 83%
- Prompt 约束强度(CFG) 中位数 6，观测区间 4 - 10，6 个样本
- 采样算法 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，6 个样本，一致性 100%
- 重绘幅度 最常用 simple，6 个样本，一致性 100%
