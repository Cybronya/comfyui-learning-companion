---
name: unknown_workflow_video_upscale_sampler_11
type: Unknown Workflow
frequency: 3
level: strong
coverage: 1
common_nodes: [CLIPLoader, CLIPTextEncode, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, ImageScaleBy, ImageUpscaleWithModel, KSampler, UpscaleModelLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.1-图生视频+放大补帧_1908814270581059585.json, 视频生成/图生视频/原生-Wan2.1-GGUF-图生视频+放大补帧_1897558094359285761.json, 视频生成/文生视频/通义万相文生视频+放大补帧_1896034997206188033.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_sampler_11

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/Wan2.1-图生视频+放大补帧_1908814270581059585.json、视频生成/图生视频/原生-Wan2.1-GGUF-图生视频+放大补帧_1897558094359285761.json、视频生成/文生视频/通义万相文生视频+放大补帧_1896034997206188033.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `KSampler`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionEncode` —— 2/3 个有
- `CLIPVisionLoader` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `UNETLoader` —— 2/3 个有
- `UnetLoaderGGUF` —— 2/3 个有
- `WanImageToVideo` —— 2/3 个有
- `WanVideoTeaCacheKJ` —— 2/3 个有
- `EmptyHunyuanLatentVideo` —— 1/3 个有
- `LayerUtility: PurgeVRAM` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 3 | 80% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 3 | 100% |
| 采样算法 | uni_pc | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，3 个样本
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
