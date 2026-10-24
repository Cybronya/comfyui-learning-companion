---
name: unknown_workflow_video_sampler_vae_101
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.7404
common_nodes: [ImageResizeKJv2, LoadImage, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSampler, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/03-15-02-WAN2.1-长视频单段生成-SVI_1988253691843141633.json, 视频生成/图生视频/Wan_FusionX_i2v_wrapper_WF图生视频_1948047192052367361.json, 视频生成/图生视频/wan 2.1 图生视频首尾帧（综合拆分）_2001590814977474562.json, 视频生成/图生视频/wanvideo2.1_svi_infinite_generate_1983813929321308162.json, 视频生成/图生视频/首尾帧-Wan2_2-Fun_1954777743701491714.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_101

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/03-15-02-WAN2.1-长视频单段生成-SVI_1988253691843141633.json、视频生成/图生视频/Wan_FusionX_i2v_wrapper_WF图生视频_1948047192052367361.json、视频生成/图生视频/wan 2.1 图生视频首尾帧（综合拆分）_2001590814977474562.json、视频生成/图生视频/wanvideo2.1_svi_infinite_generate_1983813929321308162.json、视频生成/图生视频/首尾帧-Wan2_2-Fun_1954777743701491714.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：74%

## 共有节点

全部 5 个 workflow 都包含：
- `ImageResizeKJv2`
- `LoadImage`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionLoader` —— 4/5 个有
- `LoadWanVideoT5TextEncoder` —— 4/5 个有
- `WanVideoClipVisionEncode` —— 4/5 个有
- `WanVideoLoraSelectMulti` —— 4/5 个有
- `WanVideoSetBlockSwap` —— 4/5 个有
- `WanVideoTextEncode` —— 4/5 个有
- `GetNode` —— 3/5 个有
- `WanVideoTorchCompileSettings` —— 3/5 个有
- `PreviewAny` —— 2/5 个有
- `SetNode` —— 2/5 个有
- `WanVideoSetLoRAs` —— 2/5 个有
- `AILab_QwenVL` —— 1/5 个有
- `CR Prompt Text` —— 1/5 个有
- `FloatToSigmas` —— 1/5 个有
- `Qwen_VLM_API` —— 1/5 个有
- `StringToFloatList` —— 1/5 个有
- `WanVideoTextEncodeCached` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
