---
name: unknown_workflow_video_sampler_vae_142
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 1
common_nodes: [LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/文生视频/1923688009151991809.json, 视频生成/文生视频/1923941763244093441.json, 视频生成/文生视频/1923955106968948737.json, 视频生成/文生视频/文生视频(Wan2.1-VACE-14B)_2072999779808092160.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_142

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/1923688009151991809.json、视频生成/文生视频/1923941763244093441.json、视频生成/文生视频/1923955106968948737.json、视频生成/文生视频/文生视频(Wan2.1-VACE-14B)_2072999779808092160.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 4 个 workflow 都包含：
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
- `WanVideoEnhanceAVideo` —— 3/4 个有
- `WanVideoTorchCompileSettings` —— 3/4 个有
- `ImagePadKJ` —— 2/4 个有
- `String Literal` —— 2/4 个有
- `VHS_LoadVideo` —— 2/4 个有
- `GetImageSize+` —— 1/4 个有
- `GetImageSizeAndCount` —— 1/4 个有
- `INTConstant` —— 1/4 个有
- `ImageResizeKJ` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
