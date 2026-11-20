---
name: text_to_image_video_lora_sampler_166
type: Text To Image
frequency: 4
level: weak
coverage: 0.7055
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CM_IntToFloat, Display Int (rgthree), DrawViTPose, EmptyLatentImage, GetImageRangeFromBatch, GetNode, ImageBatchMulti, ImageResizeKJv2, ImageScale, Int, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, OnnxDetectionModelLoader, PoseAndFaceDetection, PreviewImage, SetNode, SimpleMath+, TrimVideoLatent, UNETLoader, VAEDecode, VAELoader, VHS_GetImageCount, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanAnimateToVideo, easy float, easy seed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/动作迁移一致性优化版，表情调节与手部胸部抖动修复的图生视频工作流_2102907067622313985.json, 视频生成/图生视频/动作迁移一致性优化版，表情调节与手部胸部抖动修复的图生视频工作流_2104385345507909634.json, 视频生成/图生视频/自动跟随完美复制跳舞动作（懒人版）_2062939588565487618.json, 视频生成/图生视频/风格转绘 动漫转绘_2062465993141739521.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_166

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/动作迁移一致性优化版，表情调节与手部胸部抖动修复的图生视频工作流_2102907067622313985.json、视频生成/图生视频/动作迁移一致性优化版，表情调节与手部胸部抖动修复的图生视频工作流_2104385345507909634.json、视频生成/图生视频/自动跟随完美复制跳舞动作（懒人版）_2062939588565487618.json、视频生成/图生视频/风格转绘 动漫转绘_2062465993141739521.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：71%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CM_IntToFloat`
- `Display Int (rgthree)`
- `DrawViTPose`
- `EmptyLatentImage`
- `GetImageRangeFromBatch`
- `GetNode`
- `ImageBatchMulti`
- `ImageResizeKJv2`
- `ImageScale`
- `Int`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `PreviewImage`
- `SetNode`
- `SimpleMath+`
- `TrimVideoLatent`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_GetImageCount`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `WanAnimateToVideo`
- `easy float`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 2/4 个有
- `GetImageSizeAndCount` —— 2/4 个有
- `ImageConcatMulti` —— 2/4 个有
- `ImageScaleToTotalPixels` —— 2/4 个有
- `JWInteger` —— 2/4 个有
- `JjkText` —— 2/4 个有
- `LayerUtility: PurgeVRAM V2` —— 2/4 个有
- `Notif-PlaySound` —— 2/4 个有
- `RIFE VFI` —— 2/4 个有
- `SaveImage` —— 2/4 个有
- `ShellAgentPluginSaveAudios` —— 2/4 个有
- `TT_img_enc` —— 2/4 个有
- `Text Multiline` —— 2/4 个有
- `TextEncodeQwenImageEditPlus` —— 2/4 个有
- `VHS_VideoInfo` —— 2/4 个有
- `solarL_SaveImagesToZip` —— 2/4 个有
- `EmptyImage` —— 1/4 个有
- `孤海注释` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 8 | 4 | 67% |
| Prompt 约束强度(CFG) | 2.75 | 1 - 4.5 | 4 | 36% |
| 采样算法 | er_sde | - | 4 | 50% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 424 | 80 - 768 | 4 | 19% |
| 高度 | 424 | 80 - 768 | 4 | 19% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 8，4 个样本
- Prompt 约束强度(CFG) 中位数 2.75，观测区间 1 - 4.5，4 个样本，取值分散，一致性仅 36%
- 采样算法 最常用 er_sde，4 个样本，一致性 50%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 424，观测区间 80 - 768，4 个样本，取值分散，一致性仅 19%
- 高度 中位数 424，观测区间 80 - 768，4 个样本，取值分散，一致性仅 19%
- 高发问题（16/4 个样本）：Steps较低可能导致细节不足
