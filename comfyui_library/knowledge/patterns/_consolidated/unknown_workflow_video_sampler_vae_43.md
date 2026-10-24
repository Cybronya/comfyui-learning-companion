---
name: unknown_workflow_video_sampler_vae_43
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8465
common_nodes: [CLIPVisionLoader, ImageResizeKJ, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Uni3C运镜参考_1929726931179094017.json, 视频生成/图生视频/WAN2.1 FusionX 占满显存效果拉满之（图生视频）_1935000181781766145.json, 视频生成/图生视频/Wan2.1 Kijai 图生视频_1947893136549904385.json, 视频生成/图生视频/Wan2.1 特效LoRa触发词合集_1948691890660081665.json, 视频生成/图生视频/Wan2.1_官方工作流_I2V_k神版本_720P_1930306829082071042.json, 视频生成/图生视频/wan2.1_lora_官方工作流_K神版_480P_1930311338440998914.json, 视频生成/图生视频/wan2.1_lora_官方工作流_K神版_480P_1930415960338108418.json, 视频生成/图生视频/【Wan2.1系列】AI视频lora特效之《360度旋转》_1917932584058425345.json, 视频生成/图生视频/【Wan2.1系列】AI视频lora特效之《大摆锤舞蹈》_1917823045400985602.json, 视频生成/图生视频/【Wan2.1系列】AI视频lora特效之《强风特效》_1917833994954539009.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_43

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/Uni3C运镜参考_1929726931179094017.json、视频生成/图生视频/WAN2.1 FusionX 占满显存效果拉满之（图生视频）_1935000181781766145.json、视频生成/图生视频/Wan2.1 Kijai 图生视频_1947893136549904385.json、视频生成/图生视频/Wan2.1 特效LoRa触发词合集_1948691890660081665.json、视频生成/图生视频/Wan2.1_官方工作流_I2V_k神版本_720P_1930306829082071042.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPVisionLoader`
- `ImageResizeKJ`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoBlockSwap` —— 9/10 个有
- `WanVideoTorchCompileSettings` —— 9/10 个有
- `WanVideoLoraSelect` —— 6/10 个有
- `WanVideoVRAMManagement` —— 5/10 个有
- `PreviewImage` —— 4/10 个有
- `LoadImageFromUrl` —— 2/10 个有
- `Note Plus (mtb)` —— 2/10 个有
- `SaveAnimatedWEBP` —— 2/10 个有
- `INTConstant` —— 1/10 个有
- `VHS_LoadVideo` —— 1/10 个有
- `WanVideoEncode` —— 1/10 个有
- `WanVideoExperimentalArgs` —— 1/10 个有
- `WanVideoUni3C_ControlnetLoader` —— 1/10 个有
- `WanVideoUni3C_embeds` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
