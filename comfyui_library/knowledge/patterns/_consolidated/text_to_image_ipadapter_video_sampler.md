---
name: text_to_image_ipadapter_video_sampler
type: Text To Image
frequency: 3
level: strong
coverage: 0.944
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, IPAdapter, IPAdapterUnifiedLoader, ImageOnlyCheckpointLoader, KSampler, LoadImage, PreviewImage, SVD_img2vid_Conditioning, SaveAnimatedWEBP, VAEDecode, VHS_VideoCombine, VideoLinearCFGGuidance, WD14Tagger|pysssss]
problems: []
missing: []
members: [平台全量/浮墨云烟_中式水墨风格_1934505909554991105.json, 平台全量/稳定版水墨视频（加强版）_1946896053409837058.json, 视频生成/图生视频/水墨视频_1796114446914011137.json]
source: knowledge_consolidation
---

# text_to_image_ipadapter_video_sampler

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/浮墨云烟_中式水墨风格_1934505909554991105.json、平台全量/稳定版水墨视频（加强版）_1946896053409837058.json、视频生成/图生视频/水墨视频_1796114446914011137.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `IPAdapter`
- `IPAdapterUnifiedLoader`
- `ImageOnlyCheckpointLoader`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `SVD_img2vid_Conditioning`
- `SaveAnimatedWEBP`
- `VAEDecode`
- `VHS_VideoCombine`
- `VideoLinearCFGGuidance`
- `WD14Tagger|pysssss`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 3 | 100% |
| 高度 | 576 | 576 - 576 | 3 | 100% |
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 2.5 | 2.5 - 2.5 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | karras | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 高度 中位数 576，观测区间 576 - 576，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 2.5 - 2.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 karras，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
