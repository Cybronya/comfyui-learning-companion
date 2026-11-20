---
name: unknown_workflow_video_sampler_vae_142
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.8335
common_nodes: [LoadWanVideoT5TextEncoder, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/文生图/wanvideo_2.1文生图基础工作流_1973026992956248066.json, 视频生成/图生视频/wan2.1_T2V_官方工作流_k神版本_1930303919854096385.json, 视频生成/图生视频/极速图生视频工作流(self-forcing-cfg-step-distill)_1935517569509937153.json, 视频生成/文生视频/丝丝顺滑】最新wan2.1 i2v 美女奔跑 lora_1928319038026596353.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_142

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/wanvideo_2.1文生图基础工作流_1973026992956248066.json、视频生成/图生视频/wan2.1_T2V_官方工作流_k神版本_1930303919854096385.json、视频生成/图生视频/极速图生视频工作流(self-forcing-cfg-step-distill)_1935517569509937153.json、视频生成/文生视频/丝丝顺滑】最新wan2.1 i2v 美女奔跑 lora_1928319038026596353.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 4 个 workflow 都包含：
- `LoadWanVideoT5TextEncoder`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 3/4 个有
- `CLIPTextEncode` —— 3/4 个有
- `VHS_VideoCombine` —— 3/4 个有
- `WanVideoLoraSelect` —— 3/4 个有
- `WanVideoTextEmbedBridge` —— 3/4 个有
- `ImageResizeKJ` —— 2/4 个有
- `LoadImage` —— 2/4 个有
- `LoadWanVideoClipTextEncoder` —— 2/4 个有
- `WanVideoClipVisionEncode` —— 2/4 个有
- `WanVideoEmptyEmbeds` —— 2/4 个有
- `WanVideoImageToVideoEncode` —— 2/4 个有
- `WanVideoVRAMManagement` —— 2/4 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/4 个有
- `GIMMVFI_interpolate` —— 1/4 个有
- `SaveImage` —— 1/4 个有
- `WanVideoSLG` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
