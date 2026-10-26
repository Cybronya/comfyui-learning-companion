---
name: unknown_workflow_video_sampler_vae_77
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.763
common_nodes: [LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/Wan-VACE-图生视频_1933481916970487810.json, 视频生成/图生视频/CausVid-3步720P首尾帧(Wan2.1&MoviiGen&Skyreels)_1923394290066575361.json, 视频生成/图生视频/MoviiGen + VACE首尾帧-加速版_1923694325656711169.json, 视频生成/图生视频/VACE14B-1024-casvid-fast_1924010211143503873.json, 视频生成/图生视频/Wan VACE 14B首尾帧生成视频-加速版_1922976069052526594.json, 视频生成/图生视频/vace-1.3b-1280-causvid-pose-fast_1924012489724317698.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_77

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Wan-VACE-图生视频_1933481916970487810.json、视频生成/图生视频/CausVid-3步720P首尾帧(Wan2.1&MoviiGen&Skyreels)_1923394290066575361.json、视频生成/图生视频/MoviiGen + VACE首尾帧-加速版_1923694325656711169.json、视频生成/图生视频/VACE14B-1024-casvid-fast_1924010211143503873.json、视频生成/图生视频/Wan VACE 14B首尾帧生成视频-加速版_1922976069052526594.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：76%

## 共有节点

全部 6 个 workflow 都包含：
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
- `GetImageSizeAndCount` —— 5/6 个有
- `WanVideoLoraSelect` —— 5/6 个有
- `GetNode` —— 4/6 个有
- `SetNode` —— 4/6 个有
- `WanVideoVACEStartToEndFrame` —— 4/6 个有
- `ImageResizeKJ` —— 3/6 个有
- `WanVideoEnhanceAVideo` —— 3/6 个有
- `Fast Groups Bypasser (rgthree)` —— 2/6 个有
- `String Literal` —— 2/6 个有
- `VHS_LoadVideo` —— 2/6 个有
- `GetImageSize+` —— 1/6 个有
- `INTConstant` —— 1/6 个有
- `ImageResize+` —— 1/6 个有
- `ImageScale` —— 1/6 个有
- `Primitive integer [Crystools]` —— 1/6 个有
- `Text Multiline` —— 1/6 个有
- `WanVideoTorchCompileSettings` —— 1/6 个有
- `easy int` —— 1/6 个有
- `easy seed` —— 1/6 个有
- `easy showAnything` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
