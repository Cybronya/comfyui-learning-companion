---
name: text_to_image_video_lora_sampler_151
type: Text To Image
frequency: 4
level: strong
coverage: 0.85175
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Prompt Text, EmptyLatentImage, Fast Groups Bypasser (rgthree), Int, JWStringConcat, JjkText, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, ModelPatchTorchSettings, PathchSageAttentionKJ, Qwen3_VQA, RIFE VFI, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo, WanMoeKSampler, easy cleanGpuUsed, easy showAnything, solarL_SaveImagesToZip, wanBlockSwap]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/Qwen3-vl图片反推提示词，图生视频灵感提取利器_2111872864210214914.json, 图片生成/反推提示词/Qwen3-vl图片反推提示词｜反推完直接图生视频出片_2111782266522398721.json, 视频生成/图生视频/图生图自动分镜电影级视频生成 多场景创作工具_2099937489904553985.json, 视频生成/图生视频/图生图自动分镜电影级视频生成_多场景创作工具_2100566335037198337.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_151

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/反推提示词/Qwen3-vl图片反推提示词，图生视频灵感提取利器_2111872864210214914.json、图片生成/反推提示词/Qwen3-vl图片反推提示词｜反推完直接图生视频出片_2111782266522398721.json、视频生成/图生视频/图生图自动分镜电影级视频生成 多场景创作工具_2099937489904553985.json、视频生成/图生视频/图生图自动分镜电影级视频生成_多场景创作工具_2100566335037198337.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Prompt Text`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Int`
- `JWStringConcat`
- `JjkText`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderModelOnly`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `Qwen3_VQA`
- `RIFE VFI`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`
- `WanMoeKSampler`
- `easy cleanGpuUsed`
- `easy showAnything`
- `solarL_SaveImagesToZip`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 3/4 个有
- `SaveImage` —— 3/4 个有
- `孤海注释` —— 3/4 个有
- `CheckpointLoaderSimple` —— 2/4 个有
- `ConditioningZeroOut` —— 2/4 个有
- `DF_Integer` —— 2/4 个有
- `DifferentialDiffusion` —— 2/4 个有
- `INTConstant` —— 2/4 个有
- `ImageLoader` —— 2/4 个有
- `ImageResizeKJv2` —— 2/4 个有
- `LoadImage` —— 2/4 个有
- `ProcessString` —— 2/4 个有
- `SimpleMath+` —— 2/4 个有
- `Text Multiline` —— 2/4 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 2/4 个有
- `WanFirstLastFrameToVideo` —— 2/4 个有
- `easy clearCacheAll` —— 2/4 个有
- `easy promptLine` —— 2/4 个有
- `EmptyImage` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高发问题（6/4 个样本）：Steps较低可能导致细节不足
