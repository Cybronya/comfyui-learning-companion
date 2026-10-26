---
name: unknown_workflow_video_lora_sampler_470
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.5352
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DF_Integer, DrawViTPose, GetImageSizeAndCount, GetNode, ImageConcatMulti, ImageResizeKJv2, Int, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, OnnxDetectionModelLoader, PathchSageAttentionKJ, PoseAndFaceDetection, SetNode, SimpleMath+, StringToInt, TorchCompileModelWanVideoV2, TrimVideoLatent, UnetLoaderGGUF, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanAnimateToVideo, easy cleanGpuUsed, easy showAnything, easy sleep, wanBlockSwap]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/换装+换脸+换背景- Animate Wan2.2_1975014128706301953.json, 视频生成/图生视频/Animate Wan2.2换风格对口型_2005510283697291266.json, 视频生成/图生视频/服装展示模特走秀视频图生视频3.5_2066142073039970306.json, 视频生成/图生视频/模特服装细节展示-傲雪AIGC_1987427784719011841.json, 视频生成/图生视频/电商服装模特图生视频展示细节视频动作迁移_2065766712460533761.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_470

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（数字人/数字人/换装+换脸+换背景- Animate Wan2.2_1975014128706301953.json、视频生成/图生视频/Animate Wan2.2换风格对口型_2005510283697291266.json、视频生成/图生视频/服装展示模特走秀视频图生视频3.5_2066142073039970306.json、视频生成/图生视频/模特服装细节展示-傲雪AIGC_1987427784719011841.json、视频生成/图生视频/电商服装模特图生视频展示细节视频动作迁移_2065766712460533761.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：54%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DF_Integer`
- `DrawViTPose`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `Int`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `OnnxDetectionModelLoader`
- `PathchSageAttentionKJ`
- `PoseAndFaceDetection`
- `SetNode`
- `SimpleMath+`
- `StringToInt`
- `TorchCompileModelWanVideoV2`
- `TrimVideoLatent`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanAnimateToVideo`
- `easy cleanGpuUsed`
- `easy showAnything`
- `easy sleep`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `SaveImage` —— 1/5 个有
- `TT_img_enc` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | sa_solver | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 sa_solver，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
