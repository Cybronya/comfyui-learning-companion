---
name: unknown_workflow_video_lora_sampler_333
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.933333
common_nodes: [LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/KJ图生视频工作流_2066888658283753473.json, 视频生成/图生视频/KJ首尾帧图生视频工作流_2066895652839317506.json, 视频生成/图生视频/Lightx2v图生视频优化版_1935507389821157377.json, 视频生成/图生视频/MAGREF+Lightx2v 双图参考图生视频_1935539702722396162.json, 视频生成/图生视频/MAGREF+Lightx2v图生视频电商极速版_1936094603097329666.json, 视频生成/图生视频/Self-Forcing14B（Lightx2v）-图生视频_1935537593000067073.json, 视频生成/图生视频/lightx2v加速24fps版高运动最高质量版图生视频V1_1934996455494983682.json, 视频生成/图生视频/magref三图参考+uni3c控制_1937420922334683137.json, 视频生成/图生视频/magref双图参考+uni3c控制_1937380576187850754.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_333

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/KJ图生视频工作流_2066888658283753473.json、视频生成/图生视频/KJ首尾帧图生视频工作流_2066895652839317506.json、视频生成/图生视频/Lightx2v图生视频优化版_1935507389821157377.json、视频生成/图生视频/MAGREF+Lightx2v 双图参考图生视频_1935539702722396162.json、视频生成/图生视频/MAGREF+Lightx2v图生视频电商极速版_1936094603097329666.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 9 个 workflow 都包含：
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionLoader` —— 7/9 个有
- `WanVideoBlockSwap` —— 7/9 个有
- `WanVideoClipVisionEncode` —— 7/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/9 个有
- `ImageConcanate` —— 4/9 个有
- `ImageResizeKJv2` —— 4/9 个有
- `PreviewImage` —— 4/9 个有
- `easy imageRemBg` —— 4/9 个有
- `ImagePadKJ` —— 3/9 个有
- `WanVideoEnhanceAVideo` —— 3/9 个有
- `GetImageSize+` —— 2/9 个有
- `JWInteger` —— 2/9 个有
- `Text Multiline` —— 2/9 个有
- `VHS_LoadVideo` —— 2/9 个有
- `WanVideoEncode` —— 2/9 个有
- `WanVideoUni3C_ControlnetLoader` —— 2/9 个有
- `WanVideoUni3C_embeds` —— 2/9 个有
- `ColorMatch` —— 1/9 个有
- `ImageResize+` —— 1/9 个有
- `WanVideoTorchCompileSettings` —— 1/9 个有
- `WanVideoVRAMManagement` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
