---
name: unknown_workflow_video_sampler_vae_35
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8455
common_nodes: [CreateCFGScheduleFloatList, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/图生视频  Wan2.2_1972296101548191746.json, 视频生成/图生视频/WAN2.2-6步极速版-图生视频-KJ版工作流_2017911981818253314.json, 视频生成/图生视频/WAN2.2-6步极速版-图生视频-KJ版工作流_2046206194833952769.json, 视频生成/图生视频/WAN2.2-首尾帧视频-6步极速版-KJ版工作流_2014217620324618242.json, 视频生成/图生视频/wan2.2-KJ图生视频_首尾帧_2036380526440878082.json, 视频生成/图生视频/基础图生视频  WAN2.2_1988338285892255745.json, 视频生成/图生视频/首尾帧 Wan2.2_1972327481543946241.json, 视频生成/图生视频/🐳Wan2.2 图生视频 高动态高细节 邪修增强版v2🐳_1972843772218396673.json, 视频生成/文生视频/Wan2.2 图生视频 高动态高细节_1972673116709298177.json, 视频生成/文生视频/🐳Wan2.2 图生视频 高动态高细节 邪修增强版🐳_1972199974152957954.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_35

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/图生视频  Wan2.2_1972296101548191746.json、视频生成/图生视频/WAN2.2-6步极速版-图生视频-KJ版工作流_2017911981818253314.json、视频生成/图生视频/WAN2.2-6步极速版-图生视频-KJ版工作流_2046206194833952769.json、视频生成/图生视频/WAN2.2-首尾帧视频-6步极速版-KJ版工作流_2014217620324618242.json、视频生成/图生视频/wan2.2-KJ图生视频_首尾帧_2036380526440878082.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 10 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 6/10 个有
- `ImpactInt` —— 6/10 个有
- `SetNode` —— 6/10 个有
- `SimpleMath+` —— 6/10 个有
- `WanVideoLoraSelectMulti` —— 6/10 个有
- `WanVideoLoraSelect` —— 4/10 个有
- `CR Text` —— 3/10 个有
- `DownloadAndLoadGIMMVFIModel` —— 3/10 个有
- `GIMMVFI_interpolate` —— 3/10 个有
- `Seed (rgthree)` —— 3/10 个有
- `Text` —— 3/10 个有
- `easy cleanGpuUsed` —— 3/10 个有
- `Fast Groups Bypasser (rgthree)` —— 2/10 个有
- `ImageResize+` —— 2/10 个有
- `Note Plus (mtb)` —— 2/10 个有
- `UpscaleModelLoader` —— 2/10 个有
- `Anything Everywhere` —— 1/10 个有
- `INTConstant` —— 1/10 个有
- `ImageScaleToMegapixels` —— 1/10 个有
- `ImageUpscaleWithModel` —— 1/10 个有
- `Int` —— 1/10 个有
- `LayerUtility: PurgeVRAM` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
