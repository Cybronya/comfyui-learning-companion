---
name: unknown_workflow_video_sampler_vae_111
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.984
common_nodes: [ImageResizeKJ, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVACEStartToEndFrame, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/VACE 14B-图生视频+视频高清放大_1925407407495913474.json, 视频生成/图生视频/Wan2.1-FusionX-VACE首尾帧加速工作流_1935621169481711618.json, 视频生成/图生视频/Wan2.1-FusionX-VACE首尾帧图生视频_1933717714491854849.json, 视频生成/图生视频/自己用：FusionX双图首尾帧视频生成+lora_1945368931681095682.json, 视频生成/图生视频/🦖FusionX高细节首尾帧_1934430559047217153.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_111

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/VACE 14B-图生视频+视频高清放大_1925407407495913474.json、视频生成/图生视频/Wan2.1-FusionX-VACE首尾帧加速工作流_1935621169481711618.json、视频生成/图生视频/Wan2.1-FusionX-VACE首尾帧图生视频_1933717714491854849.json、视频生成/图生视频/自己用：FusionX双图首尾帧视频生成+lora_1945368931681095682.json、视频生成/图生视频/🦖FusionX高细节首尾帧_1934430559047217153.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 5 个 workflow 都包含：
- `ImageResizeKJ`
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
- `WanVideoVACEStartToEndFrame`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 4/5 个有
- `CR Prompt Text` —— 3/5 个有
- `JWInteger` —— 3/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/5 个有
- `LayerUtility: PurgeVRAM V2` —— 2/5 个有
- `WanVideoLoraSelect` —— 2/5 个有
- `ImageScale` —— 1/5 个有
- `ImageUpscaleWithModel` —— 1/5 个有
- `Text` —— 1/5 个有
- `UpscaleModelLoader` —— 1/5 个有
- `WanVideoVACEModelSelect` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
