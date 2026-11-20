---
name: unknown_workflow_video_sampler_vae_118
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9876
common_nodes: [ImageResizeKJ, LoadWanVideoT5TextEncoder, VHS_LoadVideo, VHS_VideoCombine, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/万相视频生视频_2041700321528913922.json, 平台全量/通义万相Wan2.1视频转绘teacache加速版_1899717715358076930.json, 平台全量/通义万相视频转视频_1894633108795469826.json, 视频生成/图生视频/一键爆火热舞迁移(Wan2.1-KJ)_1895658256604266497.json, 视频生成/文生视频/NEW万相视频生视频、文生视频_1896055143953727489.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_118

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/万相视频生视频_2041700321528913922.json、平台全量/通义万相Wan2.1视频转绘teacache加速版_1899717715358076930.json、平台全量/通义万相视频转视频_1894633108795469826.json、视频生成/图生视频/一键爆火热舞迁移(Wan2.1-KJ)_1895658256604266497.json、视频生成/文生视频/NEW万相视频生视频、文生视频_1896055143953727489.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 5 个 workflow 都包含：
- `ImageResizeKJ`
- `LoadWanVideoT5TextEncoder`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageConcatMulti` —— 4/5 个有
- `WanVideoBlockSwap` —— 3/5 个有
- `Note Plus (mtb)` —— 2/5 个有
- `WanVideoTeaCache` —— 2/5 个有
- `CR Upscale Image` —— 1/5 个有
- `ImageScaleDownToSize` —— 1/5 个有
- `LoadImage` —— 1/5 个有
- `Primitive integer [Crystools]` —— 1/5 个有
- `Primitive string [Crystools]` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
