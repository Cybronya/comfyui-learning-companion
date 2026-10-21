---
name: unknown_workflow_video_sampler_vae_66
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.88425
common_nodes: [LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1924016884511854593.json, 视频生成/图生视频/1991857702083293186.json, 视频生成/图生视频/1928609349776654338.json, 视频生成/图生视频/1930066639159508993.json, 视频生成/图生视频/1946416276699013121.json, 视频生成/图生视频/1923373962599067649.json, 视频生成/图生视频/1925013790104952834.json, 视频生成/文生视频/1925755745747292161.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_66

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/1924016884511854593.json、视频生成/图生视频/1991857702083293186.json、视频生成/图生视频/1928609349776654338.json、视频生成/图生视频/1930066639159508993.json、视频生成/图生视频/1946416276699013121.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 8 个 workflow 都包含：
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
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
- `ImageRepeat` —— 7/8 个有
- `WanVideoVACEStartToEndFrame` —— 7/8 个有
- `WanVideoLoraSelect` —— 5/8 个有
- `ImageAndMaskPreview` —— 4/8 个有
- `Int` —— 4/8 个有
- `JjkText` —— 4/8 个有
- `PreviewImage` —— 4/8 个有
- `JWInteger` —— 3/8 个有
- `TextInput_` —— 3/8 个有
- `ImageResizeKJv2` —— 1/8 个有
- `Note Plus (mtb)` —— 1/8 个有
- `WanVideoFreeInitArgs` —— 1/8 个有
- `WanVideoTeaCache` —— 1/8 个有
- `easy imageConcat` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
