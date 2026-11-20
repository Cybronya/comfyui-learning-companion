---
name: unknown_workflow_video_sampler_vae_183
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.893333
common_nodes: [LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/扩图终结者_1966463111370846210.json, 平台全量/高级扩图，效果好，速度快_2049399657029181442.json, 视频生成/图生视频/电商商品展示_1924016884511854593.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_183

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/扩图终结者_1966463111370846210.json、平台全量/高级扩图，效果好，速度快_2049399657029181442.json、视频生成/图生视频/电商商品展示_1924016884511854593.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 2/3 个有
- `ImagePadForOutpaint` —— 2/3 个有
- `SaveImage` —— 2/3 个有
- `WanVideoLoraSelect` —— 2/3 个有
- `ImageResizeKJv2` —— 1/3 个有
- `VHS_VideoCombine` —— 1/3 个有
- `WanVideoTeaCache` —— 1/3 个有
- `easy imageConcat` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
