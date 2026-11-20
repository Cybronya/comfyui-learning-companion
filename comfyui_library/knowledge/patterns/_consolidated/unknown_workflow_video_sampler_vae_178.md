---
name: unknown_workflow_video_sampler_vae_178
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.926
common_nodes: [GetImageSizeAndCount, ImageConcanate, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/VACE视频扩展加入图片和骨骼双重参考_1926934626474860546.json, 平台全量/VACE骨骼绑定视频生视频_1925182982384984066.json, 视频生成/图生视频/VACE双图参考，教程请看b站八月饺子_1926978789408952322.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_178

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/VACE视频扩展加入图片和骨骼双重参考_1926934626474860546.json、平台全量/VACE骨骼绑定视频生视频_1925182982384984066.json、视频生成/图生视频/VACE双图参考，教程请看b站八月饺子_1926978789408952322.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 3 个 workflow 都包含：
- `GetImageSizeAndCount`
- `ImageConcanate`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `DWPreprocessor` —— 2/3 个有
- `ImageResizeKJ` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `VHS_LoadVideo` —— 2/3 个有
- `WanVideoEnhanceAVideo` —— 2/3 个有
- `easy imageRemBg` —— 2/3 个有
- `AddLabel` —— 1/3 个有
- `Anything Everywhere` —— 1/3 个有
- `Anything Everywhere3` —— 1/3 个有
- `GetImageRangeFromBatch` —— 1/3 个有
- `ImagePadKJ` —— 1/3 个有
- `ImageResize+` —— 1/3 个有
- `PreviewMask_` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
