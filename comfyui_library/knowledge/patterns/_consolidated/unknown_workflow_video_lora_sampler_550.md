---
name: unknown_workflow_video_lora_sampler_550
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.9025
common_nodes: [CLIPLoader, CLIPVisionLoader, ImageResizeKJv2, InvertMask, LoadImage, LoadWanVideoT5TextEncoder, MaskPreview, PreviewImage, TextImageEncodeQwenVL, VHS_VideoCombine, WanVideoAddBindweaveEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEncodeLatentBatch, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/BindWeave单角色+场景一致性工作流_1989572607433469953.json, 视频生成/图生视频/BindWeave单角色一致性工作流_1989625310146646018.json, 视频生成/图生视频/BindWeave多主体角色一致性工作流_1989653435731595265.json, 视频生成/图生视频/字节Bindweave角色参考生视频工作流_1989703859226505217.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_550

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/BindWeave单角色+场景一致性工作流_1989572607433469953.json、视频生成/图生视频/BindWeave单角色一致性工作流_1989625310146646018.json、视频生成/图生视频/BindWeave多主体角色一致性工作流_1989653435731595265.json、视频生成/图生视频/字节Bindweave角色参考生视频工作流_1989703859226505217.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPVisionLoader`
- `ImageResizeKJv2`
- `InvertMask`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MaskPreview`
- `PreviewImage`
- `TextImageEncodeQwenVL`
- `VHS_VideoCombine`
- `WanVideoAddBindweaveEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEncodeLatentBatch`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AILab_ColorInput` —— 3/4 个有
- `ImageBatchMulti` —— 3/4 个有
- `MaskBatchMulti` —— 3/4 个有
- `RMBG` —— 3/4 个有
- `SolidMask` —— 3/4 个有
- `Textbox` —— 3/4 个有
- `easy int` —— 3/4 个有
- `MaskPreview+` —— 2/4 个有
- `DrawMaskOnImage` —— 1/4 个有
- `ImageConcatMulti` —— 1/4 个有
- `ImageRemoveBackground+` —— 1/4 个有
- `Label (rgthree)` —— 1/4 个有
- `PreviewAny` —— 1/4 个有
- `TransparentBGSession+` —— 1/4 个有
- `WanVideoSetLoRAs` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
