---
name: text_to_image_video_upscale_lora_3
type: Text To Image
frequency: 6
level: strong
coverage: 0.872167
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VOSR2ModelLoader, VOSR2Upscale, easy cleanGpuUsed, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/Vosr2视频超分2K工作流｜数字人视频画质增强处理_2097528025284964353.json, 数字人/数字人/Vosr2视频高清放大工作流｜1K-2K数字人画质超分增强_2097494230590648321.json, 数字人/数字人/视频超分Vosr2 DLSS 2K高清增强 数字人视频清晰度提升_2098660110603214849.json, 视频生成/图生视频/VOSR2+DLSS5视频超分放大处理生成工具_2102315334387724289.json, 视频生成/图生视频/VOSR2联合DLSS5视频超分放大，高清修复提升视频分辨率工作流_2105856991561338881.json, 视频生成/图生视频/minimax H3超分修复2K工作流｜Vosr2.0视频画质增强_2097786426866880514.json]
source: knowledge_consolidation
---

# text_to_image_video_upscale_lora_3

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（数字人/数字人/Vosr2视频超分2K工作流｜数字人视频画质增强处理_2097528025284964353.json、数字人/数字人/Vosr2视频高清放大工作流｜1K-2K数字人画质超分增强_2097494230590648321.json、数字人/数字人/视频超分Vosr2 DLSS 2K高清增强 数字人视频清晰度提升_2098660110603214849.json、视频生成/图生视频/VOSR2+DLSS5视频超分放大处理生成工具_2102315334387724289.json、视频生成/图生视频/VOSR2联合DLSS5视频超分放大，高清修复提升视频分辨率工作流_2105856991561338881.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VOSR2ModelLoader`
- `VOSR2Upscale`
- `easy cleanGpuUsed`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `PDIMAGE_LongerSize` —— 4/6 个有
- `RTXVideoSuperResolution` —— 4/6 个有
- `VHS_VideoInfo` —— 4/6 个有
- `孤海注释` —— 4/6 个有
- `PreviewAny` —— 3/6 个有
- `RH_DLSS5Enhance` —— 3/6 个有
- `EmptyImage` —— 2/6 个有
- `GH_AudioVideoMerger` —— 2/6 个有
- `GH_ImageVideoComparer` —— 2/6 个有
- `LayerFilter: GaussianBlur` —— 2/6 个有
- `PreviewImage` —— 2/6 个有
- `图像缩放V2_孤海` —— 2/6 个有
- `Int` —— 1/6 个有
- `easy mathInt` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
