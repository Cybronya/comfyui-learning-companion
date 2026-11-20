---
name: unknown_workflow_video_sampler_vae_194
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.941
common_nodes: [ImageResizeKJ, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/VACE 14B-图生视频+视频高清放大_1925407407495913474.json, 视频生成/图生视频/热门AI视频拆解之小明剑魔_1918479213039386625.json, 视频生成/文生视频/WAN2.1+Con​​trolNet + VACE 丝滑跳舞视频生成_1927351669028458498.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_194

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/VACE 14B-图生视频+视频高清放大_1925407407495913474.json、视频生成/图生视频/热门AI视频拆解之小明剑魔_1918479213039386625.json、视频生成/文生视频/WAN2.1+Con​​trolNet + VACE 丝滑跳舞视频生成_1927351669028458498.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 3 个 workflow 都包含：
- `ImageResizeKJ`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScale` —— 2/3 个有
- `ImageUpscaleWithModel` —— 2/3 个有
- `UpscaleModelLoader` —— 2/3 个有
- `VHS_LoadVideo` —— 2/3 个有
- `WanVideoSLG` —— 2/3 个有
- `WanVideoVACEStartToEndFrame` —— 2/3 个有
- `AIO_Preprocessor` —— 1/3 个有
- `CR Combine Prompt` —— 1/3 个有
- `DepthAnythingPreprocessor` —— 1/3 个有
- `Florence2` —— 1/3 个有
- `LayerUtility: PurgeVRAM V2` —— 1/3 个有
- `LoadFlorence2Model` —— 1/3 个有
- `RIFE VFI` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有
- `WanVideoLoraSelect` —— 1/3 个有
- `WanVideoTorchCompileSettings` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
