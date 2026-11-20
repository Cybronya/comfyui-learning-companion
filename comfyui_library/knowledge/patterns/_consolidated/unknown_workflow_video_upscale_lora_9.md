---
name: unknown_workflow_video_upscale_lora_9
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.780167
common_nodes: [CLIPLoader, CLIPTextEncode, ImageConcanate, KSampler, LoraLoaderModelOnly, ModelSamplingSD3, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAEEncode, VAELoader, VHS_LoadVideo, VHS_VideoCombine]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/视频高清修复 Wan2.2低噪修复洗图+SeedVR2放大_2027280368834973698.json, 平台全量/视频高清修复工作流-Wan2.2低噪洗图+SeedVR2放大_1977027877214539778.json, 平台全量/视频高清放大修复  Wan2.2低噪洗图+SeedVR2放大 视频补帧放大 视频高清放大_2016358403949469697.json, 平台全量/视频高清放大修复  视频补帧放大 视频高清放大_2017174790859132930.json, 视频生成/图生视频/视频高清修复  Wan2.2低噪洗图+SeedVR2放大 视频补帧放大 高清放大_2016324752847151106.json, 视频生成/图生视频/视频高清修复工作流-Wan2.2低噪洗图+SeedVR2放大_2050859823088062466.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_lora_9

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（平台全量/视频高清修复 Wan2.2低噪修复洗图+SeedVR2放大_2027280368834973698.json、平台全量/视频高清修复工作流-Wan2.2低噪洗图+SeedVR2放大_1977027877214539778.json、平台全量/视频高清放大修复  Wan2.2低噪洗图+SeedVR2放大 视频补帧放大 视频高清放大_2016358403949469697.json、平台全量/视频高清放大修复  视频补帧放大 视频高清放大_2017174790859132930.json、视频生成/图生视频/视频高清修复  Wan2.2低噪洗图+SeedVR2放大 视频补帧放大 高清放大_2016324752847151106.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ImageConcanate`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `PathchSageAttentionKJ` —— 5/6 个有
- `Fast Groups Bypasser (rgthree)` —— 4/6 个有
- `Image Comparer (rgthree)` —— 4/6 个有
- `ImageFromBatch+` —— 4/6 个有
- `easy cleanGpuUsed` —— 3/6 个有
- `GetNode` —— 2/6 个有
- `ImageScaleToTotalPixels` —— 2/6 个有
- `Int` —— 2/6 个有
- `PreviewImage` —— 2/6 个有
- `SetNode` —— 2/6 个有
- `VHS_VideoInfoSource` —— 2/6 个有
- `SaveImage` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 8 | 6 | 67% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 0.3 | 0.2 - 0.3 | 6 | 82% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 8，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 0.3，观测区间 0.2 - 0.3，6 个样本，取值集中（一致性 82%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
