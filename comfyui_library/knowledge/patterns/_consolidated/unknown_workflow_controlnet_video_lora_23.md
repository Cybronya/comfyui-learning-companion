---
name: unknown_workflow_controlnet_video_lora_23
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.7252
common_nodes: [CLIPVisionLoader, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Z-uni3c虚拟相机工作流_1991800857396195330.json, 视频生成/图生视频/magref三图参考+uni3c控制_1937420922334683137.json, 视频生成/图生视频/magref双图参考+uni3c控制_1937380576187850754.json, 视频生成/图生视频/uni3c虚拟相机工作流_1941553575740993537.json, 视频生成/图生视频/模仿运镜uni3c虚拟相机_1983014964149530626.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_23

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/Z-uni3c虚拟相机工作流_1991800857396195330.json、视频生成/图生视频/magref三图参考+uni3c控制_1937420922334683137.json、视频生成/图生视频/magref双图参考+uni3c控制_1937380576187850754.json、视频生成/图生视频/uni3c虚拟相机工作流_1941553575740993537.json、视频生成/图生视频/模仿运镜uni3c虚拟相机_1983014964149530626.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：73%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPVisionLoader`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 3/5 个有
- `GetNode` —— 3/5 个有
- `INTConstant` —— 3/5 个有
- `SetNode` —— 3/5 个有
- `GetImageSize+` —— 2/5 个有
- `ImageConcanate` —— 2/5 个有
- `ImagePadKJ` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `easy imageRemBg` —— 2/5 个有
- `ColorMatch` —— 1/5 个有
- `Label (rgthree)` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
