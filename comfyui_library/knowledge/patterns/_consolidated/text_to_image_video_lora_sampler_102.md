---
name: text_to_image_video_lora_sampler_102
type: Text To Image
frequency: 7
level: strong
coverage: 0.905429
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionLoader, CreateVideo, EmptyLatentImage, ImageResizeKJv2, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveVideo, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageResizeToClosest, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/SCAIL2动作迁移免骨架工作流｜图生图动作迁移｜无需绑骨直出_2101902362611896321.json, 视频生成/图生视频/Animate动作迁移自动尺寸工作流，姿态表情双驱动图生视频工具_2106442849813356545.json, 视频生成/图生视频/Animate动作迁移自动尺寸工作流｜图生视频自适应比例免裁剪_2106214971834200065.json, 视频生成/图生视频/Animate动作迁移自动尺寸｜图生视频姿态跟拍_2097227077287235585.json, 视频生成/图生视频/SCAIL2动作迁移免骨架工作流，免骨架提取动作同步更快更稳图生视频_2106444301172568065.json, 视频生成/图生视频/SCAIL2动作迁移免骨架工作流｜图生视频无需绑骨一键迁移动作_2106216466176626690.json, 视频生成/图生视频/SCAIL2动作迁移免骨架版 视频帧直接驱动人物动画_2098119288283553794.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_102

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/SCAIL2动作迁移免骨架工作流｜图生图动作迁移｜无需绑骨直出_2101902362611896321.json、视频生成/图生视频/Animate动作迁移自动尺寸工作流，姿态表情双驱动图生视频工具_2106442849813356545.json、视频生成/图生视频/Animate动作迁移自动尺寸工作流｜图生视频自适应比例免裁剪_2106214971834200065.json、视频生成/图生视频/Animate动作迁移自动尺寸｜图生视频姿态跟拍_2097227077287235585.json、视频生成/图生视频/SCAIL2动作迁移免骨架工作流，免骨架提取动作同步更快更稳图生视频_2106444301172568065.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CreateVideo`
- `EmptyLatentImage`
- `ImageResizeKJv2`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageResizeToClosest`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `GetVideoComponents` —— 4/7 个有
- `PrimitiveFloat` —— 4/7 个有
- `VHS_GetImageCount` —— 4/7 个有
- `Video Slice` —— 4/7 个有
- `WanVideoAddSCAILPoseEmbeds` —— 4/7 个有
- `WanVideoAddSCAILReferenceEmbeds` —— 4/7 个有
- `WanVideoEmptyEmbeds` —— 4/7 个有
- `DrawViTPose` —— 3/7 个有
- `OnnxDetectionModelLoader` —— 3/7 个有
- `PoseAndFaceDetection` —— 3/7 个有
- `SaveImage` —— 3/7 个有
- `WanVideoAnimateEmbeds` —— 3/7 个有
- `EmptyImage` —— 1/7 个有
- `PreviewImage` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
