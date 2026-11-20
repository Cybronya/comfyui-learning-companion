---
name: unknown_workflow_video_sampler_vae_182
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.747667
common_nodes: [GetImageSizeAndCount, ImageResizeKJ, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/人物动作控制变装跳舞视频案例_1960222237146165249.json, 视频生成/图生视频/VACE14B-1024-casvid-fast_1924010211143503873.json, 视频生成/图生视频/Wan VACE 14B首尾帧生成视频-加速版_1922976069052526594.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_182

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/人物动作控制变装跳舞视频案例_1960222237146165249.json、视频生成/图生视频/VACE14B-1024-casvid-fast_1924010211143503873.json、视频生成/图生视频/Wan VACE 14B首尾帧生成视频-加速版_1922976069052526594.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 3 个 workflow 都包含：
- `GetImageSizeAndCount`
- `ImageResizeKJ`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 2/3 个有
- `Primitive integer [Crystools]` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `VHS_LoadVideo` —— 2/3 个有
- `WanVideoExperimentalArgs` —— 2/3 个有
- `WanVideoLoraSelect` —— 2/3 个有
- `ColorMatch` —— 1/3 个有
- `DWPreprocessor` —— 1/3 个有
- `DepthAnythingV2Preprocessor` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `Text Multiline` —— 1/3 个有
- `WanVideoMagCache` —— 1/3 个有
- `WanVideoVACEStartToEndFrame` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
