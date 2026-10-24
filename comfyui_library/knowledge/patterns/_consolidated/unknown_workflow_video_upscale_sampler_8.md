---
name: unknown_workflow_video_upscale_sampler_8
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.887667
common_nodes: [CLIPLoader, CLIPTextEncode, ImageResizeKJv2, ImageScale, ImageUpscaleWithModel, KSampler, LayerUtility: PurgeVRAM V2, LoadImage, ModelSamplingSD3, PreviewImage, TrimVideoLatent, UNETLoader, UpscaleModelLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanVaceToVideo, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/VACE 14B-图生视频（快速简便版）_1925556395737829378.json, 视频生成/图生视频/动作迁移openpose姿势参考+VACE 14B图生视频（内含视频高清放大）_1926993200920088577.json, 视频生成/图生视频/视频人物替换+VACE 14B图生视频_1927528836135817218.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_sampler_8

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/VACE 14B-图生视频（快速简便版）_1925556395737829378.json、视频生成/图生视频/动作迁移openpose姿势参考+VACE 14B图生视频（内含视频高清放大）_1926993200920088577.json、视频生成/图生视频/视频人物替换+VACE 14B图生视频_1927528836135817218.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ImageResizeKJv2`
- `ImageScale`
- `ImageUpscaleWithModel`
- `KSampler`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `ModelSamplingSD3`
- `PreviewImage`
- `TrimVideoLatent`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanVaceToVideo`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJ` —— 2/3 个有
- `JWInteger` —— 2/3 个有
- `VHS_LoadVideo` —— 2/3 个有
- `easy int` —— 2/3 个有
- `EmptyImage` —— 1/3 个有
- `GroundingDinoModelLoader (segment anything)` —— 1/3 个有
- `GroundingDinoSAMSegment (segment anything)` —— 1/3 个有
- `GrowMask` —— 1/3 个有
- `INTConstant` —— 1/3 个有
- `ImageCompositeMasked` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `OpenposePreprocessor` —— 1/3 个有
- `SAMLoader` —— 1/3 个有
- `easy imageRemBg` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 3 | 100% |
| 采样算法 | uni_pc | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
