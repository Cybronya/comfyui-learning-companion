---
name: unknown_workflow_video_sampler_vae_116
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.754
common_nodes: [CLIPVisionLoader, ImageResizeKJv2, LoadImage, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSampler, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1988253691843141633.json, 视频生成/图生视频/1948047192052367361.json, 视频生成/图生视频/2001590814977474562.json, 视频生成/图生视频/1983813929321308162.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_116

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/1988253691843141633.json、视频生成/图生视频/1948047192052367361.json、视频生成/图生视频/2001590814977474562.json、视频生成/图生视频/1983813929321308162.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPVisionLoader`
- `ImageResizeKJv2`
- `LoadImage`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadWanVideoT5TextEncoder` —— 3/4 个有
- `WanVideoLoraSelectMulti` —— 3/4 个有
- `WanVideoSetBlockSwap` —— 3/4 个有
- `WanVideoTextEncode` —— 3/4 个有
- `GetNode` —— 2/4 个有
- `PreviewAny` —— 2/4 个有
- `SetNode` —— 2/4 个有
- `WanVideoTorchCompileSettings` —— 2/4 个有
- `AILab_QwenVL` —— 1/4 个有
- `CR Prompt Text` —— 1/4 个有
- `Qwen_VLM_API` —— 1/4 个有
- `WanVideoSetLoRAs` —— 1/4 个有
- `WanVideoTextEncodeCached` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
